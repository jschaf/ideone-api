from suds.client import Client
from suds.xsd.doctor import ImportDoctor, Import

class Status(object):
    AWAITING_COMPILATION = -1
    DONE = 0
    COMPILING = 1
    RUNNING = 3

class Result(object):
    NOT_RUN = 0
    COMPILATION_ERROR = 11
    RUNTIME_ERROR = 12
    TIME_LIMIT_EXCEEDED = 13
    SUCCESS = 15
    MEMORY_LIMIT_EXCEEDED = 17
    ILLEGAL_SYSTEM_CALL = 19
    INTERNAL_ERROR = 20
    
class Error(object):
    OK = 'OK'
    AUTH_ERROR = 'AUTH_ERROR'
    PASTE_NOT_FOUND = 'PASTE_NOT_FOUND'
    WRONG_LANG_ID = 'WRONG_LANG_ID'
    ACCESS_DENIED = 'ACCESS_DENIED'
    CANNOT_SUBMIT_THIS_MONTH_ANYMORE = 'CANNOT_SUBMIT_THIS_MONTH_ANYMORE'

class IdeoneError(Exception):
    pass
    
class Ideone(object):

    def __init__(self, user, password):
        self.user = user
        self.password = password

        self.api_url = 'https://ideone.com/api/1/service.wsdl'
        self._import = Import('http://schemas.xmlsoap.org/soap/encoding/')
        self._doctor = ImportDoctor(self._import)
        self.client = Client(self.api_url, doctor=self._doctor)
        self._language_dict = None

    def _transform_to_dict(self, result):
        result_dict = {}
        property_list = result.item
        for item in property_list:
            result_dict[item.key[0]] = item.value[0]
        return result_dict
        
    def _handle_error(self, result_dict):
        error = result_dict['error']
        if error == 'OK':
            return
        else:
            raise IdeoneError(error)
        
    def translate_language_name(self, language_name):
        language_id = None
        if self._language_dict:
            # Find it by comparing prefixes because the languages
            # include version information
            for k,v in self._language_dict.items():
                if v.startswith(language_name):
                    language_id = k

        else:
            languages = self.languages()
            self._handle_error(languages)

            self._language_dict = {}
            # The Ideone API loves lists.
            for language in languages.item[1].value[0].item:
                key = language.key[0]
                value = language.value[0]
                self._language_dict[key] = value
                if value.startswith(language_name):
                    language_id = key

        return language_id
            
        
    def create_submission(self, source_code, language_name, std_input="", run=True, private=False):
        language_id = self.translate_language_name(language_name)
        result = self.client.service.createSubmission(self.user, self.password, source_code,
                                                 language_id, std_input, run, private)
        result_dict = self._transform_to_dict(result)
        self._handle_error(result_dict)
        return result_dict

    def submission_status(self, link):
        result = self.client.service.getSubmissionStatus(self.user, self.password, link)
        result_dict = self._transform_to_dict(result)
        self._handle_error(result_dict)
        return result_dict

    def submission_details(self, link, with_source=True,
                               with_input=True, with_output=True,
                               with_stderr=True, with_compilation_info=True):
        result = self.client.service.getSubmissionDetails(self.user, self.password,
                                                          link,
                                                          with_source, with_input,
                                                          with_output, with_stderr,
                                                          with_compilation_info)
        result_dict = self._transform_to_dict(result)
        self._handle_error(result_dict)
        return result_dict

    def languages(self):
        result = self.client.service.getLanguages(self.user, self.password)
        result_dict = self._transform_to_dict(result)
        self._handle_error(result_dict)
        return result_dict

    def test_function(self):
        result = self.client.service.testFunction(self.user, self.password)
        result_dict = self._transform_to_dict(result)
        self._handle_error(result_dict)
        return result_dict

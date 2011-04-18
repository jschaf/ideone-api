import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ideone",
    version = "0.0.1",
    author = "Joe Schafer",
    author_email = "joe@jschaf.com",
    url = "http://github.com/jschaf/ideone-api/",
    description = "A Python binding to the Ideone API.",
    license = "BSD",
    keywords = "API ideone codepad",
    packages = ['ideone'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['suds',]
)

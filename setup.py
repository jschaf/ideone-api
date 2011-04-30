import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

version = __import__('ideone').__version__

setup(
    name = "ideone",
    version = version,
    author = "Joe Schafer",
    author_email = "joe@jschaf.com",
    url = "http://github.com/jschaf/ideone-api/",
    description = "A Python binding to the Ideone (Online Compiler) API.",
    license = "BSD",
    platforms = ["any"],
    keywords = "API, ideone, codepad",
    packages = ['ideone'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    install_requires=['suds',]
)

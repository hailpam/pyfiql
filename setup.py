from setuptools import setup, find_packages

setup(
    name='pyfiql', 
    version='0.1', 
    author = "Paolo Maresca",
    author_email = "plo.maresca@gmail.com",
    description = ("A versatile parser of FIQL filtering expressions with ability to cross compile to backend formats"),
    license = "MIT",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=find_packages(),
    long_description=read('README')
)

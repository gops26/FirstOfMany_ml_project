from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(filepath:str)-> List:
    '''
    returns the all requirements required by the working module
    '''
    requirements = []

    with open(filepath) as fileobj:
        requirements=fileobj.readlines()
        requirements =[req.replace("/n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
        return requirements
setup(
    name="First of many ml project",
    version='0.0',
    description='my first full fled1ed ml project ',
    long_description='''
        welcome to my first full fledged machine learning project "FIRST OF MANY"

        this project will include some basics of ml like data ingestion, data cleaning, data preprocessing, model training,  
    ''',
    author="gopinath k",
    author_email="kgopinath730@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)
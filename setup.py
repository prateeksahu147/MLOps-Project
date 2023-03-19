import os

from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT:str= "-e ."

def get_requirements(requirements_file_path:str)-> List[str]:
    requirements=list()
    with open(requirements_file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements_file_path:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='MLOps_Project',
    version='0.0.1',
    author='Prateek Sahu',
    author_email='prateeksahu147@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)



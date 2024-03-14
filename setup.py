from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function returns the list of requirements
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]   #Replace is used to replace \n in the file used for next line

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
name='mlProject',
version='0.0.1',
author='Vishnu Vardhan Reddy',
author_email='yvishnuvardhanreddy21@gmail.com',
packages=find_packages(),
install_requirements=get_requirements('requirements.txt'),
)
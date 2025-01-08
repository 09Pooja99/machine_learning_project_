from setuptools import setup,find_packages
from typing import List

#Declarig variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Pooja Pandey"
DESCRIPTION="This is a first FSDS Machine Leaning Project"
REQUIREMENT_FILE_NAME="requirements.txt"




def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement mention in 
    requirements.txt file

    return this function is going to return a list which contain name of libraries
    mentioned in the requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirements = [req.strip() for req in requirement_file.readlines() if req.strip() and req.strip() != "-e ."]
        return requirements




setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), #["housing"]
install_requires=get_requirements_list()
)




if __name__=="__main__":
    print(get_requirements_list())
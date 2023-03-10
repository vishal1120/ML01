from setuptools import find_packages,setup
from typing import List

HYPEN_E_dot = '-e .'
def get_requirments(file_path:str)->List[str]:
    """
    this will return the list of requried files
    """
    requiremnets = []
    with open(file_path) as file:
        requiremnets = file.readlines()
        requiremnets = [req.replace("/n"," ") for req in requiremnets]

        if HYPEN_E_dot in requiremnets:
            requiremnets.remove(HYPEN_E_dot)
    return requiremnets



setup(
name = "ML01",
version = "0.0.1",
author = "vish",
author_email= "vishalkarad1120@gmail.com",
packages= find_packages(),
install_requires= get_requirments('requirments.txt')
)

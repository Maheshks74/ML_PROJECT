from setuptools import find_packages, setup
from typing import List

Hyphen_e_dot = '-e .'

def get_requirements(file_path: str)->List[str]:
    # This function will return the list of requirements
    with open(file_path) as f_obj:
        req=f_obj.readlines()
        req=[r.replace("\n","") for r in req]  # remove newline characters
        if Hyphen_e_dot in req:
            req.remove(Hyphen_e_dot)
    return req

setup(
    name='mlproject',
    version='0.0.1',
    author="Mahesh",
    author_email="maheshbabuks979@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt')
)

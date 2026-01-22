from setuptools import find_packages,setup
from typing import List

Hyphen_e_dot = '-e .'
def get_requirements(file_path:str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if Hyphen_e_dot in requirements:
            requirements.remove(Hyphen_e_dot)
    return requirements



setup(
    name= "ML Project",
    version= 1.1,
    author= "Sahil",
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt'),
)
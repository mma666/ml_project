from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_name:str)->List[str]:
    with open(file_name) as f:
        requirements = f.readlines()
        requirements = [r.replace('\n', '') for r in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Mehdi Memar',
    author_email='mma666@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

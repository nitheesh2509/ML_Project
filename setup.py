from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function returns a list of requirements from a given file path.
    """
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        # Remove newline characters
        requirements = [req.strip() for req in requirements]
        print("Before removing '-e .':", requirements)  # Debugging line
        # Remove '-e .' if it's in the list
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
        print("After removing '-e .':", requirements)  # Debugging line
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Nitheeshkumar",
    author_email="nitheeshkumar2509@example.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    description="A machine learning project",
    url="https://github.com/nitheesh2509/ML_Project/"
)

if __name__ == "__main__":
    # Directly test the function if running the script standalone
    print("Testing get_requirements function:")
    print(get_requirements('requirements.txt'))

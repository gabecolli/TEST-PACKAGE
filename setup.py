from setuptools import setup, find_packages

setup(
    name="testpackage",
    version="1.0.0",
    author="Gabriel Colli",
    author_email="gabe@email.com",
    description="this is a test package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gabecolli/testpackage",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        # list of required packages
    ],
)

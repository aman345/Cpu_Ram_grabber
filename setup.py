#from distutils.core import setup
from setuptools import setup

setup(
    # Application name:
    name="Cpu Ram Grabber",
    
    # Version number (initial):
    version="0.1.0",
    
    # Application author details:
    author="Aman Sharma",
    author_email="amankumarsharma345@gmail.com",
    
    
    # Include additional files into the package
    include_package_data=True,
    
   
    #
    # license="LICENSE.txt",
    description="Ram and Cpu use displayer",
    
    
    
    # Dependent packages (distributions)
    install_requires=[
        "PySide2",
        "PySide2extn",
        "psutil",
        "PyQt5"
    ],
)
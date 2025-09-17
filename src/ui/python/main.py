import importlib.util
import subprocess
import sys
import time

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


def main():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(colored(">HashWizard. LOADING...", "black", "on_yellow"))
        time.sleep(0.5)
        text = """

    █████   █████                   █████         █████   ███   █████ █████                                    █████
   ▒▒███   ▒▒███                   ▒▒███         ▒▒███   ▒███  ▒▒███ ▒▒███                                    ▒▒███ 
    ▒███    ▒███   ██████    █████  ▒███████      ▒███   ▒███   ▒███  ▒███   █████████  ██████   ████████   ███████ 
    ▒███████████  ▒▒▒▒▒███  ███▒▒   ▒███▒▒███     ▒███   ▒███   ▒███  ▒███  ▒█▒▒▒▒███  ▒▒▒▒▒███ ▒▒███▒▒███ ███▒▒███ 
    ▒███▒▒▒▒▒███   ███████ ▒▒█████  ▒███ ▒███     ▒▒███  █████  ███   ▒███  ▒   ███▒    ███████  ▒███ ▒▒▒ ▒███ ▒███ 
    ▒███    ▒███  ███▒▒███  ▒▒▒▒███ ▒███ ▒███      ▒▒▒█████▒█████▒    ▒███    ███▒   █ ███▒▒███  ▒███     ▒███ ▒███ 
    █████   █████▒▒████████ ██████  ████ █████       ▒▒███ ▒▒███      █████  █████████▒▒████████ █████    ▒▒████████
   ▒▒▒▒   ▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒▒  ▒▒▒▒ ▒▒▒▒▒         ▒▒▒   ▒▒▒      ▒▒▒▒▒  ▒▒▒▒▒▒▒▒▒  ▒▒▒▒▒▒▒▒ ▒▒▒▒▒      ▒▒▒▒▒▒▒▒ 
                                                                                                                 
                         "A man captivated by his passions cannot be free." - Pythagoras
                    | Version - 0.0.0 | developer - Stdio | GitHub - @StdioHash | Site - soon |                                                                       


                                    1. Hash decryption      3. Password generation
                                    2. Text enctyption      4. Info     
                                                    
                                                     5. Exit                                                              
                                                                                                                 
"""
        print(text)
        choice = input(">Enter a number: ")

        return

if __name__ == "__main__":
    main()

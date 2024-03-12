# This module is the main module that calls other files to execute tasks

import subprocess

import somnio_config.scripts.install_script as install_script
import somnio_config.scripts.utility.dynamic_recursive as suggestion


# Version

print("Installer Utility v0.1")
print("Please run at /Home and if Win run as ADMIN")
print("Be prepared to some pop up windows")
print("\nThis script needs python and pip3 tools to run properly\n")



# Selecting the platform

platform: str = input("Which Platform are you using?(Default: Linux Desktop Environment)")



if platform == "":
    platform = "linux"

platform: str = platform.strip().lower()
platform: list = suggestion.best_suggestions(platform)

match platform[0]:
    case "linux":
        print("Linux Environment Setup")
        install_script.linux_exec()
    case "windows":
        print("Windows Environment Setup")
        install_script.win_exec()
    case "wsl":
        print("WSL Environment Setup")
        install_script.wsl_exec()
    case _:
        print("Not a valid input")
        

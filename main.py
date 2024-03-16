# This module is the main module that calls other files to execute tasks

import subprocess

import somnio_config.scripts.install_script as install_script
import somnio_config.scripts.utility.dynamic_recursive as suggestion



def main() -> None:
    # Version
    print("\nInstaller Utility v0.3")
    print("Be prepared to some pop up windows")
    print("\nThis script needs python and pip3 tools to run properly\n")
    print("\nThis script will require a reboot\n")



    # Selecting the platform

    platform_input: str = input("Which Platform are you using?(Default: Linux Container Environment)")

    if platform_input == "":
        platform_input = "cont" #This code can be refactored 


    platform_input: str = platform_input.strip().lower()
    platform: list = suggestion.best_suggestions(platform_input)

    # print(platform[0],platform) Debugging info


    match platform[0]:
        case "linux":
            print("Linux Environment Setup")
            install_script.linux_exec("linux")
        case "container":
            print("Container Environment Setup")
            install_script.linux_exec("cont")
        case _:
            print("Not a valid input")


#Exec
if __name__ == '__main__':
    main()

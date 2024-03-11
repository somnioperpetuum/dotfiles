
# * Install Script v0.1
# ! This file is a module for install.py


import subprocess


# * Environment Setup


test = "Test text"

def linux_exec() -> None:
    """
    It's used as a main function for the 
    Linux Setup Environment
    """
    log_file = open('log.txt','a')
    list_of_commands = []
    with open('Linux_Sys_INFO.txt','r') as file:
        for line in file:
            command = line.split()
            list_of_commands.append(command)
    # Runs all commands in a batch order
    for command in list_of_commands:
        result = subprocess.run(command,capture_output=True)
        # Log File Handling
        log_file.write("\n" + result.stdout.decode())
        log_file.write("\n" + result.stderr.decode())



def win_exec() -> None:
    print(test,"win")


def wsl_exec() -> None:
    print(test,"wsl")





# * Helper Functions


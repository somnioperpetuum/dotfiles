
# * Install Script v0.1
# ! This file is a module for install.py


import subprocess


# * Environment Setup


test = "Test text"

def linux_exec(kind) -> None:
    
    """
    It's used as a main function for the 
    Linux Setup Environment
    """
    match kind:
        case "linux":
            parse_and_run('Linux_Sys_INFO.txt')
            
        case "cont":
            parse_and_run('CONT_Sys_INFO.txt')
        case _:
            pass
    print(f"Finished")


# * Helper Functions

def parse_and_run(file) -> None:
    log_file = open('log.txt','a')
    list_of_commands = []
    with open(file,'r') as f:
        for line in f:
            command = line.split()
            list_of_commands.append(command)
    # Runs all commands in a batch order
    len_of_list = len(list_of_commands)

    # Clean list
    list_of_commands = [item for item in list_of_commands if item != "" ]

    for index,item in enumerate(list_of_commands):
        result = subprocess.run(item,capture_output=True)
        print(f"\nStage done!\n Current Process -> {index + 1} of {len_of_list}")
        # Log File Handling
        log_file.write("\n" + result.stdout.decode())
        log_file.write("\n" + result.stderr.decode())

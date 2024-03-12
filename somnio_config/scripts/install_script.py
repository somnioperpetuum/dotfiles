
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
            
        case "wsl":
            parse_and_run('WSL_Sys_INFO.txt')
        case _:
            pass
    print(f"Finished")
            

            



def win_exec() -> None:
    print(test,"win")






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
    for item in list_of_commands:
        result = subprocess.run(item,capture_output=True)
        print(f"\nStage done!\n Current Process -> {list_of_commands.index(item)}of {len_of_list}")
        # Log File Handling
        log_file.write("\n" + result.stdout.decode())
        log_file.write("\n" + result.stderr.decode())

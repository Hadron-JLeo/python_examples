import os

def walk_folder_check(path, env_name)->str:
    # Function to walk down a folder and check its folder
    # List directories in path
    folders = os.listdir(path)
    res:str = ""

    try:
        for folder in folders:
            if env_name in os.listdir(folder):
                res = folder
    
    except Exception as e: 
        print(e)

    return res

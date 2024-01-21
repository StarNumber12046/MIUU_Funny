import os
import json
import shutil

def main():
    f = open("conf/config.json")
    config = json.load(f)
    f.close()
    
    game_path = config["game_path"]
    backup_path = "Backup/"
    
    patches = ["resources.assets", "sharedassets1.assets"]
    
    for patch in patches:
        if os.path.exists(os.path.join(backup_path, patch)):
            shutil.copy(os.path.join(backup_path, patch), os.path.join(game_path, patch))
    
    print("Revert done!")
    
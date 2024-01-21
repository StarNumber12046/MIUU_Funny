import os
import shutil
import json

def main():
    f = open("conf/config.json", "r")
    config = json.load(f)
    f.close()
    
    game_path = config["game_path"]
    backup_path = "Backup/"
    
    patches = ["resources.assets", "sharedassets1.assets", "sharedassets0.assets"]
    
    for patch in patches:
        if os.path.exists(os.path.join(game_path, patch)):
            shutil.copy(os.path.join(game_path, patch), os.path.join(backup_path, patch))
    
    print("Backup done!")
    
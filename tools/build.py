import os
import json

def main():
    raise NotImplementedError("This does not work, you can try to fix it I guess")
    f = open("conf/config.json")
    config = json.load(f)
    f.close()
    
    game_path = config["game_path"]
    unity = config["unity_path"]
    
    os.system(f"\"{unity}\\Unity.exe\" -exit -batchmode -projectpath Unity\\miuu_funny -buildTarget Win64 -buildWindowsPlayer Build\\Unity -logfile unity.log")
    print("Build done!")
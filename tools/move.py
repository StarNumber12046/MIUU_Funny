import os
import shutil, pathlib, json

def main():
    pathlib.Path.mkdir(pathlib.Path("Build/game_files"), parents=True, exist_ok=True)
    pathlib.Path.mkdir(pathlib.Path("Build/patch_files"), parents=True, exist_ok=True)
    # Copy patch files
    shutil.copy("Build/Unity/miuu_funny_Data/sharedassets0.assets", "Build/patch_files/miuu_funny.assets")
    shutil.copy("Build/Unity/miuu_funny_Data/sharedassets0.resource", "Build/patch_files/miuu_funny.resource")
    # Copy game files
    config = json.load(open("conf/config.json"))
    game_path = config["game_path"]
    # Copy sharedassets0, sharedassets1, resources (.assets and .resource)
    for item in ["sharedassets0", "sharedassets1", "resources"]:
        if os.path.exists(os.path.join(game_path, item + ".assets")):
            shutil.copy(os.path.join(game_path, item + ".assets"), os.path.join("Build/game_files/", item + ".assets"))
        if os.path.exists(os.path.join(game_path, item + ".resource")):
            shutil.copy(os.path.join(game_path, item + ".resource"), os.path.join("Build/game_files/", item + ".resource"))
    print("Done!")
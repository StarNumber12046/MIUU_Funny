import json
import shutil
import os

def main():
    with open("conf/config.json") as f:
        config = json.load(f)

    game_path = config.get("game_path", "")
    dist_folder = "Dist/"

    if os.path.exists(dist_folder):
        for filename in os.listdir(dist_folder):
            shutil.copy(os.path.join(dist_folder, filename), game_path)
    print("Files copied!")

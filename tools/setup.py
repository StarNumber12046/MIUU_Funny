import os
import json

def main():
    f = open("conf/config.json", "w")
    path = input("What is your game path?\n> ")
    unity = input("What is your unity path?\n> ")
    json.dump({"game_path": path, "unity_path": unity}, f)
    print("Config written!")
    f.close()
    
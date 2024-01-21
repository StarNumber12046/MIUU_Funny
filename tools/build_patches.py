import os
import pathlib
import json

def main():
    
    
    conf = json.load(open("tools/patches.json"))
    for item in conf:
        
        pathlib.Path.mkdir(pathlib.Path("Build/patches/" + item["origin"]), parents=True, exist_ok=True)
        f = open("Build/patches/" + item["origin"] + "/" + item["name"]+".txt", "w")
        template = open("Templates/" + item["template"] + ".txt", "r")
        t = template.read()
        f.write(t.replace(item["template"], item["name"]).replace(item["origin"], "miuu_funny.resource"))
        f.close()

import os
import shutil
import json

def main():
    
    FIXER = ["sharedassets0.resource", "funnysounds.resource"]
    
    conf = json.load(open("tools/patches.json"))
    for item in conf:
        f = open("Build/patches/" + item["name"]+".txt", "w")
        template = open("Templates/" + item["template"] + ".txt", "r")
        t = template.read()
        f.write(t.replace(item["template"], item["name"]).replace(FIXER[0], FIXER[1]))
        f.close()

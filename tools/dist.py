import os, shutil

def main():
    shutil.copytree("Build/Temp/", "Dist/", dirs_exist_ok=True)
    shutil.copytree("Build/patch_files/", "Dist/", dirs_exist_ok=True)
    print("Dist done!")
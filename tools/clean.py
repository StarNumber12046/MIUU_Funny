import shutil, os
def main():
    shutil.rmtree("Build/")
    shutil.rmtree("Templates/")
    shutil.rmtree("Dist/")
    os.mkdir("Build/")
    os.mkdir("Build/Temp")
    os.mkdir("Templates/")
    os.mkdir("Build/patches/")
    os.mkdir("Build/Unity")
    os.mkdir("Dist/")
# Development
## Requirements
- Unity (>= 2023)
- Python (>= 3.9)
- [UABE]("https://github.com/SeriousCache/UABE/releases/tag/v3.0-beta1")

## Compiling the patches and patching the game
### Compiling the audio patches
1. Setup the tooling (`python tools.py setup`)
2. Build the project, by using `python tools.py clean` and building from the Unity GUI. Put the build files in Build/Unity
3. Copy the files in the correct places using `python tools.py move`
4. Export dumps for the audios using UABE. To do that:
    - Open UABE
    - Open Build/patch_files/miuu_funny.assets
    - Select the latest unity version available
    - Export the dump as plain text for all the AudioClips (Select > Export Dump > Plain Text). Place them in Templates/ and name them:
        - therock.txt
        - yey.txt
        - vineboom.txt
        - death.txt
        - mario.txt
5. Run `python tools.py build_patches`
6. Done! Your patches are in Build/patches/<origin - e.g. resources.assets>/
### Applying the audio patches
> [!tip]
> You need to repeat this for all the files listed in Build/patches/

1. Open the file (e.g. resources.assets)
2. For each file in the corresponding folder, in UABE go to View > Search by name and type the exact string, then (if it is found - otherwise open an issue), hit import dump and open the file
3. Once you are done, hit `File > apply and save all` and place the files in Build/Temp. Keep the same name but remove the `-mod` from .assets-mod

### Applying the texture patches
> [!tip]
> You need to repeat this for all the files listed in Build/patches/

1. Open the file (e.g. resources.assets)
2. For each file in the corresponding folder, in UABE go to View > Search by name and type the exact string, make sure it is a Texture2D (if not, press f3; if it is not found, open an issue), hit Plugins > Edit > Load and import the file, then click Done
3. Once you are done, hit `File > apply and save all` and place the files in Build/Temp. Keep the same name but remove the `-mod` from .assets-mod

Once you have finished patching, run `python tools.py dist` to put all the files in the dist folder
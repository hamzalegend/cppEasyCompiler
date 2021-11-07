import os
import sys

setting = open("compilesettings.data")

mainFilePath = ""
for line in setting:
    line = line.strip()
    if "[mainFileName]=\"":
        for char in range(15, len(line)):
            mainFilePath += line[char]
        # print(mainFilePath)


if (os.system("g++ -o ./build/a.out " + mainFilePath + " `sdl2-config --cflags --libs` ")) != 0:
    print("\n\n\n\n\n Error Compileing '" + mainFilePath+"'")
    sys.exit()
else:
    print("Done Compileing...\n\n")


os.system("./build/a.out")

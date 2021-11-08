import os

projname = input("Project Name:")

os.system(f"mkdir {projname}")
os.chdir(f"{projname}")

os.system("mkdir src")
os.system("mkdir build")
# --------------
with open('src/main.cpp', 'w') as f:
    f.write(
        '#include <iostream>\n\nint main()\n{\n\n    std::cout << "Hello ' + projname + '" << std::endl;\n    return 0;\n}')
with open('CompileAndRun.py', 'w') as f2:
    f2.write("""
import os
import sys

mainFilePath = "src/main.cpp"
# if (os.system("g++ -o ./build/a.out " + mainFilePath + " `sdl2-config --cflags --libs` ")) != 0:
if (os.system("g++ -o ./build/a.exe " + mainFilePath)) != 0:
    print("\\n Error Compileing '" + mainFilePath+"'\\n\\n\\n\\n\\n")
    sys.exit()
else:
    print("\\nDone Compileing...\\n\\n")

# os.system("cd build")
os.chdir("build")
os.system("a.exe")
os.chdir("..")

    """)

os.system("code .")
os.system("code src/main.cpp")

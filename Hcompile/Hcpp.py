import os

os.system("mkdir src")
os.system("mkdir build")

os.system(
    "echo '#include <iostream>\nint main()\n{\n    \nreturn 0;\n}' >> src/main.cpp")

os.system("cp /home/hamza/code/gcc-compiler/CompileAndRun.py .")
os.system("echo '[mainFileName]=src/main.cpp' >> compilesettings.data")
os.system("code .")
os.system("code src/main.cpp")

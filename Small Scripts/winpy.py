from code import InteractiveConsole
from os import system
from sys import executable, version, exit

console = InteractiveConsole()
console.push("import os")
python_exe = executable[:executable.rfind("\\")]
console.push(f"os.chdir(r'{python_exe}')")

print(version)
print("Start a line with $ to be interpreted in the command line.")

try:
    while True:
        code = console.raw_input(">>> ")
        if code.startswith("$"):
            system(code[1:])
            continue
        while console.push(code):
            code = console.raw_input("... ")
finally:
    exit()

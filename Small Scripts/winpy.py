from code import InteractiveConsole
from os import system
from sys import version

console = InteractiveConsole()
console.push("import os")

print(version)
print("Start a line with $ to be interpreted in the command line.")

while True:
    code = console.raw_input(">>> ")
    if code.startswith("$"):
        system(code[1:])
        continue
    while console.push(code):
        code = console.raw_input("... ")

from code import InteractiveConsole
from os import system
from sys import executable, version, exit

# Create a Python interpreter
console = InteractiveConsole(filename="<winpy console>")
# Import the os module in the interpreter for general use
console.push("import os")
# Find the Python interpreter executable's path
python_exe = executable[:executable.rfind("\\")]
# Change the directory of the interpreter to the executables's directory
console.push(f"os.chdir(r'{python_exe}')")
# Create the doc function that prints an object's __doc__ attribute
console.push("doc = lambda obj: print(getattr(obj, '__doc__'))")

# Standard Python REPL header
print(version)
# Command line usage instructions
print("Start a line with $ to be interpreted in the command line.")

try:
    while True:
        # Get console input
        code = console.raw_input(">>> ")
        if code.startswith("$"):
            # Run the command in the command line
            system(code[1:])
            continue
        # If the console needs more input to run the code...
        while console.push(code):
            # ...ask for more input until it doesn't
            code = console.raw_input("... ")
finally:
    # If a keyboad interrupt occurs, exit the program cleanly
    exit()

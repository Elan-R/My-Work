from code import InteractiveConsole
from os import system
from sys import executable, version, exit

# Create a Python interpreter
console = InteractiveConsole(filename="<winpy console>")
# Import the os module in the interpreter for general use
console.push("import os")
# Find the Python interpreter executable's path
python_path = executable[:executable.rfind("\\")]
# Change the directory of the interpreter to the executables's directory
console.push(f"os.chdir(r'{python_path}')")
# Create the doc function that prints an object's __doc__ attribute
console.push("doc = lambda obj: print(getattr(obj, '__doc__'))")
console.push("setattr(doc, '__doc__', 'A function that takes any object as an argument and prints its __doc__ attribute')")
# Create the cls function that clears the terminal
# Uses runsource instead of push to include multiple lines (a one line lambda would print 0 every time)
console.runsource("def cls():\n os.system('cls')\n")

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

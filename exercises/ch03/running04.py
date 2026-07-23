"""_summary_
    
    The 'os' module's system() function is a way to run a Python file as a script, and it is also a way to bring in code from other files or modules. This runs the command as if it is typed at the command line.
    
    In the program below, we use the os.system() function to run the code in module1.py. The os.system() function takes a string as an argument, and it executes that string as a command in the operating system's shell. 
    
"""

import os
os.system("python3 module1.py")
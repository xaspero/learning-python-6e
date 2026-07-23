"""_summary_
    The 'exec' statement is a way to run a Python file as a script, and it is also a way to bring in code from other files or modules.
    
    In the program below, we use the exec statement to run the code in module1.py. The exec statement takes a string as an argument, and it executes that string as Python code. In this case, we use the open function to read the contents of module1.py and pass it to exec.
    This is another way to run a Python file as a script, and it is also a way to bring in code from other files or modules.
"""
exec(open("module1.py").read())

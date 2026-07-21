# Ch 02: How Python Runs Programs

    6. Name two or more variations on Python execution model.
        Answer:
        1. CPython - the most common and stable version of Python. Here the source code is converted behind the scene to Bytecode to be executed by the PVM.
        2. Jython - the alternative implementation of CPython targeting the Java progrmaming language
        3. IronPython - another alternative implementation of CPython targeting the .NET programming language.

    7. How are CPython, Jython, and IronPython different?
        Answer:
            (i) CyPython is the official Python implementation that is readily available and can receive updates.
            (ii) Jython is the reimplementation of CPython for the Java programming language. It achived this by substituting the Python Bytecode and PVM with Java Bytecode and JVM to execute Python code using Java.
            (iii) IronPython is the reimplementation of the official CPython for the .NET platform.

    8. What are PyPy, Shed Skin, and Cython?
        Answer:
            (i) PyPy speed up normal Python programs at runtime by using just-in-time compiler to replace some Python code with machine code.
            (ii) Shed Skin does the same with ahead-of-time compiler, whcih translate a portion of Python code to C++ before it is runned
            (iii) Cython is a hybrid of Python/C that can be compiles into machine-code extension that can be accessed by CPython code.

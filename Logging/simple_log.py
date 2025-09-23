'''
Logging gives you superpowers that print() doesn't:
Timestamps: Automatically know when something happened.
Severity Levels: Differentiate between a simple note (INFO) and a critical error (ERROR).
Configurability: You can turn on detailed messages for debugging or turn them off for normal use, all without changing your code.
Persistence: You can easily save your logs to a file to check what happened long after your program has finished.
'''

'''
The Five Logging Levels
There are five standard levels of severity in logging. Python will only show logs at the level you set and all levels above it.
Level
When to Use It
DEBUG
Detailed information, typically of interest only when diagnosing problems.
INFO
Confirmation that things are working as expected.
WARNING
An indication that something unexpected happened, but the software is still working as expected.
ERROR
Due to a more serious problem, the software has not been able to perform some function.
CRITICAL
A very serious error, indicating that the program itself may be unable to continue running.


'''


import logging

# severity levels :

logging.debug("This is a debug message. Useful for developers.")
logging.info("This is an info message. Just confirming things are working.")
logging.warning("This is a warning. The program is still working, but pay attention.")
logging.error("This is an error. Something went wrong.")
logging.critical("This is a critical error. The program might crash!")
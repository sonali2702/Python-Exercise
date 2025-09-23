import logging

# Configure logging to write to a file named 'app.log'
logging.basicConfig(filename='app.log', 
                    filemode='a', # 'w' for write (overwrite), 'a' for append
                    level=logging.INFO ,format='%(asctime)s - %(levelname)s -%(message)s' )

logging.info("The program started.")
logging.warning("An unusual event occurred.")
logging.info("The program is finishing.")

print("Log messages have been written to app.log")



'''
%(asctime)s: The timestamp when the log was created.
%(levelname)s: The severity level (INFO, ERROR, etc.).
%(message)s: The actual log message you wrote.
'''
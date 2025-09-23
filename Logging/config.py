'''
To control the logging level and format, we use logging.basicConfig(). 
This is the simplest way to configure your logging journal.
Important: You must call basicConfig() before you do any logging.
'''
import logging

# Configure the logging system
logging.basicConfig(level=logging.INFO)

logging.debug("This message will NOT be shown, because the level is INFO.")
logging.info("This message WILL now be shown.")
logging.warning("This one will also be shown.")
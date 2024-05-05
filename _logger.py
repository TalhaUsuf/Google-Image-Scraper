import logging
from rich.logging import RichHandler

# Create a logger
logger = logging.getLogger('my_logger')

# Set the logging level
logger.setLevel(logging.DEBUG)

# Create a RichHandler for console output
console_handler = RichHandler()
console_handler.setLevel(logging.DEBUG)

# Create a file handler for file output
file_handler = logging.FileHandler('log_file.log')
file_handler.setLevel(logging.DEBUG)

# Create a formatter for the log messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add the formatter to the handlers
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)
# Will create a log of all
import logging
import os
from datetime import datetime # type: ignore

# Creates the name of the logfile with the date and time of the log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),"logs") # Get the path of the current working directory and creates folder log

# Create the directory if not exist
os.makedirs(log_path, exist_ok=True)
 
# Set the full path
LOG_FILEPATH = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s "        
)

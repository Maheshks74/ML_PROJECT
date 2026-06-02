import logging
import os
from datetime import datetime

LOG_File = f"{datetime.now().strftime('%d_%m_%y_%H_%M_%S')}.log"

base_dir = os.path.dirname(os.getcwd())
log_dir = os.path.join(base_dir, "logs")
os.makedirs(log_dir, exist_ok=True)

LOG_File_path = os.path.join(log_dir, LOG_File)

logging.basicConfig(
    filename=LOG_File_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



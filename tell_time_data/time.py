
from datetime import datetime
import time
import os

log_file_path = os.path.join(os.getcwd(), "log.txt")

for i in range(4):
    with open(log_file_path, "a") as log_file:
        log_file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "\n")
    time.sleep(5)

log_file_path = os.path.join(os.getcwd(), "log.txt")
print(log_file_path)

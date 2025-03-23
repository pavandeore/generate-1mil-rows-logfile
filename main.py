import random 
from datetime import datetime, timedelta

# define log levels and messages
log_levels = ["INFO", "ERROR", "WARNING"]
log_messages = {
    "INFO" : ["User login success - userID: {}", "File uploaded - filename: {}"],
    "ERROR" : ["Database connection failed", "Failed to process payment"],
    "WARNING" : ["Disk usage {}%"]
}

user_ids = [123, 456, 789, 101, 202]
filenames = ["report.pdf", "data.csv", "image.png", "backup.zip"]

def generate_log_entry(timestamp):
    level = random.choice(log_levels)
    if level == "INFO":
        message = random.choice(log_messages["INFO"])
        if "userID" in message:
            message = message.format(random.choice(user_ids))
        else:
            message = message.format(random.choice(filenames))
    elif level == "ERROR":
        message = random.choice(log_messages["ERROR"])
    elif level == "WARNING":
        message = random.choice(log_messages["WARNING"]).format(random.randint(80, 100))
    return f"{timestamp} {level} {message}\n"
    
def generate_log_file(filename, num_entries):
    start_time = datetime.now() - timedelta(days=1)
    with open(filename, 'w') as log_file:
        for i in range(num_entries):
            timestamp = (start_time + timedelta(seconds=i)).strftime("%Y-%m-%d %H:%M:%S")
            log_entry = generate_log_entry(timestamp)
            log_file.write(log_entry)


log_filename = "massive_log_file.log"
num_log_entries = 1000000 #1 mil

generate_log_file(log_filename, num_log_entries)
print(f"Generated log file '{log_filename}'.")

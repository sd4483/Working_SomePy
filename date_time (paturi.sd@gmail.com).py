r"""
This program gives you the date and time at that exact moment it's run.
"""
import datetime
def get_datetime():
    date_time = datetime.datetime.now()
    return date_time
print(get_datetime())

def time_diff():
    """This function gives the time difference"""
    datetime_yesterday = datetime.datetime(2018,2,19,13,0,0,0)
    datetime_now = datetime.datetime.now()
    time_delta = datetime_now - datetime_yesterday
    return time_delta
print(time_diff())

filename = datetime.datetime.now()
filename = filename.strftime("%Y-%m-%d-%H-%M-%S")
def time_file():
    with open(filename, "w") as file:
        file.write("This is day one")
time_file()

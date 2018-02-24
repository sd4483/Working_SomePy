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
filename = filename.strftime("%a.%B.%Y-%H.%M.%S")
def time_file():
    """Formatting date and time to set it as file name"""
    with open(filename+".rtf", "w") as file:
        file.write("This is another day")
time_file()

filename2 = datetime.datetime.now()
filename2 = filename2.strftime("%a %B %d %H.%M %Y")
def time_file2():
    with open(filename2+".rtf", "w") as file:
        file.write("This is another day")
time_file2()

filename3 = datetime.datetime.now()+datetime.timedelta(days=2, hours = 2)
filename3 = filename3.strftime("%a %B %d %H.%M %Y")
def time_file_after():
    """Sets the date two days in advance"""
    with open(filename3+".rtf", "w") as file:
        file.write("This is after two days")
time_file_after()

import time
filename4 = datetime.datetime.now()
filename4 = filename4.strftime("%a %B %d %H.%M %Y")
def time_intervals():
    """Gets the time in intervals of each second and then writes them in the list file"""
    lst=[]
    for i in range(0,5):
        lst.append(datetime.datetime.now())
        time.sleep(1)
    for j in lst:
        print(j)
    with open(filename4+".rtf","w") as file:
        for k in lst:
            file.write(str(k)+"\n")
time_intervals()

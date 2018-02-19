def minutes_to_hours(minutes):
    hours = minutes/60.0
    return hours
print("No. of hours: " , minutes_to_hours(20))
#//
def minutes_seconds_hours(minutes,seconds):
    hours = minutes/60 + seconds/3600
    return hours
print("No. of hours: ", minutes_seconds_hours(30,9))
#//
def minutes_seconds_hours2(seconds, minutes=70): #passing default arguments, should always pass them at end!
    hours = minutes/60 + seconds/3600
    return hours
print("No. of hours: ", minutes_seconds_hours2(9))
#//
def minutes_seconds_hours3(seconds, minutes=70): #Even when a default argument is set, python checks the print statement for new inputs and executes them!
    hours = minutes/60 + seconds/3600
    return hours
print("No. of hours: ", minutes_seconds_hours2(9,90))
#//
def minutes_to_hours2(minutes):
    hours = minutes/60.0
    print("No. of hours: ", hours)
minutes_to_hours2(20)

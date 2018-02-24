"""
[Updated]This progam can be used to get content from various txt files and merge the content into one file
"""
import datetime
import glob2
new_filename = datetime.datetime.now().strftime("%a %B %d %H.%M %Y")#For new file name
filenames = glob2.glob("*.txt")#gets all the filenames in the directory with .txt extension

def merge_file():
    for files in filenames:#iterating the contents in filenames list
        with open(files,"r") as read_file:
            j = read_file.read()
            if 'Content' in j:
                with open(new_filename+".rtf", "w") as write_file:
                        write_file.write(j)
merge_file()

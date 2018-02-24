"""
This progam can be used to get content from various txt files and merge the content into one file
"""
import datetime
import glob2
new_filename = datetime.datetime.now()#For new file name
new_filename = new_filename.strftime("%a %B %d %H.%M %Y")#Formatting the new file name
filenames = glob2.glob("*.txt")#gets all the filenames in the directory with .txt extension
some_list=[]#an empty list

def merge_file():
    for files in filenames:#iterating the contents in filenames list
        with open(files,"r") as read_file:
            j = read_file.read()
            if 'Content' in j:
                some_list.append(j)
    with open(new_filename+".rtf", "w") as write_file:
        for content in some_list:
            write_file.write(content)
merge_file()

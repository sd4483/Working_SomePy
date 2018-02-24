r"""
This program lets you find the hidden files, provided the directory you want to look in
"""
import glob2
def find_hidden():
    files = glob2.glob("*")
    print(files)
    for i in files:
        print(i)
find_hidden()

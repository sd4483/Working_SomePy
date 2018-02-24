file = open("somefile.txt", "w")#writes to file but erases it upon opening
file.write("Something") #wite takes only one argument
file.close()

file=open("anotherfile.txt", "w")
lst = ["Batman", "Superman", "Wonder Woman", "Flash"]
for i in lst:
    file.write(i+"\n")
file.close()

file=open("numberfile.txt", "w")
lst = [1,2,3]
for i in lst:
    file.write(str(i)+"\n") #write method only works with strings, so should convert to string before writing to file
file.close()

file=open("anotherfile.txt", "a")#appends to file without erasing it
file.write("Aquaman\n")
file.write("Green Arrow")
file.close()

with open("anotherfile.txt", "r") as file: #better to use this as it closes the file automatically
    i = file.readlines()
    print(i)
    for j in i:
        print(j)
with open("anotherfile.txt", "a+") as file:#can read and write to file, but pointer at end
    file.seek(0)#so to read the file, should use this method before the .read or .readlines methods
    i = file.readlines()
    print(i)

def main(filename):
    file = open(filename, "r")
    content = file.readlines()
    content = [i.rstrip("\n") for i in content]
    for i in content:
        print(len(i))
    file.close()
get_file = input("Enter the name of the file: ")
main(get_file)

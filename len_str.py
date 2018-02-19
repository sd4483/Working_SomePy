def len_str(arg):
    if type(arg) == int:
        return "Sorry, integers don't have length"
    elif type(arg) == float:
        return "Sorry, floats have no length too"
    else:
        return len(arg)

print(len_str(12.0))

import textwrap

def wrap(string, max_width):
    y=max_width
    z=0
    return_string = ""
    for i in range(0,len(string),y):
        return_string += string[0+z:y+z] + "\n"
    return return_string

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

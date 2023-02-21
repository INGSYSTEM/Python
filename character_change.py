def mutate_string(string, position, character):
    cadena = string[:position] + f"{character}" + string[(position + 1):]
    return cadena

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

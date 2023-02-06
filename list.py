if __name__ == '__main__':
    N = int(input())
    Lista = [];
    for i in range(0,N):
        comando = input().split()
        if comando[0] == "insert":
            Lista.insert(int(comando[1]),int(comando[2]))
        elif comando[0] == "append":
            Lista.append(int(comando[1]))
        elif comando[0] == "pop":
            Lista.pop()
        elif comando[0] == "print":
            print(Lista)
        elif comando[0] == "remove":
            Lista.remove(int(comando[1]))
        elif comando[0] == "sort":
            Lista.sort()
        else:
            Lista.reverse()

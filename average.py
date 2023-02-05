if __name__ == '__main__':
    n = int(input())
    suma = float(0)
    student_marks = {}
    if (2 <= n <= 10):
        for _ in range(n):
            name, *line = input().split()
            scores = list(map(float, line))
            for datos in range(len(scores)):
                if (0<= scores[datos]<= 100):
                    student_marks[name] = scores
        query_name = input()
        longitud = len(student_marks[query_name])
        for i in student_marks[query_name]:
            suma += i
        promedio = suma / longitud
        print (f"{promedio:.2f}")

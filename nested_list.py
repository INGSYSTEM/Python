if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    ordenamos_valores = sorted(list(set(elementos[1] for elementos in python_students)))
    segundo_ordenamiento = ordenamos_valores[1]
    
    score_lower = []
    for elemet in python_students:
        if (segundo_ordenamiento == elemet[1]):
            score_lower.append(elemet[0])
    for student in sorted(score_lower):
        print(student)

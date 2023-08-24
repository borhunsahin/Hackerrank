grades = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grades.append([name,score])
      
result = [ i for i in grades if i[1] != min([j[1] for j in grades]) ]
result = [ i[0] for i in result if i[1] == min(j[1] for j in result) ]

for student in sorted(result):
    print(student)
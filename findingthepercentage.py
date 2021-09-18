if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = str(input())
    scorelist =[]
    scorelist = ( student_marks[query_name])
    s = 0
    for i in range (len(scorelist)):
        s = s + scorelist[i]
        
    avg = s/(len(scorelist))
    print('%.2f'%avg)

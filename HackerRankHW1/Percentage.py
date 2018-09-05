if __name__ == '__main__':
    n = int(raw_input()) #вводим число n
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores


    query_name = raw_input()
    #for s in student_marks:
    query_score = 0
    for s in student_marks[query_name]:
        query_score += s
        average = query_score/3
    #print student_marks[name]
    print  ("{0:.2f}".format(average))
    #print average

#this is the solution for kitchen timetable from snackdown practice contest: beginner leve

try:
    count = 0
    test_cases = input()
    output = []
    for i in range(int(test_cases)):
        count = 0
        students = int(input())
        moments = [int(x) for x in input().split(' ')]
        time_required = [int (y) for y in input().split(' ')]
        time_allotted = []
        time_allotted.append(moments[0])
        for j in range(1, students):
            time_allotted.append(moments[j] - moments[j-1])
        for k in range(students):
            if time_allotted[k] >= time_required[k]:
                count = count + 1
        output.append(count)

    print(*output, sep="\n") 
        
except EOFError as e:
    print (e)
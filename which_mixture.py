try:
    test_cases = int(input())
    output = []
    for i in range(test_cases):
        mixture = [int(x) for x in input().split(' ')]
        if mixture[0]>0 and mixture[1]>0:
            output.append("Solution")
        elif mixture[0]==0:
            output.append("Liquid")
        elif mixture[1]==0:
            output.append("Solid")

    print(*output, sep="\n")
except EOFError as e:
    print (e)
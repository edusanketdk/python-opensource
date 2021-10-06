# cook your dish here
for i in range(int(input( ))):
    a,b=map(int,input().split())
    s=1000000007
    c=pow(2,a,s)-1
    print(pow(c,b,s))

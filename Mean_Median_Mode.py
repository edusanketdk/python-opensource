import collections
def mean(x):
    s=0
    for i in range(len(x)):
        s=s+int(x[i])
    
    return s/len(x)

def median(x):
    x.sort()
    if(int(len(x)%2)==0):
        return (int(x[int(len(x)/2)])+int(x[int(len(x)/2)-1]))/2
    if(int(len(x)%2)!=0):
        return int(x[int(len(x)/2)])

def mode(x):
    y=collections.Counter(x)
    data=dict(y)
    m=max(list(y.values()))
    mod=[n for n,freq in data.items() if freq == m]
    return mod


x=input("Enter each elements by a ',' between them : ")
x=x.split(",")

mean1=mean(x)
print("Mean Value of the numbers is : ",mean1)

median1=median(x)
print("Median of the numbers is : ",median1)

mode1=mode(x)
if(len(mode1)==len(x)):
    print("The is no mode in the numbers")
else:
    print("Mode of the numbers is " + ', '.join(map(str, mode1)))
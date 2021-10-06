def max_arr_sum(x):
    max=int(x[0])
    end=0
    for i in range(0,len(x)):
        end=end+int(x[i])
        if(end<0):
            end=0

        if(max<end):
            max=end

    return max

x=input("Enter each elements by a ',' between them : ")
x=x.split(",")

result=max_arr_sum(x)

print("")
print("The Max Subarray Sum is : ",result)
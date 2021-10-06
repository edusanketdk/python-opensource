# 1.fibonacci with iterative method 

# def fib(n):
#     if(n<=1):
#         return n

#     else:
#         a = 0
#         b = 1

#         for i in range(2, n+1):
#             c = a+b
#             a = b
#             b = c
#         return c

# num= int(input("Enter the number: "))
# print(fib(num))



# 2.fibonacci with recursive method
# for calculating big number it taking time. so we use Memoization
 
# def fib(n):
#     if(n<=1):
#         return n
#     else:
#         return fib(n-1)+fib(n-2)

# num= int(input("Enter the number: "))
# print(fib(num))        




# 3.fibonacci Memoization with recursive method 
# for calculating big number it taking time. so we use Memoization


arr = [-1]*100       #additional step

def fib(n):
    if(n<=1):
        return n
    else:
        if(arr[n] != -1):     #additional step
            return arr[n]     #additional step
        arr[n] = fib(n-1)+fib(n-2)
        return arr[n] 

num= int(input("Enter the number: "))
print(fib(num))  
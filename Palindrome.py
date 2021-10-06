def check_palindrome(x):
    if(len(x)%2==0):
        half1=x[:int(len(x)/2)]
        half2=x[int(len(x)/2):]
    else:
        half1=x[:int(len(x)/2)]
        half2=x[int(len(x)/2)+1:]

    if(half1==half2[::-1]):
        print("")
        print("The given string is a Palindrome")
        print("")

    else:
        print("")
        print("The given string is not a Palindrome")
        print("")

x=input("Enter the string that you want to check palindrome : ")
check_palindrome(x)

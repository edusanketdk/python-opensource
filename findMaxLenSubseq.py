# Function to find the length of the largest subsequence formed by consecutive integers
def findMaxLenSubseq(A):
 
    # construct a set out of input elements
    S = set(A)
 
    # initialize result by 0
    maxlength = 0
 
    # do for each element of the input sequence
    for e in A:
 
        # check if the current element `e` is a candidate for starting a sequence;
        # i.e., the previous element `e-1` doesn't exist in the set
        if (e - 1) not in S:
 
            # `len` stores the length of subsequence, starting with the current element
            len = 1
 
            # check for presence of elements `e+1`, `e+2`, `e+3`, … ,`e+len` in the set
            while (e + len) in S:
                len += 1
 
            # update result with the length of current consecutive subsequence
            maxlength = max(maxlength, len)
 
    # return result
    return maxlength
 
 
if __name__ == '__main__':
 
    A = [2, 0, 6, 1, 5, 3, 7]
 
    print("The length of the maximum consecutive subsequence is:",
        findMaxLenSubseq(A))
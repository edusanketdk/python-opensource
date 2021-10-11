'''
Link to problem: https://www.hackerrank.com/challenges/pairs/problem

Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

Sample Input

STDIN       Function
-----       --------
5 2         arr[] size n = 5, k =2
1 5 3 4 2   arr = [1, 5, 3, 4, 2]

Sample Output
3

Explanation:

There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1].

'''

#Solution

def pairs(k, arr):
    return len(set(arr) & set(x + k for x in arr))

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(pairs(k, arr))
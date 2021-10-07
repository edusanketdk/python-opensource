
def removals(arr, n, k):
     
  arr.sort()
  dp = [0 for i in range(n)]
 
  for i in range(n):
    dp[i] = -1
 
  ans = n - 1
  dp[0] = 0
   
  for i in range(1, n):
    dp[i] = i
    j = dp[i - 1]
     
    while (j != i and arr[i] - arr[j] > k):
      j += 1
       
    dp[i] = min(dp[i], j)
    ans = min(ans, (n - (i - j + 1)))
     
  return ans
 
a = list(map(int, input().split()))
n = len(a)
k = 4
 
print(removals(a, n, k))

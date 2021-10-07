
 
def countBT(h) :
    MOD = 1000000007
    dp = [0 for i in range(h + 1)]
     
    dp[0] = 1
    dp[1] = 1
     
    for i in range(2, h + 1) :
        dp[i] = (dp[i - 1] * ((2 * dp [i - 2])%MOD + dp[i - 1])%MOD) % MOD
     
    return dp[h]
 
h = 3
print("No. of balanced binary trees of height "+str(h)+" is: "+str(countBT(h)))
 

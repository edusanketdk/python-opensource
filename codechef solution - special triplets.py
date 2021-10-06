#!/usr/bin/env python
# coding: utf-8

# In[ ]:


try:
    T=int(input())
    for i in range(T):
        n=int(input())
        d=0
        for e in range(2,n+1):
            for b in range(2,n+1):
                c=e%b
                if  c!=0 and b%c==0:
                    d=d+1
                else:
                    pass
        print(d+(n-1))
                
    
    
except EOFError:
    pass


# In[ ]:





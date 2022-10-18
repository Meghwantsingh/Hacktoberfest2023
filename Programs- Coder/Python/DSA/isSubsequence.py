#given the 2 strings s and t , check whether that s is a subsequence of t
#ex INPUT-cb caba OUTPUT-true
def isSubsequence(s,t):

    j=0
    for i in range(len(t)):
           if(t[i]==s[j]):#for continuation
                j+=1

           if(j==len(s)):
              return"true"
    return"false"

s,t=map(input().split(' '))
print(isSubsequence(s,t))
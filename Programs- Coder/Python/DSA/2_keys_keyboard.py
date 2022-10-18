#given number, you have to find out the minimum number of steps to form that string, by only using copy and paste method
#ex INPUT-3 OUTPUT-3
def minSteps(num):
   if (n == 0 or n==1): return 0
   ans = 0
   i = 2
   #for prime number the number of steps is equal to the number itself
   while (True):
     if (n % i == 0):
        #if the number is divisible by any number add that number to the ans, because the minimum number is going to be the prime number itself
        ans += i
        n /= i
     else:
        i += 1
     if (n == 1):
        break

   return (ans)

num=int(input())
print(minSteps(num))
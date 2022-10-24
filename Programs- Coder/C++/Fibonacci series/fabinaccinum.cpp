#include <bits/stdc++.h>
using namespace std;

int fibonacci(int n)
{
    if (n <= 1)
        return n; /*Here we are printing the first three numbers of fibbonacci series
                    if the entered number by user is either=1 (or) equals=0. */

    return fibonacci(n - 1) + fibonacci(n - 2); /*printing the rest of the terms here.*/
                                    
                  /*Hope we all know the main logic of fibbonacci series,i.e is the sum 
                  of the two consecutive indices values is equal to next term
                  Ex= 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...*/
                                                
}

int32_t main()
{
 /*Example 1:

Find the Fibonacci number when n=5, using recursive relation.

Solution:

The formula to calculate the Fibonacci Sequence is: Fn = Fn-1+Fn-2

Take: F0=0 and F1=1

Using the formula, we get

F2 = F1+F0 = 1+0 = 1

F3 = F2+F1 = 1+1 = 2

F4 = F3+F2 = 2+1 = 3

F5 = F4+F3 = 3+2 = 5

Therefore, the fibonacci number is 5.

*/
     int n; 
    cin >> n;
    cout << fibonacci(n);

    return 0;
}
// fibonacci series using recursion

import java.util.Scanner;
public class RecursiveFibonacciSeries {

public static  int fibonacci(int n) {        //here n is the number of terms in series
     if ((n == 0) || (n == 1))
        return n;
     else
        return fibonacci(n - 1) + fibonacci(n - 2);     //recursive call to fibonacci function
  }

public static void main(String[] args) {
Scanner sc=new Scanner(System.in);  
System.out.print("Enter the number of terms you want in series: ");  
int n=sc.nextInt();

int  m=0;
System.out.print("The  fibonacci series is -  ");
for(int i=1; i<=n; i++) {
System.out.print("  " + fibonacci(m));
m++;
}
}

}


//Time Complexity:-  O(2^n)


 // fibonacci series using iteration

import java.util.Scanner;

public class IterativeFibonacciSeries {

public static void fibonacci(int n)     //here n is the number of terms in series
    {
        int num1 = 0, num2 = 1, m = 0;       //m is the counter which starts from 0
 while (m < n) {
   System.out.print(num1 + " ");
              int num3;
             num3 = num2 + num1;
            num1 = num2;
            num2 = num3;
            m++;
        }
    }

public static void main(String[] args) {
Scanner sc=new Scanner(System.in);  
System.out.print("Enter the number of terms you want in series: ");  
int n=sc.nextInt();

System.out.print("The  fibonacci series is -  ");
fibonacci(n);  
     }

}


//Time Complexity :- O(n)
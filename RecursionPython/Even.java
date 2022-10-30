import java.util.*;

public class Even
{
    static void calEven(int n)//static method so no need to make object
    {
        
        if(n>2)
            calEven(n-2);//recursive call till n>2.
        
        System.out.print(n+" ");//printing after the condition n>2 becomes false.

    }

    public static void main(String args[])
    {
        
        Scanner sc = new Scanner(System.in);//for the user input
        
        System.out.println("Enter any number : ");
        
        int num = sc.nextInt();//input of number from the user
        
        //calEven is a static method so no need to make the object.
        
        System.out.println("The Even Numbers : "+calEven(num*2));//function call from the user
        
        sc.close();//closing the scanner object to prevent leaking

    }
}
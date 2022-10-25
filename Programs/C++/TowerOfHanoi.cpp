
// Rules of Tower of Hanoi:
// 1. Only one disc can be moved at a time.
// 2. Only the top disc on any peg can be moved to any other peg.
// 3. A larger disc can’t be placed on a smaller peg.
#include <iostream>
using namespace std;

int binarySearch(int arr[], int find, int first, int end){ //this method is commom for all Binary Search examples.
    if(first>end){ //if first element is greater then last(end) element then it will return -1.(base condition)
        return -1;
    }
    int middle=(first+end)/2;{ //find middle of the binarySearch so we can easily Travers from its left and right side
        if(arr[middle]==find){ //if find(target) element is equal to middle then it will return that value of middle
            return middle;
        }else if(arr[middle]>find){ 
            return binarySearch(arr,find,first,middle-1);
        }
        else{
            return binarySearch(arr,find,middle+1,end); //if middle is smaller then target
        }
    }
}  
    void towerOfHanoi(int start,int finish,char source,char aux,char destination){ //start -> (first disc) and finish -> (last disc), Source(peg1) where the all discs are present initially, aux(peg2) middle one and destination(peg3) where all the discs to be moved here. 
        if(start>finish){ //base condition
            return;//return the function
        }
        //recursion(n-1)
        towerOfHanoi(start,finish-1,source,destination,aux);
        cout<<"move disc"<< finish <<" from "<<source<<" to "<<destination<<endl;
        towerOfHanoi(start,finish-1,aux,source,destination); 
    }
int TowerOfHanoi(){
    towerOfHanoi(1,4,'A','B','C'); //here 4 discs are present you can change count of disc from 1 to n. A,B,C are the peg in towerOfHanoi 
}



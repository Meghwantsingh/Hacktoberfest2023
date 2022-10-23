#include <iostream>
using namespace std;

int binarySearch(int arr[], int find, int first, int end){
    if(first>end){
        return -1;
    }
    int middle=(first+end)/2;{
        if(arr[middle]==find){
            return middle;
        }else if(arr[middle]>find){
            return binarySearch(arr,find,first,middle-1);
        }
        else{
            return binarySearch(arr,find,middle+1,end);
        }
    }
}  
    void towerOfHanoi(int start,int finish,char source,char aux,char destination){
        if(start>finish){
            return;
        }
        towerOfHanoi(start,finish-1,source,destination,aux);
        cout<<"move disc"<< finish <<" from "<<source<<" to "<<destination<<endl;
        towerOfHanoi(start,finish-1,aux,source,destination); 
    }
int TowerOfHanoi(){
    towerOfHanoi(1,4,'A','B','C');
}



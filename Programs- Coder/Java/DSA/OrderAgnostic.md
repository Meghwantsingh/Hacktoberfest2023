# Program Eg: |Input: arr[] = [-12,-34,56,12,56,78,88] target = 78| --- |Output: 5|


## Question

> Order Agnostic Binary Search.

## Solution

public class OrderAgnosticBinarySearch {
    static int OrderAgnosticBS(int[] arr, int target){
        int start = 0;
        int end = arr.length-1;

        boolean inAsc = arr[start] <= arr[end];

        while(start <= end){
            int mid = start + (end - start)/2;

            if(arr[mid] == target){
                return  mid;
            }

            if(inAsc){
                if(target > arr[mid]){
                     start = mid + 1;
                }
                else{
                    end = mid - 1;
                }
            }
            else{
                if(target < arr[mid]){
                    end = mid - 1;
                }
                else{
                    start = mid + 1;
                }
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        int arr[] = {-12,-34,56,12,56,78,88};
        int target = 78;
        int ans = OrderAgnosticBS(arr,target);
        System.out.println(ans);
    }
}

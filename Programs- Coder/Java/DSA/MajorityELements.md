# Program Eg: |Input: nums = [2,2,1,1,1,2,2] | --- |Output: 2|

## Question

> Given an array nums of size n, return the majority element.
> The majority element is the element that appears more than ⌊n / 2⌋ times.
> You may assume that the majority element
> always exists in the array.

## Solution

> class Solution {
> public int majorityElement(int[] nums) {
>
>         //a simple solution can be using Hash maps but its not optimal
>        //it will be in TC of O(nlogn) and SC of O(n)
>        /*********************OPTIMAL APPROACH (Moore’s Voting Algorithm)************/
>        int n=nums.length;
>         int vote =0,leader=0;
>        for(int i=0;i<n;i++)
>        {
>           if(vote==0) leader=nums[i];//when we start the process we choose 0th element as leader
>           if(leader==nums[i]) vote++;//now when we see its appearance again in array we UPVOTE
>           else vote--;//if we see some othe element we DOWN VOTE
>
>           //if current leader votes become 0 means its not the ans hence by help of first if
>           //we again put new element as leader, then carry on the process
>       }
>       return leader;
>
> }
> }

def sumDigits(no):  
    if no == 0:  
        return 0  
    else :  
        return int(no % 10) + sumDigits(int(no / 10))  
nums = int(input("Enter a number: "))  
print("The sum is:", sumDigits(nums))  
def power_of_num(num, topwr):  
    if topwr == 0:  
        return 1  
    else:  
        return num * power_of_num(num, topwr - 1)  
  
print('{} to the power of {} is: {} '.format(4, 7, power_of_num(3, 7)))  
print('{} to the power of {} is: {} '.format(2, 8, power_of_num(4, 3)))  
def merge_sort(list1):  
    length = len(list1)  
    if length > 1:  
        middle = length // 2  
        left_arr = list1[:middle]  
        right_arr = list1[middle:]  
  
        merge_sort(left_arr)  
        merge_sort(right_arr)  
  
        p = 0  
        q = 0  
        r = 0  
  
        left_length = len(left_arr)  
        right_length = len(right_arr)  
        while p < left_length and q < right_length:  
            if left_arr[p] < right_arr[q]:  
                list1[r] = left_arr[p]  
                p += 1  
            else:  
                list1[r] = right_arr[q]  
                q += 1  
  
            r += 1  
  
        while p < left_length:  
            list1[r] = left_arr[p]  
            p += 1  
            r += 1  
  
        while q < right_length:  
            list1[r] = right_arr[q]  
            q += 1  
            r += 1  
  
list1 = [24, 11, 50, 27, 16, 36, 60, 91]  
print("Input Array: ")  
print(list1)  
merge_sort(list1)  
print("Sorted Array :")  
print(list1) 
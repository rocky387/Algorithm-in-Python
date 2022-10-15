def Binary_Search(arr,element,low,high):
    if low>high:
        return False
    else:
        mid_element=(low+high)//2
        print("high",high,"low",low,"mid",arr[mid_element])
        if(element==arr[mid_element]):
            return mid_element
        elif element>arr[mid_element]:
            return Binary_Search(arr,element,mid_element+1,high)
        else:
            return Binary_Search(arr,element,low,mid_element-1)
    return -1

arr=[1,2,3,4,5,6]
print(Binary_Search(arr,4,0,len(arr)-1))


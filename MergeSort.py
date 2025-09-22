def merge(left,right):
    li,ri=0,0
    lenl=len(left)
    lenr=len(right)
    result=[]
    while li<lenl and ri<lenr:
        if left[li]<right[ri]:
            result.append(left[li])
            li+=1
        else:
            result.append(right[ri])
            ri+=1
    result.extend(left[li:])
    result.extend(right[ri:])
    return result
def merge_sort(arr):
    if len(arr)<2:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)


def merge(A,start,mid,end):
    n1=mid-start+1 
    n2=end-mid 
    left_arr=[0 for _ in range(n1)]
    right_arr=[0 for _ in range(n2)]
    for i in range(n1):
        left_arr[i]=A[start+i]
    for j in range(n2):
        right_arr[j]=A[mid+1+j]
    left=right=0 
    k=start 
    while(k-start<n1+n2):
        if(right>=n2 or (left<n1 and left_arr[left]<=right_arr[right])):
            A[k]=left_arr[left]
            left+=1 
        else:
            A[k]=right_arr[right]
            right+=1 
        k+=1 

def mergeSort(A,left,right):
    if(left<right):
        mid=left+(right-left)//2 
        mergeSort(A,left,mid)
        mergeSort(A,mid+1,right)
        merge(A,left,mid,right)

n=int(input())
A=[int(x) for x in input().split()]
mergeSort(A,0,n-1)
print(A)
def bubblesort(arr):
    a=len(arr)
    for i in range(a):
        for j in range(0,a-i-1):
            if arr[j]>[j+1]:
                 arr[j],arr[j+1]=arr[j+1],arr[j]
                 print("sorted list:",arr)
stack=[]
b=int (input("Enter how many eklements:"))
for i in range(b):
    element=int(input("Enter stack element:"))
    stack.append(element)
    bubblesort(stack)

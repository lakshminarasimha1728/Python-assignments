#Write a function to add integer values of an array
def add(arr):
    s=0
    for i in arr:
        s+=i
    return s

arr=list(map(int,input().split()))
print(add(arr))

#Write a function to calculate the average value of an array of integers
def avg(arr):
    s= 0
    c=0
    for i in arr:
        s+=i
        c+=1
    return s/c if c!=0 else 0
arr=list(map(int,input().split()))
print(avg(arr))

    
#Write a program to find the index of an array element
def find(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    return "Not found"
arr=list(map(int,input().split()))
e=int(input("Enter element to find: "))
print(find(arr, e))

#Write a function to test if array contains a specific value
def value(arr, val):
    for i in arr:
        if i==val:
            return True
    return False
arr=list(map(int,input().split()))
e=int(input("Enter element to check: "))
print(value(arr,e))


#Write a function to remove a specific element from an array


arr=list(map(int,input().split()))
e=int(input("Enter element to find: "))
arr.remove(e)
print(arr)
#Write a function to copy an array to another array
def copy(arr):
    b=[]
    for i in arr:
        b.append(i)
        return b
arr=list(map(int,input().split()))
print(copy(arr))

#Write a function to insert an element at a specific position in the array
arr=list(map(int,input().split()))
e=int(input("Enter element to insert: "))
p=int(input("Enter position to insert: "))
arr.insert(p,e)
print(arr)
#Write a function to find the minimum and maximum value of an array
arr=list(map(int,input().split()))
print(min(arr))
print(max(arr))

#Write a function to reverse an array of integer values
arr=list(map(int,input().split()))
arr1 = []
for i in range(len(arr)-1,-1,-1):
    arr1.append(arr[i])
print(arr1)

#Write a function to find the duplicate values of an array
arr=list(map(int,input().split()))
dup=[]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i]==arr[j] and arr[i] not in dup:
            dup.append(arr[i])
print(dup)

#Write a program to find the common values between two arrays
arr=list(map(int,input().split()))
arr1=list(map(int,input().split()))
common=[]
for i in arr:
    for j in arr1:
        if i == j and i not in common:
            common.append(i)
print(common)

#Write a method to remove duplicate elements from an array
arr=list(map(int,input().split()))
arr1=set(arr)
print(list(arr1))

#Write a method to find the second largest number in an array
arr=list(map(int,input().split()))
arr.sort()
print(arr[-2])

#Write a method to find the second smallest number in an array
arr=list(map(int,input().split()))
arr.sort()
print(arr[1])
#Write a method to find number of even number and odd numbers in an array
arr=list(map(int,input().split()))
even=0
odd=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Number of even numbers:",even )
print("Number of odd numbers:", odd)
  
#Write a function to get the difference of largest and smallest value
arr=list(map(int,input().split()))
arr.sort()
print(arr[-1]-arr[0])

#Write a method to verify if the array contains two specified elements(12,23)
arr=list(map(int,input().split()))
a,b=12,23
if a in arr and b in arr:
    print("Array contains both elements")
else:
    print("Array does not contain both elements")
#Write a program to remove the duplicate elements and return the new array
arr=list(map(int,input().split()))
arr1=list(set(arr))
print(arr1)

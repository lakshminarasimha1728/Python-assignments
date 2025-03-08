#Write a function for arithmetic operators(+,-,*,/)

a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
print("Addition: ", a+b)
print("Subtraction: ", a-b)
print("Multiplication: ", a*b)
print("Division: ", a/b)


#Write a method for increment and decrement operators(++, --)

a=0
a+=1
a=a+1
b=5
b-=1
b=b-1
print("Incremented value of a: ", a)
print("Decremented value of b: ", b)

for i in range(0,5):#"incremented for loop"
    print(i)

for i in range(5,-1,-1):#"decremented for loop"
    print(i)
#Write a program to find the two numbers equal or not

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
if x==y:
    print("Both are equal")
else:
    print("Both are not equal")
#Program for relational operators (<,<==, >, >==)

a=5
b=4
print("a<b: ", a<b)
print("a<=b: ", a<=b)
print("a>b: ", a>b)
print("a>=b: ", a>=b)
print("a==b", a==b)
print("a!=b", a!=b)


#Print the smaller and larger number

a=int(input())
b=int(input())
# to find the greater number
if a>b:
    print(a, " is greater")
else:
    print(b," is greater")

#to find the smaller number

if a<b:
    print(a, " is smaller")
else:
    print(b," is smaller")

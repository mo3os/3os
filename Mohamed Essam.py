#Question 1:
#1)
x=65
y=53
z=not y if(x%2!=0) else x
print(z)

>>> false

#Question 2: 
#1)
def getnumbersfromfunc():
 x = y = z =10
 return x
 return y
 return z
print(getnumbersfromfunc())

>>> 10

#2)
def sum(num):
     def add(x):
      return num+x
     return add 
print(sum(12)(5)) 

#Question3:
#1)
s=input("Enter the Number: ")
reverse=s[::-1]
if(s==reverse):
    print("It is palindrome")
else:
    print("No it is not palindrome")

#4)
def multiplication():
    num=int(input("Enter the Number: "))
    for i in range(1,11):
        print(num,"x",i,"=",num*i)

print(multiplication())

#5)
list=[1,2,3,4,5,6]

for i in range(len(list)-1,-1,-1):
    print(list[i])

#7)
for FizzBuzz in range(1,50):
    if FizzBuzz %3==0:
     print("Fizz")
     continue
    elif FizzBuzz %5==0:
        print("Buzz")
        continue
    elif FizzBuzz %3==0 and FizzBuzz % 5==0:
        print("FizzBuzz")
        continue
    print(FizzBuzz)





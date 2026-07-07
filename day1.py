#Basic Syntax 
print("Hello world!!") #printing





#Variable Declaration, naming convention


x = 5 #alpha
print(x)


_ = 5
print(_)



#9num = 4 
#print(9num)



#if =5
#print(if)


num_9 =3 
print(num_9)


#Camel case 
myName ='alisha'
print(myName)


#Pascal
MyName ="Alisha"
print(MyName)


#camel
my_name = "Alisha"

#User input

name =input("Enter your name:")
age = input("Enter your age:")
print(name)

print(age)
print("Name:",name,"Age:", age)


print(name,age)


#Data types: integer, float, boolean, complex

x = 4
y = 3.3 
z = True
c = 1+1j #1j do not left j alone 
print(x,y,z)
print(c)


print(type(x))
print(type(y))
print(type(z))
print(type(c))

#Import module 

import sys 
print(sys.getsizeof(x))
print(sys.getsizeof(y))
print(sys.getsizeof(z))
print(sys.getsizeof(c))



#String 

text = "Hello"
print(text)
#Escape

text = "Hello, \"Ram\""
print(text)

#tRIPLE QUOTE 
te ='''
Hi,
I am bored 
         

'''
print(te)



#Indexing


fruit="apple"
print(fruit[0])
print(fruit[0:5])
print(fruit[0:5:2])
print(fruit[::])
print(fruit[-6:-1])
print(fruit[-1:-6])

#Method
text = "Hello world"
print(text.upper())
print(text.lower())
#LENGTH 
print(len(text))
#strip
text=" hello world "
print(len(text.strip()))
print(text.split())

#replace
print(text.replace("world","there"))
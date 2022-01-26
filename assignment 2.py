#QUESTION=1
#given information
my_string ='Python is a case sensitive language'
#a
print(len(my_string))
#b
print(my_string[::-1])
#c
name=my_string[10:]
print(name)
#d
print(my_string.replace('a case sensitive','object oriented'))
#e
print(my_string.index('a'))
#f
print(my_string.replace(' ',''))


#QUESTION=2
name='Tanmay'
SID=21104116
dep='Electrical Engineering'
CGPA=9.9
print('Hey',name,'Here!')
print('My SID is',SID)
print('I am from',dep,'department and my CGPA is',CGPA)


#QUESTION=3
a=56
b=10
print(a&b)
print(a|b)
print(a^b)
print(a<<2)
print(b<<2)
print(a>>2)
print(b>>4)


#QUESTION=4
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
z=int(input("Enter third number:"))
largest=x
for i in[x,y,z]:
   if largest<i:
       largest=i
print('largest numbere is:',largest)       

#QUESTION=5
string = str(input("type a sentence:"))
if "name" in string:
 print("Yes")
else:
 print("No")

#QUESTION=6
x=float(input('Length of 1st side:'))
y=float(input('Length of 2nd side:'))
z=float(input('Length of 3rd side:'))
p=int(x)
q=int(y)
r=int(z)
#A triangle is formed only when the sum of any two side is greater than or equal to the third one             
if p>=(q+r) and q>=(p+r) and r>=(p+q):
 print('No,Triangle cannot be formed')
else:
 print('Yes,Triangle can be formed')
  

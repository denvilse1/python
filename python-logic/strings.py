a="This is Elon Musk"
print(a)
print(a[1])
print("------------------")

# printing characters in strings 
# way one 
for i in a:
    print(i,end="==")
print()
print("++++++++++++++")

for i in range(0,len(a)):
    print(a[i],end="++")

print()

print("This is Ram's pen")
print('Some once said "if you are failing to prepare, then you are preparing to fail"')
print("some once said \"God favors the brave\" : let's see")

print("comparing two strings")
a=input("Enter your first string ")
b=input("Enter your second string")

if a==b:
    print(f"both are same .i.e. is {a} and {b}")
else:
    print(f"{a} and {b} they  are not equal")


using ord() and chr()
a='d'
b=ord(a)
print(b)
b=chr(b)
print(b)

using .split()

a="my name is Elon Musk"
print(a.split())

a=" "
print(ord(a))

# analysing white spacing using the ord function
for i in a:
    print(ord(i),end="----")

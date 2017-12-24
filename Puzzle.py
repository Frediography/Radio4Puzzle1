# # It is less than 100
# # It's one more than a multiple of 3
# Exactly one of the digits is prime
# If you reverse the digits you get a prime number
# It has exactly 4 factors
# The sum of the digits is prime
# # If you multiply it by 5, it's greater than 100

mylist = []
mylist2 =[]

def GetList():
## It is less than 100
## If you multiply it by 5, it's greater than 100
    for x in range(1, 100):
        if x*5 > 100:
            mylist.append(x)

def Multipleof3(x):
# It's one more than a multiple of 3
    if (x-1) % 3 == 0:
        mylist2.append(x)

def ReverseDigits():
# If you reverse the digits you get a prime number
    for i in range (20, 10, 200):
        print(i)

# EXECUTE
GetList()
for x in mylist:
    Multipleof3(x)
ReverseDigits()
print(len(mylist2))

print(mylist)
print(mylist2)
'''
if 3 % 2 == 0:
    print (yes)
else:
    print("no")
'''

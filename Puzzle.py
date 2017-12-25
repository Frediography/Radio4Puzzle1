# # It is less than 100
# # It's one more than a multiple of 3
# # Exactly one of the digits is prime
# # If you reverse the digits you get a prime number
# It has exactly 4 factors
# The sum of the digits is prime
# # If you multiply it by 5, it's greater than 100

mylist = []
splitdigits = []
mylist2 = [] #debug list
debug = 1

def GetList():
## It is less than 100
## If you multiply it by 5, it's greater than 100
    for x in range(1, 100):
        if x*5 > 100:
            mylist.append(x)

def Multipleof3():
# It's one more than a multiple of 3
    for x in mylist:
        if (x-1) % 3 != 0:
            mylist.remove(x)
            mylist2.append(x)
    if debug == 1:
        print("Removed the following, that aren't one more than a multiple of 3: ")
        print(mylist2)

def SplitDigits():
#
# - lets first take out evens
#    for i in range(20,81,20):
#        for y in range(i, i+10):
#            if mylist2.count(y) > 0:
#                mylist2.remove(y)
#
    mylist2 = []
    for x in mylist:
        b = list(str(x))
        c = int(b[0])
        p = 0
        if PrimeDigit(c) == 1:
            p += 1
        d = int(b[1])
        if PrimeDigit(d) == 1:
            p += 1
        if p != 1:
            mylist.remove(x)
            mylist2.append(x)
    if debug == 1:
        print("Removed the following, that do not have exactly one prime digit: ")
        print(mylist2)

def ReversedNumbers():
    mylist2 = []
    for x in mylist:
        b = list(str(x))
        a = int(str(b[1]) + str(b[0]))
        if PrimeDigit(a) == 0:
            mylist.remove(x)
            mylist2.append(x)
    if debug == 1:
        print("Removed the following, that when reversed are not prime numbers: ")
        print(mylist2)

def SumIsPrime():
    mylist2 = []
    for x in mylist:
        b = list(str(x))
        c = int(b[0])
        d = int(b[1])
        e = c + d
        if PrimeDigit(e) != 1:
            mylist.remove(x)
            mylist2.append(x)
    if debug == 1:
        print("Removed the following, that when the digits are added together, do not make a prime number: ")
        print(mylist2)

def PrimeDigit(num):
    if num == 2:
        return(0)
    for i in range(2,num):
        if (num % i) == 0:
            return(0)
        else:
            return(1)

# EXECUTE
GetList()
print("New list:")
print(mylist)
Multipleof3()
print("New list:")
print(mylist)
ReversedNumbers()
print("New list:")
print(mylist)
SplitDigits()
print("New list:")
print(mylist)
SumIsPrime()
print("New list:")
print(mylist)
print(len(mylist))

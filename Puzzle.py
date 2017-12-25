# Create variables we'll use throughout:
debug = 1
debuglist = []
mylist = [] # List we'll use to cut down as we go on

# Create a function to check for prime numbers
def PrimeNumber(x):
    if x == 2:
        return(0)
    for i in range(2,x):
        if (x % i) == 0:
            return(0)
        else:
            return(1)

# # It is less than 100
def LessThan100():
    for i in range(1, 100):
        mylist.append(i) # Must start with this because of the way I've written it
    if debug == 1:
        print("Added the following numbers below 100: ")
        print(mylist)

# # It's one more than a multiple of 3
def OneMoreThanMult3():
    debuglist = []
    for i in range(1,100):
        if int((i - 1)) % 3 != 0:
            if i in mylist:
                mylist.remove(i)
                debuglist.append(i)
    if debug == 1:
        print("Removed the following, that aren't one more than a multiple of 3: ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# # Exactly one of the digits is prime
def OnePrimeDigit():
    debuglist = []
    for i in range(10, 100):
        a = 0
        b = list(str(i))
        c = int(str(b[0]))
        d = int(str(b[1]))
        if PrimeNumber(c) == 1:
            a += 1
        if PrimeNumber(d) == 1:
            a += 1
        if a != 1:
            if i in mylist:
                mylist.remove(i)
                debuglist.append(i)
    if debug == 1:
        print("Removed the following, that don't have exactly 1 prime digit ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# # If you reverse the digits you get a prime number
def ReversedPrime():
    debuglist = []
    for x in range(11,100):
        b = list(str(x))
        a = int(str(b[1]) + str(b[0]))
        if PrimeNumber(a) == 0:
            if x in mylist:
                mylist.remove(x)
                debuglist.append(x)
    if debug == 1:
        print("Removed the following, that aren't prime numbers when reversed: ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# # It has exactly 4 factors
def FourFactors():
    debuglist = []
    for i in range (10, 100):
        x = 0
        for j in range (1, i):
            if i % j == 0:
                x += 1
        if x != 4:
            if x in mylist:
                mylist.remove(x)
                debuglist.append(x)
    if debug == 1:
        print("Removed the following that don't have four factors: ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# # The sum of the digits is prime
def SumIsPrime():
    debuglist = []
    for x in range(10,100):
        b = list(str(x))
        a = int(str(b[0])) + int(str(b[1]))
        if PrimeNumber(a) == 0:
            if x in mylist:
                mylist.remove(x)
                debuglist.append(x)
    if debug == 1:
        print("Removed the following, that isn't a prime number when the digits are added together: ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# # If you multiply it by 5, it's greater than 100
def Mult5Bigger100():
    debuglist = []
    for i in range(1, 100):
        if (i * 5) < 100:
            if i in mylist:
                mylist.remove(i)
                debuglist.append(i)
    if debug == 1:
        print("Removed the following, that when multiplied by 5 aren't greater than 100: ")
        print(debuglist)
        print("The new list of ", len(mylist), " possibilities is as follows: ")
        print(mylist)

# Execute functions
LessThan100() # Need to start with this one
OneMoreThanMult3()
ReversedPrime()
SumIsPrime()
OnePrimeDigit()
FourFactors()
Mult5Bigger100()

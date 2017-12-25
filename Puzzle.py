# # It is less than 100
# # It's one more than a multiple of 3
# Exactly one of the digits is prime
# If you reverse the digits you get a prime number
# It has exactly 4 factors
# The sum of the digits is prime
# # If you multiply it by 5, it's greater than 100

mylist = []

def GetList():
## It is less than 100
## If you multiply it by 5, it's greater than 100
    for x in range(1, 100):
        if x*5 > 100:
            mylist.append(x)

def Multipleof3():
# It's one more than a multiple of 3
    for x in mylist:
        if (x-1) % 3 == 0:
            mylist.remove(x)

def ReverseDigits():
# If you reverse the digits you get a prime number
#
# - lets first take out evens
#    for i in range(20,81,20):
#        for y in range(i, i+10):
#            if mylist2.count(y) > 0:
#                mylist2.remove(y)
#
    print(mylist)
    for x in mylist:
        print(x)
        b = list(str(x))
        print(b)
        a = int(str(b[1]) + str(b[0]))
        print(a)

def PrimeDigit(num):
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number")
            return(0)
            break

# EXECUTE
GetList()
Multipleof3()
ReverseDigits()
print(mylist)

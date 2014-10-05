#!/opt/local/bin/python
import math
import sys

#List limit # of primes
def listPrimes(limit): 
    for input in range(2,limit):
        if checkPrime(input):
            print(input)

#Check if input is prime
def checkPrime(input):
    firstTry = [2,3,5]
    for p in firstTry: #Try simple ones
        if input == p:
            return True
        elif input % p == 0:
            return False
    #Brute force
    sqrt=math.floor(math.sqrt(input))+1
    for x in range(7,sqrt,2): #Check if every number btw 7 and sqrt(input) is divisble incrementing by 2 each time
        if input % x == 0:
            return False
    return True

#Prints usage screen
def usage():
    print("USAGE: "+sys.argv[0]+" Int")
    print("Please provide a valid numberical input as a paramter.")
    print("This should be the last number to test for primeness.")

if len(sys.argv) == 0:
    usage()
else:
    try:
        val = int(sys.argv[1])
        listPrimes(val)
    except ValueError:
        print("Not a valid integer")
        usage()

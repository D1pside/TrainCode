import sys
import time 
def funcA(a):
	a=str(input("High or floor?"))
	if a=="High" or a=="high":
		a="H"
		return a
	elif a=="Floor" or a=="floor":
		a="F"
		return a 
	else:
		sys.exit("Error:invalid argument")


def funcJ(j):
	u=str(input("Left ot right?"))
	if j== "Left"or j=="left":
		j=="L"
		return j
	elif j=="Right" or j=="right":
		j=="R"
		return j
	else:
		sys.exit("Error:invalid argument")


def funcU(u):
	u=int(input("Number of van?"))
	if u>4:
		sys.exit("Error:invalid argument")
	return u


def funcI(i):
	i=int(input("quantity of places"))
	if i>6:
		sys.exit("Error:invalid argument")
	return i

def Concl():
	print("Compiling your code...")
	sleep.time(6.0)
	print("Your code compiling successful!Copy your code and remember this...")
	print("Compiling...")
	print("Your code:",funcA,funcU,funcJ,funcI)
  
sys.exit(0)

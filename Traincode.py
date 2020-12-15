import sys 
##High or floor?
def funcA(a):
	a=str(input("High or floor?"))
	if a=="High" or a=="high":
		a="H"
		return a
	elif a=="Floor" or a=="floor":
		a="F"
		return a 
	else:
		sys.exit(0)

##Left ot right?
def funcJ(j):
	u=str(input("Left ot right?"))
	if j== "Left"or j=="left":
		j=="L"
		return j
	elif j=="Right" or j=="right":
		j=="R"
		return j
	else:
		sys.exit(0)

##Number of van?
def funcU(u):
	u=int(input("Number of van?"))
	if u>4:
		sys.exit(0)
	return u

##Quantity of places?
def funcI(i):
	i=int(input("quantity of places"))
	if i>6:
		sys.exit(0)
	return i
##Conclusion
def Concl():
	print("Compiling your code...")
	sleep.time(6.0)
	print("Your code compiling successful!Copy your code and remember this...")      ## Exit program code
	print("Compiling...")
	print("Your code:",a,j,u,i)



0=str(input("Decrypt your code? [y/n]"))
if o=="n" or o=="N":
	sys.exit(0)
if else o=="y" or o=="Y":                                                ## Check your answer [y/n]
	o==1
else 
	print("Invalid argument:exiting program")
	sys.exit(0)



m=str(input("Putting  first letter of your code for parts (example:H for code HL34"))
if m=="h" or m=="H":
	p=="High"
if else m=="F" or m=="f":                                   ## P for high or floor places
	p=="Floor"
else
	print("Invalid argument:exiting program")
	sys.exit(0)
del(m)
m=str(input("Putting  second letter of your code for parts (example:L for code HL34"))
if m=="L" or m=="l":
	k=="Lefy side"
if else m=="r" or "R"                                    ## K for left or right sides
	k=="Right side"
else 
	print("Invalid argument:exiting program")
	sys.exit(0)
del(m)
m=int(input("Putting third symbol of your code for parts (example:3 for code HL34"))
if m==1:
	s==1
if else m==2:
	s==2
if else m==3:                                           ## S for number of van
	s==3
if else m==4:
	s==4
else 
	print("Invalid argument:exiting program")
	sys.exit(0)
del(m)
m=int(input("Putting fourth symbol of your code for parts (example:4 for code HL34"))
if m==1:
	q==1
if else m==2:
	q==2
if else m==3:                                  ## Q for quantity of places
if else m==4:
	q==4
else 
	print("Invalid argument:exiting program")
	sys.exit(0)
del(m)



##Input decode code
print("The decryption was successful")
print("Take",p,"place")
print("Your place located on",k,"side")
print("Your van number is:",s)
print("Your took",q,"place/s")


##Exit program
sys.exit(0)

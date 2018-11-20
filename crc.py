import struct
import sys

val1='1'
val2='1'


if (len(sys.argv)>1):
        val1=str(sys.argv[1])

if (len(sys.argv)>2):
        val2=str(sys.argv[2])


def showpoly(a):
	str1 = ""
	nobits = len(a)


    	for x in range (0,nobits-2):
		if (a[x] == '1'):
			if (len(str1)==0):
				str1 +="x**"+str(nobits-x-1)	
			else: 
				str1 +="+x**"+str(nobits-x-1)

	if (a[nobits-2] == '1'):
		if (len(str1)==0):
			str1 +="x"
		else:
			str1 +="+x"

	if (a[nobits-1] == '1'):
		str1 +="+1"

	print str1;
	

def toList(x):
	l = []
	for i in range (0,len(x)):
		l.append(int(x[i]))
	return (l)
def toString(x):
	str1 =""
	for i in range (0,len(x)):
		str1+=str(x[i])
	return (str1)

def divide(val1,val2):
	a = toList(val1)
	b = toList(val2)
	working=""
	res=""

	while len(b) <= len(a) and a:
    		if a[0] == 1:
        		del a[0]
        		for j in range(len(b)-1):
            			a[j] ^= b[j+1]
        		if (len(a)>0):
				working +=toString(a)

				res+= "1"
		else:
        		del a[0]
			working +=toString(a)
        		res+="0"

	print "Result is\t",res
	print "Remainder is\t",toString(a)

	return 

print "Binary form:\t",val1," divided by ",val2
print "Decimal form:\t",int(val1,2)," divided by ",int(val2,2)
print ""

showpoly(val1)
showpoly(val2)

print "\nDivide operation:\n"

divide(val1,val2)
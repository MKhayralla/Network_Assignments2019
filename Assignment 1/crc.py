import sys 


val1 = '1'
val2 = '1'
if (len(sys.argv) < 2):
    print('usage : "python crc.py <filename>.txt"\nor\t"./crc <filename>.txt"(from dist folder)')
    sys.exit()

fileName = str(sys.argv[1])

lines = [line.rstrip('\n') for line in open(fileName)]
val1 = lines[0]
val2 = lines[1]



def showpoly(a):
    str1 = ""
    nobits = len(a)

    for x in range(0, nobits-2):
        if (a[x] == '1'):
            if (len(str1) == 0):
                str1 += "x**"+str(nobits-x-1)
            else:
                str1 += "+x**"+str(nobits-x-1)

    if (a[nobits-2] == '1'):
        if (len(str1) == 0):
            str1 += "x"
        else:
            str1 += "+x"

    if (a[nobits-1] == '1'):
        str1 += "+1"

    print str1


def toList(x):
    l = []
    for i in range(0, len(x)):
        l.append(int(x[i]))
    return l


def toString(x):
    str1 = ""
    for i in range(0, len(x)):
        str1 += str(x[i])
    return (str1)

#generator fn
def generate(val1, val2):
    print('generating the message from the payload : \t' + val1)
    a = toList(val1)
    b = toList(val2)
    c= [0] * (len(b)-1)
    a.extend(c) #adding zeros to the end of the message
    working = ""
    res = ""

    while len(b) <= len(a) and a:
        if a[0] == 1:
            del a[0]
            for j in range(len(b)-1):
                a[j] ^= b[j+1]
            if (len(a) > 0):
                working += toString(a)

                res += "1"
        else:
            del a[0]
            working += toString(a)
            res += "0"

    
    print "Result is\t", res
    print "Remainder is\t", toString(a)
    print "New message is\t", toString(val1)+toString(a)
    return toString(val1)+toString(a) #return new message

#verify fn
def verify(val1, val2):
    print('verifying the message : \t' + val1)
    a = toList(val1)
    b = toList(val2)
    working = ""
    res = ""

    while len(b) <= len(a) and a:
        if a[0] == 1:
            del a[0]
            for j in range(len(b)-1):
                a[j] ^= b[j+1]
            if (len(a) > 0):
                working += toString(a)

                res += "1"
        else:
            del a[0]
            working += toString(a)
            res += "0"

    print "Result is\t", res
    rem = toString(a)
    print "Remainder is\t", rem
    for i in range(0, len(rem)):
        if (rem[i] != '0'):
            print 'not correct !\n-------------------------\n'
            return
    print 'correct message \n-----------------------------\n'
    return

#alter fn
def alter(new_message, bitn):

    a = toList(new_message)
    if (a[bitn-1] == 1) :
		a[bitn-1]= 0 
    else :
		a[bitn-1]= 1 

    return toString(a)


showpoly(val1)
showpoly(val2)


new_message = generate(val1, val2)
verify(new_message, val2)
option = raw_input("test the alter function ? Y/N\n")
if (option == "Y") | (option == "y") :
    bitn = int(raw_input("Enter the bit index : \n"))
    altered_message = alter(new_message, bitn)
    print('expected message : \t' + new_message + '\ntransmitted message : \t' + altered_message + '\n')
    verify(altered_message, val2)
else  : sys.exit()

def add(a, b):
    print "adding %d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "substacting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "multiply %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "dividing %d / %d" % (a, b)
    return a / b

age = add(56, 32)
height = substract(8, 2)
weight = multiply(43, 79)
iq = divide(94, 6)

print "age ---> %d, height ---> %d, weight ---> %d, IQ: %d" % (age, height, weight, iq)

what = add(age, substract(height, multiply(weight, divide(iq, 4 ))))

print "That becomes", what, "Can you do it?"

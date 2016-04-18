
from sys import argv

script, filename = argv

txt = open(filename)

print "Opening... %r" % filename
txt.read()

# txt.write("raw_input('Hola hola caracola?')")

print "Closing... %r" % filename
txt.close()

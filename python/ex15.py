from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename. Another, I know, I want you work this time at least: "

file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

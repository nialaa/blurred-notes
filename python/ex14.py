from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions... If you dare :P "
print "Do yo like to throw through a window?  %s 's sandwich xDDD" % user_name
like = raw_input(prompt)

print "Where you live, %s?" % user_name
lives = raw_input(prompt)

print "what kind of computer do you have?"
computer = raw_input(prompt)

print """

Alright, so you said %r about suicide. You live in %r and with that machine (%r).
Sad but true xD

""" % (like, lives, computer)

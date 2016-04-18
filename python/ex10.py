print "I am 6'2\" tall." #escape double-quote inside string
print 'I am 6\'2" tall.' #escape single-quote inside string

tabby_cat = "\t I'm tabbed in."
persian_cat = "I' split \non a line."
backslash_cat = "I'm \\ a \\ cat."
installation = 0

fat_cat = """

I'll do a list:
\t* Cat food
\t* Fishes 
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print "Installing npm..."
while (installation < 100000):
    for i in ["/", "-", "|", "\\", "|"]:
        print "%s\r" % i,
        installation = installation + 1

from sys import argv
script,filename = argv
txt=open(filename)
print("Here's my file %r:" % filename)
print (txt.read())

from sys import argv
script,filename= argv
print("Opening the file...")
D=open(filename)
print("Now I am reading it:")
print(D.read())


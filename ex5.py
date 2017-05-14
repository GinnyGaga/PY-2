name = 'Zed A.Shaw'
age = 35 # not a lie
height = 74# inches
weight =180 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print("I'm %(name)s.I'm %(age)d year old" % {'name':'Zed A.Shaw','age':35})

print ("Let's talk about %s." %  name)

print("He's %dcm inches tall." % (height*2.54))

print("He's %d%2.2fKG pounds heavy." % weight*0.4536)

print("Actually that's not too heavy.")

print("He's got %s eyes and %s hair." % (eyes,hair))

print("His teeth are usually %s depending on the coffee." % teeth)

# this line is tricky,try to get it exactly right
print("If I add %d,%d,and %d I get %d."  % (
age,height,weight,age + height + weight))


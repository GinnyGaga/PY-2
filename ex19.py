#定义函数，函数名，和两个函数参数，主义冒号：
def cheese_and_crackers(cheese_count,boxes_of_crackers):
	print("You have %d cheeses!" % cheese_count)
	print("You have %d boxes of crackers!" % boxes_of_crackers)
	print("Man that's enough for a party!")
	print("Get a blanket.\n")


#调用函数，直接赋值给函数名。
print("We can just give the function numbers directly:")
cheese_and_crackers(20,30)


#调用函数，重新定义参数名，重新赋值。但是函数名一直不变。
print("OR,we can use variables from our script:")
amount_of_cheese=10
amount_of_crackers=50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

#调用函数，直接实现赋值运算，相加法。
print("We can even do math inside too:")
cheese_and_crackers(10+20,5+6)

#调用函数，实现变量名和运算结合起来，进行相加。此时变量名和定义def的变量名可以不一样。
print("And we can combine the two,variables and math:")
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)


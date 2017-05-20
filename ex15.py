from sys import argv  # 將代码用到的功能模块引入脚本


script,filename = argv  # argv是参数变量，它包含n个要传递给的参数，同时自身解包，將所有的参数依次赋予左边的变量名。此时要用filename获取文件名

txt=open(filename) #接受参数filename，返回一个直，我把这个直赋予了变量txt

print("Here's your file %r:" % filename) #打印一小行文本
print(txt.read()) #读取文件。文件本身可支持一些命令，格式：句点.+命令+(参数)该参数类似open和 input，不过此时txt.read不需要任何参数

print("Type the filename again:") #再打印

file_again= input(">") # 再打印

txt_again = open(file_again) # 引出 输入格式

print(txt_again.read()) # 再读取文件

print(txt.close(),txt_again.close())

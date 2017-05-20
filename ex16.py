from sys import argv #把需要的模块引入脚本

script,filename=argv #赋予变量

print("We're going to erase %r." % filename) #即将删除文件
print("If you don't want that,hit CTRL-C (^C).")#若不想删除，按
print("If you do want that,hit RETURN.")#若要删除，按

input("?")#你的选择

print ("Opening the file...") #提醒正在打开文件
target=open(filename,'w')#执行打开文件

print("Truncating the file.Goodbye!") #提醒清空了文件
target.truncate()#清空文件

print("Now I'm going to ask you for three lines.")#在清空的文件写上其他东西

line1=input("line 1: ")#定义要写的变量
line2=input("line 2: ")
line3=input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)#执行 写
target.write("\n")#换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

#print ("I'm going to write these to the file:\n %s \n %s \n %s \n" %( line1,line2,line3))
#target.write('line1\n'+'line2\n'+'line3\n')
print ("And finally,we close it.")
target.close()#关闭文件

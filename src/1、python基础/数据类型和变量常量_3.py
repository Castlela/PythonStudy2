#字符串是以单引号'或双引号"括起来的任意文本，比如'abc'，"xyz"等等。
#请注意，''或""本身只是一种表示方式，不是字符串的一部分，
#因此，字符串'abc'只有a，b，c这3个字符。如果'本身也是一个字符，
#那就可以用""括起来，比如"I'm OK"包含的字符是I，'，m，空格，O，K这6个字符。

#如果字符串内部既包含'又包含"怎么办？可以用转义字符\来标识，比如：
print('I\'m \"OK\"!');
print('I\'m learning\nPython.')

#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，
#所以\\表示的字符就是\，#可以在Python的交互式命令行用print()打印字符串看看：
print('\\\n\\')

#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，
#Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print('\\\t\\') #转义
print(r'\\\t\\') #不转义

#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，
#Python允许用'''...'''的格式表示多行内容
print('''line1
line2
line3''')

#--------------------------------------------------------
#布尔值， 一个布尔值只有True、False两种值，要么是True，要么是False
#布尔值可以用and、or和not运算。
#True and True
#True and False
#False and False
#5 > 3 and 3 > 1

#布尔值经常用在条件判断中，比如：
age = 0;
if age >= 18:
    print('adult')
else:
    print('teenager')
    
#---------------------------------------------------------
#空值 空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。

#----------------------------------------------------------
#变量 变量在程序中就是用一个变量名表示了，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。
#静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
#例如Java是静态语言，赋值语句如下

a = 1 #变量a是一个整数。
t_007 = 'T007' #变量t_007是一个字符串。
Answer = True #变量Answer是一个布尔值True。

#改变数据类型
a = 123 # a是整数
a = 'ABC' # a变为字符串

#-----------------------------------------------------------
#常量 所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。
#在Python中，通常用全部大写的变量名表示常量：
#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变
PI = 3.14159265359

#------------------------------------------------------------
#除法运算
print(10/3) #结果：3.3333333333333335
print(9/3) #结果：3.0

#地板除，两个整数的除法仍然是整数：
print(10//3) #结果：3

#-----------------------------------------------------------
#求余
print(10%3) #结果：1
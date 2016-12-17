#if语句，注意不要少写了冒号:和缩进
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

#elif 是 else if的缩写，elif不限个数
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')
    
#if语句执行，是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age = 20
if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')

#if判断条件还可以简写，比如写：
#只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False。
x = 0;
if x:
    print('True')
    
#和input结合，再判断
#input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情
s = input('birth: ')
birth = int(s) #默认input输入是字符串，和整数对比必须转整数，但是非数字字符串是转不了数字的，会报错
if birth < 2000:
    print('00前')
else:
    print('00后')
    
#pass还可以用在其他语句里做占位符，这样不确定写什么时先用pass代替，编译就不会出错了，比如：
age = 15
if age >= 18:
    pass
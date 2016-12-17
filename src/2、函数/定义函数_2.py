#使用def定义函数
#定义名为my_abs的函数
def my_aba(x):
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs(-65));

#自定义函数，并识别如果不是数字就报错
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#print(my_abs("abc")); #当传入的不是数字参数，会报自定义错误

#空函数
#实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
def nop():
    pass


#-----------------------------------------------------------------------------------
#给函数返回多个值，例如，需要返回一个坐标。
import math #导入math包，使用数学函数
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#接收返回值（特别注意：此处和JAVA不同）
x, y = move(100, 100, 60, math.pi / 6)
#打印接收到的返回值
print(x, y)

#也可以用单一变量接收，因为返回的类型是tuple
r = move(100, 100, 60, math.pi / 6)
print(r)

#写一个函数计算x^2
#def power(x):
#    return x * x

#当要计算x^n平方时，可以
#def power(x, n):
#    s = 1
#    while n > 0:
#        n = n - 1
#        s = s * x
#    return s

#-----------------------------------------------------------------------------------------------
#位置参数 调用函数时，传入的两个值按照位置顺序依次赋给参数x和n
#JAVA也没有的默认参数*
#当用power(5)调用时，默认是计算5^2 
#当用power(5,3)调用时，默认是5^3
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

#自定义函数默认年龄和城市
#调用的时候enroll('Sarah', 'F') 如果完全按默认的来，只需提供两个参数即可
#enroll('Bob', 'M', 7)、enroll('Adam', 'M', city='Tianjin')
#不按顺序调用，例如只有age用默认。enroll('Adam', 'M', city='Tianjin')
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#当函数参数设置为list时，并让每次传入list后append("END")
#以下此做法不正确，会令到每次调用add_end()时，都继续增加一个END
#例如，第一次执行是['END'],第二次执行是['END','END']
#def add_end(L=[]):
#    L.append('END')
#    return L
#正确做法应该让参数中的L=None让L指向一个不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end());

#定义的参数可以直接传入一个list，或tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#调用函数
calc([1, 2, 3])
#或
calc((1, 3, 5, 7))
#--------------------------------------------------------------------------------------------------------
#可变参数，可变参数允许你传入0个或任意个参数
#把以上函数，改为接收可变参数的函数
def calc_1(*numbers): #可变参数接收的是tuple，和普通函数相比，参数多了个*
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#调用函数
calc_1(1, 2)
#或
calc_1()
#把一个list或tuple传入可变参数
nums = [1, 2, 3]
calc_1(*nums)
#也可以是
calc_1(nums[0], nums[1], nums[2])#不建议，使用起来不方便

#----------------------------------------------------------------------------------------------------
#关键字参数 
def person(name, age, **kw): #注意这里和可变参数区别是这里是** **kw接收的是字黄dict
    print('name:', name, 'age:', age, 'other:', kw)
#函数调用,关键字参数可选填
#person('Bob', 35, city='Beijing') 
#person('Adam', 45, gender='M', job='Engineer')
#也可以先组装好字典dict再传入
extra = {'city': 'Beijing', 'job': 'Engineer'} #字典用{}定义的，要记得
person('Jack', 24, city=extra['city'], job=extra['job'])
#可以简化为以下
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) #跟以上可变参数传入一样简化，不同的是**
#以上例子缺点是不能限制传入的参数的key是哪些，要判断有无此key需要用到 'city' in kw 如：
def person_1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
#但是调用者仍可以传入不受限制的关键字参数
person_1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

#*********************************************************************************************
#限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
def person_2(name, age, *, city, job):
    print(name, age, city, job)
#调用函数    
person_2('Jack', 24, city='Beijing', job='Engineer')

#函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
#调用函数
#person('Jack', 24, 'Beijing', 'Engineer') #编译无错，运行会错，因为关键字参数必须要有key=value的形式传入
person('Jack', 24, city='Beijing', job='Engineer') #这样才对

#给关键字参数加上默认值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
#调用函数
person('Jack', 24, job='Engineer')#这时city直接取默认值 

#--------------------------------------------------------------------------------------------------------
#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#比如定义一个函数，包含上述若干种参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
    
def f2(a, b, c=0, *, d, **kw): #d是命名关键字参数，而**kw是关键字参数
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#调用函数
f1(1, 2) #a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3) #a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b') #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99) #a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None) #a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

#通过一个tuple和dict，你也可以调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw) #a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw) #a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
#所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
# *args是可变参数，args接收的是一个tuple
# **kw是关键字参数，kw接收的是一个dict。
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

#----------------------------------------------------------------------------------------------------------
#递归函数
#在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5)) #相当于 5*4*3*2*1=120
#运行过程
#fact(5)
#5 * fact(4)
#5 * (4 * fact(3))
#5 * (4 * (3 * fact(2)))
#5 * (4 * (3 * (2 * fact(1))))
#5 * (4 * (3 * (2 * 1)))
#5 * (4 * (3 * 2))
#5 * (4 * 6)
#5 * 24
#120

#解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，
#所以，把循环看成是一种特殊的尾递归函数也是可以的。
#尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
#这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，
#都只占用一个栈帧，不会出现栈溢出的情况。

def fact(n): #为了方便调用
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#可以看到，return fact_iter(num - 1, num * product)仅返回递归函数本身，
#num - 1和num * product在函数调用前就会被计算，不影响函数调用。
#两种方法调用
print(fact(10))
print(fact_iter(10,1))
#尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出。
#遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，
#所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

#使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

 
    





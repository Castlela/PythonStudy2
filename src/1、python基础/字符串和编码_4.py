#单字符转整数
print(ord('中'));#20013
print(ord('A'));#65

#整数转字符
print(chr(66)); #B
print(chr(25991));#文

#直接打印字符编码，输出字符
print('\u4e2d\u6587'); #中文

#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'));
print('中文'.encode('utf-8'));
print('中文'.encode('gb2312'));
#print( '中文'.encode('ascii')); #只有纯英文的str可以用ASCII编码为bytes

#把bytes变为str
print(b'ABC'.decode('ascii'));
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'));

#计算str包含多少个字符,注意英文A为一个字符，中文字也是一个字符
print(len('ABC')); #3
print(len('中文')); #2

#len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
print(len(b'ABC')); #3
print(len(b'\xe4\xb8\xad\xe6\x96\x87'));#6
print(len('中文'.encode('utf-8')));#6

#告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
#!/usr/bin/env python3

#告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# -*- coding: utf-8 -*-

#输出格式化的字符串。
#%运算符就是用来格式化字符串的。在字符串内部，
#%s表示用字符串替换，
#%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
#%f表示浮点数
#%x表示十六进制整数
print('Hello, %s' %'world');
print('Hi, %s, you have $%d.' % ('Michael', 1000000));

#格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('%2d-%02d' % (3, 1));
print('%.2f' % 3.1415926);

#如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True));

#有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%
print('growth rate: %d%%' % 7);

#字符串替换
a = 'abc'
print(a.replace('a', 'A'));





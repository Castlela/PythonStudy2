#dict
#Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85} #定义
print(d['Bob']); #打印字典里的value

#更改某key对应的value
d['Bob'] = 50;
print(d['Bob']);

#判断key是否存在
print('Thomas' in d); #方法一
print(d.get('Thomas'));#方法二
#方法二可设特定返回值
print(d.get('Thomas', -1));

#要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
print(d);
d.pop('Bob')
print(d);

#请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#而list相反：
#查找和插入的时间随着元素的增加而增加；
#占用空间小，浪费内存很少。
#所以，dict是用空间来换取时间的一种方法。
#dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key

#------------------------------------------------------------------------------------------------------------
#set
s = set([1, 2, 3])
print(s);

#set会自动过滤重复值
s = set([1, 1, 2, 2, 3, 3])
print(s);

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)
print(s);
s.add(4)
print(s);

#通过remove(key)方法可以删除元素：
s.remove(4)
print(s);

#set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2); #交集
print(s1 | s2); #并集


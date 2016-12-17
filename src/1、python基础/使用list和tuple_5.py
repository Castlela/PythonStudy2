#-----------------------------------------------------------------------------------------
#list list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates);

#获得list的元素个数
print(len(classmates));

#list的最后一个元素
print(classmates[-1]);
print(classmates[-2]); #倒数第二个元素

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append('Adam');
print(classmates);

#也可以把元素插入到指定的位置，比如索引号为1的位置：
classmates.insert(1, 'Jack')
print(classmates);

#要删除list末尾的元素，用pop()方法：
classmates.pop();
print(classmates);

#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1);
print(classmates);

#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah';
print(classmates);

#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True];
print(L);

#list元素也可以是另一个list，比如：
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s));
#也可以写成
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
#要拿到'php'可以写p[1]或者s[2][1]
print(p[1]);
print(s[2][1]);

#--------------------------------------------------------------------------------
#tuple 有序列表叫元组,tuple和list非常类似，但是tuple一旦初始化就不能修改
#因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
classmates = ('Michael', 'Bob', 'Tracy')

#tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来，比如：
t = (1, 2)
print(t);

#只有一个元素的tuple ()里必须加逗号
#t = (1) #这样定义 相当于 t=1
t = (1,) #正确的定义
print(t); #(1,)

#“可变的”tuple,注意其实并没改变，只是改变了指向里的内容
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t);

#list的排序
a = ['c', 'b', 'a']
a.sort();
print(a);






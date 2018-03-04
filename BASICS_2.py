# 要使用一个模块，我们必须首先导入该模块。
from math import log
from logging import log as logger
import os

# Python的os.path模块提供了 isdir() 和 isfile()函数
print(os.path.isdir(r"."))
print(os.path.isdir(r"/usr/local/bin/python"))
print(os.path.isfile(r"/usr/local/bin/python"))

# 如果导入的模块不存在，Python解释器会报 ImportError 错误
# try:
#     from cStringIO import StringIO
# except ImportError:
#     from StringIO import StringIO

# The StringIO and cStringIO modules are gone. Instead, import the io module
# and use io.StringIO or io.BytesIO for text and data respectively.
import io
print(io.BytesIO)
print(io.StringIO)

try:
    from simplejson import json
except ImportError:
    import json
print(json.__file__)


# 要在Python 2.7中引入3.x的除法规则，导入__future__的division：
# from __future__ import division
# 在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b


# 在Python中，类通过 class 关键字定义
# 按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，表示该类是从哪个类继承下来的
class Person(object):
    pass


xiaoming = Person()
xiaohong = Person()

print(xiaoming)
print(xiaohong)

#
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1, key=lambda x: x.name)

#
# __init__() 方法的第一个参数必须是 self（也可以用别的名字，但建议使用习惯用法），
# 后续参数则可以自由指定，和定义函数没有任何区别
# 解释器内部会将**kw拆分成对应的dict.
# setattr()方法接受3个参数：setattr(对象，属性，属性的值)
# setattr(self,k,v)相当于self.k = v
# kw.iteritems()历遍字典kw的所有key和value，分别匹配k，v


class Personn(object):
    def __init__(self, name, gender, birth, **kw):
        self.name = name
        self.gender = gender
        self.birth = birth
        for (k, v) in kw.items():
            setattr(self, k, v)


# Python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头(__)，该属性就无法被外部访问
# 如果一个属性以"__xxx__"的形式定义，那它又可以被外部访问了，以"__xxx__"定义的属性在Python的类中被称为特殊属性，
# 有很多预定义的特殊属性可以使用，通常我们不要把普通属性用"__xxx__"定义
# 一般来讲:
# _xxx 可以在子类中使用。
# __xxx 不可以在子类中使用。
# 由于Python是动态语言，类属性也是可以动态添加和修改的：
# Person.address = 'China'
# print p1.address
# # => 'China'
# print p2.address
# # => 'China'
# 因为类属性只有一份，所以，当Person类的address改变时，所有实例访问到的类属性都改变了
class Person2(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Person2.count += 1          # 函数里面引用类的属性需要带上类名

# NOTE: 不要在实例上修改类属性，它实际上并没有修改类属性，而是给实例绑定了一个实例属性。


# 类方法的第一个参数将传入类本身，通常将参数名命名为 cls，上面的 cls.count 实际上相当于 Person.count
# 要在class中定义类方法，需要这么写
class Person3(object):
    count = 0

    @classmethod
    def how_many(cls):
        return cls.count

    def __init__(self, name):
        self.name = name
        Person3.count += 1


print(Person3.how_many())


class Person4(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person4):
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course


t = Teacher('Alice', 'Female', 'English')
print(t.name)


# 函数isinstance()可以判断一个变量的类型，既可以用在Python内置的数据类型如str、list、dict，
# 也可以用在我们自定义的类，它们本质上都是数据类型


# python中多态

# 任何对象，只要有read()方法，就称为File-like Object，都可以传给json.load()。

# Python的网络服务器有TCPServer、UDPServer、UnixStreamServer、UnixDatagramServer，
# 而服务器运行模式有 多进程ForkingMixin 和 多线程ThreadingMixin两种。
# 要创建多进程模式的 TCPServer：
class MyTCPServer(TCPServer, ForkingMixin):
    pass


# 要创建多线程模式的 UDPServer：
class MyUDPServer(UDPServer, ThreadingMixin):
    pass


# 用 type() 函数获取变量的类型，它返回一个 Type 对象
# 用 dir() 函数获取变量的所有属性
# 如果已知一个属性名称，要获取或者设置对象的属性，就需要用 getattr() 和 setattr( )函数了
getattr(t, 'name')
getattr(t, 'name', 'default value')
setattr(t, 'name', 'VALUE')


#
lst = range(1, 10)
print(lst)
print(lst.__str__())

# Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员


class Person5(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __str__(self):
        return '(Person: %s, %s)' % (self.name, self.gender)

    __repr__ = __str__

# __cmp__()


class Student2(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        pass

    __repr__ = __str__

    def __cmp__(self, s):
        if self.name < s.name:
            return -1
        elif self.name > s.name:
            return 1
        else:
            return 0


slst = [Student2("A", 'A'), Student2("B", 'A'), Student2('C', 'B')]
print(sorted(slst))

# 要让 len() 函数工作正常，类必须提供一个特殊方法__len__()，它返回元素的个数


class Students(object):
    def __init__(self, *args):
        self.names = args

    def __len__(self):
        return len(self.names)


ss = Students('Bob', 'Alice', 'Tim')
print(len(ss))


# 要表示有理数，可以用一个Rational类来表示：
# p、q 都是整数，表示有理数 p/q。
# 如果要让Rational进行+运算，需要正确实现__add__：
# 如果要让Rational进行-运算，需要正确实现__sub__：
# 如果要让Rational进行*运算，需要正确实现__mul__：
# 如果要让Rational进行/运算，需要正确实现__div__：
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q

    def __add__(self, r):
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):
        return "%s/%s" % (self.p, self.q)

    __repr__ = __str__


# 要让int()函数正常工作，只需要实现特殊方法__int__(self):
# 要让float()函数正常工作，只需要实现特殊方法__float__(self):

# @property
class Animal(object):
    def __init__(self):
        pass

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if isinstance(name, str):
            self.__name = name
        else:
            raise ValueError


# __slots__是指一个类允许的属性列表
class Cat(object):
    __slots__ = ('name', 'age', 'hobby')

    def __init__(self, name, age, hobby):
        self.name = name
        self.age = age
        self.hobby = hobby

# __slots__的目的是限制当前类所能拥有的属性，如果不需要添加任意动态的属性，使用__slots__也能节省内存


# 一个类实例也可以变成一个可调用对象，只需要实现一个特殊方法__call__()
class Dog(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, friend):
        print("My name is {name}...".format(name=self.name))
        print("My friend is {name}...".format(name=friend))


d = Dog("Bob", 'male')
d('Tim')


#
class Fib(object):
    def __call__(self, num):
        lst = [0, 1]
        if num < 1:
            return
        i = 0
        while i < num:
            lst.append(lst[i] + lst[i + 1])
            i += 1
        return lst[:num]

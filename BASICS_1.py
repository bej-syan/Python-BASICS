# -*- coding: utf-8 -*-

# 如果一个字符串包含很多需要转义的字符，对每一个字符都进行转义会很麻烦。为了避免这种情况，我们可以在字符串前面加个前缀 r ，表示这是一个 raw 字符串，
# 里面的字符就不需要转义了。
print(r'\(~_~)/ \(~_~)/')

# 还可以在多行字符串前面添加 r ，把这个多行字符串也变成一个raw字符串：
print(
    r'''Python is created by "Guido".
It is free and easy to learn.
Let's start learn Python in imooc!''')

# 8个比特（bit）作为一个字节（byte），所以，一个字节能表示的最大的整数就是255（二进制11111111=十进制255），0 - 255被用来表示大
# 小写英文字母、数字和一些符号，这个编码表
# 被称为ASCII编码，比如大写字母 A 的编码是65，小写字母 z 的编码是122。
# 如果要表示中文，显然一个字节是不够的，至少需要两个字节，而且还不能和ASCII编码冲突，所以，中国制定了GB2312编码，用来把中文编进去。
# 类似的，日文和韩文等其他语言也有这个问题。为了统一所有文字的编码，Unicode应运而生。Unicode把所有语言都统一到一套编码里，这样就不会再有乱码问
# 题了。
# Unicode通常用两个字节表示一个字符，原有的英文编码从单字节变成双字节，只需要把高字节全部填为0就可以。
# 因为Python的诞生比Unicode标准发布的时间还要早，所以最早的Python只支持ASCII编码，普通的字符串'ABC'在Python内部都是ASCII编码的。
# Python在后来添加了对Unicode的支持，以Unicode表示的字符串用u'...'表示，比如：
print(u'中文')
print('中文')
'''Python的Unicode字符串支持"中文",
"日文",
"韩文"等多种语言'''

# 如果中文字符串在Python环境下遇到 UnicodeDecodeError，这是因为.py文件保存的格式有问题。可以在第一行添加注释
# -*- coding: utf-8 -*-

a = True
print(a and 'a=T' or 'a=F')     # a=T
# 因为Python把0、空字符串''和None看成 False，其他数值和非空字符串都看成 True
#   True and 'a=T' 计算结果是 'a=T'
#   继续计算 'a=T' or 'a=F' 计算结果还是 'a=T'

a = 'python'
print('hello,', a or 'world')        # hello, python

b = ''
print('hello,', b or 'world')        # hello, world


# tuple一旦创建完毕，就不能修改了
t = ('Adam', 'Lisa', 'Bart',)
# tuple没有 append()方法，也没有insert()和pop()方法。所以，新同学没法直接往 tuple 中添加，老同学想退出 tuple 也不行。

# 包含 0 个元素的 tuple，也就是空tuple，直接用 ()表示

t = (1)
# 因为()既可以表示tuple，又可以作为括号表示运算时的优先级，结果 (1) 被Python解释器计算出结果 1，导致我们得到的不是tuple，而是整数 1。
# 正是因为用()定义单元素的tuple有歧义，所以 Python 规定，单元素 tuple 要多加一个逗号“,”，这样就避免了歧义
t = (1,)
print(t)

# 多元素 tuple 加不加这个额外的“,”效果是一样的：
t = (1, 2, 3,)
print(t)

# 前面我们看到了tuple一旦创建就不能修改。现在，我们来看一个“可变”的tuple：
# tuple的元素确实变了，但其实变的不是 tuple 的元素，而是list的元素。
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
t = ('a', 'b', ['A', 'B'])
L = t[2]
L[0] = 'X'
L[1] = 'Y'
print(t)
L.append('Z')
print(t)

# 缩进请严格按照Python的习惯写法：4个空格，不要使用Tab，更不要混合Tab和空格，否则很容易造成因为缩进引起的语法错误
age = 20
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
elif age >= 3:
    print('kid')
else:
    print('baby')

L = ['Adam', 'Lisa', 'Bart']
for name in L:
    print(name)

N = 10
x = 0
while x < N:
    print(x)
    x = x + 1

for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        print(x * y)

d = {
    'Adam': 95,
    'Lisa': 85,
    'Bart': 59
}
print(d)
print(len(d))
print(d['Adam'])

# 通过 key 访问 dict 的value，只要 key 存在，dict就返回对应的value。如果key不存在，会直接报错：KeyError。
# 要避免 KeyError 发生，有两个办法：
#   一是先判断一下 key 是否存在，用 in 操作符：
#   二是使用dict本身提供的一个 get 方法，在Key不存在的时候，返回None
if 'Paul' in d:
    print(d['Paul'])

print(d.get('Paul'))    # prints nothing
print(d.get('Adam'))

for (k, v) in d.items():
    print("{name}: {score}".format(name=k, score=v))

# dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，查找速度都一样。而list的查找速度随着元素增加而逐渐下降。
# 不过dict的查找速度快不是没有代价的，dict的缺点是占用内存大，还会浪费很多内容，list正好相反，占用内存小，但是查找速度慢
# dict的第二个特点就是存储的key-value序对是没有顺序的
# dict的第三个特点是作为 key 的元素必须不可变
# Python的基本类型如字符串、整数、浮点数都是不可变的，都可以作为 key。但是list是可变的，就不能作为 key。
d = {
    '123': [1, 2, 3],   # key 是 str，value是list
    123: '123',         # key 是 int，value 是 str
    ('a', 'b'): True    # key 是 tuple，并且tuple的每个元素都是不可变对象，value是 boolean
}
print(d)

for key in d:
    print(key)

# set 持有一系列元素，这一点和 list 很像，但是set的元素没有重复，而且是无序的
# 创建 set 的方式是调用 set() 并传入一个 list，list的元素将作为set的元素
s = set(range(1, 100))
s2 = set(['Adam', 'Lisa'])
print(s)
print(s2)

# 由于set存储的是无序集合，所以我们没法通过索引来访问。
# 访问 set中的某个元素实际上就是判断一个元素是否在set中
print(10 in s)
print('Adam' in s2)

s = set(name.lower() for name in ['Adam', 'Lisa', 'Bart'])
print('adam' in s)
print('bart' in s)

# set存储的元素和dict的key类似，必须是不变对象，因此，任何可变对象是不能放入set中的。
# 用add()可以直接添加，而remove()前需要判断(or KeyError)
s.add(23)
print(s)
if (23 in s):
    s.remove(23)
print(s)


# abs
# cmp
print(abs(-10))
print(int('123'))
print(str(1234))

L = range(1, 101)
L2 = [ele ** 2 for ele in L]
print(sum(L2))

# Python函数
# return None可以简写为return

import math     # math包提供了sin()和 cos()函数


def movee(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = movee(100, 100, 60, math.pi / 6)
print(x, y)

# 一元二次方程形式:ax2+bx+c=0(a≠0，且a，b，c是常数)
# 求根公式:
# x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / 2*a
# x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / 2*a
import math


def quadratic_equation(a, b, c):
    x = b ** 2 - 4 * a * c
    if x < 0:
        return None
    elif x == 0:
        return (-b)/(2*a)
    if x >= 0:
        x1 = (-b + math.sqrt(x)) / (2*a)
        x2 = (-b - math.sqrt(x)) / (2*a)
        return x1, x2


print(quadratic_equation(2, 3, 0))
print(quadratic_equation(1, -6, 5))


# Python之递归函数
# 使用递归函数需要注意防止栈溢出
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限
# 的，所以，递归调用的次数过多，会导致栈溢出。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


# RecursionError: maximum recursion depth exceeded in comparison
# print(fact(10000))

# 有三根相邻的柱子，标号为A,B,C，A柱子上从下到上按金字塔状叠放着n个不同大小的圆盘，要把所有盘子一个一个移动到柱子B上，并且每次移动同一根柱子上都不能
# 出现大盘子在小盘子上方，请问至少需要多少次移动，设移动次数为H(n）。
#
# 完成 n 个盘子从 a 经过 b 到 c 的搬运只需要3步，第一步：将 n-1 个盘子从 a 经过 c 搬运到 b，即move(n-1, a, c, b)； 第二步：将 第 n 个盘子
# 从 a 移到 c，即 print a, '-->', c； 第三步： 将 n-1个盘子从 b 经过 a 搬运到 c，即move(n-1, b, a, c)；完事， 至于这 n-1 个盘子是怎么
# 搬运的呢，他又自己进入了下一个循环
# 函数 move(n, a, b, c) 的定义是将 n 个圆盘从 a 借助 b 移动到 c。


def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n-1, a, c, b)
    print(a, '-->', c)
    move(n-1, b, a, c)


move(4, 'A', 'B', 'C')


# Python之定义默认参数
# 例如Python自带的 int() 函数，其实就有两个参数
# int()函数的第二个参数是转换进制，如果不传，默认是十进制 (base=10)，如果传了，就用传入的参数。
# 默认参数只能定义在必需参数的后面：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# Python之定义可变参数
# 如果想让一个函数能接受任意个参数，我们就可以定义一个可变参数


def fn(*args):
    print(args)


fn(1, 2, 3)
fn()


# Python提供了切片（Slice）操作符
L = ['x', 'y', 'z', 'xx', 'yy', 'zz']
print(L[0:7])       # L[startIndex:number]
print(L[:3])        # 如果第一个索引是0，还可以省略
print(L[:])         # 只用一个 : ，表示从头到尾, L[:]实际上复制出了一个新list

print(L[::2])       # 0 2 4 ...
print(L[::1])       # 0 1 2 3 ...

# 利用倒序切片对 1 - 100 的数列取出：
#   * 最后10个数；
#   * 最后10个5的倍数
L = range(1, 101)
print(L[-10:])
print(L[4::5][-10:])


# 因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print("HELLOWORLD"[1:])

# 在Python中，迭代是通过 for ... in 来完成的
for i in range(1, 100):
    if i % 7 == 0:
        print(i, end=' ')
print()
for i in range(1, 100):
    if i * 7 > 98:
        continue
    print(i*7, end=' ')
print()
for i in range(0, 101, 7):
    if i > 0:
        print(i, end=' ')
print()


# Python中，迭代永远是取出元素本身，而非元素的索引。
# 使用 enumerate() 函数
for index, value in enumerate(range(1, 11)):
    print(index, value)

# 使用 enumerate() 函数，我们可以在for循环中同时绑定索引index和元素name
# 实际上，enumerate() 函数把：
['Adam', 'Lisa', 'Bart', 'Paul']
# 变成了类似：
[(0, 'Adam'), (1, 'Lisa'), (2, 'Bart'), (3, 'Paul')]
# 因此，迭代的每一个元素实际上是一个tuple
for t in enumerate(range(1, 10)):
    print(t[0], end=' ')
print()
# for循环又可以进一步简写为
for index, value in enumerate(range(1, 10)):
    print("%s: %s" % (index, value))

# 迭代dict的value
# dict对象本身就是可迭代对象，用 for 循环直接迭代 dict，可以每次拿到dict的一个key。
# 如果我们希望迭代 dict 对象的value，应该怎么做？
# dict 对象有一个 values() 方法，这个方法把dict转换成一个包含所有value的list
d = {
    'a': 11,
    'b': 12,
    'c': 13
}
print(d.values())
print(d.keys())
for e in d.values():
    print(e)

# 用 itervalues() 方法替代 values() 方法，迭代效果完全一样 Python2
# itervalues() 方法不会转换，它会在迭代过程中依次从 dict 中取出 value，所以 itervalues() 方法比 values() 方法节省了生成 list 所需的内存


# 迭代dict的key和value
for (k, v) in d.items():
    print("{} : {}".format(k, v))

#
print([x * x for x in range(1, 11)])

# [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([x * (x + 1) for x in range(1, 100, 2)])
# [1x2, 3x4, 5x6, 7x8, ..., 99x100]
print([x * y for (x, y) in zip(range(1, 100, 2), range(2, 101, 2))])

print([x * x for x in range(1, 11) if x % 2 == 0])


#
#
# python进阶
#
#
def square(x):
    print(x ** 2)


map(square, range(1, 10))


# reduce()传入的函数 f 必须接收两个参数，reduce()对list的每个元素反复调用函数f，并返回最终结果值
def add(x, y):
    return x + y


import functools

print(functools.reduce(add, range(1, 10), 0))

# python3中，要使用reduce,得从functools中引入，加上：
from functools import reduce


def is_odd(x):
    return x % 2 == 0


def is_not_empty(s):
    return s and len(s.strip()) > 0


print(filter(is_odd, range(1, 10)))


# 像这种内层函数引用了外层函数的变量（参数也算变量），然后返回内层函数的情况，称为闭包（Closure）
# 闭包的特点是返回的函数还引用了外层函数的局部变量，所以，要正确使用闭包，就要确保引用的局部变量在函数返回后不能变。
def calc_sum(lst):
    def lazy_sum():
        return sum(lst)
    return lazy_sum


def count():
    """
    Python2
    希望一次返回3个函数，分别计算1x1,2x2,3x3:
    """
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs

# f1, f2, f3 = count()
# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果全部都是 9
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。


def countt():
    """
    默认参数正好可以完成定义时获取i值且运行函数时无需参数输入的功能
    """
    fs = []
    for i in range(1, 4):
        def f(m=i):
            return m * m
        fs.append(f)
    return fs


f1, f2, f3 = countt()
print(f1(), f2(), f3())


#
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# 装饰器
# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
# 使用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码
# @log
# @performance
# @transaction
# @post('/register')
def log(f):
    def fn(*args, **kw):
        print("call {name}()...".format(name=f.__name__))
        return f(*args, **kw)
    return fn


@log
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))


print(factorial(10))

# 要让 @log 自适应任何参数定义的函数，可以利用Python的 *args 和 **kw，保证任意个数的参数总是能正常调用：
# *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，
# 必须*args参数列要在**kwargs前


# 把上面的定义翻译成高阶函数的调用，就是：
# my_func = log('DEBUG')(my_func)


def log2(prefix):
    def log_decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kw):
            print("[{prefix}]Calling {method_name}()...".format(
                prefix=prefix, method_name=f.__name__))
            return f(*args, **kw)
        return wrapper
    return log_decorator


@log2("DEBUG")
def hello_log2():
    print("hello log2...")


hello_log2()
print(hello_log2.__name__)      # output: 'wrapper', which is not expected!!!

# int()函数还提供额外的base参数，默认值为10
print(int('12345', base=8))

# functools.partial就是帮助我们创建一个偏函数的
int2 = functools.partial(int, base=2)
print(int2('1000000'))


sorted_ignore_cases = functools.partial(sorted, key=str.lower)
print(sorted_ignore_cases(['bob', 'about', 'Zoo', 'Credit']))

# 2. 函数的定义
import sys


# 实现两个数字的相加
def add(a, b):
    return a + b


def print_code(code):
    print(code)


# 多返回值型函数，与go类似，返回值可以直接为一个元组，或者用个多返回值接收（建议第二种）
def damage(x, y):
    return x + y, x - y


if __name__ == '__main__':
    print_code(add(1, 2))
    sys.setrecursionlimit(10000)
    print_code(1000)
    print(damage(5, 2))
    print(type(damage(5, 2)))

    result = damage(5, 2)
    print(result)
    r1, r2 = damage(5, 2)  # 函数返回是多个返回值是时可以自动解包
    print(r1, r2)

    # 序列赋值和链式复制  语法糖，取元组值更方便
    a, b, c = 1, 2, 3
    d = 1, 2, 3  # tuple
    print(type(d))
    e, f, g = d  # 这就是序列解包，用多个值接收一个元组,接收的变量数必须和元组长度一致，否则会报错
    print(e, f, g)

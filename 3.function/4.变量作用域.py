c = 10  # 全局变量


def demo():
    c = 50  # 局部变量
    print(c)


a = 1


def func1():
    a = 2

    def func2():
        a = 3
        print(a)

    func2()


# 使用global关键字可以将局部变量变成全局变量
def globalKeyWord():
    global inner
    inner = 3


if __name__ == '__main__':
    demo()
    func1()
    globalKeyWord()
    print(inner)
    pass

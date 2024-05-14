class Marking():

    # 初始化函数中就是给一个类设置字段
    def __init__(self, name):
        self.name = name
        self.__score = 0

    def marking(self, score):
        self.__private_met()
        self.__score = score

    def print_self(self):
        print(self.__dict__)

    def __private_met(self):  # 方法前加两个下划线代表是私有方法
        print("这是一个私有方法")


if __name__ == '__main__':
    mark = Marking("gaojinhui")
    mark.marking(100)
    mark.print_self()
    mark.__score = 1  # 这一步不会报错，相当于又给mark加了一个公用的叫__score
    mark._Marking__score = 99  # 依然可以通过这种方式访问到私有变量
    mark.print_self()

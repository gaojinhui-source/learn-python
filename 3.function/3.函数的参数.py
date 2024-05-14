def add(x, y):
    return x + y


# msg就是默认参数,默认参数必须放在必须参数的前面
def print_message(user, msg="这是默认参数"):
    print(user + "说" + msg)


# 可变参数，在参数前加一个星号代表是可变参数，实际是一个元组，可以通过解包取参数
def change_param(*args):
    print(args)
    print("可变参数的类型为", type(args))


# 可变关键字参数,实际是一个dict
def change_key_param(**args):
    print(args)
    print("可变参数的类型为", type(args))
    for k, v in args.items():
        print(k, v)


if __name__ == '__main__':
    # 1.关键字参数，参数传入的顺序可以改变
    print(add(y=1, x=2))

    # 2.必须参数 例如y就是必须参数，一般的参数都是必须参数
    # add(x=1)

    # 3.默认参数
    print_message("高锦辉")
    print_message("高锦辉", "你好")

    # 4OOP.可变参数，相当于传入一个元组
    change_param(1, 2, 3, 4, "5")

    # 5. 关键字可变参数,相当于传入一个map
    change_key_param(xian="38", beijing="32")

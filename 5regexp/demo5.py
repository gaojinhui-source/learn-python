import re


def convert(value):
    print(value)  # value不是简单的字符串，而是一个对象
    matched = value.group()
    return "!!" + matched + "!!"


if __name__ == '__main__':
    s = "Python0C++dsaGO"
    r = re.sub("GO", "C#", s, 0)  # 将匹配的结果将GO替换为C#
    # 注意，sub的第二个参数可以是一个函数
    print(r)

    r = re.sub("GO", convert, s, 0)  # 将匹配的结果将GO替换为convert的函数的返回值
    # 注意，sub的第二个参数可以是一个函数
    print(r)

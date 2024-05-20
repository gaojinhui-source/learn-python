# 数量词
import re

if __name__ == '__main__':
    s = "java  python111php22"
    a = re.findall("[a-z]{3,6}?", s)  # 匹配连续三个到6个的英文字符
    # 但是有个问题，为什么不会到java就出现呢，因为数量匹配有一个贪婪和非贪婪的概念
    # 贪婪：会一直匹配到条件不满足为止，如java，一直到为空时才会停止
    # 非贪婪：只要满足条件则立即停止，只要连续英文字符到三个就立刻停止
    # 默认贪婪
    print(a)

    s = "pytho0python1pythonn2"
    a = re.findall("python*", s)  # *表示，python的n可以出现0次或无数次
    print(a)
    a = re.findall("python+", s)  # *表示，python的n可以出现1次或无数次
    print(a)
    a = re.findall("python?", s)  # *表示，python的n可以出现0次或一次
    print(a)
    a = re.findall("python{1,2}", s)  # *表示，python的n可以出现0次或一次
    print(a)
    a = re.findall("python{1,2}?", s)  # *表示，python的n可以出现0次或非贪婪
    print(a)

import re

if __name__ == '__main__':
    qq = "100000002"
    print(len(qq))  # 长度为9
    r = re.findall("^\d{4,8}$", qq)  # 长度为8,前面加上^后面加上$表示限制长度
    # ^表示从字符串开始为止匹配，$表示从字符串末尾匹配，
    # 所以上面的意思，从前边和从后边都是长度4到8的数字
    print(r)

    qq = "100100100"
    r = re.findall("(100){3}", qq, re.I)  # re.I代表忽略大小写
    print(r)

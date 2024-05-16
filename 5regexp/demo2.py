import re

if __name__ == '__main__':
    a = "C0C++1C#2Python"
    r = re.findall("\d", a)  # \d就是指所有的数字，元字符
    print(r)

    a = "acc,abc,adc,aec,afc"
    r = re.findall("a[cf]c", a)  # a[cf]c找出中间为c或者f的两边为a,c的字符串
    print(r)

    a = "acc,abc,adc,aec,afc"
    r = re.findall("a[^cf]c", a)  # a[^cf]c找出中间不为c或者f的两边为a,c的字符串
    print(r)

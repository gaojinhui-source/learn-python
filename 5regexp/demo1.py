import re

if __name__ == '__main__':
    a = "C|C++|C#|Python"
    r1 = re.findall("Python", a)
    r2 = re.findall("Php", a)
    print(r1)
    print(r2)

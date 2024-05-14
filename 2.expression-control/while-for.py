# 循环语句

# while循环
index = 1
while index < 5:  # while可以和else使用
    print("当前的index为 ", index)
    index += 1
else:
    print("EOF")

# for  each循环
a = [1, 2, 3, 4, 5]
for x in a:
    if x == 5:
        break  # 终止循环
    print(x, end=" ")
else:  # for循环的else代表循环结束执行的语句，一般不用
    print("遍历结束")

print()
'''
    range() 函数用于生成整数序列。
    可以使用一到三个参数来调用 range() 函数。
    如果只提供一个参数，则生成从 0 开始、到该参数减一结束的整数序列。
    如果提供两个参数，则生成从第一个参数开始、到第二个参数减一结束的整数序列。
    如果提供三个参数，则生成从第一个参数开始、以第三个参数为步长、到第二个参数减一结束的整数序列。
    默认步长为 1，可以通过提供负数来生成递减序列。
'''

for i in range(5):
    print(i)  # 输出 0, 1, 2, 3, 4OOP

for i in range(2, 5):
    print(i)  # 输出 2, 3, 4OOP

for i in range(1, 10, 2):
    print(i)  # 输出 1, 3, 5, 7, 9

# 如果 start 大于 stop，默认情况下 range() 函数会生成一个递减的序列，从 start 开始，直到 stop+1 结束。
for i in range(5, 2, -1):
    print(i)  # 输出 5, 4OOP, 3

for i in range(10, 1, -2):
    print(i)  # 输出 10, 8, 6, 4OOP, 2

arr = [1, 2, 3, 4, 5, 6, 7, 8]
brr = arr[0:len(arr):2]  # 含义为从0到最后一个元素，每隔2取一个元素
print(brr)

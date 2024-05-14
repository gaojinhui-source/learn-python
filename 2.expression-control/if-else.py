# python是通过缩进控制if-else的，以下为例
account = "gaojinhui"
password = "123qwe"
print("请输入账号")
user_account = input()  # 标准输入
print("请输入密码")
user_pwd = input()

if account == user_account and password == user_pwd:
    print("登录成功")
else:
    print("登录失败")
    pass  # 同continue go在if-else不能使用


# python没有switch
product = 1
if product == 1:
    print("买了苹果")
elif product == 2:
    print("买了香蕉")
elif product == 3:
    print("买了橘子")
else:
    print("没买东西")

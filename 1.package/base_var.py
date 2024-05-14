"""
 这是doc
"""

# name和package只有在被导入时才会有值，没有导入的时候值为none
# name如果执行出来是__main__，因为他是被当做入口
# 因为如果直接在当前模块执行并获取name和package
# 通常该函数会被认为是主函数，主函数不属于任何包，并且模块名为main，
# file为执行python命令的路径例如，python c3.py file结果为c3,如果为python ./c3.py
print("name " + __name__)
print("file " + __file__)
# print("1.package "+__package__)
print("doc " + __doc__)

# __name__的特别用法
# 这样的写法说明该模块为入口模块
if __name__ == "__main__":
    print("this is main")

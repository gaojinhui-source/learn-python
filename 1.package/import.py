import sys

import common  # python在导入时会将其他模块的所有代码执行
import sub.sub_common as sub  # 可以使用as起别名
from common import port  # 可以通过这种方式直接引用变量或函数
import base_var

print(common.a)
print(sub.sub_col)

print(port)


print(sys.path)

# 后续专门把这一块重新好好学下

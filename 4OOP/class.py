class Student():
    sum = 0  # 类变量在我理解相当于该字段的默认值，可以修改
    name = ""
    age = 0

    def print_self(self):  # 一个类定义中的函数称作方法
        print(self.name, self.age, self.sum, end="\n")

    def __init__(self, name, age):  # 构造函数

        self.name = name
        self.age = age
        pass

    # 如何在实例方法访问类变量
    def class_var(self):
        print(Student.sum)
        print(self.__class__.sum)

    # 带了这个@classmethod代表这个函数是类方法,cls就是类本身
    # 除了类可以调用类方法，对象也可以调用类方法，但类方法内不可访问实例变量
    @classmethod
    def plus_sum(cls):
        cls.sum += 1
        pass

    # 静态方法，和普通函数的方法一致，对象和类都可以调用，静态方法不可访问实例变量
    @staticmethod
    def print_static():
        print("this is static method", end="\n")


if __name__ == '__main__':
    # student = Student()  # 创建一个对象
    # student.print_self()

    newStu = Student(name="tony", age=12)
    newStu.print_self()
    print(Student.sum)

    print("-----------", end="\n")
    newStu.class_var()

    newStu.print_static()
    Student.print_static()

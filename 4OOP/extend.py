class Human():
    sum = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


class Father(Human):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def print_self(self):
        print(self.__dict__)


if __name__ == '__main__':
    father = Father("爸爸", 45, "宝鸡")
    father.print_self()

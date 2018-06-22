class MyClass(object):
    def __init__(self,data1,data2):
        self.__data1 = data1
        self.data2 = data2

    def print_data1(self):
        print(self.__data1)


class1 = MyClass(78,99)
print(class1._MyClass__data1)

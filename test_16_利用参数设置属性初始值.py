class Cat:
    def __init__(self, new_name):
        print('这是一个初始化方法')
        # self.属性名 = 属性的初始值
        # self.name = 'Tom'
        self.name = new_name

    def eat(self):
        print('{}爱吃鱼'.format(self.name))

    def drink(self):
        print('{}爱喝水'.format(self.name))


# 使用类名创建对象时，会自动调用初始化方法init
tom = Cat('Tom')
print(tom.name)
lazy_cat = Cat('大懒猫')
lazy_cat.eat()

class Cat:
    def eat(self):
        print('{}爱吃鱼'.format(self.name))

    def drink(self):
        print('{}爱喝水'.format(self.name))


# 创建猫对象
tom = Cat()
# 可以使用 .属性名 利用赋值语句实现增加对象属性
tom.name = 'Tom'
tom.eat()
tom.drink()
print(tom)

# 再创建一个猫对象
lazy_cat = Cat()
lazy_cat.name = '大懒猫'
lazy_cat.eat()
lazy_cat.drink()
print(lazy_cat)

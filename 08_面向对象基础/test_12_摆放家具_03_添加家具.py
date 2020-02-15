# 1.房子(House)有户型、总面积和家具名称列表
#     新房没有任何家具
# 2.家具(HouseItem)有名字和占地面积，其中
#     席梦思(bed)占地4平米
#     衣柜(chest)占地2平米
#     餐桌(table)占地1.5平米
# 3.将以上三件家具添加到房子中
# 4.打印房子时，要求输出：户型、总面积、剩余面积、家具名称列表
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return '{}占地{:.1f}'.format(self.name, self.area)


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        # 剩余面积
        self.free_area = area
        # 家具名称列表
        self.item_list = []

    def __str__(self):
        # Python能够自动将一对括号内部的代码连接在一起
        return ('户型：{}\n总面积：{:.1f}[剩余:{:.1f}]\n家具：{}'
                .format(self.house_type, self.area,
                        self.free_area, self.item_list))

    def add_item(self, item):
        print('要添加{}'.format(item))
        # 1.判断家具面积
        if item.area > self.free_area:
            print('{}的面积太大了，无法添加'.format(item.name))
            return
        # 2.将家具的名称添加到列表中
        self.item_list.append(item.name)
        # 3.计算剩余面积
        self.free_area -= item.area


# 1.创建家具
bed = HouseItem('席梦思', 40)
chest = HouseItem('衣柜', 20)
table = HouseItem('餐桌', 1.5)

print(bed, chest, table)

# 2.创建房子对象
my_home = House('两室一厅', 60)
my_home.add_item(bed)
my_home.add_item(chest)
my_home.add_item(table)

print(my_home)

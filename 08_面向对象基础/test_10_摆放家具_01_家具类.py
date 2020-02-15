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


# 1.创建家具
bed = HouseItem('席梦思', 4)
chest = HouseItem('衣柜', 2)
table = HouseItem('餐桌', 1.5)

print(bed, chest, table)

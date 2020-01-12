students = [
    {'name': '阿土'},
    {'name': '小美'}
]
# 在学院列表中查找指定姓名
find_name = '张三'

for stu_dict in students:
    print(stu_dict)
    if stu_dict['name'] == find_name:
        print('找到了{}'.format(find_name))
        # 如果已经找到，退出循环，不再遍历后续元素
        break
else:
    # for else 在遍历循环运行完毕，没有通过break跳出循环的情况下，会运行else部分，否则不运行
    print('抱歉，没有查找到该用户')

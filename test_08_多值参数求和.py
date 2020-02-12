# 计算任意多个数字的和
# 需求
# 1.定义一个函数sum_numbers，可以接收的任意多个整数
# 2.功能要求：将传递的所有数字累加并且返回累加结果
def sum_numbers(*args):
    '''
    :param args: 数据元组
    :return: 元组求和结果
    '''
    num = 0
    for i in args:
        num += i
    return num


result = sum_numbers(1, 2, 3, 4, 5, 6, 7)
print(result)

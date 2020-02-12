def demo(num, *nums, **person):
    '''
    :param num:
    :param nums: *接收元组
    :param person: **接收字典
    :return:
    '''
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5, name='小明', age='18')

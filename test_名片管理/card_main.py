import card_tools

while True:
    # TODO(小明) 显示功能菜单
    card_tools.show_menu()


    action_str = input('请选择希望执行的操作：')
    print('您选择的操作是：【{}】'.format(action_str))

    # 1，2，3针对名片的操作
    if action_str in ['1', '2', '3']:
        # 新增名片
        if action_str == '1':
            pass
        # 显示全部
        elif action_str == '2':
            pass
        # 查询名片
        elif action_str == '3':
            pass
    # 0 退出系统
    elif action_str == '0':
        print('欢迎再次使用【名片管理系统】')
        break
        # pass
    # 其他内容输入错误，需提示用户
    else:
        print('您输入的内容不正确，请重新选择')

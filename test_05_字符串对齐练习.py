poem = [
    '\t\n登鹳雀楼',
    '王之涣',
    '白日依山尽\t\n',
    '黄河入海流',
    '欲穷千里目',
    '更上一层楼'
]

for poem_str in poem:
    # strip方法去除字符串中的空白字符
    # center方法居中显示
    # chr(12288)表示中文空格
    print('|{}|'.format(poem_str.strip().center(9, chr(12288))))

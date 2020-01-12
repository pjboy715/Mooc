def multipli_table():
    '''九九乘法表 '''
    for col in range(1, 10):
        for row in range(1, 10):
            if row <= col:
                print('{} * {} = {}'.format(col, row, col * row), end='\t')
            else:
                pass
        print('')
<<<<<<< HEAD


multipli_table()
=======
>>>>>>> origin/master

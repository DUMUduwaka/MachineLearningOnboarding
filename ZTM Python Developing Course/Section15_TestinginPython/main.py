'''Main python file'''


def do_stuff(num=0):
    '''A function that use to square'''
    try:
        if num:
            return int(num)**2
        else:
            return 'Please enter a number'
    except ValueError as err:
        return err

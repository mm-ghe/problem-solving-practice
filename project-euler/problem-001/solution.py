SUM = 0

def is_three(x):
    '''
    It checks if x is multiple of 3.
    '''
    if x % 3 == 0:
        return True
    else:
        return None

def is_five(x):
    '''
    It checks if x is multiple of 5.
    '''
    if x % 5 == 0:
        return True
    else:
        return None

for i in range (1000):
    if is_three(i) or is_five(i):
        SUM = SUM + i

print(SUM)

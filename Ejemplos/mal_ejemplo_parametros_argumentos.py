true = False
not_false = True

def func(true = False, not_true=True):
    if true == False:
        true = True
    return True if not_false else (False if not_true else False)

print(func(not true, not_true=not(not_false)))
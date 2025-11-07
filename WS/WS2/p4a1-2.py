#p4a1
#https://docs.python.org/3/tutorial/errors.html
#p4a2
print('Pick an error from 1 to 12')
uin = int(input())
if uin == 1:
    #variable definition error
    print(my_list[10])
elif uin == 2:
    #index error
    my_list = [1,2]
    print(my_list[10])
elif uin == 3:
    #value error
    print(int("hello"))
elif uin == 4:
    #Zero division Error
    print(10 / 0)
elif uin == 5:
    # KeyError
    d = {}
    print(d['missing'])
elif uin == 6:
        # TypeError
    print("a" + 1)
elif uin == 7:
        # AttributeError
    x = 5
    x.append(3)
elif uin == 8:
        # ImportError / ModuleNotFoundError
    import nonexistent_module  # ModuleNotFoundError in modern Python
elif uin == 9:
        # FileNotFoundError
    open('this_file_does_not_exist.txt')
elif uin == 10:
        # RecursionError
    def f(): return f()
    f()
elif uin == 11:
        # OverflowError (float exponent too large)
    print(10.0 ** 10000)
elif uin == 12:
        # StopIteration (raise by iterator exhaustion)
    it = iter([])
    print(next(it))
else:
    print('Pick a number 1–12')

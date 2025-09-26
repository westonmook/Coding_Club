#p3a1link below
#https://www.geeksforgeeks.org/python/how-to-check-nonetype-in-python/#
#See website for a possible answer to p3a2
#p3a3 and a4
print('Add a number any number positive or negative and see double or None!')
user_in = input()
n = None
user_in = None if user_in == "None" else int(user_in)
if user_in == n:
    print('You gotta type a number, not None homie.')
elif user_in < 0:
    print(n)
elif user_in >= 0:
    print(user_in * 2)

#iterates through each item in your list and prints it.
my_list = [10,20,30,40]
for i in range(len(my_list)):
    print(my_list[i])
#space between loops
print()
#loop modification
my_list = [10,25,31,44]
for num in range(len(my_list)):
    if my_list[num] % 2 == 0:
        print(my_list[num])

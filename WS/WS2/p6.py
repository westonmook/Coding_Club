#p6a1
#here is a useful link to the built in functions contained in python
#https://docs.python.org/3/library/functions.html
#function basics
#https://www.geeksforgeeks.org/python/python-functions/#
#p6a2
#function definition
def greet(name):
    print("Hello " + str(name) + "!")
#calling the function with name equal to arbitrary input
greet("Dilberto")
greet(7)
#p6a3
def add(a, b):
    return a + b
print(add(2,5))
greet(add(2,5))
#p6a4
def square_num_in_list(x):
    for num in range(len(x)):
        x[num] = x[num] ** 2
    return x
#call square_num_in_list and print the new list
squared_list = square_num_in_list([1,2,3,4])
print(squared_list)

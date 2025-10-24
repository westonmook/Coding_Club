my_list = [1,'intern', 'liberty', 3, 4.4]
my_stack = my_list
def push(item_to_push, stack):
    my_stack.append(item_to_push)
def remove(stack):
    global my_stack
    my_stack = my_stack[0:-1]

#print(my_stack)
#push('added item', my_stack)
#print(my_stack)
#remove(my_stack)
#print(my_stack)
#remove(my_stack)
#print(my_stack)
#my_stack.append('moore')
#print(my_stack)
#print(my_stack.pop())
#print(my_stack)

#advanced
class stack():
    def __init__(self, list1):
        self.list = list1
    
    def push(self, item_to_push):
        self.list.append(item_to_push)
    
    def remove(self):
        self.list.pop()
    
    def show(self):
        print()
        for item in self.list:
            print(item)

mystack_instantiation = stack(my_stack)
msi = mystack_instantiation
#mystack_instantiation.show()
#mystack_instantiation.remove()
#mystack_instantiation.remove()
#mystack_instantiation.remove()
#print()
#msi.show()
#msi.push('i pushed this to the end of the stack')
#msi.show()
#msi.push('now this')
#msi.show()
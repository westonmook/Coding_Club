#Alexander Gubrud
list = []
for i in range(10):
    list.append(i)

print(list)

class list_pop():
    def __init__(self, list):
        self.list = list
        self.length = len(list)
        
    def print_list(self):
        for i in range(self.length):
            print(self.list[i])

    def pop(self):
        if self.length > 0:
            popped_item = self.list[self.length - 1]
            self.list = self.list[:self.length - 1]
            self.length -= 1
            return popped_item
        else:
            return None
        
my_list = list_pop(list)
my_list.print_list()
my_list.pop()

print(f"\nList after pop: {my_list.print_list()}")

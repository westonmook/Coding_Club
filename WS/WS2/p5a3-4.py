#p5a3-4 this is one of a few solutions
word = 'python'
print(word)
stack = list(word)
print(stack)
reversed_word = ""
while stack:
    reversed_word += stack.pop()
    print(reversed_word)
print(reversed_word)

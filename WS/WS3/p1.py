#reference the link below for further help.
#https://www.pythonforbiginners.com/2025/05/python-sets-made-easy-beginner-to-pro.html
sentence = "Learning Python is exciting!"
#assigning a set to a variable
vowels = {ch.lower() for ch in sentence if ch.lower() in "aeiou" }
print(vowels)
vowels.add('y')
print(vowels)
#remove a vowel
vowels.remove('e')
print(vowels)
print('Notice!!: Run this command multiple times and watch what happens to the order inside your set.')
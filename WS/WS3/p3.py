#Dictionaries: for a tutorial on dictionaries, ask a club member or go to the link below
#https://realpython.com/python-dicts/
text='Python programming is fun. Python is powerful'
words = text.split()
print(words)
#dictionary creation
freq = {}
#putting words in the dictionary
for word in words:
    freq[word] = freq.get(word, 0) + 1
print(freq)
print()
#p3a6-7
most_common = max(freq, key=freq.get)
print("Here are the most common words in the 'text' variable")
for key in freq:
    #print(key)
    if freq[key] == freq[most_common]:
        print(key, freq[key])
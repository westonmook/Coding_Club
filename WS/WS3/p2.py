#unpacking tuples
book = ("Red Rising", "Pierce Brown", "2014")
title, author, year = book

#Printf is a is similar to a differently syntaxed .format() use your favorite!

print(f"'{title}' by {author}, published in {year}")
book2 = ("Children of Time", "Adrian Tchaikovsky", "2015")
t,a,y=book2
print(f"'{t}' by {a}, published in {y}")

#swap the order of title and year

bookswap = (year, author, title)
print(bookswap)
t,a,y=bookswap
print(f"'{t}' by {a}, published in {y}")

#conditional while
a = True
count = 1
while a:
    print(count)
    count += 1
    print("type 'q' to break the loop")
    q = input()
    if q == 'q':
        a = False

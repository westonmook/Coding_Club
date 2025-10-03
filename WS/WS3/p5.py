#Make the list with a twist.
squares = []
for n in range(1,21):
    if n % 2 == 0:
        squares.append(n**2)
print(squares)
#Now for list comprehenstion
squares2 = [n**2 for n in range(1,21) if n % 2 == 0]
print(squares2)
print("Compare the two above to see if they're the same")
#modification of numbers(integers) divisible by four
#remember modulus % always returns an integer and checks for them
quads = [n for n in range(1,21) if n % 4 == 0]
print("quads below\n" + str(quads))
#p5a5
#one liners are cool I think. They are a little convaluted, but I think they are worth learning.
cube_odds = [n**3 for n in range(1,21) if n % 2 == 1]
print("Now for cubes of odds {coo}".format(coo = cube_odds))
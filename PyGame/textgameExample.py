print('You find yourself wandering through the woods with a serious case of retrograde amnesia.')
print('there is a fork in the path before you: Do you go Left, Right, or Back?')
print('________________________________________________________________________')

#function that takes multiple inputs
def ireduction(user_input):
    adjusted_input = user_input[0].lower()
    return adjusted_input

choice1 = ireduction(input())
#first choice
if choice1 == 'l':
    print('You go left')
    print('A horrible chill goes up your spine as you progress')
    print('go back or continue in spite of your fear?')
    print('________________________________________________________________________')
    choice2a = input()
    if choice2a == 'continue':
        print('A skeleton jumps out from behind a bush. It carries a sword and an old bronze colored breastplate.')
        print('waht do you do?')
        print('________________________________________________________________________')

elif choice1 == 'Right' or choice1 == 'right' or choice1 == 'r':
    print("You walk for a little ways, but unfortunatley your eyesight isn't what you think it is, so you fall in a massive mineshaft")

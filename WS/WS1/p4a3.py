
# Get the user's score as input
score = float(input("Enter the score: "))

# Evaluate the score and print the result
if score > 90:
    print("Excellent")
elif 70 <= score <= 90:
    print("Good")
else:
    print("Needs Improvement")

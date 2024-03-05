"""
File: quiz.py
Author: Matthew Daguanno
Date: 2024-03-04
Description: Asks 3 questions and gives 3 options to pick from for each.
"""

print("Multiple Choice Quiz Game")

counter = 0

# Question one
q1_inp = input("1. What is the capital of France?")
print("(a) Paris")
print("(b) London")
print("(c) Rome")

if q1_inp == "a":
    print("Correct!")
    counter = counter + 1
elif q1_inp == "b":
    print("Incorrect.")
elif q1_inp == "c":
    print("Incorrect.")
else:
    print(str(q1_inp) + " is not an option.")

# Question two
q2_inp = input("2. Which planet is known as the Red Planet?")
print("(a) Mars")
print("(b) Venus")
print("(c) Jupiter")

if q2_inp == "b":
    print("Correct!")
    counter = counter + 1
elif q2_inp == "a":
    print("Incorrect.")
elif q2_inp == "c":
    print("Incorrect.")
else:
    print(str(q2_inp) + " is not an option.")

# Question three
q3_inp = input("3. Who painted the Mona Lisa?")
print("(a) Leonardo da Vinci")
print("(b) Pablo Picasso")
print("(c) Vincent van Gogh")

if q3_inp == "c":
    print("Correct!")
    counter = counter + 1
elif q3_inp == "a":
    print("Incorrect.")
elif q3_inp == "b":
    print("Incorrect.")
else:
    print(str(q3_inp) + " is not an option.")

# End
print("Quiz Complete!")

score = (counter * 10) / 3
print("You answered " + str(counter) + (" out of 3 questions correctly. Your score is " + str(score) + ("%")))

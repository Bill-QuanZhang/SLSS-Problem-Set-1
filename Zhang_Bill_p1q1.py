# Quiz Creation Activity

# create questions
# get score if answer right
# give out the final results

# import
import time

# Chat before the quiz
print("Welcome!")

# start quiz
done = False
while not done:
    start_answer = input("Are you ready for this quiz?(yes or no)")
    if start_answer.lower().strip("?.,!") in ["y","yes"]:
        print("Great!")
        done = True
    elif start_answer.lower().strip("?.,!") in ["n","no"]:
        print("OK, take a breath and I will wait for a second.")
        time.sleep(5)
    else:
        print("Sorry, I can't understand what you said.")
        time.sleep(1)
print("Let's start!")

# Questions
# answer_1 = input("What is the answer for 2^10?") --> 1024
# answer_2 = input("What is the color of cloud?") --> white
# answer_3 = input("What is the second prime number?") --> 3
# answer_4 = input("Did the moon shine itself?") --> no
# answer_5 = input("What is the pH for pure water?") --> 7
questions = (
    ["What is the answer for 2^10?", ["1024"]],
    ["What is the color of cloud?",["white"]],
    ["What is the second prime number?",["3"]],
    ["Did the moon shine itself?",["n","no"]],
    ["What is the pH for pure water?",["7"]]
)

# Scores
score = 0

# answer
for question in questions:
    print(question[0])
    if input().lower().strip("?.,!") in question[1]:
        score += 1
        print("Nice work!")
    else:
        score += 0
        print("Ah oh.")
    time.sleep(2)

# give out the answer
print(f"Your final score is {score}!")
if score == 5:
    print("You did a perfect job!!!")
elif score >= 3:
    print("Not bad.")
elif score >= 1:
    print("Try to be better next time.")
else:
    print("You should work harder!")
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
# answer_1 = input("What is the answer for 2^10?")
# answer_2 = input("What is the color of cloud?")
# answer_3 = input("")
# answer_4 = input("")
# answer_5 = input("")

# Scores
score = 0

# answer


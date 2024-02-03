print("welcome to my quiz game ")
playing = input("would you like to the game? (y/n): ")
if playing.lower() != 'y': 
    quit()

print("Congratulations you have entered the game!!\n")
marks = []

def score() :
    marks.append(1)

answer = input("What is the Capital of Kerala? ")
if answer.lower() == "thiruvananthapuram"  or  answer.lower() == "tvm" : 
    score()
    print("Correct Answer!!")   
else :
    print("Better luck next time")


answer = input("What is the capital of India? ")
if answer.lower() == "new delhi"  or  answer.lower() == "newdelhi" : 
    score()
    print("Correct Answer!!")    
else :
    print("Better luck next time")

print("congratulations your score is ", sum(marks))
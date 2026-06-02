score=0
def correction (answer) :
    answer = answer.lower()
    answer = answer.strip()
    return answer
questions=["What is the largest planet in our solar system?",
           "Who wrote the play Romeo and Juliet?",
           "What is the capital city of Japan?",
           "Which element has the chemical symbol O?",
           "In which continent is the Sahara Desert located?"]
answers=["jupiter",
         "william shakespeare",
         "tokyo",
         "oxygen",
         "africa"]
for i in range (len(questions) ) :
    ans=correction(input(f"Question number {i+1}:\n {questions[i]}\n"))
    if ans == answers[i] :
        score += 1
        print(f"Correct , your score is {score} out of {i+1} ")
    else :
        print(f"wrong , your score is  {score} out of {i+1}")
print(f"congratulations, your final score is {score} out of 5 !")
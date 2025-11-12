from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"], question["correct_answer"]))


quiz1 = Quizbrain(question_bank)
still_has_questions = True
while quiz1.still_has_questions():
    quiz1.next_question()

print("You've completed the quiz!")
total_q = len(question_bank)
print(f"Your final score was: {quiz1.score}/{total_q}")



from question_model import Question, n_question
from data import question_data
from quiz_brain import Quizbrain
question_bank =[]
for question in question_data:
    question_text=question["text"]
    'print(question_text)'
    question_answer=question["answer"]
    n_question =Question(question_text,question_answer)
    question_bank.append(n_question)
'print(question_bank)'
quiz =Quizbrain(question_bank)
quiz.next_quesion()
while quiz.still_has_question():
    quiz.next_quesion()

print("you have completed the quiz")
print(f"your final score is ,{quiz.score} / {quiz.question_number}")
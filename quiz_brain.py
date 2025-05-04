class Quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_lis=q_list

    def still_has_question(self):
        return  self.question_number < len(self.question_lis)


    def next_quesion(self):
        current_question=self.question_lis[self.question_number]
        self.question_number += 1
        use_answer=input(f"Q:{self.question_number}:{current_question.text} (True / False):")
        self.check_answer(use_answer,current_question.answer)

    def check_answer(self,use_answer,correct_answer):
        if use_answer.lower() == correct_answer.lower():
            self.score += 1
            print("you got it right!")
        else:
            print("you got it wrong!")
        print(f"the answer was: {correct_answer}")
        print(f"the score is: {self.score} / {self.question_number}")
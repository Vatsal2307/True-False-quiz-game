class QuizBrain:

    def __init__(self, q_list):
        self.score = 0
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}:{current_question.text}(True/False):")
        self.check_answer(user_ans, current_question.answer)

    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_ans, correct_answer):
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("That was correct")
        else:
            print("That was not correct")
        print(f"The correct answer is: {correct_answer}")
        print(f"Your score is: {self.score}/{self.question_number}")
        print("\n")


        





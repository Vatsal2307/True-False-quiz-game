from question_model import QuestionClass
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item['question']
    question_answer = item['correct_answer']
    new_question = QuestionClass(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(q_list=question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("You have completed the quiz ")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")






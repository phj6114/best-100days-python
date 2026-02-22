from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_bank.append(Question(item["text"], item["answer"]))

# call the quiz brain class and pass in the question bank
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()




# quiz.py

from question_model import Question, User
from database import Database

class Quiz:
    def __init__(self, db):
        self.db = db

    def get_questions(self):
        questions_data = self.db.get_questions()
        questions = []
        for question in questions_data:
            question_id, question_text, option1, option2, option3, option4 = question
            options = [option1, option2, option3, option4]
            correct_option = self.db.get_correct_answer(question_id)
            questions.append(Question(question_id, question_text, options, correct_option))
        return questions

    def display_question(self, question):
        print(question.question_text)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")

    def get_user_choice(self):
        while True:
            choice = input("Enter the number of your answer: ")
            if choice.isdigit() and 1 <= int(choice) <= 4:
                return int(choice) - 1
            print("Invalid input. Please enter a number between 1 and 4.")

    def evaluate_answer(self, user_answer_index, question):
        user_answer = question.options[user_answer_index]
        if user_answer.strip().lower() == question.correct_option.strip().lower():
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

    def get_user_details(self):
        name = input("Enter your name: ").strip()
        surname = input("Enter your surname: ").strip()
        group = input("Enter your group: ").strip()
        return User(name, surname, group)

    def run_quiz(self):
        user = self.get_user_details()
        questions = self.get_questions()

        for question in questions:
            self.display_question(question)
            user_choice_index = self.get_user_choice()
            user.score += self.evaluate_answer(user_choice_index, question)

        print(f"\n{user.name}, your final score is: {user.score}/{len(questions)}")

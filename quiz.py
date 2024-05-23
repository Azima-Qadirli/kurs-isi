import psycopg2

class Quiz:
    def __init__(self, db):
        self.db = db

    def get_questions(self):
        return self.db.get_questions()

    def display_question(self, question_text, options):
        print(question_text)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")

    def get_user_choice(self):
        while True:
            choice = input("Enter your answer: ")
            if choice.isdigit() and 1 <= int(choice) <= 4:
                return int(choice)
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")

    def evaluate_answer(self, user_choice, correct_option):
        if user_choice == correct_option:
            print("Correct!")
            return 1
        else:
            print("Incorrect!")
            return 0

    def run_quiz(self):
        user_name = input("Enter your name: ")
        user_surname = input("Enter your surname: ")
        user_group = input("Enter your group: ")

        questions = self.get_questions()
        score = 0
        total_questions = len(questions)

        for question in questions:
            question_id, question_text, option1, option2, option3, option4 = question
            options = [option1, option2, option3, option4]

            self.display_question(question_text, options)
            user_choice = self.get_user_choice()

            correct_answer = self.db.get_correct_answer(question_id)
            correct_option = options.index(correct_answer) + 1 if correct_answer else None

            if correct_option:
                score += self.evaluate_answer(user_choice, correct_option)
            else:
                print("No correct answer found for this question.")

        print(f"{user_name} {user_surname} ({user_group}), you have completed the quiz!\nYour final score: {score}/{total_questions}")

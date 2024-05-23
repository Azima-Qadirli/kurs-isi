from add_quiz import QuizManager

def start_quiz():
    from quiz import Quiz
    from database import Database
    
    db = Database(dbname="Oop", user="postgres", password="psql12", host="localhost", port="5432")
    quiz = Quiz(db)
    quiz.run_quiz()
    db.close()

def add_new_quiz():
    question_text = input("Enter the question: ")
    options = [
        input("Enter option 1: "),
        input("Enter option 2: "),
        input("Enter option 3: "),
        input("Enter option 4: ")
    ]
    correct_option = int(input("Enter the number of the correct option (1-4): "))

    quiz_manager = QuizManager(dbname="Oop", user="postgres", password="psql12", host="localhost", port="5432")
    quiz_manager.add_question(question_text, options, correct_option)
    quiz_manager.close()
    print("Question added successfully!")

def delete_question():
    question_id = int(input("Enter the ID of the question to delete: "))
    quiz_manager = QuizManager(dbname="Oop", user="postgres", password="psql12", host="localhost", port="5432")
    quiz_manager.delete_question(question_id)
    quiz_manager.close()
    print("Question deleted successfully!")

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Start Quiz")
        print("2. Add New Quiz")
        print("3. Delete a Question")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            start_quiz()
        elif choice == '2':
            add_new_quiz()
        elif choice == '3':
            delete_question()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()

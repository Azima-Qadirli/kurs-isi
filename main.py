# main.py

from quiz import Quiz
from database import Database

def main():
    db = Database(dbname="oop", user="postgres", password="psql12", host="localhost", port="5432")
    quiz = Quiz(db)
    quiz.run_quiz()
    db.close()

if __name__ == "__main__":
    main()

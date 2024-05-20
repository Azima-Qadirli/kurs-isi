# database.py

import psycopg2

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname="oop",
            user="postgres",
            password="psql12",
            host="localhost",
            port="5432"
        )
        self.c = self.conn.cursor()

    def get_questions(self):
        self.c.execute("SELECT * FROM queries")
        questions = self.c.fetchall()
        return questions

    def get_correct_answer(self, question_id):
        self.c.execute("SELECT correct_option FROM answer WHERE question_id = %s AND is_correct = TRUE", (question_id,))
        correct_answer = self.c.fetchone()
        return correct_answer[0] if correct_answer else None

    def close(self):
        self.c.close()
        self.conn.close()

import psycopg2

class QuizManager:
    def __init__(self, dbname, user, password, host, port):
        self.conn = psycopg2.connect(
            dbname="Oop",
            user="postgres",
            password="psql12",
            host="localhost",
            port="5432"
        )
        self.c = self.conn.cursor()

    def add_question(self, question_text, options, correct_option):
        # Insert the question and get the generated question_id
        self.c.execute(
            "INSERT INTO sual (question_text, option1, option2, option3, option4) VALUES (%s, %s, %s, %s, %s) RETURNING sual_id",
            (question_text, options[0], options[1], options[2], options[3])
        )
        question_id = self.c.fetchone()[0]

        # Insert the correct answer into the cavab table
        self.c.execute(
            "INSERT INTO cavab (sual_id, is_correct, correct_option) VALUES (%s, %s, %s)",
            (question_id, True, options[correct_option - 1])
        )
        self.conn.commit()

    def delete_question(self, question_id):
        self.c.execute("DELETE FROM cavab WHERE sual_id = %s", (question_id,))
        self.c.execute("DELETE FROM sual WHERE sual_id = %s", (question_id,))
        self.conn.commit()

    def close(self):
        self.c.close()
        self.conn.close()

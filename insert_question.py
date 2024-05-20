# insert_questions.py

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname="oop",
    user="postgres",
    password="psql12",
    host="localhost",
    port="5432"
)
c = conn.cursor()

# Sample questions and correct answers
questions = [
    ("What is the capital of France?", ["London", "Berlin", "Paris", "Rome"], 3),
    ("Who wrote the novel '1984'?", ["George Orwell", "Aldous Huxley", "J.R.R. Tolkien", "Ernest Hemingway"], 1),
    ("Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 2),
    ("What is the chemical symbol for oxygen?", ["O", "C", "H", "N"], 1),
    ("Who is the author of 'To Kill a Mockingbird'?", ["J.K. Rowling", "Harper Lee", "George Orwell", "Ernest Hemingway"], 2),
    ("What is the largest planet in our solar system?", ["Earth", "Venus", "Jupiter", "Saturn"], 3),
    ("Who developed the theory of evolution by natural selection?", ["Charles Darwin", "Albert Einstein", "Isaac Newton", "Galileo Galilei"], 1),
    ("What is the chemical symbol for iron?", ["Ir", "Fe", "Au", "Ag"], 2),
    ("Who is credited with the theory of relativity?", ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Stephen Hawking"], 2),
    ("Which of the following is not a primary color?", ["Red", "Yellow", "Green", "Blue"], 3)
]

# Insert questions into the "queries" table
for question_text, options, correct_option in questions:
    option1, option2, option3, option4 = options
    c.execute("INSERT INTO queries (question_text, option1, option2, option3, option4) VALUES (%s, %s, %s, %s, %s) RETURNING question_id",
              (question_text, option1, option2, option3, option4))

    question_id = c.fetchone()[0]

    c.execute("INSERT INTO answer (question_id, is_correct, correct_option) VALUES (%s, %s, %s)",
              (question_id, True, options[correct_option - 1]))

# Commit the transaction
conn.commit()

# Close the cursor and connection
c.close()
conn.close()

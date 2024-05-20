# question_model.py

class Question:
    def __init__(self, question_id, question_text, options, correct_option):
        self.question_id = question_id
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option

class User:
    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group
        self.score = 0

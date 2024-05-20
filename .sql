-- public.queries definition

-- Drop table

-- DROP TABLE public.queries;
-- public.queries definition

-- Drop table if it exists
-- DROP TABLE public.queries;

CREATE TABLE public.queries (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    option1 TEXT NOT NULL,
    option2 TEXT NOT NULL,
    option3 TEXT NOT NULL,
    option4 TEXT NOT NULL
);




-- public.answer definition

-- Drop table

-- DROP TABLE public.answer;

CREATE TABLE public.answer (
	question_id int8 NOT NULL,
	is_correct bool NOT NULL,
	correct_option text NOT NULL
);


INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (1, 'What is the capital of France?', 'London', 'Berlin', 'Paris', 'Madrid');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (2, 'What is the tallest mountain in the world?', 'Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (3, 'What is the largest ocean on Earth?', 'Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (4, 'In which year did the first iPhone launch?', '2004', '2005', '2006', '2007');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (5, 'What is the process of converting a gas to a liquid called?', 'Condensation', 'Evaporation', 'Sublimation', 'Deposition');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (6, 'How many hearts does an octopus have?', 'Three', 'Two', 'One', 'Three');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (7, 'What is the currency of Japan?', 'Yen', 'Yuan', 'Won', 'Rupee');
INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
  (8, 'What is the largest planet in our solar system?', 'Jupiter', 'Saturn', 'Uranus', 'Neptune');

INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
   (9, 'Which language has more native speakers?', 'English', 'Spanish', 'Russian', 'Chinese');

INSERT INTO queries (question_id, question_text, option1, option2, option3, option4) 
VALUES 
     (10, 'What car manufacturer had the highest revenue in 2020?', 'Volkswagen', 'BMW', 'Mercedes', 'Audi');

INSERT INTO answer (question_id, is_correct, correct_option)
VALUES (1, True, 'Paris');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (2,True,'Mount Everest');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (3,True,'Pacific Ocean');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (4,True,'2007');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (5,True,'Condensation');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (6,True,'three');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (7,True,'Yen');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (8,True,'Jupiter');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (9,True,'English');

INSERT INTO answer (question_id, is_correct, correct_option)
values  (10,True,'Volkswagen');

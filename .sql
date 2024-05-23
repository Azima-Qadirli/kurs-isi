DROP TABLE IF EXISTS public.sual;

-- Create the sual table with sual_id as SERIAL
CREATE TABLE public.sual (
    sual_id SERIAL PRIMARY KEY,      -- Auto-incrementing primary key
    question_text TEXT NOT NULL,     -- Text of the question
    option1 TEXT NOT NULL,           -- First option
    option2 TEXT NOT NULL,           -- Second option
    option3 TEXT NOT NULL,           -- Third option
    option4 TEXT NOT NULL            -- Fourth option
);

-- Drop the existing table if it exists
DROP TABLE IF EXISTS public.cavab;

-- Create the cavab table with a foreign key reference to sual
CREATE TABLE public.cavab (
    sual_id INT NOT NULL,            -- Foreign key to the sual table
    is_correct BOOL NOT NULL,        -- Indicates if the answer is correct (always true for the correct option)
    correct_option TEXT NOT NULL,    -- The correct option text
    FOREIGN KEY (sual_id) REFERENCES public.sual(sual_id)  -- Foreign key constraint
);



INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (1, 'What is the capital of France?', 'London', 'Berlin', 'Paris', 'Madrid');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (2, 'What is the tallest mountain in the world?', 'Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (3, 'What is the largest ocean on Earth?', 'Pacific Ocean', 'Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (4, 'In which year did the first iPhone launch?', '2004', '2005', '2006', '2007');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (5, 'What is the process of converting a gas to a liquid called?', 'Condensation', 'Evaporation', 'Sublimation', 'Deposition');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (6, 'How many hearts does an octopus have?', 'Three', 'Two', 'One', 'Three');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (7, 'What is the currency of Japan?', 'Yen', 'Yuan', 'Won', 'Rupee');
INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
  (8, 'What is the largest planet in our solar system?', 'Jupiter', 'Saturn', 'Uranus', 'Neptune');

INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
   (9, 'Which language has more native speakers?', 'English', 'Spanish', 'Russian', 'Chinese');

INSERT INTO sual (sual_id, question_text, option1, option2, option3, option4) 
VALUES 
     (10, 'What car manufacturer had the highest revenue in 2020?', 'Volkswagen', 'BMW', 'Mercedes', 'Audi');

INSERT INTO cavab (sual_id, is_correct, correct_option)
VALUES (1, True, 'Paris');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (2,True,'Mount Everest');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (3,True,'Pacific Ocean');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (4,True,'2007');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (5,True,'Condensation');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (6,True,'three');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (7,True,'Yen');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (8,True,'Jupiter');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (9,True,'English');

INSERT INTO cavab (sual_id, is_correct, correct_option)
values  (10,True,'Volkswagen');

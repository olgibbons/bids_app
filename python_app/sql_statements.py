statements = [
"""CREATE TABLE IF NOT EXISTS bids (
    bid_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    sector TEXT,
    framework TEXT,
    closing_date TEXT
);""",

"""CREATE TABLE IF NOT EXISTS rounds (
    round_id INTEGER PRIMARY KEY,
    round INTEGER,
    outcome TEXT,
    bid_id INTEGER,
    FOREIGN KEY (bid_id) REFERENCES bids (bid_id)
);""",

"""CREATE TABLE IF NOT EXISTS sections (
    section_id INTEGER PRIMARY KEY,
    section TEXT,
    limit_per_question_default INT,
    limit_unit TEXT,
    round_id INTEGER,
    FOREIGN KEY (round_id) REFERENCES rounds (round_id)
);""",

"""CREATE TABLE IF NOT EXISTS questions (
    question_id INTEGER PRIMARY KEY,
    question TEXT,
    question_weighting_value INT,
    question_limit INT,
    question_limit_unit TEXT,
    section_id INTEGER,
    FOREIGN KEY (section_id) REFERENCES sections (section_id)
);""",

"""CREATE TABLE IF NOT EXISTS answers (
    answer_id INTEGER PRIMARY KEY,
    answer TEXT,
    author TEXT,
    question_id INT,
    FOREIGN KEY (question_id) REFERENCES questions(question_id)
);"""]

"""
CREATE TABLE IF NOT EXISTS questions_answers (
    question_id INTEGER,
    answer_id INTEGER,
    PRIMARY KEY (question_id, answer_id),
    FOREIGN KEY (question_id) REFERENCES questions (question_id),
    FOREIGN KEY (answer_id) REFERENCES answers (answer_id)
);
"""

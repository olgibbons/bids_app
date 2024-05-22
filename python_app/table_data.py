import sqlite3

def insert_data(db, statements):
    try:
        with sqlite3.connect(db) as conn:
            cur = conn.cursor()
            for statement in statements:
                cur.execute(statement)

            conn.commit()
    except sqlite3.Error as e:
        print(e)

"""note olgibbons: sql at risk of injection attacks"""

insert_statements = [
"""INSERT INTO bids (title, sector, closing_date)
VALUES ("Medical Technology - Product Information Management Data Platform - Alpha phase", "DHSC", "07/02/2024");""",

"""INSERT INTO rounds (round, outcome, bid_id)
VALUES (1, "success", 1);""",

"""INSERT INTO sections (section, section_limit, limit_unit, section_weighting_total, round_id)
VALUES
("Essential Skills and Experience", 750, "char",100, 1),
("Nice-to-have", 750, "char", 100, 1);""",

"""INSERT INTO questions (question, question_weighting_value, section_id)
VALUES
("Experience of delivering an alpha phase for a large-scale data platform
which meets the GOV.UK Service Standard and Technical Code of Practice criteria,
including experience of successfully passing a service assessment", 20, 1),
("Experience of working with different types of
primary and secondary data and how to integrate
those into a central data platform, including data
cleansing and development of data standard.", 10, 1),
("Significant experience in developing, testing and
iterating prototypes through user testing/research,
ensuring this will lead to the successful delivery of
this service, and evaluating options for any future
beta phase.", 10, 1),
("Experience of developing data driven solutions,
including initial priming of a database and on-going
maintenance of data.", 10, 1),
("Significant user research experience, including in
line with GOV.UK Service Manual recommended
practices.", 10, 1),
("Experience of working with product-level and/or
healthcare data.", 34, 2);"""
]

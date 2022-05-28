"""
MuleSoft Assessment
Submitted by:
    Anusha Subramanyam
    Vidyavardhaka College of Engineering
    CSE-A, 4VV19CS015
"""

import sqlite3
import pandas as pd

conn = sqlite3.connect('Movie.db')
print("Database Created\n")
conn = sqlite3.connect(':memory:')
cur = conn.cursor()

conn.execute("""CREATE TABLE movies(
            name text, 
            actor text,
            actress text,
            director text,
            year_of_release integer
            )""")
print("Table Created\n")

print("Inserting Values into the table\n")
def insert_data(name, actor, actress, director, year_of_release):
    cur.execute("INSERT INTO movies VALUES (?, ?, ?, ?, ?)", (name, actor, actress, director, year_of_release))

insert_data('Kabhi Khushi Kabhi Ghum', 'SRK', 'Kajol', 'Karan Johar', 2001)
insert_data('Heropanti','Tiger Shroff','Kriti Sanon','Sabbir Khan',2014)
insert_data('Krrish','Hrithik Roshan','Priyanka Chopra','Rakesh Roshan',2003)
insert_data('Chennai Express','SRK','Deepika','Rohit Shetty',2013)
insert_data('URI','Vicky Kaushal','Yami Gautam','Aditya Dhar',2019)
insert_data('Kesari','Akshay Kumar','Parineeti Chopra','Anurag Singh',2019)
insert_data('Bhaghi-3','Tiger Shroff','Shradha kapoor','Ahmed Khan',2020)
insert_data('Mission Mangal','Akshay Kumar','Vidya Balan','Jagan Shakti',2019)
insert_data('Raazi','Vicky Kaushal','Alia Bhat','Meghana Gulzar',2018)
insert_data('Shershaah','Sidharth Malhotra','Kiara Advani','Vishnuvardhan',2021)

print("Querying data from the database\n")
print("* Querying the movies table using SELECT statement\n")
data = cur.execute("SELECT * FROM movies")
rows = cur.fetchall()
for i in rows:
    print(i)

print("\n")

col_names = [cn[0] for cn in cur.description]
print("{:25} {:20} {:20} {:20} {:4}".format(col_names[0], col_names[1], col_names[2], col_names[3], col_names[4]))
for row in rows:
    print("{:<25} {:<20} {:20} {:20} {:4}".format(row[0], row[1], row[2], row[3], row[4]))


print("\n* Query with parameter like actor name to select movies based on the actor's name\n")
cur.execute("SELECT * FROM movies WHERE actor=:actor",{"actor":"SRK"})
for i in cur:
    print(i)


print("\n* Query with parameter like year to select movies released after 2014\n")
cur.execute("SELECT name, director, year_of_release FROM movies WHERE year_of_release>=2014")
for i in cur:
    print(i)


cur.close()
conn.commit()
print("\nDatabase Closed")


import csv
from sys import argv, exit
from cs50 import SQL

if len(argv) != 2:
    print("Usage: python import.py data.csv ")
    exit(1)

db = SQL("sqlite:///students.db")

with open(argv[1], "r") as file:
    data = csv.DictReader(file, delimiter = ',')

    for row in data:
        name = row['name'].split()

        if len(name) == 2:
            first = name[0]
            last = name[1]
            middle = None

        else:
            first = name[0]
            middle = name[1]
            last = name[2]


        house = row['house']
        birth = row['birth']

        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)

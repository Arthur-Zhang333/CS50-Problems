import csv
from sys import argv, exit
from cs50 import SQL

if len(argv) != 2:
    print("Usage: python import.py house ")
    exit(1)

db = SQL("sqlite:///students.db")


x = db.execute("SELECT first, middle, last, birth FROM students WHERE house IN (?) ORDER BY last", argv[1])
for n in range(len(x)):
    if x[n]['middle'] == None:
        print(x[n]['first'], end = " ")
        print(x[n]['last'], end = ", ")
        print(f"born {x[n]['birth']}")

    else:
        print(x[n]['first'], end = " ")
        print(x[n]['middle'], end = "")
        print(x[n]['last'], end = ", ")
        print(f"born {x[n]['birth']}")

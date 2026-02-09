#creating csv file and writing data to it
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","Grade","Status"])
    writer.writerow(["Alice","A","Pass"])
    writer.writerow(["Bob","B","Pass"])
    writer.writerow(["Charlie","F","Fail"])
# To read data from CSV file and print names of students who passed
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        if row["Status"] == "Pass":
            print(row["Name"])
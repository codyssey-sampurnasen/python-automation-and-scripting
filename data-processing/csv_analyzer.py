"""
CSV Analyzer

Reads a CSV file and displays basic information like number of rows and columns.

Features:
- File handling
- Data inspection

Author: Sampurna Sen
"""

import csv

def analyze_csv(file_name):
    try:
        with open(file_name, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)

            print("\nTotal Rows:", len(rows))

            if len(rows) > 0:
                print("Columns:", len(rows[0]))

    except FileNotFoundError:
        print("File not found!")

# User input
file_name = input("Enter CSV file name: ")

analyze_csv(file_name)

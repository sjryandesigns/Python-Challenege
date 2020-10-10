#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Open and read csv
with open(budget_csv) as csv_file:
    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    
    #Read each row of data after header
    for row in csv_reader:
        
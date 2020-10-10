#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Define and create budget analysis function
def budget_analysis(budget_data):
    
    # Create lists for dates and profits (data columns on csv file)
    dates = []
    profits = []

    # Loop through csv file and add dates to dates list, profits to profits list     
    for date, profit in csv_reader
        dates.append(date)
        profits.append(profit)

    # Cast values in profits list as integers
    profits=[int(i) for i in profits]

    # Definte and calculate net profit and total months
    net_profit = sum(profits)
    total_months = len(dates)

    # Calculate to find average profit change, round to two decimals
    avg_change = round((net_profit / total_months), 2)

    # Loop to find row with largest profit value 
    prev_profit= 0
    increase_date=""
    increase_total=0
    # decrease_date=""
    # decrease_total= 0 

    for row in csv_reader:
               
        if int(row[1]) >= int(prev_profit):
            increase_date == row[0]
            increase_total == row[1]

        prev_profit == int(row[1])

        # if int(row[1]) < prev_profit:
        #     decrease_date== str(row[0])
        #     decrease_total == int(row[1])
        #     prev_profit == int(row[1])

    # Print Financial Analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {net_profit}")
    print(f"Average Change: ${avg_change}")
    print(f'{increase_date}')
    print(f'{increase_total}')
    # print(f"Greatest Increase in Profits: {increase_date} + {increase_total}")
    # print(f"Greatest Decrease in Profits: {decrease_date} -({increase_total})")

# Open and read csv
with open(budget_csv) as csv_file:

    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    header = next(csv_file)

    # Run function on budget csv file    
    budget_analysis(budget_csv)

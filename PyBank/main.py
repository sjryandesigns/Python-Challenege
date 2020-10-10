#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")


def budget_analysis(budget_data):
    
    date = str(budget_data[0])
    profit = float(budget_data[1])

    total_months = len(date)
    net_profit = sum(profit)
    avg_change = net_profit / total_months

    for rows in budget_data
        if profit > next(profit)
            increase_total = profit
            increase_date = date
        if profit > next(profit)
            decrease_total = profit
            decrease_date = date

            



    
    
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {str(total_months)}")
    print(f"Total: {str(net_profit)}")
    print(f"Average Change: {str(avg_change)}")
   

        



# Open and read csv
with open(budget_csv) as csv_file:
    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    
    #Read each row of data after header
    for row in csv_reader:
       budget_analysis(budget_data)
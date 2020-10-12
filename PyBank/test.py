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
    header = next(csv_file)
    
    dates = 0
    profits = 0
    profit_changes = []
    row_count=0
    prev_profit=0
    increase_total=0
    decrease_total=0
    i=0
    
    


    for row in csv_reader:
        dates += 1
        profits += int(row[1])

        if dates > 1:
            prft_change=int(row[1]) - prev_profit
            profit_changes.append(prft_change) 
        
        
        
        if int(row[1]) >= prev_profit:
            increase_total=int(row[1])
            increase_date = str(row[0])
        elif int(row[1])< prev_profit:
            decrease_total=prev_profit
            decrease_date = str(row[0])

        
            

        prev_profit=int(row[1])
    
    change_len = len(profit_changes)
    change_add = sum(profit_changes)
    avg_change = round(change_add / change_len,2)

    # increase_total = max(profit_changes)

    # increase_pos = profits.index(increase_total)
    # increase_date = dates[increase_pos]

    # decrease_total = min(profits)
    # decrease_pos = profits.index(decrease_total)
    # decrease_date = dates[decrease_pos]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {dates}")
    print(f"Total: {profits}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {increase_date} + {increase_total}")
    print(f"Greatest Decrease in Profits: {decrease_date} -({decrease_total})")
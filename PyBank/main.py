# Import modules os to create file paths and csv to read CSV files
import os
import csv

# Create file path to csv source file
budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")

# Set destination path for csv file to be created
output_path = os.path.join(os.path.dirname(__file__),"Analysis", "financial_analysis.csv")

# Open and read csv
with open(budget_csv) as csv_file:

    # Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    header = next(csv_file)
    
    # Create and initialize variables and lists for data
    dates = 0
    profits = 0
    profit_changes = []
    months = []
    profitloss= []
    prev_profit=0

    # Loop through rows in csv file
    for row in csv_reader:
        # Add to date counter and profit/loss value to running total counter
        dates += 1
        profits += int(row[1])

        # Add date value to months list and profit/loss value to profit/loss list
        months.append(str(row[0]))
        profitloss.append(int(row[1]))

        # Conditional to skip first row in calculating profit change
        if dates > 1:
            # Subtract current row profit/loss from previous row value and add value to profit change list
            prft_change=int(row[1]) - prev_profit
            profit_changes.append(prft_change) 

        # Update previous profit variable with current row profit/loss for next loop iteration
        prev_profit=int(row[1])
    
    # Calculate the sum and count of values in profit change list, then find average change with 2 decimals
    change_len = len(profit_changes)
    change_add = sum(profit_changes)
    avg_change = round(change_add / change_len,2)

    # Use profit loss list to find minimum and maximum values
    # Save index of min/max values then pull value at same index in months list
    increase_total = max(profitloss)
    increase_pos = profitloss.index(increase_total)
    increase_date = months[increase_pos]

    decrease_total = min(profitloss)
    decrease_pos = profitloss.index(decrease_total)
    decrease_date = months[decrease_pos]

    # Print Financial Analysis summary to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {dates}")
    print(f"Total: {profits}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase_total})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_total})")

# Write the following rows to the csv file    
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {dates}"])
    csvwriter.writerow([f"Total: {profits}"])
    csvwriter.writerow([f"Average Change: ${avg_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {increase_date} (${increase_total})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {decrease_date} (${decrease_total})"])
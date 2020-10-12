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
    months = []
    profitloss= []
    prev_profit=0


    for row in csv_reader:
        dates += 1
        profits += int(row[1])

        months.append(str(row[0]))
        profitloss.append(int(row[1]))

        if dates > 1:
            prft_change=int(row[1]) - prev_profit
            profit_changes.append(prft_change) 
   
        prev_profit=int(row[1])
    
    change_len = len(profit_changes)
    change_add = sum(profit_changes)
    avg_change = round(change_add / change_len,2)

    increase_total = max(profitloss)

    increase_pos = profitloss.index(increase_total)
    increase_date = months[increase_pos]

    decrease_total = min(profitloss)
    decrease_pos = profitloss.index(decrease_total)
    decrease_date = months[decrease_pos]

    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {dates}")
    print(f"Total: {profits}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {increase_date} (${increase_total})")
    print(f"Greatest Decrease in Profits: {decrease_date} (${decrease_total})")

output_path = os.path.join(os.path.dirname(__file__),"Analysis", "financal_analysis.csv")
    
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["----------------------------"])
    csvwriter.writerow([f"Total Months: {dates}"])
    csvwriter.writerow([f"Total: {profits}"])
    csvwriter.writerow([f"Average Change: ${avg_change}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {increase_date} (${increase_total})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {decrease_date} (${decrease_total})"])
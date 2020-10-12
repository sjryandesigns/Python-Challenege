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
    profit_changes = []

    # Loop through csv file and add dates to dates list, profits to profits list     
    for date, profit in csv_reader:
        dates.append(date)
        profits.append(profit)

    # Cast values in profits list as integers
    profits=[int(i) for i in profits]

    # Define and calculate net profit and total months
    net_profit = sum(profits)
    total_months = len(dates)

   # #this works
    increase_total = max(profits)
    increase_pos = profits.index(increase_total)
    increase_date = dates[increase_pos]

    decrease_total = min(profits)
    decrease_pos = profits.index(decrease_total)
    decrease_date = dates[decrease_pos]


    # Average of profit changes

    #Grab first value of list and store in variable previous
    #start looping on second row
    #calc diff between current loop & prev
    #update previous to current
    #Set value for first value in profits for use in loop
    prev_profit=profits[0]

    #Loop through profits from second value to end of list
    for i in range(1, len(profits)):
        #Calculate and record different between profit values of current loop and previous loop
        prft_change=profits[i] - prev_profit
        #Add differences from above into list of profit changes 
        profit_changes.append(prft_change) 
        #Update previous profit value with current profit value for next loop iteration
        prev_profit=profits[i]

    change_len = len(profit_changes)
    change_add = sum(profit_changes)
    avg_change = round(change_add / change_len,2)
    

    # Print Financial Analysis to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: {net_profit}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {increase_date} + {increase_total}")
    print(f"Greatest Decrease in Profits: {decrease_date} -({decrease_total})")

# Open and read csv
with open(budget_csv) as csv_file:

    #Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    header = next(csv_file)

    # Run function on budget csv file    
    budget_analysis(budget_csv)



    # # Loop to find row with largest profit value 
    # prev_profit= 0
    # increase_date=""
    # increase_total=0
    # # decrease_date=""
    # # decrease_total= 0 

    # for row in csv_reader:
               
    #     if int(row[1]) >= prev_profit:
    #         increase_date == str(row[0])
    #         increase_total == int(row[1])

    #     prev_profit == int(row[1])

        # if int(row[1]) < prev_profit:
        #     decrease_date== str(row[0])
        #     decrease_total == int(row[1])
        #     prev_profit == int(row[1])


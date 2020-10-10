#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")


def budget_analysis(budget_data):
    
    prev_profit=0
    increase_date=0
    increase_total= 0 
    decrease_date=0
    decrease_total= 0 

    date = []
    profit = []
         
    for a, b in csv.reader(csv_file, delimiter=','):
        date.append(a)
        profit.append(b)

    profit=[int(i) for i in profit]

    net_profit = sum(profit)
    total_months = len(date)
   
    avg_change = round((net_profit / total_months), 2)
     
    

    for row in csv_reader:
               
        if int(row[1]) >= prev_profit:
            increase_date == str(row[0])
            increase_total == int(row[1])
            prev_profit == int(row[1])

        if int(row[1]) < prev_profit:
            decrease_date== str(row[0])
            decrease_total == int(row[1])
            prev_profit == int(row[1])

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
    budget_analysis(budget_csv)

#     #Read each row of data after header
#     for rows in csv_reader:
#         date = str(budget_csv[0])
#         profit = int(budget_csv[1])
#         max_increase = 0
#         max_decrease = 0

#         total_months = len(date)
#         net_profit = sum(budget_csv[1])
#         avg_change = (net_profit / total_months)
    
#         if budget_csv[1]>= max_increase:
#             increase_total = int(profit)
#             increase_date = str(date)
#         if profit < max_decrease:
#             decrease_total = int(profit)
#             decrease_date = str(date)

#     print("Financial Analysis")
#     print("----------------------------")
#     print(f"Total Months: {str(total_months)}")
#     print(f"Total: {str(net_profit)}")
#     print(f"Average Change: {str(avg_change)}")
#     print(f"Greatest Increase in Profits: {increase_date} (${int(increase_total)}")
#     print(f"Greatest Decrease in Profits: {decrease_date} ($-{int(decrease_total)}")
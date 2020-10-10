# #Import modules os to create file paths and csv to read CSV files
# import os
# import csv

# #Create file path to csv source file
# budget_csv = os.path.join(os.path.dirname(__file__), "Resources", "budget_data.csv")


# # def budget_analysis(budget_data):
    
#     # date = str(budget_data[0])
#     # profit = budget_data[1]
#     # next_profit = next(profit)

#     # total_months = len(date)
#     # net_profit = sum(profit)
#     # avg_change = (net_profit / total_months)
    
#     # if profit > next_profit:
#     #     increase_total = profit
#     #     increase_date = date
#     # if profit > next_profit:
#     #     decrease_total = profit
#     #     decrease_date = date

#     # print("Financial Analysis")
#     # print("----------------------------")
#     # print(f"Total Months: {str(total_months)}")
#     # print(f"Total: {str(net_profit)}")
#     # print(f"Average Change: {str(avg_change)}")
#     # print(f"Greatest Increase in Profits: {increase_date} {str((increase_total))}")
#     # print(f"Greatest Decrease in Profits: {decrease_date} {str((decrease_total))}")

# # Open and read csv
# with open(budget_csv) as csv_file:
#     #Specify delimiter and variable that holds contents
#     csv_reader = csv.reader(csv_file, delimiter=",")

#     # Read the header row first 
#     header = next(csv_file)
    
#     #Read each row of data after header
#     for rows in csv_reader:
#         date = budget_csv[0]
#         profit = budget_csv[1]
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
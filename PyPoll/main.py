#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
poll_csv = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")


# Open and read csv
with open(poll_csv) as csv_file:
    # Specify delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    header = next(csv_file)
    
    total_votes = 0
    all_candidates_w_dup = []
    candidate_totals = {}
    #Looping through data
    for rows in csv_reader:

        #Adding one each row to get total votes    
        total_votes += 1
        
        #Adding all candidates per row to list, with duplicates
        all_candidates_w_dup.append(rows[2])

        #Conditional: If candidate is currently in dictionary, add +1 to value
        if candidate_totals.get(rows[2]):
            candidate_totals[rows[2]]+=1
        #Conditional Cont: If candidate is not currently in dictionary, add to dictionary and add 1 to value
        else:
            candidate_totals[rows[2]]=1
        

    
    # print("Election Results")
    # print("-------------------------")
    # print(f"Total Votes: {total_votes}")
    

    
#Import modules os to create file paths and csv to read CSV files
import os
import csv

#Create file path to csv source file
poll_csv = os.path.join(os.path.dirname(__file__), "Resources", "election_data.csv")

# Set destination path for csv file to be created
output_path = os.path.join(os.path.dirname(__file__),"Analysis", "financal_analysis.csv")


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

    print(candidate_totals)
  
    # # Print election results for summary table
    # print("Election Results")
    # print("-------------------------")

    # # Print count of total votes taken during loop
    # print(f"Total Votes: {total_votes}")
    # print("-------------------------")

    # # # Loop through candidate totals dictionary to print a row for each candidate
    # # for candidate in candidate_totals:

    #     # Print candidate name, the percentage of votes received out of total, and the number of votes received

    #     #  # print(f'{candidate}: '+ (round((({candidate_totals[candidate]}/total_votes)*100),3))+'% ' +{candidate_totals[candidate]})
    #     # print(candidate + ": " + str(round(((candidate_totals[candidate]/total_votes)*100),3)) + "%" + " (" + str(candidate_totals[candidate]) + ")")
    # print(candidate_totals[0[0]] + ": " + int(round(((candidate_totals[0[1]]/total_votes)*100),3)) + "%" + " (" + str(candidate_totals[0[1]]) + ")") 
    # print([key for key in candidate_totals.keys()][0],": ", str(round((([value for value in candidate_totals.values()][0]/total_votes)*100),3)),"% ", [value for value in candidate_totals.values()][0]) 

    # print(', '.join(str(key) + ', ' + str(value) for key, value in candidate_totals.items())) 
    # print([key for key in candidate_totals.keys()][1], [value for value in candidate_totals.values()][1])
    # print(([key for key in candidate_totals.keys()][2], [value for value in candidate_totals.values()][2]))    
    # print(([key for key in candidate_totals.keys()][3], [value for value in candidate_totals.values()][3])) 
        
        # print("-------------------------")

    # # print("Winner: " +str(list(candidate_totals.keys())[list(candidate_totals.values()).index(max(listVotes))]))
    
    # # Create and define winner as name from all candidate list that occurs the most times
    # winner = max(set(all_candidates_w_dup), key = all_candidates_w_dup.count)

    # # Print winner name to summary table
    # print("Winner: " +str(winner))
    # print("-------------------------")

# with open(output_path, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter=',')
#     csvwriter.writerow(["Election Results"])
#     csvwriter.writerow(["-------------------------"])
#     csvwriter.writerow([f"Total Votes: {total_votes}"])
#     csvwriter.writerow(["-------------------------"])
#     for candidate in candidate_totals:
#         csvwriter.writerow([candidate + ": " + str(round(((candidate_totals[candidate]/total_votes)*100),3)) + "%" + " (" + str(candidate_totals[candidate]) + ")"])
#     csvwriter.writerow(["-------------------------"])
#     csvwriter.writerow(["Winner: " +str(winner)])
#     csvwriter.writerow(["-------------------------"])
#import datetime
#now = datetime.datetime.now()
#print ("The timne right now is ", now)

#file_to_load = "Resources/election_results.csv"
#with open(file_to_load) as election_data:
    #print(election_data)

# Add our dependencies 
import os
import csv
# dir(os)

# Assign a variable to laod a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the files to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize a total vote counter
total_votes = 0

#Create a new list
candidate_options =[]
#Create a empty dictionary
candidate_votes = {}

#Winnng Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file 
    for row in file_reader:
        #Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate name from each row
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
    
    # Save the results to the text file
    with open(file_to_save, "w") as txt_file:

        #Print the final vote count to the terminal
        election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"----------------------\n")
        print(election_results, end="")
    
        #Save the final vote count to the text file
        txt_file.write(election_results)
        #Iterate throught the canidate list
        for candidate_name in candidate_votes:
            #Retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            #Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate_name}: received {vote_percentage:.1f}% ({votes:,}).\n")

            #Print each candidate, their voter count, and percentage to the terminal
            print(candidate_results)
            #Save the candidate results to our text file
            txt_file.write(candidate_results)

            #Determine if the votes are grater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #Set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        
        #Print the winning candidates' results to the terminal
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}\n"
            f"---------------------------\n")
            
        #Save the winning candidate's name to the text file
        txt_file.write(winning_candidate_summary)

#print (winning_candidate_summary)
#Print the candidate list.
#print(candidate_votes)
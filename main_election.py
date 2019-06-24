
import os
import csv

# Load file
csv_file = os.path.join(r"C:\Users\vuntu\Desktop\HomeWork-Python\Python-Challange\PyPoll\election_data.csv")

#Output file
txt_file = os.path.join(r"C:\Users\vuntu\Desktop\HomeWork-Python\Python-Challange\PyPoll\electionResultFile.txt")

#Total Votes Counter
total_votes = 0

# Vote counters and candidate list
candidate_votes = {}
candidate_list = []

# Winning Candidate and Winning Count Tracker
winning_cand = ""
winning_count = 0

# Read csv file
with open(csv_file) as election_data:
    csv_reader = csv.reader(election_data)

    #Read header
    header = next(csv_reader) 

    #For each row---
    for row in csv_reader:

     # Run the loader animation
        print(". ", end=""),

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extracting candidate name from each row....
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_list:

            # Add it to the list of running candidate
            candidate_list.append(candidate_name)

            # Start candidate's voting count
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    # Then add a vote to that candidate's count

# Print the results and export the data to text file

with open(txt_file, "w") as txtfile:

    # Print the final vote count
    election_results = (
        f"\n\nElection Results\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Saving final num to the text file
    txtfile.write(election_results)

    # Determine the winner
    for candidate in candidate_votes:

        # Retrieve vote count and %
        votes = candidate_votes.get(candidate)
        vote_percent = float(votes) / float(total_votes) * 100

        # Determine winning vote count and candidate
        if (votes > winning_count):
            winning_count = votes
            winning_cand = candidate

        # Print each candidate's voter count and %
        voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
        print(voter_output, end="")

        # Save each candidate's voter count and percentage to text file
        txtfile.write(voter_output)

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_cand}\n"
        f"-------------------------\n")

    print(winning_candidate_summary)
    txtfile.write(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    #txtfile.write("C:\\Users\\vuntu\\Desktop\\HomeWork-Python\\Python-Challange\\PyPoll\\electionResultFile.txt")


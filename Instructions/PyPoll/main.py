"PyPoll Homework Solution"

#Import required packages
import csv
import os

#Files to load and output
file_to_load = os.path.join('Resources','election_data.csv')
file_to_output = os.path.join('analysis','output_election_data.txt')

# Create placeholders for the variables
voter_ids=0
count = 0
percent_votes=[]
candidates_list={}
winner=[]
winner1=""

with open(file_to_load) as election_data:

    reader = csv.reader(election_data, delimiter=",")

    print(reader)

    header= next(reader)

    # Loop through each row, re-grab each field and store in the new list
    for row in reader:
    
        # Grab voterids and store it into a variable and calculate the total number of voters/votes
        voter_ids = voter_ids + 1

        # Created an empty Dictionary named candidates_list, loop through each row and store the key "candidate_name":value "number of votes"
        if row[2] not in candidates_list:
            candidates_list.update({row[2]:1})

        else:
            candidates_list[row[2]] = candidates_list [row[2]] + 1

    # Created an empty list named "percent_votes", and by looping through the Dictionary "candidates_list" with the key "candidate" I am accessing the value inside of an equation and loading list with the equation results
    winner_votes = 0 
    
    for candidate in candidates_list:
        percent_votes.append(round((candidates_list[candidate]/voter_ids)*100,3))
        winner.append(candidates_list[candidate])
        if candidates_list[candidate] > winner_votes:
            winner_votes = candidates_list[candidate]
            winner1 = candidate   
      
    # for candidate in candidates_list[candidate]:

                
    print("Election Results")
    print("_________________________")
    print("Total Votes: ",(voter_ids))
    print("_________________________")
    print("Khan:",percent_votes[0],"%", "(",candidates_list["Khan"],")")
    print("Correy:",percent_votes[1],"%", "(",candidates_list["Correy"],")")
    print("Li:",percent_votes[2],"%", "(",candidates_list["Li"],")")
    print("O'Tooley:",percent_votes[3],"%", "(",candidates_list["O'Tooley"],")")
    print("_________________________")
    print("Winner:", winner1)


# Specify the file to write to
file_to_output = os.path.join('analysis','output_election_data.txt')

# Open the file using the "write" mode. Specify the variable to hold the contents
output = open(file_to_output, 'w')

csvwriter = csv.writer(output)
output.write(
    f"Election Results\n"
    f"_________________________\n"
    f"Total Votes: {voter_ids} \n"
    f"_________________________\n"
    f"Khan:{percent_votes[0]}% {candidates_list['Khan']}\n"
    f"Correy:{percent_votes[1]}% {candidates_list['Correy']}\n"
    f"Li:{percent_votes[2]}% {candidates_list['Li']}\n"
    f"O'Tooley:{percent_votes[3]}% \n"
    # {candidates_list['O Tooley']}\n" (I was not able to figure out how to print the key of a dictionary that has an apostrophy)
    f"_________________________\n"
    f"Winner: {winner1}"
)
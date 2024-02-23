#imports os and csv 
import os
import csv

#creates a path to the data in election_data.csv
election_file = os.path.join("/Users/palashraval/Desktop/UCB_Bootcamp/Bootcamp_Duplicate/Homework/ElectionAndBudgetAnalysis/PyPoll/Resources/election_data.csv")


#sets vote counter to 0 and creates empty dictionary
vote_count = 0
candidate_dict= {}


#opens and reads the .csv file containing the election data
with open(election_file) as election:
    election_csv_reader = csv.reader(election, delimiter = ",")
#skips the header row
    next(election_csv_reader)
#looks at each row which contains information for each voter 
    for row in election_csv_reader:
#counts the total amount of voters
        vote_count = vote_count + 1
#creates entry in dictionary if candidate name not already present and sets the count to 1
        if row[2] not in candidate_dict:
            candidate_dict[row[2]] = 1
#increases the count for the respective candidate by 1
        else:
            candidate_dict[row[2]] = candidate_dict[row[2]] + 1 

#calculates the total amount of votes casted
sum = 0
for votes in candidate_dict:
    sum = sum + candidate_dict[votes]

#creates empty dictionary 
percentage_dict = {}
#fills dictionary with candidate and the percentage of votes they got to 3 decimal places
for name in candidate_dict:
    percentage_dict[name] = round(candidate_dict[name]/sum * 100, 3)

#shows all the results in the terminal 
print("Election Results")
print()
print("----------------------------")
print()
print(f"Total Votes: {vote_count}")
print()
print("----------------------------")
print()
#prints the percentage of votes and votes for each candidate
for candidate in candidate_dict:
    print(f"{candidate}: {percentage_dict[candidate]}% ({candidate_dict[candidate]})")
    print()
print()

#gives the names of all the candidates
people_names = candidate_dict.keys()
#creates empty list
people_list = []

#places the names of each candidate into the created list
for person in people_names:
    people_list.append(person)

#creates empty dictionary
vote_number_list = []

#gives the votes that each candidate received
voting_values = candidate_dict.values()

#places the number of votes for each candidate into a list
for vote in voting_values:
    vote_number_list.append(vote)

#gives the highest vote count in the list and the associated candidate (winner)
tot_votes = 0
for o in range(len(vote_number_list)):
    if int(vote_number_list[o]) > tot_votes:
        winner_candidate = people_list[o]
        tot_votes = vote_number_list[o]


#shows the winner of the election in the terminal 
print(f"Winner: {winner_candidate}")
print()
print("----------------------------")






#creates a new .txt file and writes the election data summary into it
with open("/Users/palashraval/Desktop/UCB_Bootcamp/Bootcamp_Duplicate/Homework/ElectionAndBudgetAnalysis/PyPoll/Analysis/election_results.txt", "w") as pollresults:
    pollresults.writelines("Election Results")
    pollresults.write("\n")
    pollresults.writelines("----------------------------")
    pollresults.write("\n")
    pollresults.writelines(f"Total Votes: {vote_count}")
    pollresults.write("\n")
    pollresults.writelines("----------------------------")
    pollresults.write("\n")
    for candidate in candidate_dict:
        pollresults.write(f"{candidate}: {percentage_dict[candidate]}% ({candidate_dict[candidate]})")
        pollresults.write("\n")
    pollresults.write("\n")
    pollresults.writelines("----------------------------")
    pollresults.write("\n")
    pollresults.writelines(f"Winner: {winner_candidate}")
    pollresults.write("\n")
    pollresults.writelines("----------------------------")

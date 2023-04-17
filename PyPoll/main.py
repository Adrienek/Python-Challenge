#reference csv file
import csv
path = 'Resources/election_data.csv'
f = open (path)
csv_reader = csv.reader(f)

#Skip the first line
next(f)

#reference writing txt file
path1 = 'Analysis/poll_analysis.txt'
f1 = open(path1,'w')
txt_file =csv.writer(f1)

#set variables
total_num_votes = 0

canidates= []
canidates_votes = {}

winner_name=""
winner_votes=0
winner_percentage = 0

#create a loop in the csv data
for row in csv_reader:
    #count the number of total votes
    total_num_votes += 1    
    #assign canidate's names to the index
    canidate_name= row[2]
    #create a conditional to assure no duplicates
    if canidate_name not in canidates:
         canidates.append(canidate_name) 
         canidates_votes[canidate_name] = 0
    #count number of individual votes
    canidates_votes[canidate_name]+= 1

#assign election results as a variable
election_results = (
    f'                \n'
    f'Election Results: \n'
    f'-----------------------\n'
    f'Total votes: {total_num_votes}\n'
    f'-----------------------\n'
    f'                \n')
#print and write election results
print(election_results)
txt_file.writerow([election_results])

#create loop for the canidates in the votes list.
for canidate_name in canidates_votes:
     votes = canidates_votes[canidate_name]
     #calculate the percentage of votes each client had
     vote_percentage = (votes / total_num_votes) * 100
    #assign results as a variable
     results =(f'{canidate_name}: {round(vote_percentage,2)}% , ({votes})')
     #print and write results
     print(results)
     txt_file.writerow([results])
    #write a conditional for the winner to pull only the canidate with the most votes.
     if (votes>winner_votes):
          winner_name = canidate_name
          winner_votes = votes
          winner_percentage = vote_percentage

#assign winner summary as a variable
winner_summary =(
    f'------------------------------- \n'
    f'The winner of the election is {winner_name} with {winner_votes} votes and {round(winner_percentage,2)}% vote percentage. \n')

#print and write winner summary.
print(winner_summary)
txt_file.writerow([winner_summary])
#reference csv file
import csv
path = 'Resources/election_data.csv'
f = open (path)
csv_reader = csv.reader(f)

next(f)


#set variables
total_num_votes = 0

canidates= []
canidates_votes = {}

winner_name=""
winner_votes=0
winner_percentage = 0
for row in csv_reader:
   
    total_num_votes += 1    

    canidate_name= row[2]
    
    if canidate_name not in canidates:
         canidates.append(canidate_name) 
         canidates_votes[canidate_name] = 0
    
    canidates_votes[canidate_name]+= 1

print(f'Election Results:')
print(f'                ')
print(f'-----------------------')
print(f'                ')
print(f'Total votes: {total_num_votes}')
print(f'                ')
print(f'-----------------------')
print(f'                ')

for canidate_name in canidates_votes:
     votes = canidates_votes[canidate_name]
     vote_percentage = (votes / total_num_votes) * 100
     results =(f'{canidate_name}: {round(vote_percentage,2)}% , ({votes})')
     print(results)
     print(f'          ')
     if (votes>winner_votes):
          winner_name = canidate_name
          winner_votes = votes
          winner_percentage = vote_percentage

print(f'-------------------------------')
print(f'The winner of the election is {winner_name} with {winner_votes} votes and {round(winner_percentage,2)}% vote percentage.')
print(f'             ')
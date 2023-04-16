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

for row in csv_reader:
    #total number of votes cast
    total_num_votes += 1    

    canidate_name= row[2]
    # A complete list of candidates who received votes  
    # The total number of votes each candidate won
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

print(f'                ')
print(f'-----------------------')
print(f'                ')

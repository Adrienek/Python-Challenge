#reference csv file
import csv
path = 'Resources/budget_data.csv'
f = open (path)
csv_reader = csv.reader(f)

#set variables
total_month_count = 1
months = []

profit_loss = []
net_total = 0
header=next(csv_reader)

#create a function for average
def calc_avg (x,y):
    avg = (x)/(y)
    return avg

big_inc = 0
big_dec = 0

for row in csv_reader:
    #total months
    months.append(row[0])
    total_month_count += 1

    #net total of profit/losses
    profit_loss.append(row[1])
    
    net_total += float(row[1])
    #average change

    #greatest increase
    
    if float(row[1]) > float(big_inc):
        big_inc = row[1]
        date_inc = row[0]
    #greatest decrease
    if float(row[1]) < float(big_dec):
        big_dec = row[1]
        date_dec = row[0]
#print values
print(f'              ')
print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total months: {total_month_count}')
print(f'              ')
print(f'${"%0.2f" %(net_total)}')
print(f'              ')
print(f'Average Change: ${"%0.2f" %(calc_avg(net_total,total_month_count))}')
print(f'              ')
print(f'Greatest Increase in Profits: {date_inc} (${big_inc})')
print(f'              ')
print(f'Greatest Decrease in Profits: {date_dec} (${big_dec})')
print(f'              ')

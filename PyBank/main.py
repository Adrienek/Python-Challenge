#reference csv file
import csv
path = 'Resources/budget_data.csv'
f = open (path)
csv_reader = csv.reader(f)

#reference writing txt file
path1 = 'Analysis/bank_analysis.txt'
f1 = open(path1,'w')
txt_file =csv.writer(f1)

#set variables
total_month_count = 0
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
#create loop for csv file
for row in csv_reader:
    #total months
    months.append(row[0])
    total_month_count += 1

    #net total of profit/losses
    profit_loss.append(row[1])
    
    net_total += float(row[1])
  
    #greatest increase
    
    if float(row[1]) > float(big_inc):
        big_inc = row[1]
        date_inc = row[0]
    #greatest decrease
    if float(row[1]) < float(big_dec):
        big_dec = row[1]
        date_dec = row[0]

#assign summary as variable and calculate average.
summary =(
    f'Financial Analysis\n'
    f'----------------------------\n'
    f'Total months: {total_month_count}\n'
    f'Net Total: ${"%0.2f" %(net_total)}\n'
    f'Average Change: ${"%0.2f" %(calc_avg(net_total,total_month_count))}\n'
    f'Greatest Increase in Profits: {date_inc} (${big_inc})\n'
    f'Greatest Decrease in Profits: {date_dec} (${big_dec})\n')

#print and write summary
print(summary)
txt_file.writerow([summary])

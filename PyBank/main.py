import csv

path = 'Resources/budget_data.csv'

f = open (path)

csv_reader = csv.reader(f)

total_month_count = -1
months = []

profit_loss = []
net_total = 0

#def add(p_l):
    #return p_l+p_l

for row in csv_reader:
    months.append(row[0])
    total_month_count += 1

    profit_loss
    net_total += profit_loss


print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total months: {total_month_count} ')

print(net_total)

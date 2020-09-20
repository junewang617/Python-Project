#Import modules
import os
import csv

#Path to collect data from Resources folder
csvpath = os.path.join('..', 'PyBank','Resources','budget_data.csv')

#Open and read csv file and skip header
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #Initiate lists and profits/losses
    total_months = []
    profit_loss = []
    net_total = 0
    
    #Loop through the data
    for row in csvreader:  
        total_months.append(row[0])
        profit_loss.append(int(row[1]))
        net_total += int(row[1])

    #List comprehension to calculate change for each month
    change = [(profit_loss[i] - profit_loss[i - 1]) for i in range(len(profit_loss))]
    #Calculate the average change of all months
    avg_change = (sum(change) - change[0])/(len(total_months) - 1)
    
#Get the greatest increase and decrease with corresponding months 
greatest_increase = max(change)
greatest_decrease = min(change)
increase_month = change.index(greatest_increase)
decrease_month = change.index(greatest_decrease)

#Print output to terminal
print("Financial Analysis")
print("-------------------------------------------------------------------")

print(f'Total Months: {len(total_months)}')
print(f'Total Profit/Losses: ${int(net_total)}')
print(f'Average Change: ${(float(avg_change)):.2f}')
print(f'Greatest Increase in Profits: {str(total_months[int(increase_month)])} (${int(greatest_increase)})')
print(f'Greatest Deacrease in Profits: {str(total_months[int(decrease_month)])} (${int(greatest_decrease)})')

#Create and print analysis output to textfile
output_path = os.path.join('..', 'PyBank', 'Analysis', 'budget_output.txt')

f = open(output_path, "w")
print("Financial Analysis", file=f)
print("-------------------------------------------------------------------", file=f)
print(f'Total Months: {len(total_months)}', file=f)
print(f'Total Profit/Losses: ${int(net_total)}', file=f)
print(f'Average Change: ${(float(avg_change)):.2f}', file=f)
print(f'Greatest Increase in Profits: {str(total_months[int(increase_month)])} (${int(greatest_increase)})', file=f)
print(f'Greatest Decrease in Profits: {str(total_months[int(decrease_month)])} (${int(greatest_decrease)})', file=f)

f.close()
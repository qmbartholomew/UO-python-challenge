import os
import csv

# Specify the file to write to (Using os library so that the path is machine/OS agnostic)
output_path = os.path.join('analysis', 'budget_analysis.txt')
csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
row_count = 0
total = 0
avg = 0.00
max_profit = ['', 0]
min_profit = ['', 0]
prev_profit = None
profit_change = []

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        profit = int(row[1])
        row_count += 1
        total += profit
        # Skip first row of data (no profit to compare to) then determine the change in profit
        if prev_profit is not None:
            change = profit - prev_profit
            profit_change.append(change)

            if change > max_profit[1]:
                max_profit[0] = row[0]
                max_profit[1] = change
            if change < min_profit[1]:
                min_profit[0] = row[0]
                min_profit[1] = change
        prev_profit = profit

avg = sum(profit_change) / len(profit_change)

# Create a new text file + print to terminal
with open(output_path, 'w') as file:
    file.write('Financial Analysis' + '\n')
    file.write('\n' + '----------------------------' + '\n')
    file.write(f'\n Total Months: {row_count} \n')
    file.write(f'\n Total: ${total} \n')
    file.write(f'\n Average Change: ${avg:.2f} \n')
    file.write(f'\n Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]}) \n')
    file.write(f'\n Greatest Decrease in Profits: {min_profit[0]} (${min_profit[1]})')


print('Financial Analysis' + '\n')
print('\n' + '----------------------------' + '\n')
print(f'\n Total Months: {row_count} \n')
print(f'\n Total: ${total} \n')
print(f'\n Average Change: ${avg:.2f} \n')
print(f'\n Greatest Increase in Profits: {max_profit[0]} (${max_profit[1]}) \n')
print(f'\n Greatest Decrease in Profits: {min_profit[0]} (${min_profit[1]})')
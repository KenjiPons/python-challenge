# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank","analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months_counter = []
total_months = int(len(total_months_counter))
total_net = 0
total_loss = 0
net_worth = 0
greatest_profit = 0
greatest_profit_date = [0]
greatest_loss = 0
greatest_loss_date = [0]
profit_loss_changes = []


# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data, delimiter = ",")

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    for row in reader: 
        print(row)
        Profit_or_loss_amount = int(row[1])
        ## Command to count any row that is not the header
        if row[0] != "Date":
                total_months_counter.append(row[0])
                total_months = int(len(total_months_counter))
        ## Module for positive values
        if Profit_or_loss_amount > 0:
            print("Positive number detected!")
            total_net = total_net + int(row[1])
            net_worth = net_worth + int(row[1])
            ## Module to obtain the greatest increase in profits throughout these periods
            if greatest_profit < int(row[1]):
                print(f'The greatest profit {greatest_profit} was smaller than {row[1]}')
                greatest_profit = 0 + int(row[1])
                greatest_profit_date.append(row[0])
                greatest_profit_date.pop(0)
            else:
                 greatest_profit = greatest_profit    

        ## Module for any value below zero
        if Profit_or_loss_amount < 0:
             print("Negative number detected!")
             Absolute_Value = abs(int(Profit_or_loss_amount))
             print(f'The absolute value of this negative number is {Absolute_Value}')
             total_loss = total_loss - Absolute_Value
             print(f'We lost {Profit_or_loss_amount}. Our total loss so far is: {total_loss}')
             net_worth = net_worth - Absolute_Value
             ##Module to obtain the greatest loss throughout these periods. 
             if abs(int(greatest_loss)) < abs(int(Profit_or_loss_amount)):
                print(f'The greatest loss {greatest_loss} was smaller than {row[1]}')
                greatest_loss = Profit_or_loss_amount
                greatest_loss_date.append(row[0])
                greatest_loss_date.pop(0)
        profit_loss_changes.append(row[1])

## Print how many months we analyzed
print(f'We analyzed a total of {total_months} months!')

## Print the total value, greatest profit and loss of this company after substracting and adding each loss/profit.
print(f'The net value of this company is a {net_worth} profit/loss this fiscal year')
print(f'{greatest_profit} is the greatest profit this branch has ever seen. It happened on {greatest_profit_date}! ') 
print(f'{greatest_loss} is the greatest loss this branch has ever seen. It happened on {greatest_loss_date}!') 
ls = [str(total_months), str(net_worth), str(greatest_profit), str(greatest_profit_date), str(greatest_loss), str(greatest_loss_date)]
lsstatement = ["Total months: " , "Total: ", "Greatest profit: ", "Greatest loss: "]

# # Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write(f'{lsstatement[0]}{ls[0]}\n')
    txt_file.write(f'{lsstatement[1]}{ls[1]}\n')
    txt_file.write(f'{lsstatement[2]} {ls[2]} {ls[3]}\n')
    txt_file.write(f'{lsstatement[3]} {ls[4]} {ls[5]}\n')
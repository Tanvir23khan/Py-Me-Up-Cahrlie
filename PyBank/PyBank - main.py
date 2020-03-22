# Import modules os and csv

import os
import csv

# Initialize the variables as required & create empty list to store data/values from csv file
total_months = 0
total_profit = 0
monthly_change = []
months = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0
previous_profit = []

# Set the path for the CSV file in PyBankcsv
PyBankcsv = os.path.join('.', 'PyBank', 'Resources', 'budget_data.csv')

# Open & Read CSV file

with open(PyBankcsv, newline='') as csvfile:
    
    # CSV reader  & variable that holds the data
    budget_data = csv.reader(csvfile, delimiter=',')
    
    # Read the header row & then skips the header row (next)
    budget_data_header = next(budget_data)
    row = next(budget_data)
    
    # Calculate total number of months, total amount (net amt) of  "Profit/Losses"
    # Set vaiables for rows

    previous_profit = int(row[1])
    total_months = total_months + 1
    total_profit = total_profit + int(row[1])
    
    # Loop (for) through each row of the Budget_data csv file, reads each row of file after header
    for row in budget_data:
        
        # Calculate total number of months included in the dataset
        total_months = total_months + 1
        
        # Calculate Net total amount of "Profit/Losses" over the entire period
        total_profit = total_profit + int(row[1])

        # Calculate change (profit or loss) from the current month to previous month and append the info
        revenue_change = int(row[1]) - previous_profit
        monthly_change.append(revenue_change)
        previous_profit = int(row[1])

        # Calculate the average change in profit or loss over the entire period
        average_change = round ((sum(monthly_change)/ len(monthly_change)), 2)

        # Append the month since will need it when calculating the greatest increase and decrease in profits
        months.append(row[0])
        
        # Calculate the greatest Increase in profits
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate the greatest decrease in profits
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
        # Find the max and min change in the profits
        greatest_increase_profits = max(monthly_change)
        greatest_decrease_profits = min(monthly_change)

# Print Analysis to terminal
print(f"Financial Analysis")
print(f"--------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase_profits})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease_profits})")


# Write the Financial Analysis as a text file
# Specify file to write/print output to and where it is located & save as "txt" file
output_file = os.path.join('.', 'PyBank', 'Resources', 'budget_data_analysis.txt')

# Open file using "Write" = "w" module and specify file name
with open(output_file, 'w',) as textfile:

# Write outcome in textfile: (\n = new line)
    textfile.write(f"Financial Analysis\n")
    textfile.write(f"-------------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${total_profit}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month}, (${greatest_increase_profits})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month}, (${greatest_decrease_profits})\n")
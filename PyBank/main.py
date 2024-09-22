# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# constants
INPUT_PATH = os.path.join("Resources", "budget_data.csv")
OUTPUT_PATH = os.path.join("analysis", "budget_analysis.txt")

# print(__file__)
# print(os.path.realpath(__file__))
# print(os.path.dirname(__file__))
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change = []
month_of_change = []
greatest_increase = ["",0]
greatest_decrease = ["",float('inf')]
# Open and read the csv
with open(INPUT_PATH) as input_file:
    reader = csv.reader(input_file)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    # Track the total and net change
   

    # Process each row of data
    for row in reader:
        print(row)
        # Track the total
        total_months += 1
        total_net += int(row[1])

        # Track the net change
        net_change_value = int(row[1]) - prev_net
        net_change.append(net_change_value)
        month_of_change.append(row[0])
        prev_net = int(row[1])


        # Calculate the greatest increase in profits (month and amount)
        if net_change_value > greatest_increase [1]:
            greatest_increase = [row [0], net_change_value]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change_value < greatest_decrease [1]:
            greatest_decrease = [row[0], net_change_value]


# Calculate the average net change across the months
average_change = sum(net_change)/len(net_change)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months:{total_months}\n"
    f"Total:${total_net}\n"
    f"Average Change:${average_change:.2f}\n"
    f"Greatest Increase in Profits:{greatest_increase[0]}(${greatest_increase[1]})\n"
    f"Greatest Decrease in Losses:{greatest_decrease[0]}(${greatest_decrease[1]})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(OUTPUT_PATH, "w") as txt_file:
    txt_file.write(output)

import csv

# Path to the CSV file
csvpath = "PyBank/Resources/budget_data.csv"

# Initialize variables
month_count = 0
total_profit = 0
changes = []  # List to store profit changes
greatest_increase = 0
greatest_decrease = 0
increase_month = ""
decrease_month = ""

# Open the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    csv_header = next(csvreader)

    last_month_profit = 0

    # Iterate through each row in the CSV file
    for row in csvreader:
        month_count += 1
        total_profit += int(row[1])

        # Calculate profit change
        if month_count == 1:
            last_month_profit = int(row[1])
        else:
            change = int(row[1]) - last_month_profit
            last_month_profit = int(row[1])
            changes.append(change)

            # Find greatest increase and decrease in profits
            if change > greatest_increase:
                greatest_increase = change
                increase_month = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                decrease_month = row[0]

# Calculate average change
avg_change = sum(changes) / len(changes)

# Output the results
print(f"Total Months: {month_count}")
print(f"Total Profit: {total_profit}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")
import csv
from collections import defaultdict

csvpath = "PyPoll\Resources\election_data.csv"

vote_count = 0
candidate_dict = defaultdict(int)

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)  # Skip header row

    for row in csvreader:
        vote_count += 1
        candidate_dict[row[2]] += 1

output_lines = [
    "Election Results",
    "-------------------------",
    f"Total Votes: {vote_count}",
    "-------------------------"
]

max_cand = max(candidate_dict, key=candidate_dict.get)
max_votes = candidate_dict[max_cand]

for candidate, votes in candidate_dict.items():
    percentage = (votes / vote_count) * 100
    output_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")

output_lines.extend([
    "-------------------------",
    f"Winner: {max_cand}",
    "-------------------------"
])

output = "\n".join(output_lines)

with open("Output_SamWise.txt", 'w') as f:
    f.write(output)

print(output)
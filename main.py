import numpy as np
from itertools import combinations
import pandas as pd

# Load the data from the uploaded CSV file
file_path = 'data.csv'
data = pd.read_csv(file_path)

# Group the data by astrological experience level
grouped = data.groupby('astrological_experience')

# Calculate the matching percentage of responses for two random participants in each group
results = {}

for level, group in grouped:
  random_pairs = list(combinations(group.index, 2))  # Create all possible pairs
  match_percentages = []

  for pair in random_pairs:
    participant_1 = group.loc[pair[0], 'answer1':'answer12']
    participant_2 = group.loc[pair[1], 'answer1':'answer12']
    match_count = np.sum(participant_1 == participant_2)
    match_percentage = (match_count / 12) * 100
    match_percentages.append(match_percentage)

  average_match_percentage = np.mean(match_percentages)
  results[level] = average_match_percentage

# Print the results
exp_level = 0
for level in results:
	rounded_agreement_level = round(results[level], 1)
  print(f"{exp_level}: {rounded_agreement_level}%")
  exp_level += 1
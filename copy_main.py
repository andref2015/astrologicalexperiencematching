import numpy as np
import pandas as pd
from itertools import combinations

data = pd.read_csv('data.csv')

# Group the data by astrological experience level
grouped = data.groupby('astrological_experience')

# Calculate the matching percentage of responses for two random participants in each group
results = {}

for experience_level, group in grouped:
	# Create all possible pairs
	random_pairs = list(combinations(group.index, 2))  

	match_percentages = []
	for pair in random_pairs:
		participant_1 = group.loc[pair[0], 'answer1':'answer12']
		participant_2 = group.loc[pair[1], 'answer1':'answer12']
		match_count = np.sum(participant_1 == participant_2)
		match_percentage = (match_count / 12) * 100
		match_percentages.append(match_percentage)

	average_match_percentage = np.mean(match_percentages)
	results[experience_level] = average_match_percentage

# Print the results
for i, level in enumerate(results):
	rounded_agreement_level = round(results[level], 1)
	print(f"{i}: {rounded_agreement_level}%")
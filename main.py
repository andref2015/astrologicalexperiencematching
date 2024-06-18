import numpy as np
import pandas as pd
from itertools import combinations

data = pd.read_csv('data.csv')

results = {}

groups = data.groupby('astrological_experience')

for experience_level, group in groups:
	all_combinations = list(combinations(group.index, 2))
	match_percentages = []

	for pair in all_combinations:
		participant_1 = group.loc[pair[0]]["answer1":"answer12"]
		participant_2 = group.loc[pair[1]]["answer1":"answer12"]
		answers_in_common = np.sum(participant_1 == participant_2)
		percent_in_common = answers_in_common / 12 * 100
		match_percentages.append(percent_in_common)

	average_match_percentage = np.mean(match_percentages)
	results[experience_level] = average_match_percentage

for result in results:
	rounded_result = round(results[result], 1)
	print(f"Group {result}: {rounded_result}%")
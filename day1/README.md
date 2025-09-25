# Advent of Code - Historian Hysteria Solution :star:

Day 1 part 1 solution achieves the correct result (2344935).
Day 1 part 2 solution achieves the correct result (27647262).
day 3 part 1 solution achieves the correcct result (163931492).


## Exploration Process
Started with a DataFrame approach to load and explore two lists from `input.txt`. Used pandas for data loading and initial analysis, including visualizing the data structure and understanding the problem requirements.

Key discoveries during exploration:
- Standard DataFrame row-wise sorting preserves relationships (not what we needed)
- Required breaking row relationships to sort lists independently

## Part 1 Solution
Simplified approach using DataFrame column operations:
- Load data with pandas
- Drop columns to create separate single-column DataFrames
- Sort each list independently 
- Calculate sum of absolute differences between corresponding sorted elements

## Part 2 Solution
- Converted the left and right columns into flat lists for easier processing.
- Used Counter from the collections module to count how many times each number appears in each list.
- Looped over all keys in both Counter dictionaries to find matching numbers.
- For each match, multiplied the number by how often it appears in each list (key * count_in_list1 * count_in_list2) and summed these contributions to compute the final similarity score.



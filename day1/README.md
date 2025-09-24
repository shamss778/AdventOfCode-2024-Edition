# Advent of Code - Historian Hysteria Solution :star:

## Exploration Process
Started with a DataFrame approach to load and explore two lists from `input.txt`. Used pandas for data loading and initial analysis, including visualizing the data structure and understanding the problem requirements.

Key discoveries during exploration:
- Standard DataFrame row-wise sorting preserves relationships (not what we needed)
- Required breaking row relationships to sort lists independently

## Final Solution
Simplified approach using DataFrame column operations:
- Load data with pandas
- Drop columns to create separate single-column DataFrames
- Sort each list independently 
- Calculate sum of absolute differences between corresponding sorted elements

The final solution achieves the correct result (2344935) while maintaining clean, readable code structure.

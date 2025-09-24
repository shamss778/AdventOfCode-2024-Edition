# Historian Hysteria - DataFrame Sorting Approach

## Problem Context
Required to calculate the sum of absolute differences between two sorted lists for an Advent of Code challenge.

## Initial Approach
Started with a single DataFrame containing both lists to maintain data structure and readability. Attempted to use standard DataFrame sorting methods.

## Issue Encountered
Standard DataFrame row-based sorting (`df.sort_values()`) maintains row relationships, which was incompatible with the problem requirements. The challenge specifically needed each list sorted independently to find the smallest-to-smallest, second-smallest-to-second-smallest pairings.

## Solution Implementation
Extracted each column as separate Series, sorted them individually, then recombined into a new DataFrame. This approach:
- Breaks the original row relationships (intentionally)
- Sorts each list independently as required by the problem
- Maintains clean data structure for subsequent calculations
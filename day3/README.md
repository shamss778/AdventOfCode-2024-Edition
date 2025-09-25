## My Solution
- Read the entire input file as a single string so I could scan for valid instructions.
- Used a manual loop to extract matching mul(X,Y) patterns by checking individual characters and following the exact syntax rules.
- For each valid pattern, converted the numbers to integers, multiplied them, and added up the results for the final sum.
- After checking solved problems, I realized my approach was much more complex and procedural than needed—using regular expressions or built-in methods would have simplified the solution considerably, which is an area I need to work on.
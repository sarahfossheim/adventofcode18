# To make sure you didn't miss any, you scan the likely candidate boxes again, counting the number that have an ID containing exactly two of any letter and then separately counting those with exactly three of any letter. You can multiply those two counts together to get a rudimentary checksum and compare it to what your device predicts.

# For example, if you see the following box IDs:

# abcdef contains no letters that appear exactly two or three times.
# bababc contains two a and three b, so it counts for both.
# abbcde contains two b, but no letter appears exactly three times.
# abcccd contains three c, but no letter appears exactly two times.
# aabcdd contains two a and two d, but it only counts once.
# abcdee contains two e.
# ababab contains three a and three b, but it only counts once.
# Of these box IDs, four of them contain a letter which appears exactly twice, and three of them contain a letter which appears exactly three times. Multiplying these together produces a checksum of 4 * 3 = 12.

# What is the checksum for your list of box IDs?

# Import libraries
import csv

# Set variables
count_two = 0
count_three = 0

# Open input file
with open('input.csv', 'rb') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Loop through the rows
    for row in csvreader:
    	# Count the matching letters in the string
    	row = row[0]
    	row_dict = dict.fromkeys(row, 0)
    	for i in row:
    		row_dict[i] += 1

    	# Get all the values
    	row_dict_val = row_dict.values()

    	# Check if any values occured 2x or 3x
    	if 2 in row_dict_val:
    		count_two += 1
    	if 3 in row_dict_val:
    		count_three +=1

# Multiply both numbers
print count_two * count_three
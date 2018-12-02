# Confident that your list of box IDs is complete, you're ready to find the boxes full of prototype fabric.

# The boxes will have IDs which differ by exactly one character at the same position in both strings. For example, given the following box IDs:

# abcde
# fghij
# klmno
# pqrst
# fguij
# axcye
# wvxyz
# The IDs abcde and axcye are close, but they differ by two characters (the second and fourth). However, the IDs fghij and fguij differ by exactly one character, the third (h and u). Those must be the correct boxes.

# What letters are common between the two correct box IDs? (In the example above, this is found by removing the differing character from either ID, producing fgij.)

# Import libraries
import csv

id_array = []

# Open input file
with open('input.csv', 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

  # Create an array out of the csv object
  for row in csvreader:
  	id_array.append(row[0])

# Loop through the array of IDs
for row in id_array:
	# Compare each ID to the other IDs
	for row_comp in id_array:
		difference = 0

		# Loop through the characters of the ID and count all the mismatches
		for i in range(len(row)):
			if row[i] != row_comp[i]:
				difference += 1

		# Find the common characters when there's only 1 mismatch
		if difference == 1:
			common = []
			for i in range(len(row)):
				if row[i] == row_comp[i]:
					common.append(row[i])

			# Print the answer
			print "".join(common)
			print row, row_comp

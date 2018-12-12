# --- Day 3: No Matter How You Slice It ---
# The Elves managed to locate the chimney-squeeze prototype fabric for Santa's suit (thanks to someone who helpfully wrote its box IDs on the wall of the warehouse in the middle of the night). Unfortunately, anomalies are still affecting them - nobody can even agree on how to cut the fabric.

# The whole piece of fabric they're working on is a very large square - at least 1000 inches on each side.

# Each Elf has made a claim about which area of fabric would be ideal for Santa's suit. All claims have an ID and consist of a single rectangle with edges parallel to the edges of the fabric. Each claim's rectangle is defined as follows:

# The number of inches between the left edge of the fabric and the left edge of the rectangle.
# The number of inches between the top edge of the fabric and the top edge of the rectangle.
# The width of the rectangle in inches.
# The height of the rectangle in inches.
# A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3 inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4 inches tall. Visually, it claims the square inches of fabric represented by # (and ignores the square inches of fabric represented by .) in the diagram below:

# ...........
# ...........
# ...#####...
# ...#####...
# ...#####...
# ...#####...
# ...........
# ...........
# ...........
# The problem is that many of the claims overlap, causing two or more claims to cover part of the same areas. For example, consider the following claims:

# #1 @ 1,3: 4x4
# #2 @ 3,1: 4x4
# #3 @ 5,5: 2x2
# Visually, these claim the following areas:

# ........
# ........
# ........
# .11XX4..
# .11XX4..
# .11XXX3.
# .111133.
# ........
# The four square inches marked with X are claimed by both 1 and 2. (Claim 3, while adjacent to the others, does not overlap either of them.)

# If the Elves all proceed with their own plans, none of them will have enough fabric. How many square inches of fabric are within two or more claims?

# Import libraries
import csv

# Set variables
claims = []
squares = {}
overlap = 0

# Read file
with open('input.csv', 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

  # Create an array out of the csv object
  for row in csvreader:
  	square = {"top":0, "left":0, "width": 0, "height": 0}
  	square["left"] = row[2].split(",")[0]
  	square["top"] = row[2].split(",")[1].split(":")[0]
  	square["width"] = row[3].split("x")[0]
  	square["height"] = row[3].split("x")[1]
  	claims.append(square)

# Loop through all the claims
for claim in claims:
	# Find the coordinates in height (y)
	for y in range(int(claim["height"])):
		# Find the coordinates in width (x)
		for x in range(int(claim["width"])):
			coordinate = str(y + int(claim["top"])) + "_" + str(x + int(claim["left"]))
			squares[coordinate] = squares.get(coordinate, 0) + 1

for key, val in squares.items():
	if val > 1:
		overlap += 1

print "Overlap is"
print overlap


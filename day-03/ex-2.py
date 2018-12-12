# # --- Part Two ---
# Amidst the chaos, you notice that exactly one claim doesn't overlap by even a single square inch 
# of fabric with any other claim. If you can somehow draw attention to it, 
# maybe the Elves will be able to make Santa's suit after all!

# For example, in the claims above, only claim 3 is intact after all claims are made.

# What is the ID of the only claim that doesn't overlap?


# Import libraries
import csv

# Set variables
claims = []
squares = {}
claim_id_overlap = {}

# Read file
with open('input.csv', 'rb') as csvfile:
  csvreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

  # Create an array out of the csv object
  for row in csvreader:
    square = {"top":0, "left":0, "width": 0, "height": 0, "id": 0}
    square["id"] = row[0]
    square["left"] = row[2].split(",")[0]
    square["top"] = row[2].split(",")[1].split(":")[0]
    square["width"] = row[3].split("x")[0]
    square["height"] = row[3].split("x")[1]
    claims.append(square)

# Loop through all the claims
for claim in claims:
  # Get the id of the current claim, and set it to count 1
  idx_current = claim["id"]
  claim_id_overlap[idx_current] = 1

  # Find the coordinates in height (y)
  for y in range(int(claim["height"])):
    # Find the coordinates in width (x)
    for x in range(int(claim["width"])):
      # Create the coordinate format
      coordinate = str(y + int(claim["top"])) + "_" + str(x + int(claim["left"]))

      # Add 1 to the overlap of the current claim id, and the id of the claim it overlaps with 
      if coordinate in squares:
        claim_id_overlap[squares[coordinate]] += 1
        claim_id_overlap[idx_current] += 1

      # Set the id of the current coordinate
      squares[coordinate] = idx_current

# Find the id where the value is 1
for idx, val in claim_id_overlap.items():
  if val == 1:
    print idx
    break
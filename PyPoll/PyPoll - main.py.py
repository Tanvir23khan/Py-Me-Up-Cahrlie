# PyPoll
# Import Dependencies
import os
import csv

# Set the path for the CSV file in PyPollcsv
PyPollcsv = os.path.join('.', 'PyPoll', 'Resources', 'election_data.csv')


# Open CSV file to read 
with open(PyPollcsv, 'r') as csv_file:
	
	# Read CSV file
	election_data = csv.reader(csv_file, delimiter=",")
	
	# Skip header
	election_data_header = next(election_data)

	
    # Initialize the variables as required & create empty "dictionaries" to store data/values from csv file
    # Using dictionaries is best when we do not know how many candidates are participating

	votes_candidates = {}
	candidates_percentage = {}
	total_votes = 0
	
	# Loop through each row of election data  and 
	for row in election_data:
		# count number votes for each candidate and store them in a dictionary "votes_candidates"
		if row[2] not in votes_candidates:
			votes_candidates[row[2]] = 1
		else:
			votes_candidates[row[2]] += 1
		# the total number of votes cast
		total_votes += 1

    # keys(), values() and items() methods return lists in congruent order if the dict is not altered. - Checkpoint
	# Converting dictionary "votes_candidates = {}"" into the list to get complete list of candidates (tuples) who received votes using keys()(built in dictionary method):
    # A complete list of candidate who received votes
    # the keys method deliovers its elemts when they are needed by the rest of the code

	candidates_list = list(votes_candidates.keys())
        # print(candidates_list)
    
    # To get a list of all the values in a dictionary, use the values() method (built in dictionary method):
    # Find who rec'd maximum number of votes (popular votes) is winner candidate, using max() function

	winner = max(votes_candidates.values())
        #print(winner)

    
	# Converting "candidates:number of votes" dictionary to a list of tupules using items()method
    # step: Converting "candidates (key):number of votes(values)" dictionary to a list of tuples and assigning new variable name


	list_candidates_votes = list(votes_candidates.items())
     
    
	# Loop through each candidates(key), votes(value) in list 
	for candidates, votes in list_candidates_votes:
		
        # calculate the percentage of votes each candidate won and store it a dictionary
        # use format function to get three deimal points
		votes_percentage = "{0:.3f}".format((votes/total_votes)*100)
		candidates_percentage[candidates] = votes_percentage
		
        # Find the winner of the election based on maximum number of vote (popular votes) or highest%
		if votes == winner:
			winner_candidate = candidates



    # Print Analysis to terminal
print(f"Election Results ")
print(f"-------------------------------")
print(f"Total Votes: {total_votes}")
print(f"{candidates_list[0]}: {candidates_percentage[candidates_list[0]]}% ({votes_candidates[candidates_list[0]]})")
print(f"{candidates_list[1]}: {candidates_percentage[candidates_list[1]]}% ({votes_candidates[candidates_list[1]]})")
print(f"{candidates_list[2]}: {candidates_percentage[candidates_list[2]]}% ({votes_candidates[candidates_list[2]]})")
print(f"{candidates_list[3]}: {candidates_percentage[candidates_list[3]]}% ({votes_candidates[candidates_list[3]]})")
print(f"-------------------------------")
print(f"Winner : {winner_candidate}")
print(f"-------------------------------")



# Write the Financial Analysis as a text file
# Specify file to write/print output to and where it is located & save as "txt" file
output_file = os.path.join('.', 'PyPoll', 'Resources', 'election_result.txt')

# Open file using "Write" = "w"  and specify file name
with open(output_file, 'w',) as textfile:

# Write outcome in textfile: (\n = new line)
    textfile.write(f"Election Results \n")
    textfile.write(f"------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write(f"{candidates_list[0]}: {candidates_percentage[candidates_list[0]]}% ({votes_candidates[candidates_list[0]]})\n")
    textfile.write(f"{candidates_list[1]}: {candidates_percentage[candidates_list[1]]}% ({votes_candidates[candidates_list[1]]})\n")
    textfile.write(f"{candidates_list[2]}: {candidates_percentage[candidates_list[2]]}% ({votes_candidates[candidates_list[2]]})\n")
    textfile.write(f"{candidates_list[3]}: {candidates_percentage[candidates_list[3]]}% ({votes_candidates[candidates_list[3]]})\n")
    textfile.write(f"------------------------------\n")
    textfile.write(f"Winner : {winner_candidate}\n")
    textfile.write(f"------------------------------\n")



    #*********************************************************************************************************************************************************
    # CHECKPOINTS, Notes to myself
    # Find short cut for print fuction rather than typing each row
    # work on more examples of dictionaries with built in methods                                                                                                                                      
    # keys(), values() and items() methods return lists in congruent order if the dict is not altered. - Checkpoint
	# Converting dictionary into the list to get complete list of candidates (tuples) who received votes using keys() function
    # keys() function returns a list of all the names of the keys.
    # we'll need the code that can be used to execute the conversion of the values from the dictionary to a list, like this: - Checkpoint
    # votes_candidates = {}
    # candidates_list = list(data.key())
    # print(candidates_list)
    # P/O all key (name) candidate as a list
    # To get a list of all the values in a dictionary, use the values() function:
    # Find who rec'd maximum number of votes (popular votes) is winner candidate, using max() function
    # Could have use zip function - list = zip(dict.keys(), dict.values())  --> list = zip(candiadtes_list, winner) so need to tedious repetition for output
    # Example: 
    # dict = { 'a': 1, 'b': 2, 'c': 3 }
    # dict.items()
    # Output: [('a', 1), ('c', 3), ('b', 2)]
    #***********************************************************************************************************************************************************

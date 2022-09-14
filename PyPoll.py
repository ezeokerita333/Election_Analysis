#import datetime
#now = datetime.datetime.now()
#print ("The timne right now is ", now)

#file_to_load = "Resources/election_results.csv"
#with open(file_to_load) as election_data:
    #print(election_data)

import os
import csv
#dir(os)

file_to_load = os.path.join("Resources", "election_results.csv")

file_to_save = os.path.join("analysis", "election_analysis.txt")
with open(file_to_load) as election_data:
    #txt_file.write("Counties in the Election\n-------------------------------\nArapahoe\nDenver\nJefferson")
    file_reader = csv.reader(election_data)
    headers = next(file_reader)
    print(headers)
# importing required libraries
# Sys for reading command line args and pandas to read and manipulate the csv dataframes
import sys
import pandas as pd

#Getting the location of all csv files from the command line arguments that were passed
csv_files_list = sys.argv[1:]
#Frames list stores all the csv dataframes that need to be concatenated
frames = []
#file_names list stores all the name of csv files that are needed to add to the final column of combined CSV file
file_names = []

#looping through all the CSV files passed in command line
for i in csv_files_list:
    #reading current CSV
    curr_csv = pd.read_csv(i)
    #adding the current vsc dataframe into the frames list
    frames.append(curr_csv)
    #finding out the number of rows in the current csv dataframe
    rows = curr_csv.shape[0]
    #appending the current csv file name to the file name list (file name will be appended n times where n is number of rows)
    #split function uses / to split the string and get the csv file name only
    file_names.append([i.split("/")[2]]*rows)

#the file_name is a 2d list so we flatten it to mae it a 1d list
flatten_file_name = [i for sub in file_names for i in sub] 
#print(flatten_file_name)
combined_csv = pd.concat(frames)
combined_csv['filename'] = flatten_file_name
#print(combined_csv.to_string(index=False))
print(combined_csv.to_csv(sep=',', index=False))



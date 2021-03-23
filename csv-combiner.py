# importing required libraries
# Sys for reading command line args and pandas to read and manipulate the csv dataframes
import sys
import pandas as pd

#Getting the location in string format of all csv files from the command line arguments that were passed
csv_files_list = sys.argv[1:]
#variable used to remove headers for 2nd csv file and further files
count = 0
#looping through all the CSV files passed in command line
for i in csv_files_list:
    #splitting the whole csv files into smaller parts
    for j in pd.read_csv(i,chunksize=100):
        #split function uses / to split the string and get the csv file name only
        #Adding the file name column with respective filename
        j['filename'] = i.split('/')[-1]
        #printing the current csv in CSV format 
        if count == 0:
            #for first csv file include header
            print(j.to_csv(sep=',',index=False, header = True),  end="")
        else:
            #for second csv file do not include header
            print(j.to_csv(sep=',',index=False, header = False), end="")
        count+=1




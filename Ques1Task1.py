import pandas as pd
import glob

all_files = glob.glob("*.csv") # get all csv files
print(all_files)
with open('output.txt', 'w') as file: # open the output file in write mode
    for filename in all_files:
        df = pd.read_csv(filename)
        if filename=="CSV1.csv":
            file.write(df['SHORT-TEXT'].str.cat(sep=',')) # write the text column to the file
        else:
            file.write(df['TEXT'].str.cat(sep=',')) # write the text column to the file
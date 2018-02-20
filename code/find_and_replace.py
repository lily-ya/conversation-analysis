# -*- coding: utf-8 -*-

''' (2)
replace words in your data file. This is useful for replacing models with brands, converting different words into a single word (e.g., replacing ‘engine’, ‘acceleration’ with ‘performance’, replacing aspirational words or phrases with ‘aspiration’, etc. ). 
To use this script, create a folder called CSV within the Python Scripts directory. 
Put words and phrases to replace in the file Models.csv file for illustration, and place the file Models.csv in this CSV folder. 
Make sure your data file is in the regular Python27 directory. Make sure the name of the data file is the same as the name of the file in the script. 
Now run the script, which will replace all the words and phrases you mentioned in the Models.csv file. 
'''
#created by Jonathan Malott (jm72636) on Sep 19 2016
from tempfile import NamedTemporaryFile
import shutil
import csv

#CSVs in a csv directory
macros = ["Models.csv"]

for x in macros:
    filename = 'edmunds_Extraction.csv'
    tempfile = NamedTemporaryFile(delete=False)

    with open(filename, 'rb') as csvFile, tempfile:
        reader = csv.reader(csvFile, delimiter=',', quotechar='"')
        writer = csv.writer(tempfile, delimiter=',', quotechar='"')

        for row in reader:

            #this item is the forum post
            item = row[2]

            with open(x, 'rb') as csvfile:
                read = csv.reader(csvfile, delimiter=',', quotechar='|')
                for row2 in read:
                        #replace
                        row[2] = row[2].lower().replace(row2[1].lower(),row2[0].lower())

            writer.writerow(row)

    shutil.move(tempfile.name, filename)
    print "Working on "+x

import csv
from os import listdir
from os.path import join

  
# -*- coding: utf-8 -*-
""" Concatenating and Merging ZOOM.US subscribers report.

1 - you need to download your subriscribers report at: https://us02web.zoom.us/account/report/webinar
2 - select everyday you want to download
3 - save it in the your PC
4 - set path where are files in var paths_to_concatenate 
5 - run this app

"""



# Here you can select report's path
paths_to_concatenate = ["example_report"]

# output spreadsheet
full_spreadsheet = 'full_spreadsheet.csv'

def process_all_files(path, full_spreadsheet):
    room_name = ''
    data_to_spreadsheet = []
    with open(path, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        i = 0
        for row in reader:
            if i == 3:
                room_name = row[0]
            if i > 11:
                if len(row) == 12:
                    row[11] = room_name
                else:
                    row.append(room_name)

                data_to_spreadsheet.append(row)
            i = i + 1

    with open(full_spreadsheet, 'a', newline='',encoding='utf-8-sig') as f:
        for item in data_to_spreadsheet:
            writer = csv.writer(f)
            writer.writerow(item)
      

for path in paths_to_concatenate:
    for f in listdir(path):
        file_path = join(path, f)
        process_all_files(file_path,full_spreadsheet)
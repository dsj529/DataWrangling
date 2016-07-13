# -*- coding: utf-8 -*-
# Find the time and value of max load for each of the regions
# COAST, EAST, FAR_WEST, NORTH, NORTH_C, SOUTHERN, SOUTH_C, WEST
# and write the result out in a csv file, using pipe character | as the delimiter.
# An example output can be seen in the "example.csv" file.

import xlrd
import os
import csv
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"
outfile = "2013_Max_Loads.csv"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    data = [['Station','Year','Month','Day','Hour','Max Load']]
    
    sheet_data=[[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    header=sheet_data[0]
    for region in list(enumerate(header))[1:-1]:
        col=region[0]
        label=region[1]
        region_maxVal=max(sheet.col_values(col,start_rowx=1,end_rowx=None))
        region_maxIdx=sheet.col_values(col,start_rowx=1,end_rowx=None).index(region_maxVal)
        #region_maxTimeX=sheet.cell_value(region_maxIdx,0)
        region_maxTimePy=xlrd.xldate_as_tuple(sheet.cell_value(region_maxIdx+1,0),0)
        vals=[label,region_maxTimePy[0],region_maxTimePy[1],region_maxTimePy[2],region_maxTimePy[3],region_maxVal]
        data.append(vals)
    return data

def save_file(data, filename):
   with open(filename, 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter='|')
        for r in data:
            writer.writerow(r)
   return
    
def test():
    open_zip(datafile)
    data = parse_file(datafile)
    save_file(data, outfile)

    number_of_rows = 0
    stations = []

    ans = {'FAR_WEST': {'Max Load': '2281.2722140000024',
                        'Year': '2013',
                        'Month': '6',
                        'Day': '26',
                        'Hour': '17'}}
    correct_stations = ['COAST', 'EAST', 'FAR_WEST', 'NORTH',
                        'NORTH_C', 'SOUTHERN', 'SOUTH_C', 'WEST']
    fields = ['Year', 'Month', 'Day', 'Hour', 'Max Load']

    with open(outfile) as of:
        csvfile = csv.DictReader(of, delimiter="|")
        for line in csvfile:
            station = line['Station']
            if station == 'FAR_WEST':
                for field in fields:
                    # Check if 'Max Load' is within .1 of answer
                    if field == 'Max Load':
                        max_answer = round(float(ans[station][field]), 1)
                        max_line = round(float(line[field]), 1)
                        assert max_answer == max_line

                    # Otherwise check for equality
                    else:
                        assert ans[station][field] == line[field]

            number_of_rows += 1
            stations.append(station)

        # Output should be 8 lines not including header
        assert number_of_rows == 8

        # Check Station Names
        assert set(stations) == set(correct_stations)

        
if __name__ == "__main__":
    test()

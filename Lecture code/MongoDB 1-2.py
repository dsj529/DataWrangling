#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)
    
    sheet_data=[[sheet.cell_value(r,col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    coast_col=sheet_data[0].index('COAST')
    time_col=sheet_data[0].index('Hour_End')
    coast_data=sheet.col_values(coast_col, 1, sheet.nrows)
    time_data=sheet.col_values(time_col,1, sheet.nrows)
    
    coast_max=max(coast_data)
    max_time=xlrd.xldate_as_tuple(time_data[coast_data.index(coast_max)],0)
    
    coast_min=min(coast_data)
    min_time=xlrd.xldate_as_tuple(time_data[coast_data.index(coast_min)],0)
    coast_avg=sum(coast_data)/len(coast_data)
    
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    
    
    data = {
            'maxtime': max_time,
            'maxvalue': coast_max,
            'mintime': min_time,
            'minvalue': coast_min,
            'avgcoast': coast_avg
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
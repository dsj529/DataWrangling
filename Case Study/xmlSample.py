"""
Code used to generate a sample of the Dresden OSM-XML data.
Please note: I have not written this code to preserve well-formedness within the sample document,
but only show the first 25,000 rows of data used in the OSM analyses.
"""


sourcePath = 'c:/users/dsj/documents/coding/data wrangling (mongodb)/case study/dresden_germany.osm'
targetPath = 'c:/users/dsj/documents/coding/data wrangling (mongodb)/case study/dresden_sample.osm'

with open(sourcePath,'rb') as source, open(targetPath, 'wb') as target:
    for i in range(25000):
        line = source.readline()
        target.write(line)
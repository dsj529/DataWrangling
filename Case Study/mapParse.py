import xml.etree.ElementTree as ET
import pprint

def count_tags(filename):
    tags = {}
    count = 0
    for _, elem in ET.iterparse(filename):
        if count == 1900000:
            break
        if elem.tag in tags:
            tags[elem.tag] += 1
        else:
            tags[elem.tag] = 1
        count += 1
    return tags

def test():

    tags = count_tags('c:/users/dsj/documents/coding/data wrangling (mongodb)/case study/dresden_germany.osm')
    pprint.pprint(tags)
    
if __name__ == "__main__":
    test()
	
	
"""
Output: {'bounds': 1, 'nd': 264603, 'node': 1108290, 'tag': 495553, 'way': 31553}
"""	
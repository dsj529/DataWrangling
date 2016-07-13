"""
Your task in this exercise has two steps:

- audit the OSMFILE and change the variable 'mapping' to reflect the changes needed to fix 
    the unexpected street types to the appropriate ones in the expected list.
    You have to add mappings only for the actual problems you find in this OSMFILE,
    not a generalized solution, since that may and will depend on the particular area you are auditing.
- write the update_name function, to actually fix the street name.
    The function takes a string with street name as an argument and should return the fixed name
    We have provided a simple test so that you see what exactly is expected
"""
import xml.etree.cElementTree as ET
import re
import pprint

OSMFILE = 'c:/users/dsj/documents/coding/data wrangling (mongodb)/case study/dresden_germany.osm'
""" 
    Notes: Due to the differences of German street-naming versus English, I have chosen not to normalize street type names in this routine,
    but rather to normalize the spellings.  Rather than include the unicode characters for umlauted vowels, or the Ess-set, I am replacing their
    occurrence with ASCII-compliant alternatives.
    
    The unicode/ascii string comparison was based on sample code found on stackoverflow.com
    """
# UPDATE THIS VARIABLE
mapping = {u"\xdf" : "ss",
           u"\xf6" : "oe",
           u"\xfc" : "ue",
           u"\xe4" : "ae",
           u"\xe9" : "e",  # &eacute;
           ### second pass
           u"\xdc" : "Ue",
           u"\xc4" : "Ae",
           u"\xd6" : "Oe"
           }


def audit_street_type(streets, street_name):
    for k,v in mapping.iteritems():
        if re.search(k, street_name):
            street_name=re.sub(k,v,street_name)
    if street_name != street_name.encode('ascii', 'replace'):
        streets.append(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    streets = []
    counter = 0
    for _, elem in ET.iterparse(osm_file, events=("start",)):
        if counter == 1900000:
            break
        if counter%50000 == 0:
            print "I'm here: ", counter
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(streets, tag.attrib['v'])
        counter += 1
    return streets


def test():
    sts = audit(OSMFILE)
    pprint.pprint(sts)


if __name__ == '__main__':
    test()
    
""""
Output: "[]"
"""
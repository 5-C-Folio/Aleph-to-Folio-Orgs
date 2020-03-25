from csv import DictReader
from marshSchema import urlRecord, organizationRecord, aliasRecord
import json

def string_to_dict(string):
    sp_string = string.split(';')
    altList = []
    for row in sp_string:
        sprow = row.split(':')
        altname = aliasRecord( value=sprow[1], description=sprow[0])
        altList.append(altname)
    return altList


def coral_create(file):
    with open(file, 'r', encoding='utf8') as dictfile:
        coral_orgs = DictReader(dictfile)
        recList = []
        for org in coral_orgs:
            newRec = organizationRecord(code=org['orgCode'],
                                        name=org['name'],
                                        status='Active',
                                        description=org['noteText'],
                                        isVendor=bool(org['is Vendor']),
                                        aliases=string_to_dict(org['Aliases'])
                                        )
            recList.append(newRec)
    return  recList





if __name__ == '__main__':
    coral = coral_create('C:\\Users\\aneslin\Documents\\Python\\orgcleanMap\\orgs\\Coral\\umass_organizations-Cleaned-v1.csv')
    with open("coralfile.txt", 'w', encoding='latin-1', newline="\n") as target:
        json.dump(coral, target, indent=4)






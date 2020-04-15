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

def coral_getter(contact_file, orgCode):
    c_list = []
    with open (contact_file, 'r') as c_file:
        c_dict = DictReader(c_file)
        for row in c_dict:
            try:
                if row['organizationCode'] == orgCode:

                    c_list.append(row["ID"])
            except KeyError:
                print('invalid column headers')
                exit()

        return c_list




def coral_create(main_file, contact_file, interface_file):
    with open(main_file, 'r', encoding='utf8') as dictfile:
        coral_orgs = DictReader(dictfile)
        recList = []
        for org in coral_orgs:
            c_list = coral_getter(contact_file, org['orgCode'])
            i_list = coral_getter(interface_file,org['orgCode'])
            if org['is Vendor'] == 'True':
                isVen = True
            else:
                isVen = False
            newRec = organizationRecord(
                                        id = None,
                                        code=org['orgCode'],
                                        name=org['name'],
                                        status='Active',
                                        description=org['noteText'],
                                        isVendor=isVen,
                                        aliases=string_to_dict(org['Aliases']),
                                        contacts=c_list,
                                        interfaces = i_list

                                        )
            recList.append(newRec)
    return  recList





if __name__ == '__main__':
    coral = coral_create('orgs\\Coral\\umass_organizations-Cleaned-v1.csv','orgs/Contacts/UMcontacts-ID.csv',
                         'orgs/Coral/um_interfaces_v3_FOLIO_IDS-csv.csv')
    with open("um_coralfilev3.txt", 'w', encoding='latin-1', newline="\n") as target:
        json.dump(coral, target, indent=4)






from csv import DictReader
from marshSchema import  organizationRecord, aliasRecord
import json
from sys import argv

def string_to_dict(string):
    #todo smith uses , to split- umass ;
    sp_string = string.split(',')
    altList = []
    for row in sp_string:
        sprow = row.split(':')
        altname = aliasRecord( value=sprow[1].lstrip(), description=sprow[0])
        altList.append(altname)
    return altList


def coral_getter(contact_file, orgCode):
    c_list = []
    with open (contact_file, 'r') as c_file:
        c_dict = DictReader(c_file)
        for row in c_dict:
            try:
                if row['orgCode'] == orgCode:
                    if len(row['ID']) > 1:
                        c_list.append(row["ID"])
            except KeyError:
                print(f'invalid column headers in file {contact_file}')
                exit()

        return c_list


def coral_create(main_file, contact_file, interface_file):
    with open(main_file, 'r', encoding='utf8') as dictfile:
        coral_orgs = DictReader(dictfile)
        recList = []
        for org in coral_orgs:
            c_list = coral_getter(contact_file, org['orgCode'])
            i_list = coral_getter(interface_file, org['orgCode'])
            print (f"{len(c_list)} contact created and {len(i_list)} interfaces created for {org['name']}")
            if org['is Vendor'] == 'True':
                isVen = True
            else:
                isVen = False
            newRec = organizationRecord(
                                        id=None,
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
    try:
        if argv[1] =='help':
            print("select select the Cleaned Aleph org file, the contacts file and the interfaces file")
            exit()
        else:
            alephFile = argv[1]
            contactsFile = argv[2]
            interfaceFile = argv[3]
    except IndexError:
        print("select select the Cleaned Aleph org file, the contacts file and the interfaces file")
        exit()
    conf = input(f'''You have selected: \n {alephFile} as the Aleph Organization file \n {contactsFile} as the contact file \n {interfaceFile} as the interface file \n if this is correct, type "yes to continue, or any key to exit''')
    #coral = coral_create('orgs\\Coral\\smith_organizations-Cleaned-v1.csv','orgs/Contacts/sc_contacts_v1_FOLIO_IDs.csv',
                         #'orgs/Coral/sc_interfaces_v2_FOLIO_IDs.csv')
    if conf in ["yes", "Yes", "Y", 'y']:
        coral = coral_create(alephFile, contactsFile, interfaceFile)
        with open("scfinal//sc_coralfilev4.txt", 'w', encoding='latin-1', newline="\n") as target:
            json.dump(coral, target, indent=4)
            print(f"writing to {target.name}")
    else:
        print("exiting")
        exit()





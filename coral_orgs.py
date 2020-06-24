from csv import DictReader
from FolioSchemaModels import  organizationRecord, aliasRecord
import json
from sys import argv

def string_to_dict(string):
    #todo smith uses , to split- umass ;
    sp_string = string.split(';')
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
                print(f'invalid column headers in file {contact_file}. Headers should be "orgCode" and "ID"  \n fields used: {c_dict.fieldnames}')
                exit()

        return c_list


def coral_create(main_file, contact_file, interface_file):

    with open(main_file, 'r', encoding='utf8') as dictfile:
        coral_orgs = DictReader(dictfile)
        recList = []
        for org in coral_orgs:
            c_list = coral_getter(contact_file, org['orgCode'])
            if interface_file.lower() not in ["null", 'n', 'none']:
                i_list = coral_getter(interface_file, org['orgCode'])
            else:
                i_list = []
            print (f"{len(c_list)} contact created and {len(i_list)} interfaces created for {org['name']}")
            if org['is Vendor'] == 'True':
                isVen = True
            else:
                isVen = False
            newRec = organizationRecord(
                                        id=None,
                                        code=org['orgCode'].replace(" ", ""),
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
            print("select select the Cleaned Coral org file, the contacts file and the interfaces file")
            exit()
        else:
            coralFile = argv[1]
            contactsFile = argv[2]
            interfaceFile = argv[3]
    except IndexError:
        print("select select the Cleaned coral org file, the contacts file and the interfaces file")
        exit()
    code = input("input the two character organization code> ")
    conf = input(f'''You have selected: \n {coralFile} as the Coral Organization file \n {contactsFile} as the contact file \n {interfaceFile} as the interface file \n if this is correct, type "yes to continue, or any key to exit''')
    #coral = coral_create('orgs\\Coral\\smith_organizations-Cleaned-v1.csv','orgs/Contacts/sc_contacts_v1_FOLIO_IDs.csv',
                         #'orgs/Coral/sc_interfaces_v2_FOLIO_IDs.csv')
    if conf in ["yes", "Yes", "Y", 'y']:
        coral = coral_create(coralFile, contactsFile, interfaceFile)
        try:
            with open(f"{code}final//{code}_coralfile.txt", 'w', encoding='latin-1', newline="\n") as target:
                json.dump(coral, target, indent=4)
                print(f"writing to {target.name}")
        except FileNotFoundError:
            print(f'{code}final directory does not exit')
            exit()
    else:
        print("exiting")
        exit()





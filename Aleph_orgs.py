from csv import DictReader
import json
import uuid
from FolioSchemaModels import phoneRecord, urlRecord, organizationRecord, addressRecord, emailRecord
from sys import argv


def categories_getter(value):
    # currently is only designed to have type 1 or 3 in the export file. Should be controlled in Z72_reader function
    if value["Z72_REC_KEY 2"] == "1":
        # uuid for general
        categories = ["9c321c44-774c-491f-9012-2024b93cb453"]
    elif value["Z72_REC_KEY 2"] == "3":
        # uuid for remittance
        categories = ["0172e314-d3c1-437f-9174-b730844197fa"]
    return categories


def orgmaker(z70, z72, prefix):
    jsonRecords = []
    with open(z70, 'r', encoding='latin-1', newline='\n') as file:
        dictFile = DictReader(file, delimiter = '|')
        for row in dictFile:
            stat = 'Active'
            Z72_file = (Z72_reader(row['Z70_REC_KEY'].rstrip(),z72))
            folio_description = (addressNoteGetter(Z72_file))
            newRec = organizationRecord(
                                        id = None,
                                        code=prefix + row['Z70_REC_KEY'].rstrip(),
                                        name=prefix + " " + row['Z70_VENDOR_NAME'],
                                        status=stat,
                                        addresses=addressMaker(Z72_file),
                                        phoneNumbers=phoneMaker(Z72_file),
                                        erpCode=row["Z70_ADDITIONAL_VENDOR_CODE"].rstrip(),
                                        emails=emailMaker(Z72_file),
                                        urls=urlMaker(Z72_file),
                                        description=row['Z70_NOTE'],
                                        isVendor=True
                                        )
            if folio_description is not None and len(folio_description) > 1:
                newRec.description = newRec.description + ' \n' + folio_description
            jsonRecords.append(newRec)
            print(newRec.code)
    return jsonRecords


def Z72_reader(code, file):
    with open(file, 'r', encoding='latin-1') as file2:
        dictFile = DictReader(file2, delimiter=',')
        contact_List = []
        for row in dictFile:
            if row['Z72_REC_KEY 1'] == code:
                contact_List.append(row)

    return contact_List


def addressNoteGetter(z72_file):
    export_list = []
    for row in z72_file:
        if len(row['Z72_NOTE']) > 1:
            addLine = row['Z72_NOTE']
            export_list.append(addLine)
    return("""
 """.join(export_list))


def addressMaker(z72_file):
    export_list = []
    for value in z72_file:

        categories = categories_getter(value)
        addLine = addressRecord(addressLine1=value["Z72_VENDOR_ADDRESS"],
                                city=value['Z72_VENDOR_CITY'],
                                zipCode=value['Z72_VENDOR_POSTAL_CODE'],
                                stateRegion=value['Z72_VENDOR_STATE'],
                                country=value["Z72_VENDOR_COUNTRY"],
                                categories=categories
                                )
        export_list.append(addLine)

    return export_list


def phoneMaker(z72_file):
    phonelist = []
    for value in z72_file:
        categories = categories_getter(value)
        if value['Z72_VENDOR_TEL']:
            phoneMain = (value['Z72_VENDOR_TEL'])
            phone1 = phoneRecord(phoneNumber=phoneMain, type='Office', categories=categories)
            if len(phone1["phoneNumber"]) > 1:
                phonelist.append(phone1)
        if value['Z72_VENDOR_FAX']:
                phoneFax = value['Z72_VENDOR_FAX']
                phone2 = phoneRecord(phoneNumber=phoneFax, type='Fax', categories=categories)
                if len(phone2["phoneNumber"]) > 1:
                    phonelist.append(phone2)
    return phonelist


def emailMaker(z72_file):
        exportList = []
        for value in z72_file:
            categories = categories_getter(value)
            email = emailRecord(value=value['Z72_VENDOR_EM'], categories=categories)
            if len(email["value"]) > 1:
                exportList.append(email)
        return exportList


def urlMaker(z72_file):
        exportList = []
        for value in z72_file:
            url = urlRecord(value=value['Z72_VENDOR_IP'],
                            categories=["9c321c44-774c-491f-9012-2024b93cb453"],
                            isPrimary=True)
            if len(url["value"]) > 1:
                exportList.append(url)
        return exportList


def uuidgen(inst, code):
    x = uuid.uuid1()
    uuid.uuid5("")


if __name__ == "__main__":
    try:
        if argv[1] == 'help':
            print('''select the path of the 7Z0 file, the cleaned Z72 file, and the Organization Prefix ''')
            exit()
        else:
            z70 = str(argv[1])
            z72 = str(argv[2])
    except IndexError:
        print('invalid commands; select the path of the 7Z0 file, the cleaned Z72 file, and the Organization Prefix  ')
        exit()
    code = input("input the two character organization code> ")
    conf = input(f"you have selected {z70} as the Z70 file, {z72} as the Z72 file and {code} as the organization code.> "
                 f"type 'yes' for correct, any other key to exit> ")
    if conf in ['Yes', 'yes', 'Y', 'y']:
        x = orgmaker(z70, z72, code)
        # x = orgmaker("orgs//AlephRnd2 orgs//AMH_Z70_RAW.txt", "orgs//AlephRnd2 orgs//Cleaned Z72//AMH_Z72-Cleaned_V2.csv",  "AC")
        with open(f"final//{code}_aleph_orgsv.txt", 'w', encoding='latin-1', newline="\n") as target:
            json.dump(x, target, indent=4)
            print(f"print file written to {target.name}")

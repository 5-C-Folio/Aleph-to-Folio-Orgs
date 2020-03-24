from csv import DictReader
import json
import uuid
from marshSchema import phoneRecord, urlRecord, organizationRecord , addressRecord, emailRecord

def categories_getter(value):
    #currently is only designed to have type 1 or 3 in the export file. Should be controlled in Z72_reader function
    if value["Z72_REC_KEY 2"] == "1":
        categories = ["UUIDplaceholder1"]
    elif value["Z72_REC_KEY 2"] == "3":
        categories = ["618084d5-57ed-49a8-8e91-bae476e1d247"]
    return categories


def orgmaker(z70, z72, prefix):
    jsonRecords = []
    with open(z70, 'r', encoding='latin-1') as file:
        dictFile = DictReader(file, delimiter = '|')
        for row in dictFile:
            stat = 'Active'
            Z72_file = (Z72_reader(row['Z70_REC_KEY'].rstrip(),z72))
            folio_description = (addressNoteGetter(Z72_file))
            newRec = organizationRecord(code = prefix + row['Z70_REC_KEY'].rstrip(),
                                        name = prefix + " " + row['Z70_VENDOR_NAME'],
                                        status = stat,
                                        addresses = addressMaker(Z72_file),
                                        phoneNumbers = phoneMaker(Z72_file),
                                        erpCode = row["Z70_ADDITIONAL_VENDOR_CODE"].rstrip(),
                                        emails = emailMaker(Z72_file),
                                        urls = urlMaker(Z72_file),
                                        description = row['Z70_NOTE'],
                                        isVendor = True
                                        )
            if  folio_description is not None and len(folio_description)> 1:
                print(folio_description)
                newRec.description = newRec.description + folio_description
            jsonRecords.append(newRec)
            print(newRec["name"])
    return jsonRecords


def Z72_reader(code, file):
    with open(file, 'r', encoding='latin-1') as file2:
        dictFile = DictReader(file2, delimiter = ',')
        contact_List= []
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

                addLine = addressRecord(addressLine1 = value["Z72_VENDOR_ADDRESS"],
                                    city = value['Z72_VENDOR_CITY'],
                                    zipCode = value['Z72_VENDOR_POSTAL_CODE'],
                                    stateRegion = value['Z72_VENDOR_STATE'],
                                    country = value["Z72_VENDOR_COUNTRY"],
                                    categories = categories
                                    )
                export_list.append(addLine)
        print(export_list)
        return(export_list)




def  phoneMaker(z72_file):
            phonelist = []
            for value in z72_file:
                categories = categories_getter(value)
                if value['Z72_VENDOR_TEL']:
                        phoneMain = (value['Z72_VENDOR_TEL'])
                        phone1 = phoneRecord(phoneNumber=phoneMain, type='Office', categories = categories)
                        if len(phone1["phoneNumber"]) >1:
                            phonelist.append(phone1)
                if value['Z72_VENDOR_FAX']:
                        phoneFax = value['Z72_VENDOR_FAX']
                        phone2 = phoneRecord(phoneNumber=phoneFax, type='Fax', categories = categories)
                        if len(phone2["phoneNumber"]) >1:
                            phonelist.append(phone2)
            return phonelist


def emailMaker(z72_file):
                exportList = []
                for value in z72_file:
                    categories = categories_getter(value)
                    email = emailRecord(value=value['Z72_VENDOR_EM'], categories = categories)
                    if len(email["value"]) > 1:
                        exportList.append(email)
                return exportList

def urlMaker(z72_file):
                exportList= []
                for value in z72_file:
                        url = urlRecord(value=value['Z72_VENDOR_IP'], isPrimary = True)
                        if len(url["value"]) > 1:
                            exportList.append(url)
                return exportList

def uuidgen(inst, code):
    x = uuid.uuid1()
    uuid.uuid5("")

if __name__ == "__main__":

    x = orgmaker("orgs//Rnd2 orgs//MHC_Z70_RAW.txt", "orgs//Rnd2 orgs//Cleaned Z72//MHC_Z72-Cleaned_V2.csv",  "MH")
    with open("testfile.txt", 'w', encoding='latin-1', newline="\n") as target:
        json.dump(x,target, indent=4)


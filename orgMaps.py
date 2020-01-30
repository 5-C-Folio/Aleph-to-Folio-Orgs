from csv import DictReader
import json
import uuid
from marshSchema import phoneRecord, urlRecord, organizationRecord , addressRecord, emailRecord


def orgmaker(z70, z72, rec_keys):
    jsonRecords = []
    with open(z70, 'r', encoding='latin-1') as file:
        dictFile = DictReader(file, delimiter = '|')
        for row in dictFile:

            if row['Z70_STATUS'] == 'AC':
                stat = 'Active'
            else:
                stat = 'Inactive'


            newRec = organizationRecord(code = row['Z70_REC_KEY'].rstrip(),
                                        name = row['Z70_VENDOR_NAME'],
                                        status = stat,
                                        addresses = addressMaker(row['Z70_REC_KEY'].rstrip(),z72, rec_keys),
                                        phoneNumbers = phoneMaker(row['Z70_REC_KEY'].rstrip(),z72, rec_keys),
                                        erpCode = row["Z70_ADDITIONAL_VENDOR_CODE"],
                                        emails = emailMaker(row['Z70_REC_KEY'].rstrip(),z72,rec_keys),
                                        urls = urlMaker(row['Z70_REC_KEY'].strip(),z72,rec_keys),
                                        isVendor = True
                                        )

            jsonRecords.append(newRec)
            print(newRec["name"])
    return jsonRecords

def addressMaker(code,file,rec_keys):
    with open(file, 'r', encoding='latin-1') as file2:
        dictFile = DictReader(file2, delimiter = '|')
        export_list = []
        for row in dictFile:

            if row['Z72_REC_KEY 1'].rstrip() == code and row['Z72_REC_KEY 2'] in rec_keys:
                addLine = addressRecord(addressLine1 = row["Z72_VENDOR_ADDRESS"],
                                    city = row['Z72_VENDOR_CITY'],
                                    zipCode = row['Z72_VENDOR_POSTAL_CODE'],
                                    stateRegion = row['Z72_VENDOR_STATE'],
                                    country = row["Z72_VENDOR_COUNTRY"],

                                    )
                export_list.append(addLine)
        return(export_list)
def  phoneMaker(code,file,rec_keys):
    with open(file, 'r', encoding='latin-1') as file2:
            dictFile = DictReader(file2, delimiter = '|')
            phonelist = []
            for row in dictFile:

                if row['Z72_REC_KEY 1'].rstrip() == code and row['Z72_REC_KEY 2'] in rec_keys:

                    if row['Z72_VENDOR_TEL']:
                        phoneMain = (row['Z72_VENDOR_TEL'])
                        phone1 = phoneRecord(phoneNumber=phoneMain, type='Office')
                        if len(phone1["phoneNumber"]) >1:
                            phonelist.append(phone1)
                    if row['Z72_VENDOR_FAX']:
                        phoneFax = row['Z72_VENDOR_FAX']
                        phone2 = phoneRecord(phoneNumber=phoneFax, type='Fax')
                        if len(phone2["phoneNumber"]) >1:
                            phonelist.append(phone2)
            return phonelist


def emailMaker(code,file,rec_keys):
    with open(file, 'r', encoding='latin-1') as file2:
                dictFile = DictReader(file2, delimiter = '|')
                exportList = []
                for row in dictFile:
                        if row['Z72_REC_KEY 1'].rstrip() == code and row['Z72_REC_KEY 2'] in rec_keys:
                            email = emailRecord(value=row['Z72_VENDOR_EM'])
                            if len(email["value"]) > 1:
                                exportList.append(email)
                return exportList

def urlMaker(code,file,rec_keys):
    with open(file , 'r', encoding='latin-1') as file2:
                dictFile = DictReader(file2, delimiter = '|')
                exportList = []
                for row in dictFile:
                        if row['Z72_REC_KEY 1'].rstrip() == code and row['Z72_REC_KEY 2'] in rec_keys:
                            url = urlRecord(value=row['Z72_VENDOR_IP'])
                            if len(url["value"]) > 1:
                                exportList.append(url)
                return exportList

def uuidgen(inst, code):
    x = uuid.uuid1()
    uuid.uuid5("")

if __name__ == "__main__":

    x = orgmaker("orgs//uma_org_Z70.txt", "orgs//uma_org_address_Z72-txt_final_clean (2).txt", ["1", "3"])
    with open("testfile.txt", 'w', encoding='latin-1') as target:
        json.dump(x,target, indent=4)


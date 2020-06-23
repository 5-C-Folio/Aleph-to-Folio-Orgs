import json
from sys import argv

def json_read(file):
    with open(file, 'r') as coralFile:
        coralJson = json.load(coralFile)
        return coralJson
def main(aleph_file,coral_file):
    aleph_index = []
    aleph_json = json_read(aleph_file)
    for record in aleph_json:
        aleph_index.append(record['code'])
    coral_index = []
    exportlist= []
    coral_json = json_read(coral_file)

    for c_record in coral_json:
        coral_index.append(c_record['code'])

    for coral_record in coral_json:

        if coral_record['code'] in aleph_index:

            aleph_record = aleph_json[aleph_index.index(coral_record['code'])]
            print(f" matching coral {coral_record['code']} to {aleph_record['code']}")
            aleph_record["aliases"] = coral_record['aliases']
            aleph_record['description'] = aleph_record['description'] + ' \n ' + coral_record['description']
            aleph_record['interfaces']=coral_record['interfaces']
            if len(coral_record['contacts']) >0 :
                aleph_record['contacts'] = coral_record['contacts']
            exportlist.append(aleph_record)
        else:
            exportlist.append(coral_record)

    for a_record in aleph_json:
        if a_record["code"] not in coral_index:
            exportlist.append(a_record)
    return exportlist
if __name__ == '__main__':
    try:
        if argv[1] == 'help':
            print("select select the aleph file and the coral file ")
            exit()
        else:
            aleph_file = argv[1]
            coral_file = argv[2]

    except IndexError:
        print("select select the aleph file and the coral file ")
        exit()
    code = input("input the two character organization code> ")
    conf = input(f'''You have selected: {code}final as the write directory \n {aleph_file} as the Aleph vendor file \n {coral_file} as the Coral Organization file \n "yes to continue, or any key to exit> ''')
    if conf in ["yes", "Yes", "Y", 'y']:
        try:
            with open (f'{code}final//{code}_organization_merged4.txt', 'w') as merged:
                filemerge = main(aleph_file, coral_file)

            #json.dump(filemerge,merged, indent=4)
                for row in filemerge:
                    x = json.dumps(row)
                    x = x + ",\n"
                    merged.write(x)
        except FileNotFoundError:
            print("invalid write location")
            exit()
    else:
        print ("exiting")
        exit()







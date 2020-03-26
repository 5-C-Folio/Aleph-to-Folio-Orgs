import json


def json_read(file):
    with open(file, 'r') as coralFile:
        coralJson = json.load(coralFile)
        return coralJson

aleph_index = []
aleph_json = json_read('smc_aleph.txt')
for record in aleph_json:
    aleph_index.append(record['code'])
coral_index = []
exportlist= []
coral_json = json_read('sc_coralfile.txt')
for c_record in coral_json:
    coral_index.append(c_record['code'])

for coral_record in coral_json:
    if coral_record['code'] in aleph_index:
        aleph_record = aleph_json[aleph_index.index(coral_record['code'])]
        aleph_record["aliases"] = coral_record['aliases']
        aleph_record['description'] = aleph_record['description'] + ' \n ' + coral_record['description']
        exportlist.append(aleph_record)
    else:
        exportlist.append(coral_record)

for a_record in aleph_json:
    if a_record["code"] not in coral_index:
        exportlist.append(a_record)


with open ('sc_merged_file.txt', 'w') as merged:
    json.dump(exportlist, merged, indent=4)






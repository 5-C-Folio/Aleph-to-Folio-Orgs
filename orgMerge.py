import json


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
            aleph_record["aliases"] = coral_record['aliases']
            aleph_record['description'] = aleph_record['description'] + ' \n ' + coral_record['description']
            exportlist.append(aleph_record)
        else:
            exportlist.append(coral_record)

    for a_record in aleph_json:
        if a_record["code"] not in coral_index:
            exportlist.append(a_record)
    return exportlist
if __name__ == '__main__':
    with open ('um_merged_filev3.txt', 'w') as merged:
        filemerge = main('UMA_aleph_orgsv3.txt','sc_coralfilev2.txt')
        for row in filemerge:
            x = json.dumps(row)
            x = x + "\n"
            merged.write(x)






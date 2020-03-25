## Aleph-to-Folio-Orgs

### Requirements
* Python 3.x
* Warlock
### Purpose
Takes an export of the Z70 and Z72 Aleph tables and combines them into single json file that validates with the Folio organization schema, and other schema used in the organization record. (emailRecord, phoneRecord, addressRecord, urlRecord)   
### Instructions
1) Generate files from the Z70 and Z72 in csv format
2) Split out Z72_rec_key into Z72_REC_KEY 1 and Z72_REC_KEY 2, with the code 1 and that record identifier in 2, with the first column being 20 characters, and the second 1.  
3)  Clear out consecutive spaces in all fields 
4)  Fields that have invalid values according the the json schema may fail.  This  includes URLS that do not start with "http{x}://"  
5)  Add the correct corresponding Z70 and Z72 csvs to the bottom of the file as well as a valid prefix for the org codes. If other addresses are needed from the Z72, change the values in the list.
``` 
fields required in Z72: 
Z72_REC_KEY 1,Z72_REC_KEY 2,Z72_VENDOR_TEL,Z72_VENDOR_FAX,
Z72_VENDOR_EM,Z72_VENDOR_IP, Z72_VENDOR_ADDRESS,Z72_VENDOR_CITY, 
Z72_VENDOR_STATE,Z72_VENDOR_POSTAL_CODE, Z72_VENDOR_COUNTRY,Z72_NOTE 
```

6) before running, remove BOM or Z70 will not match

### Known Issues
* can only take address type 1 or address type 3
* must remove BOM
* May cause minor formatting problems with concating notes from different fields 
* should have argv for parameters so program can be run from command line 

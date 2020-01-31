## Aleph-to-Folio-Orgs


###Purpose
Takes an export of the Z70 and Z72 Aleph tables and combines them into
Requires the following pre processing of the z70:
*the REC_KEY must be split into the code and the 1-5 digit identifier


###Knonw Issues
* Re-opens z72 files way to many times.  The z72 should be initially opened and remain open for the run of the program.  

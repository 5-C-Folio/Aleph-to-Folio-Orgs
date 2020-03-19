--Query to pull only active address.  @school is the code of the school
SELECT ad.Z72_REC_KEY, ad.Z72_VENDOR_TEL, ad.Z72_VENDOR_FAX, ad.Z72_VENDOR_EM,
ad.Z72_VENDOR_IP, ad.Z72_VENDOR_ADDRESS, ad.Z72_VENDOR_CITY, ad.Z72_VENDOR_STATE, ad.Z72_VENDOR_POSTAL_CODE,
ad.Z72_VENDOR_COUNTRY, ad.Z72_NOTE
 from @school.Z72 ad 
INNER JOIN
@school.Z70 ven
on substr(ven.Z70_REC_KEY,0,20) = SUBSTR(ad.Z72_REC_KEY,0,20)
where ven.Z70_STATUS !='NA'

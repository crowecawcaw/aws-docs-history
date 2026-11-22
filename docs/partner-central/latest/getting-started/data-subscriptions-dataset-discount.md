

# Partner Discount Business Report dataset

The Detailed Billing Report for channel and resell partners: one row for each discounted invoice line, with the billed amount and the discount of every partner-program component, for the current month and the six months before it. AWS Partner Central delivers this dataset to the `discount_business_report` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


| Column name | Type | 
| --- | --- | 
| dbr\_id\_pk (key column) | string | 
| program | string | 
| payer\_account\_id | bigint | 
| spp\_name | string | 
| invoice\_id | string | 
| product\_code | string | 
| linked\_account\_id | bigint | 
| sum\_amount | string | 
| support\_rate | double | 
| net\_new\_business\_rate | double | 
| partner\_originated\_rate | double | 
| internal\_rate | double | 
| no\_eur\_rate | double | 
| shareshift\_rate | double | 
| exception\_rate | double | 
| psp\_rate | double | 
| base\_or\_base\_tech\_rate | double | 
| br\_exception\_rate | double | 
| support\_discount | double | 
| net\_new\_business\_discount | string | 
| partner\_originated\_discount | double | 
| internal\_discount | double | 
| no\_eur\_discount | double | 
| shareshift\_discount | double | 
| exception\_discount | double | 
| psp\_discount | double | 
| base\_or\_base\_tech\_discount | string | 
| br\_exception\_discount | string | 
| total\_discount | double | 
| automated\_amount | double | 
| discount\_start\_date | string | 
| discount\_end\_date | string | 
| ocb\_shield\_rate | bigint | 
| ocb\_shield\_discount | bigint | 
| grow\_rate | double | 
| grow\_discount | double | 
| psd\_rate | double | 
| psd\_discount | double | 
| pod\_plus\_rate | double | 
| pod\_plus\_discount | double | 
| scaga\_rate | double | 
| scaga\_discount | double | 
| pgd\_plus\_rate | double | 
| pgd\_plus\_discount | double | 
| pgd\_rate | double | 
| pgd\_discount | double | 
| nci\_exception\_discount | string | 
| nci\_exception\_rate | double | 
| abc\_discount | double | 
| abc\_discount\_rate | double | 
| bill\_period | string | 
| row\_type | string | 
| row\_modified\_date | timestamp | 
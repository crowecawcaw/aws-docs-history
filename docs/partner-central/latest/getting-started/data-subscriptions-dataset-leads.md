

# ACE Leads dataset

Lead lifecycle data from the ACE Lead Tool: AWS-shared and partner-imported leads, acceptance, qualification stages, ownership, and conversion to opportunities. AWS Partner Central delivers this dataset to the `leads` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


| Column name | Type | 
| --- | --- | 
| lead\_id\_pk (key column) | string | 
| lead\_id | string | 
| engagement\_id | string | 
| opportunity\_id | string | 
| lead\_source | string | 
| lead\_status | string | 
| is\_lead\_converted | string | 
| lead\_converted\_date | timestamp | 
| lead\_created\_date | timestamp | 
| current\_lead\_stage | string | 
| is\_lead\_active | string | 
| lead\_owner | string | 
| row\_type | string | 
| row\_modified\_date | timestamp | 


# Partner Account Relationships dataset

End customer AWS accounts in an active billing-transfer relationship with a distribution seller, with the relationship type, effective start date, and sector. AWS Partner Central delivers this dataset to the `account_relationships` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


| Column name | Type | 
| --- | --- | 
| account\_relationship\_id\_pk (key column) | string | 
| relationship\_type | string | 
| relationship\_aws\_account\_id | string | 
| partner\_name | string | 
| program\_management\_aws\_account\_id | string | 
| effective\_start\_date | date | 
| sector | string | 
| ultimate\_parent\_program | string | 
| row\_type | string | 
| row\_modified\_date | timestamp | 
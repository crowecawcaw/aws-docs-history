

# Partner Marketing Campaigns dataset

Marketing campaign performance: lead flow, opportunity attribution, and pipeline metrics for each campaign and KPI. AWS Partner Central delivers this dataset to the `marketing_campaigns` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


| Column name | Type | 
| --- | --- | 
| campaign\_id\_pk (key column) | string | 
| campaign\_name | string | 
| campaign\_start\_date | date | 
| campaign\_end\_date | date | 
| kpi\_created\_date | date | 
| opportunity\_launched\_date | date | 
| opportunity\_aws\_closed\_date | date | 
| opportunity\_stage | string | 
| geo | string | 
| region | string | 
| country | string | 
| segment | string | 
| industry | string | 
| opportunity\_name | string | 
| kpi\_name | string | 
| kpi\_id | string | 
| annualized\_revenue | decimal(38,2) | 
| lead\_stage | string | 
| row\_type | string | 
| row\_modified\_date | timestamp | 
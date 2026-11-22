

# ACE Opportunity Pipeline dataset

Opportunity lifecycle data: stages, monthly and annual recurring revenue, win and loss, ownership, and geographic, segment, and industry dimensions. AWS Partner Central delivers this dataset to the `opportunity_pipeline` folder in your bucket.

The following table lists the columns in the dataset.

Every row includes a `row_type` value of `INSERT`, `UPDATE`, or `DELETE`, and a `row_modified_date` timestamp. Apply rows to your copy of the data by key column, in order of `row_modified_date`.


| Column name | Type | 
| --- | --- | 
| opportunity\_id\_pk (key column) | string | 
| opportunity\_id | string | 
| partner\_accepted\_time | timestamp | 
| won\_date | date | 
| opportunity\_approved\_rejected\_date | date | 
| ace\_submitted\_date | date | 
| opportunity\_target\_close\_date | date | 
| last\_activity\_date | timestamp | 
| ownership | string | 
| partner\_primary\_need\_from\_aws | string | 
| opportunity\_business\_unit | string | 
| opportunity\_geo | string | 
| opportunity\_region | string | 
| opportunity\_segment | string | 
| engagement\_type | string | 
| opportunity\_stage\_name | string | 
| aws\_opportunity\_stage\_name | string | 
| opportunity\_pipeline\_status | string | 
| opportunity\_status | string | 
| opportunity\_country | string | 
| opportunity\_industry | string | 
| customer\_company\_name | string | 
| customer\_type | string | 
| opportunity\_solution\_tag | string | 
| is\_genai\_opportunity | string | 
| currency | string | 
| workload | string | 
| delivery\_model | string | 
| state\_province | string | 
| postal\_code | string | 
| multi\_partner\_engagement | string | 
| partner\_sales\_rep\_name | string | 
| partner\_sales\_rep\_email | string | 
| aws\_sales\_rep\_email | string | 
| aws\_account\_id | string | 
| partner\_crm\_unique\_id | string | 
| partner\_project\_title | string | 
| offer\_id | string | 
| next\_step | string | 
| primary\_campaign\_source | string | 
| ace\_crm\_integration\_status | string | 
| opportunity\_partner\_acceptance\_status | string | 
| aws\_marketplace\_engagement\_score | string | 
| aws\_marketplace\_solution\_engagement\_score | string | 
| estimated\_pipeline\_revenue\_mrr | decimal(38,2) | 
| is\_greenfield | integer | 
| row\_type | string | 
| row\_modified\_date | timestamp | 
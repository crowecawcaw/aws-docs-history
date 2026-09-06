

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_WLM\_ERROR
<a name="r_STL_WLM_ERROR"></a>

Records all WLM-related errors as they occur.

STL\_WLM\_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STL_WLM_ERROR-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| recordtime  | timestamp  | Time that the error occurred.  | 
| pid  | integer  | ID for the process that generated the error.  | 
| error\_string  | character(256)  | Error description.  | 
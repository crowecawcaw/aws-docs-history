

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_COPY\_JOB\_INFO
<a name="SYS_COPY_JOB_INFO"></a>

Use SYS\_COPY\_JOB\_INFO to view messages logged about a COPY JOB.

This view contains information about errors in a COPY JOB that has run.

SYS\_COPY\_JOB\_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_COPY_JOB_INFO-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| job\_id | bigint | The copy job identifier. | 
| job\_name | character(128) | The name of the copy job. | 
| database\_name | character(128) | The name of the database. | 
| record\_time | timestamp | The time (UTC) when the message was logged. | 
| message | chaacter(512) | This message of the logged event for a COPY JOB. | 
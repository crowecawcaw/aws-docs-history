

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_COPY\_JOB\_DETAIL
<a name="SYS_COPY_JOB_DETAIL"></a>

Use SYS\_COPY\_JOB\_DETAIL to view details of COPY JOB commands.

This view contains the COPY JOB commands that have been created. If COPY JOB attempts to load a file and it fails to load, the file is skipped on future automatic COPY JOB attempts.

SYS\_COPY\_JOB\_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SYS_COPY_JOB_DETAIL-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| user\_id | integer | The identifier of the user that owns the job. | 
| database\_name | text | The name of the database containing the job. | 
| job\_id | integer | The copy job identifier. | 
| job\_name | text | The name of the copy job. | 
| file\_location | text | The Amazon S3 bucket name for the entry. | 
| file\_name | text | The Amazon S3 key name for the entry. | 
| file\_size | bigint | The size of the entry in bytes. | 
| file\_etag | text | The Amazon S3 entity tag (ETag) for the entry. | 
| job\_text | character(256) | The parameters of the COPY statement. | 
| modification\_time | timestamp | The time (UTC) at which the S3 object was created or modified initiating ingestion. In S3 listing mode, this is the object modification time. For notification mode, this is the time the notification event occurred. | 
| enqueue\_time | timestamp | The time (UTC) at which the entry was added to the ingestion queue. | 
| status | char(1) | The status of the entry. Valid values: P for pending ingestion, I for ingested, E for error ingesting, and U for unknown (indicating some kind of unexpected state). | 

The following example returns one row where for ingested entries.

```
SELECT * FROM SYS_COPY_JOB_DETAIL WHERE status ilike '%ingested%' limit 1;


user_id | 100
database_name | dev
job_name | many_job_4_3
job_id | 110702
file_location | saral-sqs-system4623202051-0
file_name | frenzy-9/4623202051/file_0_107
file_size | 11302
file_etag | 51b2d78ac5b5aecf4ee6f8374815ad19
modification_time | 2024-07-15 20:43:14
enqueue_time | 2024-07-15 20:44:24
status | Ingested
```
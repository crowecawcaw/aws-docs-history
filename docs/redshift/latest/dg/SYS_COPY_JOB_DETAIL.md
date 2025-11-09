Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_COPY_JOB_DETAIL

Use SYS_COPY_JOB_DETAIL to view details of COPY JOB commands.

This view contains the COPY JOB commands that have been created.
If COPY JOB attempts to load a file and it fails to load, the file is skipped on future automatic COPY JOB attempts.

SYS_COPY_JOB_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name       | Data type      | Description                                                                                                                                                                                                                  |
| ----------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id           | integer        | The identifier of the user that owns the job.                                                                                                                                                                                |
| database_name     | text           | The name of the database containing the job.                                                                                                                                                                                 |
| job_id            | integer        | The copy job identifier.                                                                                                                                                                                                     |
| job_name          | text           | The name of the copy job.                                                                                                                                                                                                    |
| file_location     | text           | The Amazon S3 bucket name for the entry.                                                                                                                                                                                     |
| file_name         | text           | The Amazon S3 key name for the entry.                                                                                                                                                                                        |
| file_size         | bigint         | The size of the entry in bytes.                                                                                                                                                                                              |
| file_etag         | text           | The Amazon S3 entity tag (ETag) for the entry.                                                                                                                                                                               |
| job_text          | character(256) | The parameters of the COPY statement.                                                                                                                                                                                        |
| modification_time | timestamp      | The time (UTC) at which the S3 object was created or modified initiating ingestion.<br>In S3 listing mode, this is the object modification time.<br>For notification mode, this is the time the notification event occurred. |
| enqueue_time      | timestamp      | The time (UTC) at which the entry was added to the ingestion queue.                                                                                                                                                          |
| status            | char(1)        | The status of the entry.<br>Valid values: `P` for pending ingestion, `I` for ingested, `E` for error ingesting,<br>and `U` for unknown (indicating some kind of unexpected state).                                           |

The following example returns one row where for ingested entries.

```
`SELECT * FROM SYS_COPY_JOB_DETAIL WHERE status ilike '%ingested%' limit 1;`
`user_id | 100
database_name | dev
job_name | many_job_4_3
job_id | 110702
file_location | saral-sqs-system4623202051-0
file_name | frenzy-9/4623202051/file_0_107
file_size | 11302
file_etag | 51b2d78ac5b5aecf4ee6f8374815ad19
modification_time | 2024-07-15 20:43:14
enqueue_time | 2024-07-15 20:44:24
status | Ingested`
```

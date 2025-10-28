Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_COPY_JOB_INFO

Use SYS_COPY_JOB_INFO to view messages logged about a COPY JOB.

This view contains information about errors in a COPY JOB that has run.

SYS_COPY_JOB_INFO is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type      | Description                                      |
| ------------- | -------------- | ------------------------------------------------ |
| job_id        | bigint         | The copy job identifier.                         |
| job_name      | character(128) | The name of the copy job.                        |
| database_name | character(128) | The name of the database.                        |
| record_time   | timestamp      | The time (UTC) when the message was logged.      |
| message       | chaacter(512)  | This message of the logged event for a COPY JOB. |

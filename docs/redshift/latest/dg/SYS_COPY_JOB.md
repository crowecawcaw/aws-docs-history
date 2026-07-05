Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_COPY\_JOB

Use SYS\_COPY\_JOB to view details of COPY JOB commands.

This view contains the COPY JOB commands that have been created.

SYS\_COPY\_JOB is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name        | Data type      | Description                                                                                                              |
| ------------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------ |
| job\_id            | bigint         | The copy job identifier.                                                                                                 |
| job\_name          | character(128) | The name of the copy job.                                                                                                |
| iam\_role          | character(128) | The IAM role specified in the COPY<br>statement.                                                                         |
| job\_text          | character(256) | The parameters of the COPY statement.                                                                                    |
| is\_auto           | integer        | Indicates whether the COPY JOB is automatically<br>run by Amazon Redshift. A `1` indicates true, `0`<br>indicates false. |
| on\_error\_suspend | integer        | This information is for internal use only.                                                                               |

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_COPY_JOB_INTEGRATIONS

Use SVV_COPY_JOB_INTEGRATIONS to view details of S3 event integrations.

This view contains the S3 event integrations that have been created.

SVV_COPY_JOB_INTEGRATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type | Description                                                                            |
| ------------- | --------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| job_owner     | integer   | The identifier of the owner of the job.                                                |
| channel_arn   | name      | The integration identifier.                                                            |
| bucket        | text      | The Amazon S3 bucket name associated with the integration.                             |
| channel state | name      | The state of the integration. Valid values: `Pending`, `Established`, and `Inactive` . |
| db_name       | name      | The database name of the dependent object.                                             |
| job_name      | text      | The name of the job.                                                                   |
| job_state     | integer   | The state of the job. Valid values: `0` for active, `1` for pending.                   | The following example returns S3 integrations for the current database. `` `SELECT * FROM SVV_COPY_JOB_INTEGRATIONS WHERE db_name = pg_catalog.current_database();` `` |

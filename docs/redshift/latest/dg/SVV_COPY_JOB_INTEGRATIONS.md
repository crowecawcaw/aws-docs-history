

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_COPY\_JOB\_INTEGRATIONS
<a name="SVV_COPY_JOB_INTEGRATIONS"></a>

Use SVV\_COPY\_JOB\_INTEGRATIONS to view details of S3 event integrations.

This view contains the S3 event integrations that have been created.

SVV\_COPY\_JOB\_INTEGRATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SVV_COPY_JOB_INTEGRATIONS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| job\_owner | integer | The identifier of the owner of the job. | 
| channel\_arn | name | The integration identifier. | 
| bucket | text | The Amazon S3 bucket name associated with the integration. | 
| channel state | name | The state of the integration. Valid values: Pending, Established, and Inactive . | 
| db\_name | name | The database name of the dependent object. | 
| job\_name | text | The name of the job. | 
| job\_state | integer | The state of the job. Valid values: 0 for active, 1 for pending. | 

The following example returns S3 integrations for the current database.

```
SELECT * FROM SVV_COPY_JOB_INTEGRATIONS WHERE db_name = pg_catalog.current_database();
```
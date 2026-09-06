

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SYS\_SCHEMA\_QUOTA\_VIOLATIONS
<a name="r_SYS_SCHEMA_QUOTA_VIOLATIONS"></a>

Records the occurrence, transaction ID, and other useful information when a schema quota is exceeded. This system table is a translation of [STL\_SCHEMA\_QUOTA\_VIOLATIONS](r_STL_SCHEMA_QUOTA_VIOLATIONS.md).

r\_SYS\_SCHEMA\_QUOTA\_VIOLATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="r_STL_SCHEMA_QUOTA_VIOLATIONS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| owner\_id | integer | The ID of the schema owner. | 
| user\_id | integer | The ID of the user who generated the entry. | 
| transaction\_id | bigint | The transaction ID associated with the statement. | 
| session\_id | integer  | The process ID associated with the statement. | 
| schema\_id | integer | The namespace or schema ID. | 
| schema\_name | character (128) | The namespace or schema name. | 
| quota | integer | The amount of disk space (in MB) that the schema can use. | 
| disk\_usage | integer | The disk space (in MB) that is currently used by the schema. | 
| record\_time | timestamp without time zone | The time when the violation occurred. | 

## Sample queries
<a name="r_STL_SCHEMA_QUOTA_VIOLATIONS-sample-queries"></a>

The following query shows the result of a quota violation:

```
SELECT user_id, TRIM(schema_name) "schema_name", quota, disk_usage, record_time FROM
sys_schema_quota_violations WHERE SCHEMA_NAME = 'sales_schema' ORDER BY timestamp DESC;
```

This query returns the following sample output for the specified schema:

```
user_id| schema_name  | quota | disk_usage | record_time
-------+--------------+-------+------------+----------------------------
104    | sales_schema | 2048  | 2798       | 2020-04-20 20:09:25.494723
(1 row)
```
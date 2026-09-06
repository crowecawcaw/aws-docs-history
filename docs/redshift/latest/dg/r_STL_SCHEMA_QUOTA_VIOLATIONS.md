

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_SCHEMA\_QUOTA\_VIOLATIONS
<a name="r_STL_SCHEMA_QUOTA_VIOLATIONS"></a>

Records the occurrence, timestamp, XID, and other useful information when a schema quota is exceeded.

STL\_SCHEMA\_QUOTA\_VIOLATIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_SCHEMA\_QUOTA\_VIOLATIONS](r_SYS_SCHEMA_QUOTA_VIOLATIONS.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STL_SCHEMA_QUOTA_VIOLATIONS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| ownerid | integer | The ID of the schema owner. | 
| xid | bigint | The transaction ID associated with the statement. | 
| pid | integer  | The process ID associated with the statement. | 
| userid | integer | The ID of the user who generated the entry. | 
| schema\_id | integer | The namespace or schema ID. | 
| schema\_name | character (128) | The namespace or schema name. | 
| quota | integer | The amount of disk space (in MB) that the schema can use. | 
| disk\_usage | integer | The disk space (in MB) that is currently used by the schema. | 
| disk\_usage\_pct | double precision | The disk space percentage that is currently used by the schema out of the configured quota. | 
| timestamp | timestamp without time zone | The time when the violation occurred. | 

## Sample queries
<a name="r_STL_SCHEMA_QUOTA_VIOLATIONS-sample-queries"></a>

The following query shows the result of quota violation:

```
SELECT userid, TRIM(SCHEMA_NAME) "schema_name", quota, disk_usage, disk_usage_pct, timestamp FROM
stl_schema_quota_violations WHERE SCHEMA_NAME = 'sales_schema' ORDER BY timestamp DESC;
```

This query returns the following sample output for the specified schema:

```
userid | schema_name  | quota | disk_usage | disk_usage_pct |timestamp
-------+--------------+-------+------------+----------------+----------------------------
104    | sales_schema | 2048  | 2798       |  136.62        | 2020-04-20 20:09:25.494723
(1 row)
```


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ALL\_SCHEMAS
<a name="r_SVV_ALL_SCHEMAS"></a>

Use SVV\_ALL\_SCHEMAS to view a union of Amazon Redshift schemas as shown in SVV\_REDSHIFT\_SCHEMAS and the consolidated list of all external schemas from all databases. For more information about Amazon Redshift schemas, see [SVV\_REDSHIFT\_SCHEMAS](r_SVV_REDSHIFT_SCHEMAS.md).

SVV\_ALL\_SCHEMAS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW SCHEMAS](r_SHOW_SCHEMAS.md) command for schema discovery. SHOW SCHEMAS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_ALL_SCHEMAS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database\_name | varchar(128) | The name of the database where the schema exists. | 
| schema\_name | varchar(128) | The name of the schema. | 
| schema\_owner | integer | The user ID of the schema owner. For information about user IDs, see [PG\_USER\_INFO](pg_user_info.md). | 
| schema\_type | varchar(128) | The type of the schema. Possible values are external, local, and shared schemas. | 
| schema\_acl | varchar(128) | The string that defines the permissions for the specified user or user group for the schema. | 
| source\_database | varchar(128) | The name of the source database for external schema. | 
| schema\_option | varchar(256) | The options of the schema. This is an external schema attribute. | 

## Sample query
<a name="r_SVV_ALL_SCHEMAS-sample-query"></a>

The following example returns the output of SVV\_ALL\_SCHEMAS.

```
SELECT *
FROM svv_all_schemas
WHERE database_name = 'tickit_db'
ORDER BY database_name,
    SCHEMA_NAME;


 database_name |    schema_name     | schema_owner | schema_type | schema_acl | source_database | schema_option
---------------+--------------------+--------------+-------------+------------+-----------------+--------------- 
   tickit_db   |       public       |       1      |   shared    |            |                 |
```
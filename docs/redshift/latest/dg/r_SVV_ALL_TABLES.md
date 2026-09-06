

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ALL\_TABLES
<a name="r_SVV_ALL_TABLES"></a>

Use SVV\_ALL\_TABLES to view a union of Amazon Redshift tables as shown in SVV\_REDSHIFT\_TABLES and the consolidated list of all external tables from all external schemas. For information about Amazon Redshift tables, see [SVV\_REDSHIFT\_TABLES](r_SVV_REDSHIFT_TABLES.md).

SVV\_ALL\_TABLES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW TABLES](r_SHOW_TABLES.md) command for table discovery. SHOW TABLES works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_ALL_TABLES-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database\_name | varchar(128) | The name of the database where the table exists. | 
| schema\_name | varchar(128) | The schema name for the table. | 
| table\_name | varchar(128) | The name of the table. | 
| table\_acl | varchar(128) | The string that defines the permission for the specified user or user group for the table. | 
| table\_type | varchar(128) | The type of the table. Possible values are views, base tables, external tables, and shared tables. | 
| remarks | varchar(256) | Remarks. | 

## Sample queries
<a name="r_SVV_ALL_TABLES-sample-queries"></a>

The following example returns the output of SVV\_ALL\_TABLES.

```
SELECT *
FROM svv_all_tables
WHERE database_name = 'tickit_db'
ORDER BY TABLE_NAME,
    SCHEMA_NAME
LIMIT 5;

 database_name | schema_name |        table_name        | table_type | table_acl | remarks
---------------+-------------+--------------------------+------------+-----------+---------
   tickit_db   |    public   | tickit_category_redshift |    TABLE   |           |
   tickit_db   |    public   |   tickit_date_redshift   |    TABLE   |           |
   tickit_db   |    public   |   tickit_event_redshift  |    TABLE   |           |
   tickit_db   |    public   | tickit_listing_redshift  |    TABLE   |           |
   tickit_db   |    public   |   tickit_sales_redshift  |    TABLE   |           |
```

If the table\_acl value is null, no access privileges have been explicitly granted to the corresponding table.
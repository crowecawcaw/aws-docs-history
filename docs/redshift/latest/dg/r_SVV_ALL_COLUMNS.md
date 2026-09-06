

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_ALL\_COLUMNS
<a name="r_SVV_ALL_COLUMNS"></a>

Use SVV\_ALL\_COLUMNS to view a union of columns from Amazon Redshift tables as shown in SVV\_REDSHIFT\_COLUMNS and the consolidated list of all external columns from all external tables. For information about Amazon Redshift columns, see [SVV\_REDSHIFT\_COLUMNS](r_SVV_REDSHIFT_COLUMNS.md).

SVV\_ALL\_COLUMNS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW COLUMNS](r_SHOW_COLUMNS.md) command for column discovery. SHOW COLUMNS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_ALL_COLUMNS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| database\_name | varchar(128) | The name of the database. | 
| schema\_name | varchar(128) | The name of the schema. | 
| table\_name | varchar(128) | The name of the table. | 
| column\_name | varchar(128) | The name of the column. | 
| ordinal\_position | integer | The position of the column in the table. | 
| column\_default | varchar(4000) | The default value of the column. | 
| is\_nullable | varchar(3) | A value that indicates whether the column is nullable. Possible values are yes and no. | 
| data\_type | varchar(128) | The data type of the column. | 
| character\_maximum\_length | integer | The maximum number of characters in the column. | 
| numeric\_precision | integer | The numeric precision. | 
| numeric\_scale | integer | The numeric scale. | 
| remarks | varchar(256) | Remarks. | 

## Sample queries
<a name="r_SVV_ALL_COLUMNS-sample-queries"></a>

The following example returns the output of SVV\_ALL\_COLUMNS.

```
SELECT *
FROM svv_all_columns
WHERE database_name = 'tickit_db'
    AND TABLE_NAME = 'tickit_sales_redshift'
ORDER BY COLUMN_NAME,
    SCHEMA_NAME
LIMIT 5;

 database_name | schema_name |     table_name        | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | numeric_precision | numeric_scale | remarks
 --------------+-------------+-----------------------+-------------+------------------+----------------+-------------+-----------+--------------------------+-------------------+---------------+---------
   tickit_db   |    public   | tickit_sales_redshift |    buyerid  |        4         |                |      NO     |  integer  |                          |         32        |       0       |
   tickit_db   |    public   | tickit_sales_redshift | commission  |        9         |                |     YES     |  numeric  |                          |          8        |	2       |
   tickit_db   |    public   | tickit_sales_redshift |    dateid   |        7         |                |      NO     |  smallint |                          |         16        |       0       |
   tickit_db   |    public   | tickit_sales_redshift |   eventid   |        5         |                |      NO     |  integer  |                          |         32        |       0       |
   tickit_db   |    public   | tickit_sales_redshift |    listid   |        2         |                |      NO     |  integer  |                          |         32        |       0       |
```
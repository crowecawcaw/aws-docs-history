

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_COLUMNS
<a name="r_SVV_COLUMNS"></a>

Use SVV\_COLUMNS to view catalog information about the columns of local and external tables and views, including [late-binding views](r_CREATE_VIEW.md#r_CREATE_VIEW_late-binding-views).

SVV\_COLUMNS is visible to all users by default. To control access to your database's metadata, enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view permissions for object metadata by users and roles. For more information, see [Metadata security](t_metadata_security.md).

The SVV\_COLUMNS view joins table metadata from the [System catalog tables](c_intro_catalog_views.md) (tables with a PG prefix) and the [SVV\_EXTERNAL\_COLUMNS](r_SVV_EXTERNAL_COLUMNS.md) system view. The system catalog tables describe Amazon Redshift database tables. SVV\_EXTERNAL\_COLUMNS describes external tables that are used with Amazon Redshift Spectrum. 

All users can see all rows from the system catalog tables. Regular users can see column definitions from the SVV\_EXTERNAL\_COLUMNS view only for external tables to which they have been granted access. Although regular users can see table metadata in the system catalog tables, they can only select data from user-defined tables if they own the table or have been granted access. 

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW COLUMNS](r_SHOW_COLUMNS.md) command for column discovery. SHOW COLUMNS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_COLUMNS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| table\_catalog | text | The name of the catalog where the table is. | 
| table\_schema | text | The schema name for the table. | 
| table\_name | text | The name of the table. | 
| column\_name | text | The name of the column. | 
| ordinal\_position | int | The position of the column in the table. | 
| column\_default | text | The default value of the column. | 
| is\_nullable | text | A value that indicates whether the column is nullable. | 
| data\_type | text | The data type of the column. | 
| character\_maximum\_length | int | The maximum number of characters in the column. | 
| numeric\_precision | int | The numeric precision. If the data\_type column is numeric, this column returns the number of significant digits in the entire value. | 
| numeric\_precision\_radix | int | The numeric precision radix. If the data\_type column is numeric, this column returns the base of the columns numeric\_precision and numeric\_scale. | 
| numeric\_scale | int | The numeric scale. If the data\_type column is numeric, this column returns the number of significant digits in the decimal value. | 
| datetime\_precision | int | The datetime precision. | 
| interval\_type | text | The interval type. | 
| interval\_precision | text | The interval precision. | 
| character\_set\_catalog | text | The character set catalog. | 
| character\_set\_schema | text | The character set schema. | 
| character\_set\_name | text | The character set name. | 
| collation\_catalog | text | The collation catalog. | 
| collation\_schema | text | The collation schema. | 
| collation\_name | text | The collation name. | 
| domain\_name | text | The domain name. | 
| remarks | text | Remarks. | 
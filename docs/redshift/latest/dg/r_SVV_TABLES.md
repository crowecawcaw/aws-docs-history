

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_TABLES
<a name="r_SVV_TABLES"></a>

Use SVV\_TABLES to view tables in local and external catalogs.

SVV\_TABLES is visible to all users by default. To control access to your database's metadata, enable metadata security for your provisioned cluster or serverless workgroup. Metadata security lets you separate view permissions for object metadata by users and roles. For more information, see [Metadata security](t_metadata_security.md).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW TABLES](r_SHOW_TABLES.md) command for table discovery. SHOW TABLES works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_TABLES-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| table\_catalog | text  | The name of the catalog where the table exists. | 
| table\_schema | text | The name the schema for the table. | 
| table\_name | text | The name of the table. | 
| table\_type | text  | The type of table. Possible values are views, external tables, and base tables. | 
| remarks | text | Remarks. | 


 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_EXTERNAL\_DATABASES
<a name="r_SVV_EXTERNAL_DATABASES"></a>

Use SVV\_EXTERNAL\_DATABASES to view details for external databases. 

SVV\_EXTERNAL\_DATABASES is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

## Table columns
<a name="SVV_EXTERNAL_DATABASES-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| eskind | integer  | The type of the external catalog for the database; 1 indicates a data catalog, 2 indicates a Hive metastore. | 
| esoptions | text | Details of the catalog where the database resides. | 
| databasename | text | The name of the database in the external catalog. | 
| location | text | The location of the database. | 
| parameters | text | Database parameters. | 
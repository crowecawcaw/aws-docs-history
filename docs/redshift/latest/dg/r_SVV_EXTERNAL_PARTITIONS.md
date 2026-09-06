

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_EXTERNAL\_PARTITIONS
<a name="r_SVV_EXTERNAL_PARTITIONS"></a>

Use SVV\_EXTERNAL\_PARTITIONS to view details for partitions in external tables. 

SVV\_EXTERNAL\_PARTITIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data)..

## Table columns
<a name="r_SVV_EXTERNAL_PARTITIONS-table-columns"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| schemaname | text  | The name of the Amazon Redshift external schema for the external table with the specified partitions.  | 
| tablename | text | The name of the external table. | 
| values | text  | Values for the partition. | 
| location | text | The location of the partition. The column size is limited to 128 characters. Longer values are truncated. | 
| input\_format | text  | The input format. | 
| output\_format | text | The output format. | 
| serialization\_lib | text  | The serialization library. | 
| serde\_parameters | text | SerDe parameters. | 
| compressed | integer | A value that indicates whether the partition is compressed; 1 indicates compressed, 0 indicates not compressed. | 
| parameters | text | Partition properties. | 
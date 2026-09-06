

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# SVV\_EXTERNAL\_SCHEMAS
<a name="r_SVV_EXTERNAL_SCHEMAS"></a>

Use SVV\_EXTERNAL\_SCHEMAS to view information about external schemas. For more information, see [CREATE EXTERNAL SCHEMA](r_CREATE_EXTERNAL_SCHEMA.md).

SVV\_EXTERNAL\_SCHEMAS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

For more information about best practices when querying system tables and views, see [Querying System Tables](https://docs.aws.amazon.com/redshift/latest/mgmt/discovering-metadata-system-tables.html).

**Note**  
Use the [SHOW SCHEMAS](r_SHOW_SCHEMAS.md) command for schema discovery. SHOW SCHEMAS works consistently across local, datashare, and external catalog contexts and is updated as new features are released. For more information, see [Best practices for discovering metadata](https://docs.aws.amazon.com/redshift/latest/mgmt/best-practices-discovering-metadata.html).

## Table columns
<a name="r_SVV_EXTERNAL_SCHEMAS-table-columns2"></a>


| Column name  | Data type  | Description  | 
| --- | --- | --- | 
| esoid | oid | External schema ID. | 
| eskind | smallint  | The type of the external catalog for the external schema: 1 indicates a data catalog, 2 indicates a Hive metastore, 3 indicates a federated query to Aurora PostgreSQL or Amazon RDS PostgreSQL, 4 indicates a schema for a local Amazon Redshift database, 5 indicates a schema for a remote Amazon Redshift database, 6 indicates a schema for a system table, 8 indicates a schema for remote MySQL databases, 9 indicates a schema for an Amazon Kinesis data stream, and 10 indicates an Amazon Managed Streaming for Apache Kafka data stream. | 
| schemaname | name | External schema name. | 
| esowner | integer | User ID of the external schema owner. | 
| databasename | text | External database name. | 
| esoptions | text | External schema options. | 

## Example
<a name="r_SVV_EXTERNAL_SCHEMAS-example"></a>

The following example shows details for external schemas. 

```
select * from svv_external_schemas;

esoid  | eskind | schemaname | esowner | databasename | esoptions                                                   
-------+--------+------------+---------+--------------+-------------------------------------------------------------
100133 |      1 | spectrum   |     100 | redshift     | {"IAM_ROLE":"arn:aws:iam::123456789012:role/mySpectrumRole"}
```
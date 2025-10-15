# Joining custom metadata with S3 metadata
 tables

You can analyze data across your AWS managed metadata tables and customer (self-managed) metadata
 tables. By using a standard SQL `JOIN` operator, you can query data from these multiple
 sources.

The following example SQL query finds matching records between an AWS managed journal table
 (`"journal"`) and a self-managed metadata table
 (``my_self_managed_metadata_table``). The query also filters
 information based on `CREATE` events, which indicate that a new object (or a new version of the
 object) was written to the bucket. (For more information, see the [S3 Metadata journal tables schema](metadata-tables-schema.md "metadata-tables-schema.md").)


```
SELECT *
FROM "s3tablescatalog/aws-s3"."`b_`general-purpose-bucket-name``"."journal" a
JOIN "`my_namespace`"."`my_self_managed_metadata_table`" b
ON a.bucket = b.bucket AND a.key = b.key AND a.version_id = b.version_id
WHERE a.record_type = 'CREATE';
```
The following example SQL query finds matching records between an AWS managed inventory table
 (`"inventory"`) and a self-managed metadata table
 (``my_self_managed_metadata_table``):


```
SELECT *
FROM "s3tablescatalog/aws-s3"."`b_`general-purpose-bucket-name``"."inventory" a
JOIN "`my_namespace`"."`my_self_managed_metadata_table`" b
ON a.bucket = b.bucket AND a.key = b.key AND a.version_id = b.version_id;
```

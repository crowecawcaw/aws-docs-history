

# ALTER TABLE SET TBLPROPERTIES
<a name="alter-table-set-tblproperties"></a>

Adds custom or predefined metadata properties to a table and sets their assigned values. To see the properties in a table, use the [SHOW TBLPROPERTIES](show-tblproperties.md) command.

Apache Hive [Managed tables](https://cwiki.apache.org/confluence/display/Hive/Managed+vs.+External+Tables) are not supported, so setting `'EXTERNAL'='FALSE'` has no effect.

## Synopsis
<a name="synopsis"></a>

```
ALTER TABLE table_name SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])
```

## Parameters
<a name="parameters"></a>

**SET TBLPROPERTIES ('property\_name' = 'property\_value' [ , ... ])**  
Specifies the metadata properties to add as `property_name` and the value for each as `property value`. If `property_name` already exists, its value is set to the newly specified `property_value`.  
The following predefined table properties have special uses.   



<table>
<thead>
  <tr><th>Predefined property</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><code>classification</code> </td><td>Indicates the data type for AWS Glue. Possible values are <code>csv</code>, <code>parquet</code>, <code>orc</code>, <code>avro</code>, or <code>json</code>. Tables created for Athena in the CloudTrail console add <code>cloudtrail</code> as a value for the <code>classification</code> property. For more information, see the TBLPROPERTIES section of <a href="create-table.md">CREATE TABLE</a>.</td></tr>
  <tr><td><code>has_encrypted_data</code></td><td>Indicates whether the dataset specified by <code>LOCATION</code> is CSE-KMS encrypted. For more information, see the TBLPROPERTIES section of <a href="create-table.md">CREATE TABLE</a> and <a href="creating-tables-based-on-encrypted-datasets-in-s3.md">Create tables based on encrypted datasets in Amazon S3</a>.</td></tr>
  <tr><td><code>encryption_option</code></td><td>Indicates the highest level of encryption used in the underlying dataset specified by <code>LOCATION</code>. For more information, see the TBLPROPERTIES section of <a href="create-table.md">CREATE TABLE</a> and <a href="creating-tables-based-on-encrypted-datasets-in-s3.md">Create tables based on encrypted datasets in Amazon S3</a>.</td></tr>
  <tr><td><code>kms_key</code></td><td>Indicates the AWS KMS key ARN used to encrypt and decrypt SSE-KMS or CSE-KMS data files in the underlying dataset specified by <code>LOCATION</code>. For more information, see the TBLPROPERTIES section of <a href="create-table.md">CREATE TABLE</a> and <a href="creating-tables-based-on-encrypted-datasets-in-s3.md">Create tables based on encrypted datasets in Amazon S3</a>.</td></tr>
  <tr><td><code>orc.compress</code></td><td>Specifies a compression format for data in ORC format. For more information, see <a href="orc-serde.md">ORC SerDe</a>.</td></tr>
  <tr><td><code>parquet.compression</code></td><td>Specifies a compression format for data in Parquet format. For more information, see <a href="parquet-serde.md">Parquet SerDe</a>.</td></tr>
  <tr><td><code>write.compression</code></td><td>Specifies a compression format for data in the text file or JSON formats. For the Parquet and ORC formats, use the <code>parquet.compression</code> and <code>orc.compress</code> properties respectively.</td></tr>
  <tr><td><code>compression_level</code></td><td>Specifies a compression level to use. This property applies only to ZSTD compression. Possible values are from 1 to 22. The default value is 3. For more information, see <a href="compression-support-zstd-levels.md">Use ZSTD compression levels</a>.</td></tr>
  <tr><td><code>projection.*</code></td><td>Custom properties used in partition projection that allow Athena to know what partition patterns to expect when it runs a query on a table. For more information, see <a href="partition-projection.md">Use partition projection with Amazon Athena</a>.</td></tr>
  <tr><td><code>skip.header.line.count</code></td><td>Ignores headers in data when you define a table. For more information, see <a href="lazy-simple-serde.md#lazy-simple-serde-ignoring-headers">Ignoring headers</a>.</td></tr>
  <tr><td><code>storage.location.template</code></td><td>Specifies a custom Amazon S3 path template for projected partitions. For more information, see <a href="partition-projection-setting-up.md">Set up partition projection</a>.</td></tr>
</tbody>
</table>


## Examples
<a name="examples"></a>

The following example adds a comment note to table properties.

```
ALTER TABLE orders 
SET TBLPROPERTIES ('notes'="Please don't drop this table.");
```

The following example modifies the table `existing_table` to use Parquet file format with ZSTD compression and ZSTD compression level 4.

```
ALTER TABLE existing_table 
SET TBLPROPERTIES ('parquet.compression' = 'ZSTD', 'compression_level' = 4)
```
# ALTER TABLE SET TBLPROPERTIES

Adds custom or predefined metadata properties to a table and sets their assigned values.
To see the properties in a table, use the [SHOW TBLPROPERTIES](show-tblproperties.md "show-tblproperties.md") command.

Apache Hive [Managed tables](https://cwiki.apache.org/confluence/display/Hive/Managed+vs.+External+Tables "https://cwiki.apache.org/confluence/display/Hive/Managed+vs.+External+Tables") are not supported, so setting `'EXTERNAL'='FALSE'`
has no effect.

## Synopsis

```
ALTER TABLE table_name SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])
```

## Parameters

**SET TBLPROPERTIES ('property_name' = 'property_value' [ , ... ])**

Specifies the metadata properties to add as `property_name` and
the value for each as `property value`. If
`property_name` already exists, its value is set to the newly
specified `property_value`.

The following predefined table properties have special uses.

| Predefined property         | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `classification`            | Indicates the data type for AWS Glue. Possible values are<br>`csv`, `parquet`,<br>`orc`, `avro`, or `json`.<br>Tables created for Athena in the CloudTrail console add<br>`cloudtrail` as a value for the<br>`classification` property. For more<br>information, see the TBLPROPERTIES section of [CREATE TABLE](create-table.md "create-table.md").                                                                                    |
| `has_encrypted_data`        | Indicates whether the dataset specified by<br>`LOCATION` is CSE-KMS encrypted. For more<br>information, see the TBLPROPERTIES section of [CREATE TABLE](create-table.md "create-table.md")<br>and [Create tables based on encrypted datasets in Amazon S3](creating-tables-based-on-encrypted-datasets-in-s3.md "creating-tables-based-on-encrypted-datasets-in-s3.md").                                                                |
| `encryption_option`         | Indicates the highest level of encryption used in the underlying<br>dataset specified by `LOCATION`. For more<br>information, see the TBLPROPERTIES section of [CREATE TABLE](create-table.md "create-table.md")<br>and [Create tables based on encrypted datasets in Amazon S3](creating-tables-based-on-encrypted-datasets-in-s3.md "creating-tables-based-on-encrypted-datasets-in-s3.md").                                          |
| `kms_key`                   | Indicates the AWS KMS key ARN used to encrypt and decrypt SSE-KMS or CSE-KMS<br>data files in the underlying dataset specified by `LOCATION`. For more<br>information, see the TBLPROPERTIES section of [CREATE TABLE](create-table.md "create-table.md")<br>and [Create tables based on encrypted datasets in Amazon S3](creating-tables-based-on-encrypted-datasets-in-s3.md "creating-tables-based-on-encrypted-datasets-in-s3.md"). |
| `orc.compress`              | Specifies a compression format for data in ORC format.<br>For more information, see [ORC SerDe](orc-serde.md "orc-serde.md").                                                                                                                                                                                                                                                                                                           |
| `parquet.compression`       | Specifies a compression format for data in Parquet<br>format. For more information, see [Parquet SerDe](parquet-serde.md "parquet-serde.md").                                                                                                                                                                                                                                                                                           |
| `write.compression`         | Specifies a compression format for data in the text file<br>or JSON formats. For the Parquet and ORC formats, use the<br>`parquet.compression` and<br>`orc.compress` properties<br>respectively.                                                                                                                                                                                                                                        |
| `compression_level`         | Specifies a compression level to use. This property<br>applies only to ZSTD compression. Possible values are from 1<br>to 22. The default value is 3. For more information, see<br>[Use ZSTD compression levels](compression-support-zstd-levels.md "compression-support-zstd-levels.md").                                                                                                                                              |
| `projection.*`              | Custom properties used in partition projection that allow<br>Athena to know what partition patterns to expect when it runs<br>a query on a table. For more information, see [Use partition projection with Amazon Athena](partition-projection.md "partition-projection.md").                                                                                                                                                           |
| `skip.header.line.count`    | Ignores headers in data when you define a table. For more<br>information, see [Ignoring headers](lazy-simple-serde.md#lazy-simple-serde-ignoring-headers "lazy-simple-serde.md#lazy-simple-serde-ignoring-headers").                                                                                                                                                                                                                    |
| `storage.location.template` | Specifies a custom Amazon S3 path template for projected<br>partitions. For more information, see [Set up partition projection](partition-projection-setting-up.md "partition-projection-setting-up.md").                                                                                                                                                                                                                               |

## Examples

The following example adds a comment note to table properties.

```
ALTER TABLE orders
SET TBLPROPERTIES ('notes'="Please don't drop this table.");
```

The following example modifies the table `existing_table` to use Parquet
file format with ZSTD compression and ZSTD compression level 4.

```
ALTER TABLE existing_table
SET TBLPROPERTIES ('parquet.compression' = 'ZSTD', 'compression_level' = 4)
```

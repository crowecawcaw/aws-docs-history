

# Query Linux Foundation Delta Lake tables
<a name="delta-lake-tables"></a>

Linux Foundation [Delta Lake](https://delta.io/) is a table format for big data analytics. You can use Amazon Athena to read Delta Lake tables stored in Amazon S3 directly without having to generate manifest files or run the `MSCK REPAIR` statement.

The Delta Lake format stores the minimum and maximum values per column of each data file. The Athena implementation makes use of this information to enable file-skipping on predicates to eliminate unwanted files from consideration.

## Considerations and limitations
<a name="delta-lake-tables-considerations-and-limitations"></a>

Delta Lake support in Athena has the following considerations and limitations:
+ **Tables with AWS Glue catalog only** – Native Delta Lake support is supported only through tables registered with AWS Glue. If you have a Delta Lake table that is registered with another metastore, you can still keep it and treat it as your primary metastore. Because Delta Lake metadata is stored in the file system (for example, in Amazon S3) rather than in the metastore, Athena requires only the location property in AWS Glue to read from your Delta Lake tables.
+ **V3 engine only** – Delta Lake queries are supported only on Athena engine version 3. You must ensure that the workgroup you create is configured to use Athena engine version 3.
+ **No time travel support** – There is no support for queries that use Delta Lake’s time travel capabilities.
+ **Read only** – Write DML statements like `UPDATE`, `INSERT`, or `DELETE` are not supported.
+ **Lake Formation support** – Lake Formation integration is available for Delta Lake tables with their schema in sync with AWS Glue. For more information, see [Using AWS Lake Formation with Amazon Athena](https://docs.aws.amazon.com/lake-formation/latest/dg/athena-lf.html) and [Set up permissions for a Delta Lake table](https://docs.aws.amazon.com/lake-formation/latest/dg/set-up-delta-table.html) in the *AWS Lake Formation Developer Guide*.
+ **Limited DDL support** – The following DDL statements are supported: `CREATE EXTERNAL TABLE`, `SHOW COLUMNS`, `SHOW TBLPROPERTIES`, `SHOW PARTITIONS`, `SHOW CREATE TABLE`, and `DESCRIBE`. For information on using the `CREATE EXTERNAL TABLE` statement, see the [Get started with Delta Lake tables](delta-lake-tables-getting-started.md) section.
+ **Skipping Amazon Glacier objects not supported ** – If objects in the Linux Foundation Delta Lake table are in an Amazon Glacier storage class, setting the `read_restored_glacier_objects` table property to `false` has no effect.

  For example, suppose you issue the following command:

  ```
  ALTER TABLE {{table_name}} SET TBLPROPERTIES ('read_restored_glacier_objects' = 'false')
  ```

  For Iceberg and Delta Lake tables, the command produces the error Unsupported table property key: read\_restored\_glacier\_objects. For Hudi tables, the `ALTER TABLE` command does not produce an error, but Amazon Glacier objects are still not skipped. Running `SELECT` queries after the `ALTER TABLE` command continues to return all objects.
+ **Encrypted tables** – Athena does not support natively reading CSE-KMS encrypted Delta Lake tables. This includes SELECT statements and DDL statements.

### Delta Lake versioning and Athena
<a name="delta-lake-tables-versioning"></a>

Athena does not use the [versioning](https://docs.delta.io/latest/releases.html) listed in the Delta Lake documentation. To determine whether your Delta Lake tables are compatible with Athena, consider the following two characteristics:
+ **Reader version ** – Every Delta Lake table has a reader version. Currently, this is a number between 1 and 3. Queries that include a table with a reader version that Athena does not support will fail.
+ **Table features ** – Every Delta Lake table also can declare a set of reader/writer features. Because Athena's support of Delta Lake is read-only, table writer feature compatibility does not apply. However, queries on tables with unsupported table reader features will fail.

The following table shows the Delta Lake reader versions and Delta Lake table reader features that Athena supports.



| Query type | Supported reader versions | Supported reader features | 
| --- | --- | --- | 
| DQL (SELECT statements) | <= 3 | [Column mapping](https://docs.delta.io/latest/delta-column-mapping.html), [timestampNtz](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#timestamp-without-timezone-timestampntz), [deletion vectors](https://docs.delta.io/latest/delta-deletion-vectors.html) | 
| DDL | <= 1 | Not applicable. Reader features can be declared only on tables with a reader version of 2 or greater. | 
+ For a list of Delta Lake table features, see [Valid feature names in table features](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#valid-feature-names-in-table-features) on GitHub.com
+ For a list of Delta Lake features by protocol version, see [Features by protocol version](https://docs.delta.io/latest/versioning.html#features-by-protocol-version) on GitHub.com.

To create a Delta Lake table in Athena with a reader version greater than 1, see [Synchronize Delta Lake metadata](delta-lake-tables-syncing-metadata.md).

**Topics**
+ [Considerations and limitations](#delta-lake-tables-considerations-and-limitations)
+ [Supported column data types](delta-lake-tables-supported-data-types-columns.md)
+ [Get started with Delta Lake tables](delta-lake-tables-getting-started.md)
+ [Query Delta Lake tables with SQL](delta-lake-tables-querying.md)
+ [Synchronize Delta Lake metadata](delta-lake-tables-syncing-metadata.md)
+ [Additional resources](delta-lake-tables-additional-resources.md)
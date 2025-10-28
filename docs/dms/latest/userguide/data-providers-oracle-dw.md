# Using an Oracle Data Warehouse database as a source in DMS Schema Conversion

You can use Oracle Data Warehouse databases as a migration source in DMS Schema Conversion
to convert database code objects and application code to Amazon Redshift.

For information about supported Oracle database versions, see
[Source data providers for DMS Schema Conversion](CHAP_Introduction.md#CHAP_Introduction.Sources.SchemaConversion "CHAP_Introduction.md#CHAP_Introduction.Sources.SchemaConversion").
For more information about using DMS Schema Conversion with a source Oracle database, see the
[Oracle to PostgreSQL migration step-by-step walkthrough](../sbs/schema-conversion-oracle-postgresql.md "../sbs/schema-conversion-oracle-postgresql.md").

## Privileges for using an Oracle Data Warehouse database as a source

The following privileges are required for Oracle Data Warehouse as a source:

- CONNECT
- SELECT_CATALOG_ROLE
- SELECT ANY DICTIONARY

## Oracle Data Warehouse to Amazon Redshift conversion settings

For information about editing DMS Schema Conversion settings, see
[Specifying schema conversion settings for
migration projects](schema-conversion-settings.md "schema-conversion-settings.md").

Oracle Data Warehouse to Amazon Redshift conversion settings include the following:

- **Add comments in the converted code for the action items of selected
  severity and higher**: This setting limits the number of comments with action items in the
  converted code. DMS adds comments in the converted code for action items of the selected severity
  and higher.

For example, to minimize the number of comments in your converted code, choose **Errors only**. To
include comments for all action items in your converted code, choose **All messages**.

- **The maximum number of tables for the target Amazon Redshift cluster**:
  This setting sets the maximum number of tables that DMS can apply to your target Amazon Redshift cluster. Amazon Redshift has quotas that limit the
  use tables for different cluster node types. This setting supports the following values:

      + **Auto**: DMS determines the number of tables to apply to your target Amazon Redshift cluster depending on the node type.
      + **Set a value**: Set the number of tables manually.

  DMS converts all your source tables, even if the number of tables is more than your Amazon Redshift cluster can store.
  DMS stores the converted code in your project and doesn't apply it to the target database. If
  you reach the Amazon Redshift cluster quota for the tables when you apply the converted code, DMS displays a
  warning message. Also, DMS applies tables to your target Amazon Redshift cluster until the number of tables
  reaches the limit.

For information about Amazon Redshift table quotas, see
[Quotas and limits in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-limits.md "../../../redshift/latest/mgmt/amazon-redshift-limits.md").

- **Use the UNION ALL view**: This setting lets you set the maximum number of target tables that DMS
  can create for a single source table.

Amazon Redshift doesn't support table partitioning. To emulate table partitioning and make queries run faster,
DMS can migrate each partition of your source table to a separate table in Amazon Redshift. Then, DMS creates a
view that includes data from all of the target tables it creates.

DMS automatically determines the number of partitions in your source table. Depending on the type
of source table partitioning, this number can exceed the quota for the tables that you can apply to
your Amazon Redshift cluster. To avoid reaching this quota, enter the maximum number of target tables that
DMS can create for partitions of a single source table. The default option is 368 tables, which
represents a partition for 366 days of a year, plus two tables for NO RANGE and UNKNOWN partitions.

- **Datetype format elements that you use in the Oracle code are similar
  to datetime format strings in Amazon Redshift**: Use this setting to convert data type formatting
  functions such as `TO_CHAR`, `TO_DATE`, and `TO_NUMBER` with datetime format
  elements that Amazon Redshift doesn't support. By default, DMS uses extension pack functions to emulate these unsupported
  format elements in the converted code.

The datetime format model in Oracle includes more elements than the datetime format strings in Amazon Redshift.
When your source code includes only datetime format elements that Amazon Redshift supports, set this value to avoid
extension pack functions in the converted code. Avoiding the extension functions makes the converted code
run faster.

- **Numeric format elements that you use in the Oracle code are similar
  to numeric format strings in Amazon Redshift**: Use this setting to convert numeric data type formatting
  functions that Amazon Redshift doesn't support. By default, DMS uses extension pack functions to emulate these unsupported
  format elements in the converted code.

The numeric format model in Oracle includes more elements than the numeric format strings in Amazon Redshift.
When your source code includes only numeric format elements that Amazon Redshift supports, set this value to avoid
extension pack functions in the converted code. Avoiding the extension functions makes the converted code
run faster.

- **Use the NVL function to emulate the behavior of Oracle LEAD and
  LAG functions**: If your source code doesn't use the default values for offset in the `LEAD`
  and `LAG` functions, DMS can emulate these functions with the `NVL` function. By default,
  DMS raises an action item for each use of the `LEAD`
  and `LAG` functions. Emulating these functions using `NVL` makes the converted code
  run faster.
- **Emulate the behavior of primary and unique keys**: Set this setting
  to cause DMS to emulate the behavior of primary and unique key constraints on the target Amazon Redshift cluster. Amazon Redshift
  doesn't enforce primary and unique key constraints, and uses them for informational purposes only. If your source code
  uses primary or unique key constraints, set this setting to ensure that DMS emulates their behavior.
- **Use compression encoding**: Set this setting to apply compression encoding to
  Amazon Redshift table columns. DMS assigns compression encoding automatically using the default Redshift algorithm. For information
  about compression encoding, see
  [Compression encodings](../../../redshift/latest/dg/c_Compression_encodings.md "../../../redshift/latest/dg/c_Compression_encodings.md")
  in the _Amazon Redshift Database Developer Guide_.

Amazon Redshift doesn't apply compression by default to columns that are defined as sort and distribution keys.
To apply compression to these columns, set **Use compression encoding for KEY columns**.
You can only select this option when you set **Use compression encoding**.

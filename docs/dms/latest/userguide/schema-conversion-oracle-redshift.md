# Oracle to Amazon Redshift conversion settings

The following settings apply when the source is Oracle and the
target is Amazon Redshift. You can configure these settings using the AWS Management Console or the [ModifyConversionConfiguration](../APIReference/API_ModifyConversionConfiguration.md "../APIReference/API_ModifyConversionConfiguration.md") API operation.

This topic covers settings specific to the Oracle to Amazon Redshift
conversion path. In addition to these settings, DMS Schema Conversion provides settings that
apply to all source and target pairs, such as the severity level for action-item
comments in converted SQL and the option to use generative AI for conversion. For
those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common "schema-conversion-settings.md#schema-conversion-settings-common").

Each setting shows the AWS Management Console label followed by the API and AWS CLI
parameter name in parentheses. Use the parameter name when configuring settings
with the API or AWS CLI. The settings are listed in the same order that they
appear in the AWS Management Console.

The following settings are available for the Oracle to Amazon Redshift
conversion path:

**Maximum number of tables for target**
(`RedshiftTablesNumber`)

Specifies the maximum number of tables that DMS Schema Conversion can apply to
your target Amazon Redshift cluster. Amazon Redshift has quotas that limit the number of
tables for different cluster node types.

The following table describes the valid values for this
setting.

| Console value | Behavior                                                                                                                                |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `Auto`        | DMS Schema Conversion determines the number of tables to apply to<br>your target Amazon Redshift cluster depending on the node<br>type. |
| `9900`        | Limits the target to 9,900 tables.                                                                                                      |
| `100000`      | Limits the target to 100,000 tables.                                                                                                    |

DMS Schema Conversion converts all your source tables, even if the number of
tables exceeds your Amazon Redshift cluster quota. DMS Schema Conversion stores the converted
code in your project but doesn't apply it to the target database. If
you reach the Amazon Redshift cluster quota when you apply the converted code,
DMS Schema Conversion displays a warning message.

For information about Amazon Redshift table quotas, see [Quotas and
limits in Amazon Redshift](../../../redshift/latest/mgmt/amazon-redshift-limits.md "../../../redshift/latest/mgmt/amazon-redshift-limits.md").

**Type:** String (`Auto` |
`9900` | `100000`)

**Default:**
`Auto`

**Use the UNION ALL view**
(`ConvertingSettings`)

Specifies whether DMS Schema Conversion uses a UNION ALL view to emulate table
partitioning on Amazon Redshift.

Amazon Redshift doesn't support table partitioning. To emulate table partitioning
and make queries run faster, DMS Schema Conversion can migrate each partition of your
source table to a separate table in Amazon Redshift. Then, DMS Schema Conversion creates a view
that includes data from all of the target tables using UNION ALL.

This setting supports the following values:

- `true` — DMS Schema Conversion creates separate tables for each
  partition and a UNION ALL view. When enabled, the **Max
  number of target tables** setting becomes
  available.
- `false` — DMS Schema Conversion doesn't use UNION ALL
  views.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Max number of target tables**
(`PartitionNumberLimit`)

Specifies the maximum number of target tables that DMS Schema Conversion can
create for partitions of a single source table. This setting is
available only when `ConvertingSettings` is
`true`.

Depending on the type of source table partitioning, the number of
partitions can exceed the Amazon Redshift cluster quota. To avoid reaching this
quota, enter the maximum number of target tables that DMS Schema Conversion can
create for a single source table.

The default value is 368 tables. This represents a partition for
366 days of a year, plus two tables for NO RANGE and UNKNOWN
partitions.

**Type:** Integer

**Default:**
`368`

**Use compression encoding**
(`UseCompressionEncodingZstd`)

Specifies whether DMS Schema Conversion assigns compression encoding to columns
automatically using the default Amazon Redshift algorithm.

This setting supports the following values:

- `true` — DMS Schema Conversion applies compression encoding to
  table columns.
- `false` — DMS Schema Conversion doesn't apply compression
  encoding.

For information about compression encoding, see [Compression
encodings](../../../redshift/latest/dg/c_Compression_encodings.md "../../../redshift/latest/dg/c_Compression_encodings.md") in the _Amazon Redshift Database Developer
Guide_.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Use compression encoding for KEY columns**
(`UseCompressionEncodingZstdForKeyFields`)

Specifies whether DMS Schema Conversion assigns compression encoding to
columns that are defined as sort and distribution keys. Amazon Redshift doesn't
apply compression by default to these columns. You can use this
setting only when `UseCompressionEncodingZstd` is
`true`.

This setting supports the following values:

- `true` — DMS Schema Conversion applies compression encoding to
  KEY columns.
- `false` — DMS Schema Conversion doesn't apply compression to
  KEY columns.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Emulate the behavior of primary and unique keys**
(`AutomatePrimaryKeyUniqueConstraint`)

Specifies whether DMS Schema Conversion emulates the behavior of primary and
unique key constraints on the target Amazon Redshift cluster. Amazon Redshift doesn't enforce
unique and primary key constraints and uses them for informational
purposes only. If you use these constraints in your source code, select
this option to emulate their behavior in the converted code.

This setting supports the following values:

- `true` — DMS Schema Conversion emulates primary and unique key
  constraint behavior on the target.
- `false` — DMS Schema Conversion doesn't emulate key constraint
  behavior.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Don't use extension pack functions for datetime format
elements**
(`DatetimeFormatsEqual`)

Specifies whether DMS Schema Conversion converts datetime formatting functions
(such as `TO_CHAR`, `TO_DATE`, and
`TO_NUMBER`) without using extension pack functions. The
datetime format model in Oracle includes more elements compared to
datetime format strings in Amazon Redshift. When your source code includes only
datetime format elements that Amazon Redshift supports, you don't need the
extension pack functions in the converted code.

This setting supports the following values:

- `true` — DMS Schema Conversion converts formatting functions to
  native Amazon Redshift functions without using extension pack functions.
  The converted code runs faster.
- `false` — DMS Schema Conversion uses extension pack functions to
  emulate unsupported format elements in the converted code.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Don't use extension pack functions for numeric format
elements**
(`NumberFormatsEqual`)

Specifies whether DMS Schema Conversion converts numeric formatting functions
without using extension pack functions. The numeric format model in
Oracle includes more elements compared to numeric format strings in
Amazon Redshift. When your source code includes only numeric format elements that
Amazon Redshift supports, you don't need the extension pack functions in the
converted code.

This setting supports the following values:

- `true` — DMS Schema Conversion converts numeric formatting
  functions to native Amazon Redshift functions without using extension pack
  functions. The converted code runs faster.
- `false` — DMS Schema Conversion uses extension pack functions to
  emulate unsupported format elements in the converted code.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

**Use the NVL function to emulate the behavior of Oracle LEAD and
LAG functions**
(`LeadLagFunctionsEqual`)

By default, DMS Schema Conversion raises an action item for each `LEAD`
and `LAG` function. When your source code doesn't use the
default values for offset in these functions, DMS Schema Conversion can emulate
their usage with the `NVL` function.

This setting supports the following values:

- `true` — DMS Schema Conversion emulates these functions using
  `NVL`. The converted code runs faster.
- `false` — DMS Schema Conversion raises an action item for each
  use of the `LEAD` and `LAG`
  functions.

**Type:** Boolean (`true` |
`false`)

**Default:**
`false`

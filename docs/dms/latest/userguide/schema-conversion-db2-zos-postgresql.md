

# IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion settings
<a name="schema-conversion-db2-zos-postgresql"></a>

**Important**  
DMS Schema Conversion doesn't provide a AWS Management Console experience for the IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion path. You can't create or configure these migration projects in the AWS Management Console, so you configure every setting on this page with the AWS CLI or the AWS Database Migration Service API. Because there is no AWS Management Console for this conversion path, each setting is identified only by its API and AWS CLI parameter name, not by a AWS Management Console label.

The following settings apply when the source is IBM Db2 for z/OS and the target is Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL. Configure these settings using the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation or the AWS CLI.

This topic covers settings specific to the IBM Db2 for z/OS to PostgreSQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section names `DB2ZOS_TO_POSTGRESQL`, `DB2ZOS_TO_POSTGRESQL_14`, or `DB2ZOS_TO_POSTGRESQL_15`. All three versioned sections accept the same keys. To find which section names your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

`ConvertNumberToBigint`  
Controls how IBM Db2 for z/OS numeric columns without explicit precision are mapped on the target.  
+ `false` — Numeric columns are mapped to PostgreSQL `NUMERIC`.
+ `true` — Numeric columns without explicit precision are mapped to PostgreSQL `BIGINT`. Use this when these columns hold integer values and you want the most efficient integer type.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`SchemaNameTemplate`  
Controls how the target PostgreSQL schema name is generated from the IBM Db2 for z/OS database and schema names.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-zos-postgresql.html)
**Type:** String (enum)  
**Default:** `DB_SCHEMA`

`GenerateUniqueNamesForConstraints`  
Controls whether constraint names are made unique across all schemas on the target.  
+ `true` — DMS Schema Conversion appends a hash suffix to each constraint name to guarantee uniqueness across schemas.
+ `false` — Constraint names are kept as-is, which might cause naming conflicts in multi-schema migrations.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

`KeepStatementElementsLayout`  
Controls whether the original whitespace and formatting of SQL statement elements is preserved in the converted output.  
+ `YES` — The original layout is preserved. Converted SQL retains the indentation and line breaks of the source.
+ `NO` — Statement elements are reformatted using the standard DMS Schema Conversion output style.
**Type:** String (enum: `YES` \| `NO`)  
**Default:** `YES`

`DynamicResultSetsToRefcursorsArray`  
Controls how IBM Db2 for z/OS stored procedures that return dynamic result sets are converted.  
+ `false` — Dynamic result sets are left as action items.
+ `true` — Dynamic result sets are converted using a PostgreSQL `refcursor` array, which lets the caller iterate over multiple result sets.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`ExcludeTablePartitions`  
Controls whether table partition definitions are included in the converted DDL.  
+ `false` — Table partition definitions are converted.
+ `true` — Table partition definitions are excluded from the converted DDL. Use this when your target instance doesn't need partition-level DDL or when you manage partitioning separately.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`ParttnedTabPkUnqToSecondaryIdx`  
Controls how primary key and unique constraints on partitioned tables are converted.  
+ `false` — Primary key and unique constraints are kept as constraints on the target.
+ `true` — Primary key and unique constraints on partitioned tables are converted to secondary indexes instead of constraints.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
Use the exact spelling `ParttnedTabPkUnqToSecondaryIdx` when you call the API or AWS CLI.

`PartitionCount`  
The default number of partitions to use when converting partitioned tables.  
**Type:** Integer  
**Default:** `50`

`PartitionMaxCount`  
The maximum number of partitions allowed when converting partitioned tables.  
**Type:** Integer  
**Default:** `100`

`TableSize`  
The table size threshold, in megabytes, that DMS Schema Conversion uses to determine the partitioning strategy during conversion.  
**Type:** Number (MB)  
**Default:** `100.0`

`UseEnforcePartition`  
Controls whether DMS Schema Conversion generates explicit partition enforcement clauses in the converted DDL for partitioned tables.  
+ `false` — Partition enforcement clauses are not generated.
+ `true` — DMS Schema Conversion generates partition enforcement clauses for tables larger than the `TableSize` threshold.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`UsePartitionsProportionally`  
Controls whether DMS Schema Conversion scales the number of generated partitions in proportion to table size.  
+ `false` — A fixed number of partitions is used.
+ `true` — The number of partitions increases proportionally with table size.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`StringRepresentationOfDate`  
Controls the string format used when representing IBM Db2 `DATE` values in converted code.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-zos-postgresql.html)
**Type:** String (enum)  
**Default:** `ISO`

`StringRepresentationOfTime`  
Controls the string format used when representing IBM Db2 `TIME` values in converted code.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-zos-postgresql.html)
**Type:** String (enum)  
**Default:** `ISO`

The following settings control which schemas and databases appear in the schema tree view. They affect what you can select for conversion; they don't change the converted SQL output.

`TreeSettingsHideEmpty`  
Controls whether schemas that contain no objects appear in the schema tree view.  
+ `true` — Empty schemas are hidden.
+ `false` — All schemas are shown, including empty ones.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

`TreeSettingsHideEmptyDb`  
Controls whether databases that contain no objects appear in the schema tree view.  
+ `true` — Empty databases are hidden.
+ `false` — All databases are shown, including empty ones.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

`TreeSettingsSystemSchemas`  
Controls whether system schemas appear in the schema tree view alongside user schemas.  
+ `false` — Only user schemas are shown.
+ `true` — System schemas are shown alongside user schemas.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

## Example: Configure IBM Db2 for z/OS to PostgreSQL settings
<a name="schema-conversion-db2-zos-postgresql-example"></a>

The following example sets the partition count and the date format. Apply the same settings to each section name that your project uses (check the output of [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first).

```
{
  "DB2ZOS_TO_POSTGRESQL_15": {
    "PartitionCount": 20,
    "StringRepresentationOfDate": "EUR"
  },
  "DB2ZOS_TO_POSTGRESQL_14": {
    "PartitionCount": 20,
    "StringRepresentationOfDate": "EUR"
  },
  "DB2ZOS_TO_POSTGRESQL": {
    "PartitionCount": 20,
    "StringRepresentationOfDate": "EUR"
  }
}
```
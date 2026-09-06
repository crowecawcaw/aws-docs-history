

# IBM Db2 for z/OS to Amazon RDS for Db2 conversion settings
<a name="schema-conversion-db2-zos-db2"></a>

**Important**  
DMS Schema Conversion does not provide a AWS Management Console experience for the IBM Db2 for z/OS to Amazon RDS for Db2 conversion path. You cannot create or configure these migration projects in the AWS Management Console, so you configure every setting on this page with the AWS CLI or the AWS Database Migration Service API. Because there is no AWS Management Console for this conversion path, each setting is identified only by its API and AWS CLI parameter name, not by a AWS Management Console label.

The following settings apply when the source is IBM Db2 for z/OS and the target is Amazon RDS for Db2. Configure these settings using the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation or the AWS CLI.

This topic covers settings specific to the IBM Db2 for z/OS to Amazon RDS for Db2 conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section name `DB2ZOS_TO_DB2LUW`. To find which section names your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

`ConvertNumberToBigint`  
Specifies whether DMS Schema Conversion maps IBM Db2 for z/OS numeric columns without explicit precision to `BIGINT`.  
+ `false` — Numeric columns are mapped to the default numeric type on the target.
+ `true` — Numeric columns without explicit precision are mapped to `BIGINT`. Use this when these columns hold integer values and you want the most efficient integer type.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

`SchemaNameTemplate`  
Controls how the target schema name is generated from the IBM Db2 for z/OS database and schema names.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-db2-zos-db2.html)
**Type:** String (enum)  
**Default:** `DB_SCHEMA`

You configure these settings with the JSON format that the API and AWS CLI require, as shown in the following example.

## Example: Configure IBM Db2 for z/OS to Amazon RDS for Db2 settings
<a name="schema-conversion-db2-zos-db2-example"></a>

The following example sets `SchemaNameTemplate` for the `DB2ZOS_TO_DB2LUW` section.

```
{
  "DB2ZOS_TO_DB2LUW": {
    "SchemaNameTemplate": "SCHEMA"
  }
}
```
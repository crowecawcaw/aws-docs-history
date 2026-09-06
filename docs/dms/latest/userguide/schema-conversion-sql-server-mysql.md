

# SQL Server to MySQL conversion settings
<a name="schema-conversion-sql-server-mysql"></a>

The following settings apply when the source is Microsoft SQL Server and the target is Amazon RDS for MySQL or Amazon Aurora MySQL. You can configure these settings using the AWS Management Console or the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation.

This topic covers settings specific to the SQL Server to MySQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section name `MSSQL_TO_MYSQL`. To confirm the section names that your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses. Use the parameter name when configuring settings with the API or AWS CLI.

**Create additional routines to handle open datasets** (`OpenDatasetsProcedures`)  
Specifies whether DMS Schema Conversion emulates the source SQL Server pattern of storing the output of an `EXEC` statement in a table, which MySQL does not support directly.  
+ `false` — These patterns are left as action items.
+ `true` — DMS Schema Conversion creates temporary tables and an additional procedure to emulate this pattern on the target.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

The following example shows how to configure this setting with the API or AWS CLI.

## Example: Configure SQL Server to MySQL settings
<a name="schema-conversion-sql-server-mysql-example"></a>

The following example turns on `OpenDatasetsProcedures` for the `MSSQL_TO_MYSQL` section.

```
{
  "MSSQL_TO_MYSQL": {
    "OpenDatasetsProcedures": true
  }
}
```
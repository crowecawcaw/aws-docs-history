

# Oracle to MySQL conversion settings
<a name="schema-conversion-oracle-mysql"></a>

The following settings apply when the source is Oracle and the target is Amazon RDS for MySQL or Amazon Aurora MySQL. You can configure these settings using the AWS Management Console or the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation.

This topic covers settings specific to the Oracle to MySQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section name `ORACLE_TO_MYSQL`. To confirm the section names that your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses. Use the parameter name when configuring settings with the API or AWS CLI.

**Generate row id** (`GenerateRowId`)  
Your source Oracle database can use the `ROWID` pseudocolumn. MySQL doesn't support similar functionality. This setting specifies whether DMS Schema Conversion emulates the `ROWID` pseudocolumn in the converted code.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-oracle-mysql.html)
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
For the Oracle to MySQL conversion path, `GenerateRowId` is a Boolean (`true` \| `false`) and emulates the `ROWID` pseudocolumn by using the `bigint` data type only. For the Oracle to PostgreSQL conversion path, the same setting is a string enumeration that also offers a `character varying` emulation option (`GENERATE_AS_CHARACTER_DOMAIN_TYPE`). For more information, see [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md).

By default, DMS Schema Conversion emulates Oracle conversion functions in the converted code so that the result matches the Oracle behavior. If your source code doesn't rely on Oracle-specific formatting, you can convert these functions to the native MySQL equivalents instead. Native functions run faster, so set these options to `true` only after you verify that your usage is compatible with MySQL.

**Use a native MySQL TO\_CHAR function** (`ToCharFunctionOracle`)  
Specifies whether DMS Schema Conversion converts Oracle `TO_CHAR` function calls to the native MySQL function instead of emulating the Oracle-specific formatting.  
+ `false` — DMS Schema Conversion emulates the Oracle-specific formatting of `TO_CHAR` in the converted code.
+ `true` — Calls are converted to the native MySQL `TO_CHAR` function. Use this when your source code doesn't use Oracle-specific format strings.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Use a native MySQL TO\_DATE function** (`ToDateFunctionOracle`)  
Specifies whether DMS Schema Conversion converts Oracle `TO_DATE` function calls to the native MySQL function instead of emulating the Oracle-specific formatting.  
+ `false` — DMS Schema Conversion emulates the Oracle-specific formatting of `TO_DATE` in the converted code.
+ `true` — Calls are converted to the native MySQL `TO_DATE` function. Use this when your source code doesn't use Oracle-specific format strings.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Use a native MySQL TO\_NUMBER function** (`ToNumber`)  
Specifies whether DMS Schema Conversion converts Oracle `TO_NUMBER` function calls to the native MySQL function instead of emulating the Oracle-specific formatting.  
+ `false` — DMS Schema Conversion emulates the Oracle-specific formatting of `TO_NUMBER` in the converted code.
+ `true` — Calls are converted to the native MySQL `TO_NUMBER` function. Use this when your source code doesn't use Oracle-specific format strings.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Improve the performance of the converted code where the database and applications use the same time zone** (`ToTimeZone`)  
Specifies whether DMS Schema Conversion emulates time zones in the converted code.  
+ `true` — DMS Schema Conversion doesn't emulate time zones. Use this when your database and applications use the same time zone. The converted code runs faster.
+ `false` — DMS Schema Conversion emulates time zones in the converted code.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

## Example: Configure Oracle to MySQL settings
<a name="schema-conversion-oracle-mysql-example"></a>

The following example converts Oracle conversion functions to their native MySQL equivalents for the `ORACLE_TO_MYSQL` section.

```
{
  "ORACLE_TO_MYSQL": {
    "ToCharFunctionOracle": true,
    "ToDateFunctionOracle": true,
    "ToNumber": true
  }
}
```
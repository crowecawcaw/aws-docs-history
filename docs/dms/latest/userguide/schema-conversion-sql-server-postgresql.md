

# SQL Server to PostgreSQL conversion settings
<a name="schema-conversion-sql-server-postgresql"></a>

The following settings apply when the source is Microsoft SQL Server and the target is Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL. You can configure these settings using the AWS Management Console or the [`ModifyConversionConfiguration`](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation.

This topic covers settings specific to the SQL Server to PostgreSQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section names `MSSQL_TO_POSTGRESQL`, `MSSQL_TO_POSTGRESQL_14`, or `MSSQL_TO_POSTGRESQL_15`. All three versioned sections accept the same keys. To find which section names your project uses, call [`DescribeConversionConfiguration`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses. Use the parameter name when configuring settings with the API or AWS CLI.

Settings that control how source SQL Server metadata — object names, schema structure, and index definitions — are handled during conversion.

**Treat source database object names as case sensitive** (`CaseSensitivityNames`)  
Controls how object names (tables, columns, procedures, and so on) are handled during conversion.  
+ `true` — Object names are preserved in their original case and wrapped in double-quote identifiers (for example, `"MyTable"`). Use this when your application references objects using mixed-case names.
+ `false` — Object names are folded to lower case without quoting (for example, `mytable`). This matches the default PostgreSQL case-folding behaviour.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Generate unique names for indexes** (`UniqueIndexGeneration`)  
Controls whether DMS Schema Conversion generates unique index names across the target PostgreSQL schema. In SQL Server, indexes can share the same name across different tables. In PostgreSQL, all index names within a schema must be unique.  
+ `true` — DMS Schema Conversion generates unique names for all indexes, appending a suffix where necessary to avoid collisions. Use this when your source schema has indexes with the same name on different tables.
+ `false` — Index names are preserved as-is from the source. If the same index name exists on multiple tables, deployment to PostgreSQL may fail with a duplicate name error.
**Type:** Boolean (`true` \| `false`)  
**Default:** `true`

**Convert procedures to functions** (`ConvertProceduresToFunction`)  
Controls whether stored procedures are converted to PostgreSQL functions or procedures.  
+ `false` — Procedures are converted to PostgreSQL `PROCEDURE` objects (requires PostgreSQL 11 or later).
+ `true` — Procedures that return a result set are converted to PostgreSQL `FUNCTION` objects. Use this when your application reads a result set from a procedure call, or when targeting PostgreSQL 10 or earlier.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Create additional routines to handle open datasets** (`OpenDatasetsProcedures`)  
Controls how procedures that store the output of `EXEC` into a table are converted.  
+ `false` — These patterns are left as action items.
+ `true` — DMS Schema Conversion creates temporary tables and an additional procedure to emulate this pattern on the target.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Schema names** (`SchemaNameTemplate`)  
Controls how the target PostgreSQL schema name is generated from the SQL Server two-part naming convention (database \+ schema).      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-sql-server-postgresql.html)
**Type:** String (enum)  
**Default:** `DB_SCHEMA`

Settings that control how SQL Server code — identifiers, parameters, data types, and unsupported functions — is handled during conversion.

**Keep object names in the same case** (`AvoidCastingToLowerCase`)  
Controls whether DMS Schema Conversion adds automatic `LOWER()` casts around identifiers in converted code.  
+ `false` — DMS Schema Conversion adds `LOWER()` casts where needed to normalise case comparisons.
+ `true` — No automatic `LOWER()` casts are added. Use this when your PostgreSQL database uses the `citext` extension or a case-insensitive collation to handle comparisons natively.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
This setting has no effect when `UseCitextForAllStringDatatypes` is enabled. When all string types are mapped to `CITEXT`, case-insensitive comparison is handled natively by the type itself, so no `LOWER()` casts are generated regardless of this setting.

**Keep original parameter names** (`KeepOriginalParameterManes`)  
Controls whether original parameter names from T-SQL routines are preserved in the converted PostgreSQL routine signature.  
+ `false` — Parameters may be renamed to avoid conflicts with PostgreSQL reserved words or naming conventions.
+ `true` — Original parameter names are kept verbatim. Use this when your application calls routines using named parameter syntax (for example, `my_proc(param_name => value)`).
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
The API parameter name is `KeepOriginalParameterManes` (ending in *Manes*, not *Names*). Use this exact spelling when calling the API or AWS CLI. Using `KeepOriginalParameterNames` will not work.

**Use CITEXT for all string datatypes** (`UseCitextForAllStringDatatypes`)  
Controls the target data type for all character columns and parameters.  
+ `false` — Character types (`CHAR`, `VARCHAR`, `NCHAR`, `NVARCHAR`) are mapped to the corresponding PostgreSQL types.
+ `true` — All character types are mapped to `CITEXT` (case-insensitive text). Use this when migrating from a case-insensitive SQL Server collation and you want to preserve that behaviour in PostgreSQL without modifying queries.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
When this setting is enabled, DMS Schema Conversion automatically adds `CREATE EXTENSION IF NOT EXISTS citext;` to the converted schema scripts (both when applying to the target and when saving to a file). However, the `citext` module must be available in your target PostgreSQL database before you apply the converted schema.  
When `UseCitextForAllStringDatatypes` is enabled, the **Keep object names in the same case** (`AvoidCastingToLowerCase`) setting has no effect, because `CITEXT` handles case-insensitive comparison natively.

**Convert unsupported built-in objects to stub objects** (`ConvUnsupportedBuiltinsToStubs`)  
Controls what happens when DMS Schema Conversion encounters a T-SQL built-in function that has no direct PostgreSQL equivalent.  
+ `false` — The unsupported function is left as an action item in the assessment report. The converted object is marked as requiring manual review.
+ `true` — The unsupported function is replaced with a stub function that has the same signature but raises a runtime error. The converted object compiles successfully, letting you deploy and test the rest of the schema before addressing individual stubs. Stub functions generate migration issue 7822.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Create stub objects in a separate schema** (`CreateStubsInSeparateSchema`)  
Controls where stub objects are placed when `ConvUnsupportedBuiltinsToStubs` is enabled.  
+ `false` — Stub objects are created in the same schema as the calling objects.
+ `true` — Stub objects are placed in a dedicated `aws_sqlserver_stub` schema on the target. Use this to keep stub code isolated from converted application objects.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

## Example: configure SQL Server to PostgreSQL settings
<a name="schema-conversion-sql-server-postgresql-example"></a>

The following example sets `SchemaNameTemplate`, `ConvertProceduresToFunction`, and `UseCitextForAllStringDatatypes`. Apply the same settings to each section name that your project uses (check the output of [`DescribeConversionConfiguration`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first).

```
{
  "MSSQL_TO_POSTGRESQL_15": {
    "SchemaNameTemplate": "SCHEMA",
    "ConvertProceduresToFunction": true,
    "UseCitextForAllStringDatatypes": true
  },
  "MSSQL_TO_POSTGRESQL_14": {
    "SchemaNameTemplate": "SCHEMA",
    "ConvertProceduresToFunction": true,
    "UseCitextForAllStringDatatypes": true
  },
  "MSSQL_TO_POSTGRESQL": {
    "SchemaNameTemplate": "SCHEMA",
    "ConvertProceduresToFunction": true,
    "UseCitextForAllStringDatatypes": true
  }
}
```
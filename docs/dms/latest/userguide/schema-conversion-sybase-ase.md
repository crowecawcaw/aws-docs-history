

# SAP ASE (Sybase ASE) to PostgreSQL conversion settings
<a name="schema-conversion-sybase-ase"></a>

The following settings apply when the source is SAP ASE (Sybase ASE) and the target is Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL. You can configure these settings using the AWS Management Console or the [ModifyConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyConversionConfiguration.html) API operation.

This topic covers settings specific to the SAP ASE to PostgreSQL conversion path. In addition to these settings, DMS Schema Conversion provides settings that apply to all source and target pairs, such as the severity level for action-item comments in converted SQL and the option to use generative AI for conversion. For those settings, see [Common conversion settings](schema-conversion-settings.md#schema-conversion-settings-common).

When you use the API or AWS CLI, specify conversion path settings under the section names `SYBASE_ASE_TO_POSTGRESQL`, `SYBASE_ASE_TO_POSTGRESQL_14`, or `SYBASE_ASE_TO_POSTGRESQL_15`. All three versioned sections accept the same keys. To find which section names your project uses, call [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first and update only the sections present in the response.

Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses. Use the parameter name when configuring settings with the API or AWS CLI.

**Target engine version** (`SYBASE_ASE_TO_POSTGRESQL_target_engine_version`)  
Choose the engine version for your target database. This setting is the PostgreSQL major version feature set that DMS Schema Conversion targets for conversion, and it determines which versioned settings section DMS Schema Conversion applies (`SYBASE_ASE_TO_POSTGRESQL_14` or `SYBASE_ASE_TO_POSTGRESQL_15`). The value `15` targets the features of PostgreSQL 15 and later versions, and `14` targets the features of PostgreSQL 14, so your target database can run a later version than the value you choose (for example, a value of `15` for a PostgreSQL 16 target). Unlike the other settings on this page, this setting isn't stored in a conversion path section. Instead, it's stored in the top-level `Conversion version` section, as shown in the following example.  

```
{
  "Conversion version": {
    "SYBASE_ASE_TO_POSTGRESQL_target_engine_version": "15"
  }
}
```
**Type:** String (`14` \| `15`)  
**Default:** `15`

Settings that control how source SAP ASE metadata — object names, schema structure, and index definitions — is handled during conversion.

**Treat source database object names as case sensitive** (`CaseSensitivityNames`)  
Specifies whether DMS Schema Conversion treats source object names as case sensitive during conversion.  
+ `true` — DMS Schema Conversion preserves object names in their original case and wraps them in double-quote identifiers (for example, `"MyTable"`). Use this when your application references objects using mixed-case names.
+ `false` — DMS Schema Conversion folds object names to lower case without quoting (for example, `mytable`).
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Generate unique names for indexes** (`GenerateUniqueNamesForIndexes`)  
Specifies whether DMS Schema Conversion generates unique index names across the target schema. In SAP ASE, you can create indexes with the same name on different tables, but PostgreSQL requires all index names within a schema to be unique.  
+ `false` — DMS Schema Conversion preserves index names as-is from the source. If the same index name exists on multiple tables, deployment to PostgreSQL might fail with a duplicate name error.
+ `true` — DMS Schema Conversion adds a prefix to index names to guarantee uniqueness across the schema. Use this when your source schema has indexes with the same name on different tables.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

**Schema names** (`SchemaNameTemplate`)  
Controls how the target PostgreSQL schema name is generated from the SAP ASE two-part naming convention (database \+ schema).      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-sybase-ase.html)
**Type:** String (enum)  
**Default:** `DB_SCHEMA`

Settings that control how SAP ASE code — identifiers and case-insensitive operations — is handled during conversion.

**Avoid casting operands to lowercase for case-insensitive operations** (`AvoidCastingToLowerCase`)  
Specifies whether DMS Schema Conversion adds automatic `LOWER()` casts around operands for case-insensitive operations in the converted code.  
+ `false` — DMS Schema Conversion adds `LOWER()` casts to normalize operands before case-insensitive comparisons.
+ `true` — DMS Schema Conversion doesn't add automatic `LOWER()` casts. Use this when your PostgreSQL database uses the `citext` extension or a case-insensitive collation to handle comparisons natively.
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`

## Example: configure SAP ASE to PostgreSQL settings
<a name="schema-conversion-sybase-ase-example"></a>

The following example sets `CaseSensitivityNames` and `SchemaNameTemplate`. Apply the same settings to each section name that your project uses (check the output of [DescribeConversionConfiguration](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeConversionConfiguration.html) first).

```
{
  "SYBASE_ASE_TO_POSTGRESQL_15": {
    "CaseSensitivityNames": true,
    "SchemaNameTemplate": "SCHEMA"
  },
  "SYBASE_ASE_TO_POSTGRESQL_14": {
    "CaseSensitivityNames": true,
    "SchemaNameTemplate": "SCHEMA"
  },
  "SYBASE_ASE_TO_POSTGRESQL": {
    "CaseSensitivityNames": true,
    "SchemaNameTemplate": "SCHEMA"
  }
}
```
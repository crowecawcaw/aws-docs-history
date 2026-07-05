# Specifying schema conversion settings for migration projects

Schema conversion settings let you customize how DMS Schema Conversion transforms source
database objects into target-compatible SQL. Settings that apply to all conversion
paths are documented in the sections below. For settings specific to a conversion
path, see the corresponding topic in the navigation.

## Common conversion settings

The following two settings apply to every conversion path. Each
setting shows the AWS Management Console label followed by the API and AWS CLI parameter name
in parentheses.

**Comments in converted SQL code**
(`ShowSeverityLevelInSql`)

Controls the minimum severity level of action items for which DMS Schema Conversion
inserts a comment into the converted SQL output. Only action items at or
above the chosen level receive a comment.

**Values:**

| Console label           | API/CLI value                                      | Action items that receive a comment                     |
| ----------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| **Errors only**         | `CRITICAL`                                         | Critical errors that prevent the object from<br>working |
| **Errors and warnings** | `HIGH`                                             | Critical errors and high-severity warnings              |
| **All messages**        | `MEDIUM`                                           | Critical, high, and medium-severity action<br>items     |
| `LOW`                   | All action items except informational<br>notes     |
| `INFO`                  | All action items, including informational<br>notes |

**Default:**
`CRITICAL`

**Use generative AI to convert schemas**
(`EnableGenAiConversion`)

When enabled, DMS Schema Conversion uses a generative AI model to convert SQL
constructs that rule-based logic cannot handle. This reduces the number
of action items that require manual resolution.

**Type:** Boolean
(`true` | `false`)

**Default:**
`false`

###### Note

Generative AI features in DMS Schema Conversion are available only in
supported AWS Regions. If your primary Region is not supported,
this setting has no effect. For a list of supported Regions and
cross-region inference routing, see [Cross-region inference in DMS Schema Conversion](CHAP_Security.DataProtection.CrossRegionInference.md#CHAP_Security.DataProtection.CrossRegionInference.SchemaConversion "CHAP_Security.DataProtection.CrossRegionInference.md#CHAP_Security.DataProtection.CrossRegionInference.SchemaConversion").

###### Note

Generative AI conversion is supported only for specific
conversion paths. For a list of supported paths and the SQL
elements within scope, see [Converting database objects with generative AI](schema-conversion-convert.databaseobjects.md "schema-conversion-convert.databaseobjects.md").

## Modifying settings

###### Note

You cannot modify settings while any schema conversion operation is running
on the same project.

AWS Management Console

1. Sign in to the AWS Management Console and open the AWS DMS console at
   [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/ "https://console.aws.amazon.com/dms/v2/").
2. In the navigation pane, choose **Migration
   projects**.
3. Choose your migration project.
4. Choose **Schema conversion**, then choose
   **Launch schema conversion**.
5. In the schema conversion view, choose
   **Settings**.
6. In the **Conversion** section, change the
   settings.
7. Choose **Apply**, then choose
   **Schema conversion** to return to the
   schema view.

AWS CLI
Use the [`modify-conversion-configuration`](../../../cli/latest/reference/dms/modify-conversion-configuration.md "../../../cli/latest/reference/dms/modify-conversion-configuration.md") command.
Pass settings as a nested JSON object to the
`--conversion-configuration` parameter. Use section
names as the top-level keys, such as `"Common project
 settings"` for common settings or a conversion path specific
name such as `"MSSQL_TO_POSTGRESQL_15"`. A flat JSON
structure without section names as top-level keys is not valid.

###### Note

You can pass the conversion configuration to
`--conversion-configuration` in the following ways.
This is a standard AWS CLI feature that works with any string
parameter.

- **Inline:**
  `--conversion-configuration '{"Common project
 settings":{...}}'` (use single quotes to avoid
  escaping the JSON double quotes)
- **Relative path:**
  `--conversion-configuration
 file://settings.json`
- **Absolute path:**
  `--conversion-configuration
 file:///tmp/settings.json`

The full JSON structure looks like this:

```
{
  "Common project settings": {
    "ShowSeverityLevelInSql": "CRITICAL",
    "EnableGenAiConversion": false
  },
  "`conversion_path_section_name`": {
    "SettingName": value,
    ...
  }
}
```

Include only the sections and keys you want to change. The [`modify-conversion-configuration`](../../../cli/latest/reference/dms/modify-conversion-configuration.md "../../../cli/latest/reference/dms/modify-conversion-configuration.md") command
merges the supplied values with the existing configuration. The
following example sets `ShowSeverityLevelInSql` to
`HIGH`:

```
aws dms modify-conversion-configuration \
      --migration-project-identifier `migration_project_arn` \
      --conversion-configuration '{
        "Common project settings": {
          "ShowSeverityLevelInSql": "HIGH"
        }
      }'
```

###### Topics

- [Oracle to MySQL conversion settings](schema-conversion-oracle-mysql.md "schema-conversion-oracle-mysql.md")
- [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md "schema-conversion-oracle-postgresql.md")
- [SQL Server to MySQL conversion settings](schema-conversion-sql-server-mysql.md "schema-conversion-sql-server-mysql.md")
- [SQL Server to PostgreSQL conversion settings](schema-conversion-sql-server-postgresql.md "schema-conversion-sql-server-postgresql.md")
- [PostgreSQL to MySQL conversion settings](schema-conversion-postgresql-mysql.md "schema-conversion-postgresql-mysql.md")
- [IBM Db2 for LUW to Amazon RDS for PostgreSQL conversion settings](schema-conversion-db2-luw-postgresql.md "schema-conversion-db2-luw-postgresql.md")
- [IBM Db2 for z/OS to Amazon RDS for Db2 conversion settings](schema-conversion-db2-zos-db2.md "schema-conversion-db2-zos-db2.md")
- [IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion settings](schema-conversion-db2-zos-postgresql.md "schema-conversion-db2-zos-postgresql.md")
- [SAP ASE (Sybase ASE) to PostgreSQL conversion settings](schema-conversion-sybase-ase.md "schema-conversion-sybase-ase.md")

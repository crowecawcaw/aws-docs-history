

# Specifying schema conversion settings for migration projects
<a name="schema-conversion-settings"></a>

Schema conversion settings let you customize two things: how DMS Schema Conversion converts source database objects into target-compatible SQL, and which schemas and databases appear in the schema conversion view. Settings that apply to all conversion paths are documented in the sections below. For settings specific to a conversion path, see the corresponding topic in the navigation.

## Common conversion settings
<a name="schema-conversion-settings-common"></a>

The following two settings apply to every conversion path. Each setting shows the AWS Management Console label followed by the API and AWS CLI parameter name in parentheses.

**Comments in converted SQL code** (`ShowSeverityLevelInSql`)  
Controls the minimum severity level of action items for which DMS Schema Conversion inserts a comment into the converted SQL output. Only action items at or above the chosen level receive a comment.  
**Values:**      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html)
**Default:** `CRITICAL`

**Use generative AI to convert schemas** (`EnableGenAiConversion`)  
When enabled, DMS Schema Conversion uses a generative AI model to convert SQL constructs that rule-based logic cannot handle. This reduces the number of action items that require manual resolution.  
**Type:** Boolean (`true` \| `false`)  
**Default:** `false`  
Generative AI features in DMS Schema Conversion are available only in supported AWS Regions. If your primary Region is not supported, this setting has no effect. For a list of supported Regions and cross-region inference routing, see [Cross-region inference in DMS Schema Conversion](CHAP_Security.DataProtection.CrossRegionInference.md#CHAP_Security.DataProtection.CrossRegionInference.SchemaConversion).
Generative AI conversion is supported only for specific conversion paths. For a list of supported paths and the SQL elements within scope, see [Converting database objects with generative AI](schema-conversion-convert.databaseobjects.md).

## Tree view settings
<a name="schema-conversion-settings-treeview"></a>

Tree view settings differ from the other schema conversion settings. They do not change the converted SQL. Instead, they control which schemas and databases appear in the source and target database panes of the schema conversion view. This determines what you can select for conversion. Tree view settings apply to every conversion path.

**Important**  
You can configure tree view settings only in the AWS Management Console. You cannot set them with the AWS Database Migration Service API or the AWS CLI.

You configure tree view settings in the **Tree view** section of the **Settings** page. To open this page, follow the AWS Management Console steps in [Modifying settings](#schema-conversion-settings-cli). Then choose **Tree view**. You set each of the following controls independently for the source pane and the target pane.

**Hide empty schemas**  
Hides schemas that contain no objects. Select this control to remove empty schemas from the pane. This lets you focus on the schemas that have objects to convert.  
**Default:** Selected. DMS Schema Conversion hides empty schemas unless you clear this control.

**System databases or schemas**  
Hides the system databases or schemas that you choose. DMS Schema Conversion provides a list of the common system objects for your source or target engine. Select the ones that you want to hide.  
For a PostgreSQL source, the list includes objects such as `pg_catalog` and `information_schema`. For a MySQL target, the list includes objects such as `mysql` and `performance_schema`.  
**Default:** DMS Schema Conversion preselects the standard system objects for your source or target engine.

**User-defined databases or schemas**  
Hides the databases or schemas whose names you enter. Separate two or more names with a comma. Use the percent sign (%) as a wildcard to match any number of characters in a database or schema name.  
**Default:** None.

## Modifying settings
<a name="schema-conversion-settings-cli"></a>

**Note**  
You cannot modify settings while any schema conversion operation is running on the same project.

------
#### [ AWS Management Console ]

1. Sign in to the AWS Management Console and open the AWS DMS console at [https://console.aws.amazon.com/dms/v2/](https://console.aws.amazon.com/dms/v2/).

1. In the navigation pane, choose **Migration projects**.

1. Choose your migration project.

1. Choose **Schema conversion**, then choose **Launch schema conversion**.

1. In the schema conversion view, choose **Settings**.

1. In the **Conversion** section, change the settings.

1. Choose **Apply**, then choose **Schema conversion** to return to the schema view.

------
#### [ AWS CLI ]

Use the [`modify-conversion-configuration`](https://docs.aws.amazon.com/cli/latest/reference/dms/modify-conversion-configuration.html) command. Pass settings as a nested JSON object to the `--conversion-configuration` parameter. Use section names as the top-level keys, such as `"Common project settings"` for common settings or a conversion path specific name such as `"MSSQL_TO_POSTGRESQL_15"`. A flat JSON structure without section names as top-level keys is not valid.

**Note**  
You can pass the conversion configuration to `--conversion-configuration` in the following ways. This is a standard AWS CLI feature that works with any string parameter.  
**Inline:** `--conversion-configuration '{"Common project settings":{...}}'` (use single quotes to avoid escaping the JSON double quotes)
**Relative path:** `--conversion-configuration file://settings.json`
**Absolute path:** `--conversion-configuration file:///tmp/settings.json`

The full JSON structure looks like this:

```
{
  "Common project settings": {
    "ShowSeverityLevelInSql": "CRITICAL",
    "EnableGenAiConversion": false
  },
  "{{conversion_path_section_name}}": {
    "SettingName": value,
    ...
  }
}
```

Include only the sections and keys you want to change. The [`modify-conversion-configuration`](https://docs.aws.amazon.com/cli/latest/reference/dms/modify-conversion-configuration.html) command merges the supplied values with the existing configuration. The following example sets `ShowSeverityLevelInSql` to `HIGH`:

```
aws dms modify-conversion-configuration \
      --migration-project-identifier {{migration_project_arn}} \
      --conversion-configuration '{
        "Common project settings": {
          "ShowSeverityLevelInSql": "HIGH"
        }
      }'
```

------

**Topics**
+ [Common conversion settings](#schema-conversion-settings-common)
+ [Tree view settings](#schema-conversion-settings-treeview)
+ [Modifying settings](#schema-conversion-settings-cli)
+ [Oracle to MySQL conversion settings](schema-conversion-oracle-mysql.md)
+ [Oracle to PostgreSQL conversion settings](schema-conversion-oracle-postgresql.md)
+ [Oracle to Amazon Redshift conversion settings](schema-conversion-oracle-redshift.md)
+ [SQL Server to MySQL conversion settings](schema-conversion-sql-server-mysql.md)
+ [SQL Server to PostgreSQL conversion settings](schema-conversion-sql-server-postgresql.md)
+ [MySQL to PostgreSQL conversion settings](schema-conversion-mysql-postgresql.md)
+ [PostgreSQL to MySQL conversion settings](schema-conversion-postgresql-mysql.md)
+ [IBM Db2 for LUW to Amazon RDS for PostgreSQL conversion settings](schema-conversion-db2-luw-postgresql.md)
+ [IBM Db2 for z/OS to Amazon RDS for Db2 conversion settings](schema-conversion-db2-zos-db2.md)
+ [IBM Db2 for z/OS to Amazon RDS for PostgreSQL conversion settings](schema-conversion-db2-zos-postgresql.md)
+ [SAP ASE (Sybase ASE) to PostgreSQL conversion settings](schema-conversion-sybase-ase.md)
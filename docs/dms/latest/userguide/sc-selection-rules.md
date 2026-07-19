# Selection rules in DMS Schema Conversion

DMS Schema Conversion converts database schemas from one engine to another. You use
_selection rules_ to control which database objects DMS Schema Conversion acts on
during operations such as assessment, conversion, and export. A selection rules is a JSON
object that you pass through the `SelectionRules` parameter (or
`--selection-rules` in the AWS CLI). Without a selection rule, an operation
has nothing to act on. With a rule, you can scope the operation to a single object, an
entire schema, an entire database (for Microsoft SQL Server and SAP ASE (Sybase ASE) sources), or
a group of objects matched by a pattern.

###### Note

When you use the AWS Management Console, DMS Schema Conversion constructs selection rules
automatically based on your choices in the migration project UI. You only need to
write selection rules directly when using the DMS Schema Conversion API or AWS CLI.

You use the same rule shape on both the source and target sides of a migration
project. The `server-name` field in the object locator specifies whether the
rule targets the source data provider or the target data provider. A single migration
project commonly uses both kinds of rules: source rules for assessment and conversion;
target rules for SQL export.

## Selection rules format

A selection rules document is a JSON object with a single `rules`
array. Each entry in the array is one rule, and every rule must contain all of the
following fields.

| Parameter        | Value                                                  | Description                                                                                                                                                                                               |
| ---------------- | ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rule-type`      | `selection`                                            | A value that identifies the type of rule.<br>For all selection rules, set this to `selection`.<br>Required parameter.                                                                                     |
| `rule-id`        | A numeric (integer) value.                             | A unique numeric identifier for the rule.<br>Required parameter.                                                                                                                                          |
| `rule-name`      | An alphanumeric value.                                 | A unique name to identify the rule.<br>Required parameter.                                                                                                                                                |
| `rule-action`    | `explicit`, `include`, or `exclude`                    | A value that determines how the object locator is interpreted. See [Rule actions](#dms-sc-selection-rule-actions "#dms-sc-selection-rule-actions").<br>Required parameter.                                |
| `object-locator` | A JSON object containing engine-specific locator keys. | An object that identifies the database objects the rule applies to. See [Object locator hierarchy](#dms-sc-selection-rule-object-locator "#dms-sc-selection-rule-object-locator").<br>Required parameter. |

The following minimal example targets one schema on a source server.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`"
      }
    }
  ]
}
```

###### Note

When using the AWS CLI, you can pass the selection rules in the following
ways. This is a standard AWS CLI feature that works with any string
parameter.

- Inline: `--selection-rules '{"rules":[...]}'` (use single
  quotes to avoid escaping the JSON double quotes)
- Relative path: `--selection-rules file://example-rules.json`
- Absolute path: `--selection-rules file:///tmp/example-rules.json`

All field values inside `object-locator` must be non-empty strings. An
empty string (for example, `"schema-name": ""`) is rejected with the error.

###### Note

The `database-name` key is valid only for Microsoft SQL Server and SAP ASE (Sybase ASE)
sources. Sending `database-name` in a locator for any other source
engine is rejected as an unsupported key.

## Writing rules

### Object locator hierarchy

The `object-locator` identifies one or more database objects through a
hierarchy of engine-specific keys. Each key narrows the scope; omit a lower-level key
to widen the scope. The hierarchy depends on the source engine:

- **Microsoft SQL Server and SAP ASE (Sybase ASE)** —
  `server-name` `→` `database-name` `→` `schema-name` `→` object-level
  key (for example, `table-name`). These engines have an extra
  `database-name` level between the server and the schema.
- **All other engines** (Oracle, IBM Db2 for z/OS,
  and all target engines: PostgreSQL, Aurora PostgreSQL, MySQL, Aurora MySQL, and IBM Db2
  LUW) — `server-name` `→` `schema-name` `→` object-level
  key. These engines have no `database-name` level; the schema is the
  top container directly under `server-name`.

The following example selects one specific Microsoft SQL Server table.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "`schema_name`",
        "table-name": "`table_name`"
      }
    }
  ]
}
```

To widen the scope to the entire schema, omit the leaf-level key. The rule then
applies to all addressable object types in that schema, including tables, views,
procedures, functions, sequences, and any other objects the source engine
exposes.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "`schema_name`"
      }
    }
  ]
}
```

The locator keys you can use depend on the source or target engine. For the full
key reference per engine, see [Object locator keys by database](#dms-sc-selection-rule-locator-keys "#dms-sc-selection-rule-locator-keys").

### Source rules and target rules

No explicit `rule-type` field marks a rule as
"source" or "target". You control the distinction entirely through the
`server-name` value in the `object-locator`: if
`server-name` matches your **source**
data provider, the rule targets the source metadata tree; if it matches your
**target** data provider, the rule targets the
target metadata tree.

For `server-name` you can use either:

- The **Server Name** value configured in the
  data provider. This is typically a hostname or IP address, but must match the
  value stored in the data provider exactly — not a different DNS name or IP that
  resolves to the same machine.
- The **resource ID** of the data provider —
  the last segment of its ARN (for example, if the ARN is
  `arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS`,
  the resource ID is `EXAMPLEABCDEFGHIJKLMNOPQRS`).

### Rule actions

Use the `rule-action` field to specify how DMS Schema Conversion interprets the
values inside the object locator. You can use wildcards only with
`include` and `exclude`.

| Value        | Behavior                                                                                                                                                                                                                                                                                                      | When to use it                                                          |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| `"include"`  | Selects all objects whose names match the pattern. Supports<br>`%` (any sequence of zero or more characters) and `_`<br>(any single character) as wildcards. Use `[_]` to match a<br>literal underscore and `[%]` to match a literal percent<br>character.                                                    | Use to match a group of objects with a shared naming<br>pattern.        |
| `"exclude"`  | Removes objects from the set already selected by preceding<br>`include` rules. An `exclude` rule with no preceding<br>`include` has no effect.                                                                                                                                                                | Use to carve out exceptions from a broader<br>`include`.                |
| `"explicit"` | Selects exactly the named object. Every locator value, including<br>`schema-name`, `database-name`, and any leaf key such<br>as `table-name` or `scalar-function-name`, is matched<br>as a literal string. Wildcard characters such as `%`,<br>`_`, `[`, and `]` have no special meaning<br>under `explicit`. | Use when you know the exact name of every object you want to act<br>on. |

###### Note

Some operations only accept `"explicit"` rules and do not support
`"include"` or `"exclude"`. Check the [AWS API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
for the specific operation to confirm which rule actions it supports.

## Object locator reference

### Object locator keys by database

The following tabs show the locator keys for each supported database.

SQL Server

| Key                          | Selects                                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`                | The server.                                                                                                                                    |
| `database-name`              | A database on the server.                                                                                                                      |
| `schema-name`                | A schema within the database.                                                                                                                  |
| `table-name`                 | A table by default, or a view when used with `"table-type": "view"`.                                                                           |
| `table-type`                 | `"table"` (default) or `"view"`.                                                                                                               |
| `procedure-name`             | A stored procedure.                                                                                                                            |
| `scalar-function-name`       | A scalar-valued function.                                                                                                                      |
| `table-valued-function-name` | A table-valued function.                                                                                                                       |
| `inline-function-name`       | An inline function.                                                                                                                            |
| `aggregate-function-name`    | An aggregate function.                                                                                                                         |
| `synonym-name`               | A synonym.                                                                                                                                     |
| `sequence-name`              | A sequence.                                                                                                                                    |
| `type-name`                  | A type.                                                                                                                                        |
| `table-type-name`            | A table type.                                                                                                                                  |
| `user-defined-type-name`     | A user-defined type.                                                                                                                           |
| `xml-schema-collection-name` | An XML schema collection.                                                                                                                      |
| `statement-name`             | A statement.                                                                                                                                   |
| `category-name`              | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

Oracle

| Key                      | Selects                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`            | The server.                                                                                                                                    |
| `schema-name`            | A schema (Oracle user).                                                                                                                        |
| `table-name`             | A table by default, or a view when used with `"table-type": "view"`.                                                                           |
| `table-type`             | `"table"` (default) or `"view"`.                                                                                                               |
| `procedure-name`         | A stored procedure.                                                                                                                            |
| `function-name`          | A function.                                                                                                                                    |
| `package-name`           | A package.                                                                                                                                     |
| `sequence-name`          | A sequence.                                                                                                                                    |
| `synonym-name`           | A synonym.                                                                                                                                     |
| `type-name`              | A user-defined type.                                                                                                                           |
| `materialized-view-name` | A materialized view.                                                                                                                           |
| `category-name`          | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

SAP ASE (Sybase ASE)

| Key                          | Selects                                                                                                                                        |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`                | The server.                                                                                                                                    |
| `database-name`              | A database on the server.                                                                                                                      |
| `schema-name`                | A schema within the database.                                                                                                                  |
| `table-name`                 | A table by default, or a view when used with `"table-type": "view"`.                                                                           |
| `table-type`                 | `"table"` (default) or `"view"`.                                                                                                               |
| `materialized-view-name`     | A materialized view.                                                                                                                           |
| `procedure-name`             | A stored procedure.                                                                                                                            |
| `scalar-function-name`       | A scalar-valued function.                                                                                                                      |
| `table-valued-function-name` | A table-valued function.                                                                                                                       |
| `user-defined-type-name`     | A user-defined type.                                                                                                                           |
| `default-name`               | A user-defined default. Reachable through `Describe*` only.                                                                                    |
| `category-name`              | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

PostgreSQL

| Key                      | Selects                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`            | The server.                                                                                                                                    |
| `schema-name`            | A schema.                                                                                                                                      |
| `table-name`             | A table or a view; use `table-type` to distinguish.                                                                                            |
| `function-name`          | A function.                                                                                                                                    |
| `procedure-name`         | A stored procedure.                                                                                                                            |
| `sequence-name`          | A sequence.                                                                                                                                    |
| `materialized-view-name` | A materialized view.                                                                                                                           |
| `type-name`              | A user-defined type.                                                                                                                           |
| `domain-name`            | A domain.                                                                                                                                      |
| `category-name`          | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

MySQL

| Key              | Selects                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`    | The server.                                                                                                                                    |
| `schema-name`    | A schema.                                                                                                                                      |
| `table-name`     | A table or a view; use `table-type` to distinguish.                                                                                            |
| `procedure-name` | A stored procedure.                                                                                                                            |
| `function-name`  | A function.                                                                                                                                    |
| `event-name`     | An event.                                                                                                                                      |
| `category-name`  | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

IBM Db2 for z/OS

| Key              | Selects                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`    | The server.                                                                                                                                    |
| `schema-name`    | A schema.                                                                                                                                      |
| `table-name`     | A table, view, or global temporary table; use `table-type` to distinguish.                                                                     |
| `table-type`     | `"table"` (default) or `"view"`.                                                                                                               |
| `procedure-name` | A stored procedure or external procedure.                                                                                                      |
| `function-name`  | A function (inline, scalar, sourced, table, or external function).                                                                             |
| `sequence-name`  | A sequence.                                                                                                                                    |
| `alias-name`     | An alias. No PostgreSQL target model; use `StartMetadataModelExportAsScript` with `Origin: SOURCE`.                                            |
| `mqtable-name`   | A materialized query table (MQT). No PostgreSQL target model.                                                                                  |
| `type-name`      | A user-defined type (distinct type or structured type). No PostgreSQL target model.                                                            |
| `category-name`  | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

IBM Db2 LUW

| Key              | Selects                                                                                                                                        |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `server-name`    | The server.                                                                                                                                    |
| `schema-name`    | A schema.                                                                                                                                      |
| `table-name`     | A table or a view; use `table-type` to distinguish.                                                                                            |
| `procedure-name` | A stored procedure.                                                                                                                            |
| `function-name`  | A function (scalar, sourced, or table function).                                                                                               |
| `sequence-name`  | A sequence.                                                                                                                                    |
| `module-name`    | A module.                                                                                                                                      |
| `category-name`  | An object class. Use to target an entire category of objects; see [Category names by engine](#dms-sc-category-names "#dms-sc-category-names"). |

## Category names by engine

The `category-name` value in a selection rules targets an entire
object class rather than individual objects. Category names are engine-specific and
case-sensitive. Whether an operation accepts `category-name` depends on
the operation — check the [AWS API Reference](../APIReference/API_Operations.md "../APIReference/API_Operations.md") for the operation you are using. The
tabs below cover both source and target engines.

###### Important

Sending a category name from one engine to a project configured for a
different engine returns error.

SQL Server
The following category names apply to Microsoft SQL Server sources.

| `category-name` value        | What it groups                           |
| ---------------------------- | ---------------------------------------- |
| `Tables`                     | Base tables.                             |
| `Views`                      | Views.                                   |
| `Procedures`                 | Stored procedures.                       |
| `SQL scalar functions`       | Scalar T-SQL functions.                  |
| `SQL table-valued functions` | Multi-statement table-valued functions.  |
| `SQL inline functions`       | Inline table-valued functions.           |
| `Aggregate functions`        | User-defined aggregate functions.        |
| `Synonyms`                   | T-SQL synonyms.                          |
| `Sequences`                  | Sequence objects.                        |
| `Types`                      | XML schema collections and column types. |
| `Table types`                | Table-typed parameter declarations.      |
| `User-Defined Types`         | Alias and CLR user-defined types.        |
| `XML Schema Collections`     | XML schema collections.                  |
| `Statements`                 | SQL statements.                          |

Oracle
The following category names apply to Oracle sources.

| `category-name` value    | What it groups                                      |
| ------------------------ | --------------------------------------------------- |
| `Tables`                 | Tables.                                             |
| `External Tables`        | External tables.                                    |
| `Views`                  | Views.                                              |
| `Packages`               | PL/SQL package specifications and bodies.           |
| `Procedures`             | Stored procedures.                                  |
| `Functions`              | All user functions, including scalar and pipelined. |
| `User Defined Types`     | Object types.                                       |
| `Collection Types`       | VARRAY and nested-table types.                      |
| `Sequences`              | Sequences.                                          |
| `Materialized Views`     | Materialized views.                                 |
| `Materialized View Logs` | Materialized-view change logs.                      |
| `Synonyms`               | Public and private synonyms.                        |
| `Clusters`               | Index and hash clusters.                            |
| `Database Links`         | Database links.                                     |

SAP ASE (Sybase ASE)
The following category names apply to SAP ASE (Sybase ASE) sources.

| `category-name` value    | What it groups                                                           |
| ------------------------ | ------------------------------------------------------------------------ |
| `Tables`                 | Base tables.                                                             |
| `Views`                  | Views.                                                                   |
| `Procedures`             | Stored procedures.                                                       |
| `Scalar Functions`       | Scalar T-SQL functions.                                                  |
| `Table Valued Functions` | Table-valued functions.                                                  |
| `Materialized Views`     | Materialized views.                                                      |
| `User Defined Types`     | Alias user-defined types.                                                |
| `Defaults`               | Bound default objects. Describe-only; cannot be converted independently. |

PostgreSQL
The following category names apply to PostgreSQL and Aurora PostgreSQL targets.

| `category-name` value | What it groups      |
| --------------------- | ------------------- |
| `Tables`              | Base tables.        |
| `Views`               | Views.              |
| `Functions`           | Functions.          |
| `Procedures`          | Stored procedures.  |
| `Sequences`           | Sequences.          |
| `Materialized Views`  | Materialized views. |
| `Types`               | User-defined types. |
| `Domains`             | Domains.            |

MySQL
The following category names apply to MySQL and Aurora MySQL targets.

| `category-name` value | What it groups     |
| --------------------- | ------------------ |
| `Tables`              | Base tables.       |
| `Views`               | Views.             |
| `Functions`           | Functions.         |
| `Procedures`          | Stored procedures. |
| `Events`              | Events.            |

IBM Db2 for z/OS
The following category names apply to IBM Db2 for z/OS sources.

| `category-name` value       | Locator key                            | What it groups                                                   |
| --------------------------- | -------------------------------------- | ---------------------------------------------------------------- |
| `Tables`                    | `table-name` + `"table-type": "table"` | Base tables.                                                     |
| `Global Temporary Tables`   | `table-name` + `"table-type": "table"` | Global temporary tables. No PostgreSQL target model.             |
| `Materialized Query Tables` | `mqtable-name`                         | Materialized query tables (MQTs). No PostgreSQL target model.    |
| `Views`                     | `table-name` + `"table-type": "view"`  | Views.                                                           |
| `Aliases`                   | `alias-name`                           | Aliases. No PostgreSQL target model.                             |
| `Procedures`                | `procedure-name`                       | Stored procedures.                                               |
| `Functions`                 | `function-name`                        | All function sub-types: scalar, table, inline, sourced.          |
| `Sequences`                 | `sequence-name`                        | Sequences.                                                       |
| `User Defined Types`        | `type-name`                            | Distinct types and structured types. No PostgreSQL target model. |
| `External Routines`         | `function-name` / `procedure-name`     | External functions and external procedures.                      |

IBM Db2 LUW
The following category names apply to IBM Db2 LUW targets.

| `category-name` value | What it groups                      |
| --------------------- | ----------------------------------- |
| `Tables`              | Base tables.                        |
| `Views`               | Views.                              |
| `Functions`           | Functions (scalar, sourced, table). |
| `Procedures`          | Stored procedures.                  |
| `Sequences`           | Sequences.                          |
| `Modules`             | Modules.                            |

## Selection rules examples

The following examples show how to write selection rules for common migration
scenarios. Each example uses the `--selection-rules` parameter value
you would pass to DMS Schema Conversion API operations such as
`StartMetadataModelConversion` or
`StartMetadataModelAssessment`.

Select one specific table for conversion from a Microsoft SQL Server source. Microsoft SQL Server
requires `database-name` in addition to `schema-name`.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "`schema_name`",
        "table-name": "`table_name`"
      }
    }
  ]
}
```

Select all objects in an Oracle schema by omitting the object-level key.
Oracle has no `database-name` level; the schema is the top container
under `server-name`.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`"
      }
    }
  ]
}
```

Oracle views are addressed using `table-name` with
`"table-type": "view"`. There is no separate
`view-name` key.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`",
        "table-name": "`view_name`",
        "table-type": "view"
      }
    }
  ]
}
```

Select one specific stored procedure from an IBM Db2 for z/OS source.
IBM Db2 for z/OS uses `procedure-name` and goes directly from
`server-name` to `schema-name` with no
`database-name` level.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`",
        "procedure-name": "`procedure_name`"
      }
    }
  ]
}
```

Select every procedure in a SAP ASE (Sybase ASE) schema by using
`%` as a wildcard for `procedure-name`. SAP ASE (Sybase ASE)
requires `database-name` between `server-name` and
`schema-name`.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "include",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "%"
      }
    }
  ]
}
```

Use `%` to match multiple tables by prefix. This example selects
all tables whose names start with `Fact_`.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "include",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "table-name": "Fact_%"
      }
    }
  ]
}
```

Include all objects in an Oracle schema, then exclude any tables whose names
start with `TMP_`. Rules are evaluated in `rule-id` order;
`exclude` takes precedence when it matches.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "include",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`"
      }
    },
    {
      "rule-type": "selection",
      "rule-id": "2",
      "rule-name": "`rule_name`",
      "rule-action": "exclude",
      "object-locator": {
        "server-name": "`source_server`",
        "schema-name": "`schema_name`",
        "table-name": "TMP_%"
      }
    }
  ]
}
```

Use multiple `explicit` rules in a single document to select a
specific set of procedures by name.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "PROC_A"
      }
    },
    {
      "rule-type": "selection",
      "rule-id": "2",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "PROC_B"
      }
    },
    {
      "rule-type": "selection",
      "rule-id": "3",
      "rule-name": "`rule_name`",
      "rule-action": "explicit",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "PROC_C"
      }
    }
  ]
}
```

Use an `include` rule to match every procedure whose name starts
with `PROC_`, then an `exclude` rule to remove
`PROC_TEST` from that set. An `exclude` rule must follow
an `include` rule; a standalone `exclude` has no
effect.

```
{
  "rules": [
    {
      "rule-type": "selection",
      "rule-id": "1",
      "rule-name": "`rule_name`",
      "rule-action": "include",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "PROC_%"
      }
    },
    {
      "rule-type": "selection",
      "rule-id": "2",
      "rule-name": "`rule_name`",
      "rule-action": "exclude",
      "object-locator": {
        "server-name": "`source_server`",
        "database-name": "`database_name`",
        "schema-name": "dbo",
        "procedure-name": "PROC_TEST"
      }
    }
  ]
}
```

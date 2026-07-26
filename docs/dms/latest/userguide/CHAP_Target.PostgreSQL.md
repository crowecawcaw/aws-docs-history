# Using a PostgreSQL database as a target for AWS Database Migration Service

You can migrate data to PostgreSQL databases using AWS DMS, either from another
PostgreSQL database or from one of the other supported databases.

For information about versions
of PostgreSQL that AWS DMS supports as a target, see [Targets for AWS DMS](CHAP_Introduction.Targets.md "CHAP_Introduction.Targets.md").

###### Note

- Amazon Aurora Serverless is available as a target for Amazon Aurora with
  PostgreSQL compatibility. For more information about Amazon Aurora Serverless, see
  [Using
  Amazon Aurora Serverless v2](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.md") in the
  _Amazon Aurora User Guide_.
- Aurora Serverless DB clusters are accessible only from an Amazon VPC and
  can't use a [public IP address](../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.md "../../../AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.requirements.md"). So, if you intend to have a replication instance
  in a different region than Aurora PostgreSQL Serverless, you must configure
  [vpc peering](CHAP_ReplicationInstance.VPC.md#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCPeer "CHAP_ReplicationInstance.VPC.md#CHAP_ReplicationInstance.VPC.Configurations.ScenarioVPCPeer"). Otherwise, check the availability of Aurora PostgreSQL
  Serverless [regions](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Serverless "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.Serverless"), and decide to use one of those regions for both Aurora
  PostgreSQL Serverless and your replication instance.
- Babelfish capability is built into Amazon Aurora and doesn't have an
  additional cost. For more information, see [Using Babelfish for Aurora PostgreSQL
  as a target for AWS Database Migration Service](#CHAP_Target.PostgreSQL.Babelfish "#CHAP_Target.PostgreSQL.Babelfish").
  AWS DMS takes a table-by-table approach when migrating data from source to target
  in the Full Load phase. Table order during the full load phase cannot be guaranteed.
  Tables are out of sync during the full load phase and while cached transactions for
  individual tables are being applied. As a result, active referential integrity
  constraints can result in task failure during the full load phase.

In PostgreSQL, foreign keys (referential integrity constraints) are implemented using
triggers. During the full load phase, AWS DMS loads each table one at a time. We strongly
recommend that you disable foreign key constraints during a full load, using one of the
following methods:

- Temporarily disable all triggers from the instance, and finish the full
  load.
- Use the `session_replication_role` parameter in PostgreSQL.
  At any given time, a trigger can be in one of the following states:
  `origin`, `replica`, `always`, or
  `disabled`. When the `session_replication_role` parameter is
  set to `replica`, only triggers in the `replica` state are active,
  and they are fired when they are called. Otherwise, the triggers remain inactive.

PostgreSQL has a failsafe mechanism to prevent a table from being truncated, even when
`session_replication_role` is set. You can use this as an alternative to
disabling triggers, to help the full load run to completion. To do this, set the target
table preparation mode to `DO_NOTHING`. Otherwise, DROP and TRUNCATE
operations fail when there are foreign key constraints.

In Amazon RDS, you can control set this parameter using a parameter group. For a PostgreSQL
instance running on Amazon EC2, you can set the parameter directly.

For additional details on working with a PostgreSQL database as a target for AWS DMS,
see the following sections:

###### Topics

- [Limitations on using PostgreSQL as a target for AWS Database Migration Service](#CHAP_Target.PostgreSQL.Limitations "#CHAP_Target.PostgreSQL.Limitations")
- [Limitations on using Amazon Aurora PostgreSQL Limitless as a target for AWS Database Migration Service](#CHAP_Target.PostgreSQL.Aurora.Limitations "#CHAP_Target.PostgreSQL.Aurora.Limitations")
- [Security requirements when using a PostgreSQL database as a target for AWS Database Migration Service](#CHAP_Target.PostgreSQL.Security "#CHAP_Target.PostgreSQL.Security")
- [Endpoint settings and Extra Connection Attributes (ECAs) when using PostgreSQL as a target for AWS DMS](#CHAP_Target.PostgreSQL.ConnectionAttrib "#CHAP_Target.PostgreSQL.ConnectionAttrib")
- [Target data types for PostgreSQL](#CHAP_Target.PostgreSQL.DataTypes "#CHAP_Target.PostgreSQL.DataTypes")
- [Using Babelfish for Aurora PostgreSQL as a target for AWS Database Migration Service](#CHAP_Target.PostgreSQL.Babelfish "#CHAP_Target.PostgreSQL.Babelfish")

## Limitations on using PostgreSQL as a target for AWS Database Migration Service

The following limitations apply when using a PostgreSQL database as a target for
AWS DMS:

- For heterogeneous migrations, the JSON data type is converted to the Native CLOB data type internally.
- In an Oracle to PostgreSQL migration, if a column in Oracle contains a
  NULL character (hex value U+0000), AWS DMS converts the NULL character to a
  space (hex value U+0020). This is due to a PostgreSQL limitation.
- AWS DMS doesn't support replication to a table with a unique index created with coalesce function.
- If your tables use sequences, then update the value of `NEXTVAL`
  for each sequence in the target database after you stop the replication from the
  source database. AWS DMS copies data from your source database, but doesn't migrate
  sequences to the target during the ongoing replication.

## Limitations on using Amazon Aurora PostgreSQL Limitless as a target for AWS Database Migration Service

The following limitations apply when using Amazon Aurora PostgreSQL Limitless as a
target for AWS DMS:

- AWS DMS Data Validation does not support Amazon Aurora PostgreSQL
  Limitless.
- AWS DMS migrates source tables as Standard tables, which are not distributed.
  After migration, you can convert these Standard tables to Limitless tables by
  following the official conversion guide.

## Security requirements when using a PostgreSQL database as a target for AWS Database Migration Service

For security purposes, the user account used for the data migration must be a
registered user in any PostgreSQL database that you use as a target.

Your PostgreSQL target endpoint requires minimum user permissions to run an AWS DMS migration, see the following examples.

```

    CREATE USER newuser WITH PASSWORD 'your-password';
    ALTER SCHEMA schema_name OWNER TO newuser;

```

Or,

```

    GRANT USAGE ON SCHEMA schema_name TO myuser;
    GRANT CONNECT ON DATABASE postgres to myuser;
    GRANT CREATE ON DATABASE postgres TO myuser;
    GRANT CREATE ON SCHEMA schema_name TO myuser;
    GRANT UPDATE, INSERT, SELECT, DELETE, TRUNCATE ON ALL TABLES IN SCHEMA schema_name TO myuser;
    GRANT TRUNCATE ON schema_name."BasicFeed" TO myuser;

```

## Endpoint settings and Extra Connection Attributes (ECAs) when using PostgreSQL as a target for AWS DMS

You can use endpoint settings and Extra Connection Attributes (ECAs) to configure your
PostgreSQL target database.

You specify the settings when you create the target
endpoint using the AWS DMS console, or by using the `create-endpoint` command in the
[AWS CLI](../../../cli/latest/reference/dms/index.md "../../../cli/latest/reference/dms/index.md"), with the
`--postgre-sql-settings '{"`EndpointSetting`":
 `"value"`, `...`}'` JSON syntax.

You specify ECAs using the `ExtraConnectionAttributes` parameter for your endpoint.

The following table shows the endpoint settings that you can use with PostgreSQL as a target.

| Name                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ConnectionTimeout`                                             | Use this extra connection attribute (ECA) to set the endpoint<br>connection timeout for the PostgreSQL instance, in seconds. The<br>default value is 10 seconds. ECA Example:<br>`ConnectionTimeout=30`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `MaxFileSize`                                                   | Specifies the maximum size (in KB) of any .csv file used to<br>transfer data to PostgreSQL.<br>Default value: 32,768 KB (32 MB)<br>Valid values: 1–1,048,576 KB (up to 1.1 GB)<br>Example: `--postgre-sql-settings '{"MaxFileSize":<br>512}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `ExecuteTimeout`                                                | Sets the client statement timeout for the<br>PostgreSQL instance, in seconds. The default value is 60<br>seconds.<br>Example: `--postgre-sql-settings '{"ExecuteTimeout": 100}'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `AfterConnectScript= SET<br>session_replication_role = replica` | This attribute has AWS DMS bypass foreign keys and user triggers<br>to reduce the time it takes to bulk load data.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `MapUnboundedNumericAsString`                                   | This parameter treats columns with unbounded NUMERIC data<br>types as STRING in order to successfully migrate without losing<br>precision of the numeric value. Use this parameter only for<br>replication from PostgreSQL source to PostgreSQL target, or<br>databases with PostgreSQL compatibility.<br>Default value: false<br>Valid values: false/true<br>Example: `--postgre-sql-settings '{"MapUnboundedNumericAsString": "true"}`<br>Using this parameter might result in some replication performance degradation because of<br>transformation from numeric to string and back to numeric. This parameter is supported for use<br>by DMS version 3.4.4 and higher<br>NoteOnly use `MapUnboundedNumericAsString` in PostgreSQL source and target endpoints together.Use of `MapUnboundedNumericAsString` on source PostgreSQL endpoints restricts precision to 28 during CDC.<br>Use of `MapUnboundedNumericAsString` on target endpoints, migrates data with Precision 28 Scale 6.Do not use `MapUnboundedNumericAsString` with non-PostgreSQL targets.During CDC, unbounded NUMERIC values are truncated to 1,000 characters<br>if their string representation exceeds that limit. |
| `loadUsingCSV`                                                  | Use this Extra Connection Attribute (ECA) to transfer data<br>for full-load operations using \COPY command.<br>Default value: `true`<br>Valid values: true/false<br>ECA Example: `loadUsingCSV=true;`<br>**Note:*<br>• Setting this ECA<br>to false might result in some replication performance degradation<br>because of INSERTs being executed directly.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `DatabaseMode`                                                  | Use this attribute to change the default behaviour of the replication’s handling<br>of Postgresql compatible endpoints that require some additional configuration,<br>such as Babelfish endpoints.<br>Default value: `DEFAULT`<br>Valid values: `DEFAULT`, `BABELFISH`<br>Example: `DatabaseMode=default;`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `BabelfishDatabaseName`                                         | Use this attribute to specify the name of the target Babelfish T-SQL database being migrated to.<br>This is required if `DatabaseMode` is set to `Babelfish`. This is not the reserved `babelfish_db` database.<br>Example: `BabelfishDatabaseName=TargetDb;`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## Target data types for PostgreSQL

The PostgreSQL database endpoint for AWS DMS supports most PostgreSQL database
data types. The following table shows the PostgreSQL database target data types that
are supported when using AWS DMS and the default mapping from AWS DMS data
types.

For additional information about AWS DMS data types, see [Data types for AWS Database Migration Service](CHAP_Reference.DataTypes.md "CHAP_Reference.DataTypes.md").

| AWS DMS data type | PostgreSQL data type                                                                                                                                          |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BOOLEAN           | BOOLEAN                                                                                                                                                       |
| BLOB              | BYTEA                                                                                                                                                         |
| BYTES             | BYTEA                                                                                                                                                         |
| DATE              | DATE                                                                                                                                                          |
| TIME              | TIME                                                                                                                                                          |
| DATETIME          | If the scale is from 0 through 6, then use TIMESTAMP.<br>If the scale is from 7 through 9, then use VARCHAR<br>(37).                                          |
| INT1              | SMALLINT                                                                                                                                                      |
| INT2              | SMALLINT                                                                                                                                                      |
| INT4              | INTEGER                                                                                                                                                       |
| INT8              | BIGINT                                                                                                                                                        |
| NUMERIC           | DECIMAL (P,S)                                                                                                                                                 |
| REAL4             | FLOAT4                                                                                                                                                        |
| REAL8             | FLOAT8                                                                                                                                                        |
| STRING            | If the length is from 1 through 21,845, then use VARCHAR<br>(length in bytes).<br>If the length is 21,846 through 2,147,483,647, then use<br>VARCHAR (65535). |
| UINT1             | SMALLINT                                                                                                                                                      |
| UINT2             | INTEGER                                                                                                                                                       |
| UINT4             | BIGINT                                                                                                                                                        |
| UINT8             | BIGINT                                                                                                                                                        |
| WSTRING           | If the length is from 1 through 21,845, then use VARCHAR<br>(length in bytes).<br>If the length is 21,846 through 2,147,483,647, then use<br>VARCHAR (65535). |
| NCLOB             | TEXT                                                                                                                                                          |
| CLOB              | TEXT                                                                                                                                                          |

###### Note

When replicating from a PostgreSQL source, AWS DMS creates the target table
with the same data types for all columns, apart from columns with user-defined
data types. In such cases, the data type is created as "character varying" in
the target.

## Using Babelfish for Aurora PostgreSQL as a target for AWS Database Migration Service

You can migrate SQL Server source tables to a Babelfish for Amazon Aurora PostgreSQL target using
AWS Database Migration Service. With Babelfish, Aurora PostgreSQL understands T-SQL, Microsoft SQL Server's
proprietary SQL dialect, and supports the same communications protocol. So, applications
written for SQL Server can now work with Aurora with fewer code changes. Babelfish
capability is built into Amazon Aurora and doesn't have an additional cost. You can
activate Babelfish on your Amazon Aurora cluster from the Amazon RDS console.

When you create your AWS DMS target endpoint using the AWS DMS console, API, or CLI
commands, specify the target engine as **Amazon Aurora PostgreSQL**, and name the
database, **babelfish\_db**. In the **Endpoint Settings**
section, add settings to set `DatabaseMode` to `Babelfish` and
`BabelfishDatabaseName` to the name of the target Babelfish T-SQL database.

### Adding transformation rules to your migration task

When you define a migration task for a Babelfish target, you need to include transformation rules
that ensure DMS uses the pre-created T-SQL Babelfish tables in the target database.

First, add a transformation rule to your migration task that makes all table names
lowercase. Babelfish stores as lowercase in the PostgreSQL `pg_class`
catalog the names of tables that you create using T-SQL. However, when you have SQL
Server tables with mixed-case names, DMS creates the tables using PostgreSQL native
data types instead of the T-SQL compatible data types. For that reason, be sure to
add a transformation rule that makes all table names lowercase. Note that column names
should not be transformed to lowercase.

Next, if you used the multidatabase migration mode when you defined your cluster,
add a transformation rule that renames the original SQL Server schema. Make sure to
rename the SQL Server schema name to include the name of the T-SQL database. For
example, if the original SQL Server schema name is dbo, and your T-SQL database name
is mydb, rename the schema to mydb\_dbo using a transformation rule.

###### Note

When using Babelfish for Aurora PostgreSQL 16 or later, the default migration mode
is "multidatabase". When running AWS DMS migration tasks, ensure to review the
migration mode parameter and update the transformation rules if needed.

If you use single database mode, you don't need a transformation rule to
rename schema names. Schema names have a one-to-one mapping with the target T-SQL
database in Babelfish.

The following sample transformation rule makes all table names lowercase, and renames the original
SQL Server schema name from `dbo` to `mydb_dbo`.

```
{
   "rules": [
   {
      "rule-type": "transformation",
      "rule-id": "566251737",
      "rule-name": "566251737",
      "rule-target": "schema",
      "object-locator": {
         "schema-name": "dbo"
      },
      "rule-action": "rename",
      "value": "mydb_dbo",
      "old-value": null
   },
   {
      "rule-type": "transformation",
      "rule-id": "566139410",
      "rule-name": "566139410",
      "rule-target": "table",
      "object-locator": {
         "schema-name": "%",
         "table-name": "%"
      },
      "rule-action": "convert-lowercase",
      "value": null,
      "old-value": null
   },
   {
      "rule-type": "selection",
      "rule-id": "566111704",
      "rule-name": "566111704",
      "object-locator": {
         "schema-name": "dbo",
         "table-name": "%"
      },
      "rule-action": "include",
      "filters": []
   }
]
}

```

### Limitations to using a PostgreSQL target endpoint with Babelfish tables

The following limitations apply when using a PostgreSQL target endpoint with Babelfish tables:

- For **Target table preparation** mode, use only the
  **Do nothing** or **Truncate** modes.
  Don't use the **Drop tables on target** mode. In that mode,
  DMS creates the tables as PostgreSQL tables that T-SQL might not
  recognize.
- AWS DMS doesn't support the sql\_variant data type.
- Babelfish under Postgres endpoint does not support
  `HIERARCHYID`, `GEOMETRY` (prior to 3.5.4) and
  `GEOGRAPHY` (prior to 3.5.4) data types. To migrate these
  data types, you can add transformation rules to convert the data type to
  wstring(250).
- Babelfish only supports migrating `BINARY`,
  `VARBINARY`, and `IMAGE` data types using the `BYTEA`
  data type.
  For earlier versions of Aurora PostgreSQL, you can use DMS to migrate
  these tables to a [Babelfish target
  endpoint](CHAP_Target.Babelfish.md "CHAP_Target.Babelfish.md"). You don't have to specify a length for the `BYTEA` data type,
  as shown in the following example.

```
[Picture] [VARBINARY](max) NULL
```

Change the preceding T-SQL data type to the T-SQL supported `BYTEA` data type.

```
[Picture] BYTEA NULL
```

- For earlier versions of Aurora PostgreSQL Babelfish, if you create a migration task for
  ongoing replication from SQL Server
  to Babelfish using the PostgreSQL target endpoint, you need to assign the
  `SERIAL` data type to any tables that use
  `IDENTITY` columns. Starting with Aurora PostgreSQL (version 15.3/14.8 and higher)
  and Babelfish (version 3.2.0 and higher), the identity column is supported, and it is no longer required
  to assign the SERIAL data type.
  For more information, see [SERIAL Usage](../sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.tsql.sequences..md "../sql-server-to-aurora-postgresql-migration-playbook/chap-sql-server-aurora-pg.tsql.sequences..md") in the Sequences and Identity section of the
  _SQL Server to Aurora PostgreSQL Migration Playbook_.
  Then, when you create the table in Babelfish, change the column definition
  from the following.

```
    [IDCol] [INT] IDENTITY(1,1) NOT NULL PRIMARY KEY
```

Change the preceding into the following.

```
    [IDCol] SERIAL PRIMARY KEY
```

Babelfish-compatible Aurora PostgreSQL creates a sequence using the
default configuration and adds a `NOT NULL` constraint to the
column. The newly created sequence behaves like a regular sequence
(incremented by 1) and has no composite `SERIAL` option.

- After migrating data with tables that use `IDENTITY`
  columns or the `SERIAL` data type, reset the PostgreSQL-based
  sequence object based on the maximum value for the column. After performing
  a full load of the tables, use the following T-SQL query to generate
  statements to seed the associated sequence object.

```
DECLARE @schema_prefix NVARCHAR(200) = ''

IF current_setting('babelfishpg_tsql.migration_mode') = 'multi-db'
        SET @schema_prefix = db_name() + '_'

SELECT 'SELECT setval(pg_get_serial_sequence(''' + @schema_prefix + schema_name(tables.schema_id) + '.' + tables.name + ''', ''' + columns.name + ''')
               ,(select max(' + columns.name + ') from ' + schema_name(tables.schema_id) + '.' + tables.name + '));'
FROM sys.tables tables
JOIN sys.columns columns ON tables.object_id = columns.object_id
WHERE columns.is_identity = 1

UNION ALL

SELECT 'SELECT setval(pg_get_serial_sequence(''' + @schema_prefix + table_schema + '.' + table_name + ''',
''' + column_name + '''),(select max(' + column_name + ') from ' + table_schema + '.' + table_name + '));'
FROM information_schema.columns
WHERE column_default LIKE 'nextval(%';

```

The query generates a series of SELECT statements that you execute in order to update the maximum IDENTITY and SERIAL values.

- For Babelfish versions prior to 3.2, **Full LOB mode** might result in a
  table error. If that happens, create a separate task for the tables that
  failed to load. Then use **Limited LOB mode** to specify
  the appropriate value for the **Maximum LOB size
  (KB)**. Another option is to set the SQL Server Endpoint Connection
  Attribute setting `ForceFullLob=True`.
- For Babelfish versions prior to 3.2, performing data
  validation with Babelfish tables that don't use integer based primary keys
  generates a message that a suitable unique key can't be found.
  Starting with Aurora PostgreSQL (version 15.3/14.8 and higher) and Babelfish
  (version 3.2.0 and higher), data validation for non-integer primary keys is supported.
- Because of precision differences in the number of decimal places for
  seconds, DMS reports data validation failures for Babelfish tables that use
  `DATETIME` data types. To suppress those failures, you can
  add the following validation rule type for `DATETIME` data
  types.

```
{
         "rule-type": "validation",
         "rule-id": "3",
         "rule-name": "3",
         "rule-target": "column",
         "object-locator": {
             "schema-name": "dbo",
             "table-name": "%",
             "column-name": "%",
             "data-type": "datetime"
         },
         "rule-action": "override-validation-function",
         "source-function": "case when ${column-name} is NULL then NULL else 0 end",
         "target-function": "case when ${column-name} is NULL then NULL else 0 end"
     }

```

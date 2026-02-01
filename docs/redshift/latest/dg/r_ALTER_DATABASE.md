Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# ALTER DATABASE

Changes the attributes of a database.

## Required privileges

To use ALTER DATABASE, one of the following privileges is required..

- Superuser
- Users with the ALTER DATABASE privilege
- Database owner

## Syntax

```
ALTER DATABASE database_name
{
  RENAME TO new_name
  | OWNER TO new_owner
  | [ CONNECTION LIMIT { limit | UNLIMITED } ]
    [ COLLATE { CASE_SENSITIVE | CS | CASE_INSENSITIVE | CI } ]
    [ ISOLATION LEVEL { SNAPSHOT | SERIALIZABLE } ]
| INTEGRATION
 {
  REFRESH { { ALL | INERROR } TABLES [ IN SCHEMA schema [, ...] ] | TABLE schema.table [, ...] }
   | SET
     [ QUERY_ALL_STATES [=] { TRUE | FALSE } ]
     [ ACCEPTINVCHARS [=] { TRUE | FALSE } ]
     [ REFRESH_INTERVAL <interval> ]
     [ TRUNCATECOLUMNS [=] { TRUE | FALSE } ]
     [ HISTORY_MODE [=] {TRUE | FALSE} [ FOR { {ALL} TABLES [IN SCHEMA schema [, ...] ] | TABLE schema.table [, ...] } ] ]
 }
}
```

## Parameters

_database_name_

Name of the database to alter. Typically, you alter a database that you are
not currently connected to; in any case, the changes take effect only in
subsequent sessions. You can change the owner of the current database, but you
can't rename it:

```
alter database tickit rename to newtickit;
ERROR:  current database may not be renamed
```

RENAME TO

Renames the specified database. For more information about valid names, see
[Names and identifiers](r_names.md "r_names.md"). You can't rename the
dev, padb_harvest, template0, template1, or sys:internal databases, and you
can't rename the current database. Only the database owner or a
[superuser](r_superusers.md#def_superusers "r_superusers.md#def_superusers") can rename a database; non-superuser owners must also have
the CREATEDB privilege.

_new_name_

New database name.

OWNER TO

Changes the owner of the specified database. You can change the owner of the
current database or some other database. Only a superuser can change the
owner.

_new_owner_

New database owner. The new owner must be an existing database user with
write privileges. For more information about user privileges, see [GRANT](r_GRANT.md "r_GRANT.md").

CONNECTION LIMIT { _limit_ | UNLIMITED }

The maximum number of database connections users are permitted to have open
concurrently. The limit is not enforced for superusers. Use the UNLIMITED
keyword to permit the maximum number of concurrent connections.

A limit on the number of connections for each user might also apply. For more
information, see [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md").
The default is UNLIMITED. To view current connections, query the [STV_SESSIONS](r_STV_SESSIONS.md "r_STV_SESSIONS.md") system
view.

###### Note

If both user and database connection limits apply, an unused connection
slot must be available that is within both limits when a user attempts to
connect.

COLLATE { CASE_SENSITIVE | CS | CASE_INSENSITIVE | CI }

A clause that specifies whether string search or comparison is
case-sensitive or case-insensitive.

You can change the case sensitivity of the current database even if it's empty.

You must have ALTER permission for the current database to change case
sensitivity. Superusers or database owners with the CREATE DATABASE permission
can also change database case sensitivity.

CASE_SENSITIVE and CS are interchangeable and yield the same results.
Similarly, CASE_INSENSITIVE and CI are interchangeable and yield the same results.

ISOLATION LEVEL { SNAPSHOT | SERIALIZABLE }

A clause that specifies the isolation level used when queries run against a
database. For more information on isolation levels, see
[Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

- SNAPSHOT isolation – provides an isolation level with
  protection against update and delete conflicts.
- SERIALIZABLE isolation – provides full serializability for
  concurrent transactions.

Consider the following items when altering the isolation level of a
database:

- You must have the superuser or CREATE DATABASE privilege to the
  current database to change the database isolation level.
- You can't alter the isolation level of the `dev` database.
- You can't alter the isolation level within a transaction block.
- The alter isolation level command fails if other users are connected
  to the database.
- The alter isolation level command can alter the isolation level
  settings of the current session.

INTEGRATION

Alter a zero-ETL integration database.

REFRESH {{ ALL | INERROR } TABLES [IN SCHEMA _schema_ [,
...]] | TABLE _schema.table_ [, ...]}

A clause that specifies whether Amazon Redshift will refresh all tables or tables with
errors in the specified schema or table. The refresh will trigger the tables in
the specified schema or table to be fully replicated from the source
database.

For more information, see [Zero-ETL integrations](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md") in the
_Amazon Redshift Management Guide_. For more information about integration
states, see [SVV_INTEGRATION_TABLE_STATE](r_SVV_INTEGRATION_TABLE_STATE.md "r_SVV_INTEGRATION_TABLE_STATE.md") and [SVV_INTEGRATION](r_SVV_INTEGRATION.md "r_SVV_INTEGRATION.md").

QUERY_ALL_STATES [=] { TRUE | FALSE }

The QUERY_ALL_STATES clause sets whether zero-ETL integration tables can be queried in
all states (`Synced`, `Failed`,
`ResyncRequired`, and `ResyncInitiated`). By default,
a zero-ETL integration table can only be queried in `Synced` state.

ACCEPTINVCHARS [=] { TRUE | FALSE }

The ACCEPTINVCHARS clause sets whether zero-ETL integration tables continue with
ingestion when invalid characters are detected for the VARCHAR data type. When
invalid characters are encountered, the invalid character is replaced with a
default `?` character.

REFRESH_INTERVAL <interval>

The REFRESH_INTERVAL clause sets the approximate time interval, in seconds,
to refresh data from the zero-ETL source to the target database. The
`interval` can be set 0–432,000 seconds (5 days) for
zero-ETL integrations whose source type is Aurora MySQL, Aurora PostgreSQL, or RDS for MySQL. For
Amazon DynamoDB zero-ETL integrations, the `interval` can be set 900–432,000
seconds (15 minutes –5 days).

For more information about creating databases with zero-ETL integrations, see [Creating
destination databases in Amazon Redshift](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md") in the
_Amazon Redshift Management Guide_.

TRUNCATECOLUMNS [=] { TRUE | FALSE }

The TRUNCATECOLUMNS clause sets whether zero-ETL integration tables continue with
ingestion when the values for the VARCHAR column or SUPER column attributes are beyond the limit. When
`TRUE`, the values are truncated to fit into the column and the values of overflowing JSON attributes are truncated to fit into the SUPER column.

HISTORY_MODE [=] {TRUE | FALSE} [ FOR { {ALL} TABLES [IN SCHEMA schema [, ...]]
| TABLE schema.table [, ...]} ]

A clause that specifies whether Amazon Redshift will set history mode for all tables or
tables in the specified schema that participate in zero-ETL integration. This option is
only applicable for databases created for zero-ETL integration.

The HISTORY_MODE clause can be set to `TRUE` or
`FALSE`. The default is `FALSE`. Switching history
mode on and off is only applicable to tables that are in the
`Synced` state. For information about HISTORY_MODE, see [History mode](../mgmt/zero-etl-history-mode.md "../mgmt/zero-etl-history-mode.md") in the _Amazon Redshift Management Guide_.

## Usage notes

ALTER DATABASE commands apply to subsequent sessions not current sessions. You must
reconnect to the altered database to see the effect of the change.

## Examples

The following example renames a database named TICKIT_SANDBOX to TICKIT_TEST:

```
alter database tickit_sandbox rename to tickit_test;
```

The following example changes the owner of the TICKIT database (the current database)
to DWUSER:

```
alter database tickit owner to dwuser;

```

The following example changes the database case sensitivity of the sampledb
database:

```
ALTER DATABASE sampledb COLLATE CASE_INSENSITIVE;
```

The following example alters a database named `sampledb` with
SNAPSHOT isolation level.

```
ALTER DATABASE sampledb ISOLATION LEVEL SNAPSHOT;
```

The following example refreshes the tables
`schema1.sample_table1` and
`schema2.sample_table2` in the database
`sample_integration_db` in your zero-ETL integration.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH TABLE schema1.sample_table1, schema2.sample_table2;
```

The following example refreshes all synced and failed tables within your
zero-ETL integration.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH ALL tables;
```

The following example sets the refresh interval for zero-ETL integrations to 600
seconds..

```
ALTER DATABASE sample_integration_db INTEGRATION SET REFRESH_INTERVAL 600;
```

The following example refreshes all tables that are in the
`ErrorState` in the schema
`sample_schema`.

```
ALTER DATABASE sample_integration_db INTEGRATION REFRESH INERROR TABLES in SCHEMA sample_schema;
```

The following example switches history mode on for table
`myschema.table1`.

```
ALTER DATABASE sample_integration_db INTEGRATION SET HISTORY_MODE = true FOR TABLE myschema.table1
```

The following example switches history mode on for all tables in
`myschema`.

```
ALTER DATABASE sample_integration_db INTEGRATION SET HISTORY_MODE = true for ALL TABLES IN SCHEMA myschema
```

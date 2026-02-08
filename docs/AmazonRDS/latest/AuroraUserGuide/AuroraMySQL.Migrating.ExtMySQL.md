# Reducing the time for physical migration to

Amazon Aurora MySQL

You can make the following database modifications to speed up the process of migrating a database to
Amazon Aurora MySQL.

###### Important

Make sure to perform these updates on a copy of a production database, rather than on a production database. You
can then back up the copy and restore it to your Aurora MySQL DB cluster to avoid any service interruptions on your
production database.

## Unsupported table types

Aurora MySQL supports only the InnoDB engine for database tables. If you have MyISAM tables in your database, then
those tables must be converted before migrating to Aurora MySQL. The conversion process requires additional space for
the MyISAM to InnoDB conversion during the migration procedure.

To reduce your chances of running out of space or to speed up the migration process, convert all of your MyISAM
tables to InnoDB tables before migrating them. The size of the resulting InnoDB table is equivalent to the size
required by Aurora MySQL for that table. To convert a MyISAM table to InnoDB, run the following command:

```
ALTER TABLE `schema`.`table_name` engine=innodb, algorithm=copy;
```

Aurora MySQL doesn't support compressed tables or pages, that is, tables created with
`ROW_FORMAT=COMPRESSED` or `COMPRESSION = {"zlib"|"lz4"}`.

To reduce your chances of running out of space or to speed up the migration process, expand your compressed tables
by setting `ROW_FORMAT` to `DEFAULT`, `COMPACT`, `DYNAMIC`, or
`REDUNDANT`. For compressed pages, set `COMPRESSION="none"`.

For more information, see [InnoDB row
formats](https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-row-format.html") and [InnoDB table
and page compression](https://dev.mysql.com/doc/refman/8.0/en/innodb-compression.html "https://dev.mysql.com/doc/refman/8.0/en/innodb-compression.html")in the MySQL documentation.

You can use the following SQL script on your existing MySQL DB instance to list the tables in your database that
are MyISAM tables or compressed tables.

```
-- This script examines a MySQL database for conditions that block
-- migrating the database into Aurora MySQL.
-- It must be run from an account that has read permission for the
-- INFORMATION_SCHEMA database.

-- Verify that this is a supported version of MySQL.

select msg as `==> Checking current version of MySQL.`
from
  (
  select
    'This script should be run on MySQL version 5.6 or higher. ' +
    'Earlier versions are not supported.' as msg,
    cast(substring_index(version(), '.', 1) as unsigned) * 100 +
      cast(substring_index(substring_index(version(), '.', 2), '.', -1)
      as unsigned)
    as major_minor
  ) as T
where major_minor <> 506;


-- List MyISAM and compressed tables. Include the table size.

select concat(TABLE_SCHEMA, '.', TABLE_NAME) as `==> MyISAM or Compressed Tables`,
round(((data_length + index_length) / 1024 / 1024), 2) "Approx size (MB)"
from INFORMATION_SCHEMA.TABLES
where
  ENGINE <> 'InnoDB'
  and
  (
    -- User tables
    TABLE_SCHEMA not in ('mysql', 'performance_schema',
                         'information_schema')
    or
    -- Non-standard system tables
    (
      TABLE_SCHEMA = 'mysql' and TABLE_NAME not in
        (
          'columns_priv', 'db', 'event', 'func', 'general_log',
          'help_category', 'help_keyword', 'help_relation',
          'help_topic', 'host', 'ndb_binlog_index', 'plugin',
          'proc', 'procs_priv', 'proxies_priv', 'servers', 'slow_log',
          'tables_priv', 'time_zone', 'time_zone_leap_second',
          'time_zone_name', 'time_zone_transition',
          'time_zone_transition_type', 'user'
        )
    )
  )
  or
  (
    -- Compressed tables
       ROW_FORMAT = 'Compressed'
  );
```

## User accounts with unsupported privileges

User accounts with privileges that aren't supported by Aurora MySQL are imported without the unsupported privileges.
For the list of supported privileges, see [Role-based privilege model](AuroraMySQL.md#AuroraMySQL.privilege-model "AuroraMySQL.md#AuroraMySQL.privilege-model").

You can run the following SQL query on your source database to list the user accounts that have unsupported
privileges.

```
SELECT
    user,
    host
FROM
    mysql.user
WHERE
    Shutdown_priv = 'y'
    OR File_priv = 'y'
    OR Super_priv = 'y'
    OR Create_tablespace_priv = 'y';
```

## Dynamic privileges in Aurora MySQL version

3

Dynamic privileges aren't imported. Aurora MySQL version 3 supports the following dynamic privileges.

```
'APPLICATION_PASSWORD_ADMIN',
'CONNECTION_ADMIN',
'REPLICATION_APPLIER',
'ROLE_ADMIN',
'SESSION_VARIABLES_ADMIN',
'SET_USER_ID',
'XA_RECOVER_ADMIN'
```

The following example script grants the supported dynamic privileges to the user accounts in the Aurora MySQL DB
cluster.

```
-- This script finds the user accounts that have Aurora MySQL supported dynamic privileges
-- and grants them to corresponding user accounts in the Aurora MySQL DB cluster.

/home/ec2-user/opt/mysql/8.0.26/bin/mysql -uusername -pxxxxx -P8026 -h127.0.0.1 -BNe "SELECT
  CONCAT('GRANT ', GRANTS, ' ON *.* TO ', GRANTEE ,';') AS grant_statement
  FROM (select GRANTEE, group_concat(privilege_type) AS GRANTS FROM information_schema.user_privileges
      WHERE privilege_type IN (
        'APPLICATION_PASSWORD_ADMIN',
        'CONNECTION_ADMIN',
        'REPLICATION_APPLIER',
        'ROLE_ADMIN',
        'SESSION_VARIABLES_ADMIN',
        'SET_USER_ID',
        'XA_RECOVER_ADMIN')
      AND GRANTEE NOT IN (\"'mysql.session'@'localhost'\",\"'mysql.infoschema'@'localhost'\",\"'mysql.sys'@'localhost'\") GROUP BY GRANTEE)
      AS PRIVGRANTS; " | /home/ec2-user/opt/mysql/8.0.26/bin/mysql -u `master_username` -p `master_password` -h `DB_cluster_endpoint`
```

## Stored objects with 'rdsadmin'@'localhost' as the

definer

Functions, procedures, views, events, and triggers with `'rdsadmin'@'localhost'` as the definer aren't
imported.

You can use the following SQL script on your source MySQL database to list the stored objects that have the
unsupported definer.

```
-- This SQL query lists routines with `rdsadmin`@`localhost` as the definer.

SELECT
    ROUTINE_SCHEMA,
    ROUTINE_NAME
FROM
    information_schema.routines
WHERE
    definer = 'rdsadmin@localhost';

-- This SQL query lists triggers with `rdsadmin`@`localhost` as the definer.

SELECT
    TRIGGER_SCHEMA,
    TRIGGER_NAME,
    DEFINER
FROM
    information_schema.triggers
WHERE
    DEFINER = 'rdsadmin@localhost';

-- This SQL query lists events with `rdsadmin`@`localhost` as the definer.

SELECT
    EVENT_SCHEMA,
    EVENT_NAME
FROM
    information_schema.events
WHERE
    DEFINER = 'rdsadmin@localhost';

-- This SQL query lists views with `rdsadmin`@`localhost` as the definer.
SELECT
    TABLE_SCHEMA,
    TABLE_NAME
FROM
    information_schema.views
WHERE
    DEFINER = 'rdsadmin@localhost';
```

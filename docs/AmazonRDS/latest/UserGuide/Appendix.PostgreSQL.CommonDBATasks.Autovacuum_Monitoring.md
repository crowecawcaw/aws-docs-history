# Installing autovacuum monitoring and diagnostic tools in RDS for PostgreSQL

The `postgres_get_av_diag()` function is currently available in the following
RDS for PostgreSQL versions:

- 17.2 and higher 17 versions
- 16.7 and higher 16 versions
- 15.11 and higher 15 versions
- 14.16 and higher 14 versions
- 13.19 and higher 13 versions
  In order to use `postgres_get_av_diag()`, create the `rds_tools`
  extension.

```
postgres=> CREATE EXTENSION rds_tools ;
CREATE EXTENSION
```

Verify that the extension is installed.

```
postgres=> \dx rds_tools
             List of installed extensions
   Name    | Version |  Schema   |                    Description
 ----------+---------+-----------+----------------------------------------------------------
 rds_tools |   1.8   | rds_tools | miscellaneous administrative functions for RDS PostgreSQL
 1 row
```

Verify that the function is created.

```
postgres=> SELECT
    proname function_name,
    pronamespace::regnamespace function_schema,
    proowner::regrole function_owner
FROM
    pg_proc
WHERE
    proname = 'postgres_get_av_diag';
    function_name     | function_schema | function_owner
----------------------+-----------------+----------------
 postgres_get_av_diag | rds_tools       | rds_superuser
(1 row)
```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Use SHOW commands

If the driver metadata API doesn't cover your use case, you can use
Amazon Redshift `SHOW` commands to retrieve metadata. `SHOW`
commands are optimized for fast metadata retrieval. They're useful when you
need metadata in an interactive SQL session, or when your application connects
through a client that doesn't expose the driver metadata API.

The following `SHOW` commands are supported for common discovery operations:

- [SHOW DATABASES](../dg/r_SHOW_DATABASES.md "../dg/r_SHOW_DATABASES.md")
- [SHOW SCHEMAS](../dg/r_SHOW_SCHEMAS.md "../dg/r_SHOW_SCHEMAS.md")
- [SHOW TABLES](../dg/r_SHOW_TABLES.md "../dg/r_SHOW_TABLES.md")
- [SHOW COLUMNS](../dg/r_SHOW_COLUMNS.md "../dg/r_SHOW_COLUMNS.md")
- [SHOW CONSTRAINTS](../dg/r_SHOW_CONSTRAINTS.md "../dg/r_SHOW_CONSTRAINTS.md")
- [SHOW GRANTS](../dg/r_SHOW_GRANTS.md "../dg/r_SHOW_GRANTS.md")
- [SHOW FUNCTIONS](../dg/r_SHOW_FUNCTIONS.md "../dg/r_SHOW_FUNCTIONS.md")
- [SHOW PROCEDURES](../dg/r_SHOW_PROCEDURES.md "../dg/r_SHOW_PROCEDURES.md")
- [SHOW PARAMETERS](../dg/r_SHOW_PARAMETERS.md "../dg/r_SHOW_PARAMETERS.md")

## Examples

```
`SHOW SCHEMAS FROM DATABASE dev;`
`database_name | schema_name | schema_owner | schema_type | schema_acl | source_database | schema_option
---------------+----------------------+--------------+-------------+-----------------------------+-----------------+---------------
dev | pg_automv | 1 | local | | |
dev | pg_catalog | 1 | local | jpuser=UC/jpuser~=U/jpuser | |
dev | public | 1 | local | jpuser=UC/jpuser~=UC/jpuser | |
dev | information_schema | 1 | local | jpuser=UC/jpuser~=U/jpuser | |
dev | schemad79cd6d93bf043 | 1 | local | | |`
```

```
`SHOW TABLES FROM SCHEMA dev.s1 LIKE '%view' LIMIT 1;`
`database_name | schema_name | table_name | table_type | table_acl | remarks | owner | last_altered_time | last_modified_time | dist_style | table_subtype
---------------+-------------+-------------------+------------+--------------------------------------+---------+-------+-------------------+--------------------+------------+-------------------
dev | s1 | late_binding_view | VIEW | {alice=arwdRxtDPA/alice,bob=d/alice} | | alice | | | | LATE BINDING VIEW`
```

```
`SHOW COLUMNS FROM TABLE second_db.public.t22;`
`database_name | schema_name | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | numeric_precision | numeric_scale | remarks | sort_key_type | sort_key | dist_key | encoding | collation
---------------+-------------+------------+-------------+------------------+----------------+-------------+-----------------------------+--------------------------+-------------------+---------------+---------+---------------+----------+----------+----------+-----------
 second_db | public | t22 | col1 | 1 | | YES | integer | | 32 | 0 | | INTERLEAVED | -1 | | mostly8 |
 second_db | public | t22 | col2 | 2 | | YES | character varying | 100 | | | | INTERLEAVED | 2 | | text255 | default
 second_db | public | t22 | col3 | 3 | | YES | timestamp without time zone | | | | | | 0 | | raw |
 second_db | public | t22 | col4 | 4 | | YES | numeric | | 10 | 2 | | | 0 | | az64 |`
```

For more information, see [SHOW](../dg/r_SHOW.md "../dg/r_SHOW.md") in the
_Amazon Redshift Database Developer Guide_.

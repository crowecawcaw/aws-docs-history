Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW PROCEDURES

Shows a list of procedures in a schema, along with information about the listed objects.

Each output row has columns `database_name`, `schema_name`, `procedure_name`, `number_of_arguments`, `argument_list`, `return_type`, remarks.

If more than 10,000 rows would results from SHOW PROCEDURES, then the command raises an error.

## Required permissions

To view a procedure in a Redshift schema, the current user must satisfy one of the following criteria:

- Be a superuser
- Be the owner of the procedure
- Granted USAGE privilege on the parent schema and granted EXECUTE on the procedure

## Syntax

```
SHOW PROCEDURES FROM SCHEMA
[*database\_name*.]*schema\_name*
[LIKE '*filter\_pattern*'] [LIMIT *row\_limit*]
```

## Parameters

database_name

The name of the database that contains the procedures to list.

schema_name

The name of the schema that contains the procedures to list.

filter_pattern

A valid UTF-8 character expression with a pattern to match procedure names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:

| Metacharacter | Description                                     |
| ------------- | ----------------------------------------------- |
| %             | Matches any sequence of zero or more characters |
| \_            | Matches any single character                    |

Note that the filter_pattern only matches the procedure name.

row_limit

The maximum number of rows to return. The _row_limit_ can be 0–10,000.

## Examples

The following example shows procedures from schema demo_db.demo_schema:

```
SHOW PROCEDURES FROM SCHEMA demo_db.demo_schema;
 database_name | schema_name |  procedure_name   | number_of_arguments |                argument_list                 |                           return_type                            | remarks
---------------+-------------+-------------------+---------------------+----------------------------------------------+------------------------------------------------------------------+---------
 demo_db       | demo_schema | f1                |                   4 | character varying, numeric, numeric, numeric | numeric, character varying, timestamp without time zone, boolean |
 demo_db       | demo_schema | sp_get_result_set |                   2 | integer, refcursor                           | refcursor                                                        |
 demo_db       | demo_schema | sp_process_data   |                   2 | numeric, numeric                             | numeric, character varying                                       |
```

The following example shows procedures from schema demo_schema with names ending in 'data':

```
SHOW PROCEDURES FROM SCHEMA demo_schema like '%data';
 database_name | schema_name | procedure_name  | number_of_arguments |  argument_list   |        return_type         | remarks
---------------+-------------+-----------------+---------------------+------------------+----------------------------+---------
 demo_db       | demo_schema | sp_process_data |                   2 | numeric, numeric | numeric, character varying |
```

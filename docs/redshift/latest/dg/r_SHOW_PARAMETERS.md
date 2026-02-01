Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW PARAMETERS

Shows a list of parameters for a function/procedure, along with some information about the parameters.

Each output row has columns database_name, schema_name, procedure_name or function_name, parameter_name, ordinal_position, parameter_type (IN/OUT), data_type, character_maximum_length, numeric_precision, numeric_scale, and remarks.

## Required permissions

To view a function/procedure in a redshift schema, the current user must satisfy one of the following criteria:

- Be a superuser
- Be the owner of the function
- Granted USAGE privilege on the parent schema and granted EXECUTE on the function

## Syntax

```
SHOW PARAMETERS OF {FUNCTION| PROCEDURE}
[*database\_name*.]*schema\_name*.*function\_name*(*argtype* [, ...] )
[LIKE '*filter\_pattern*'];
```

## Parameters

_database_name_

The name of the database that contains the function to list.

_schema_name_

The name of the schema that contains the function to list.

_filter_pattern_

A valid UTF-8 character expression with a pattern to match table names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:

| Metacharacter | Description                                     |
| ------------- | ----------------------------------------------- |
| %             | Matches any sequence of zero or more characters |
| \_            | Matches any single character                    |

## Examples

The following example shows parameters of procedure demo_db.demo_schema.f1:

```
SHOW PARAMETERS OF PROCEDURE demo_db.demo_schema.f1(VARCHAR, DECIMAL, DECIMAL, DECIMAL);
 database_name | schema_name | procedure_name |  parameter_name  | ordinal_position | parameter_type |          data_type          | character_maximum_length | numeric_precision | numeric_scale
---------------+-------------+----------------+------------------+------------------+----------------+-----------------------------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f1             | operation        |                1 | IN             | character varying           |                       10 |                   |
 demo_db       | demo_schema | f1             | value1           |                2 | IN             | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | value2           |                3 | IN             | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | result           |                4 | INOUT          | numeric                     |                          |                18 |             0
 demo_db       | demo_schema | f1             | operation_status |                5 | OUT            | character varying           |                       50 |                   |
 demo_db       | demo_schema | f1             | calculation_time |                6 | OUT            | timestamp without time zone |                          |                   |
 demo_db       | demo_schema | f1             | is_successful    |                7 | OUT            | boolean                     |                          |                   |
```

The following example shows parameters of procedure demo_schema.f1 with names starting with 'val':

```
SHOW PARAMETERS OF PROCEDURE demo_schema.f1(VARCHAR, DECIMAL, DECIMAL, DECIMAL) like 'val%';
 database_name | schema_name | procedure_name | parameter_name | ordinal_position | parameter_type | data_type | character_maximum_length | numeric_precision | numeric_scale
---------------+-------------+----------------+----------------+------------------+----------------+-----------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f1             | value1         |                2 | IN             | numeric   |                          |                18 |             0
 demo_db       | demo_schema | f1             | value2         |                3 | IN             | numeric   |                          |                18 |             0
```

The following example shows parameters of function demo_schema.f2:

```
SHOW PARAMETERS OF FUNCTION demo_schema.f2(INT, VARCHAR, DECIMAL, DATE, TIMESTAMP, BOOLEAN);
 database_name | schema_name | function_name | parameter_name  | ordinal_position | parameter_type |          data_type          | character_maximum_length | numeric_precision | numeric_scale
---------------+-------------+---------------+-----------------+------------------+----------------+-----------------------------+--------------------------+-------------------+---------------
 demo_db       | demo_schema | f2            |                 |                0 | RETURN         | character varying           |                       -1 |                   |
 demo_db       | demo_schema | f2            | int_param       |                1 | IN             | integer                     |                          |                32 |             0
 demo_db       | demo_schema | f2            | varchar_param   |                2 | IN             | character varying           |                       -1 |                   |
 demo_db       | demo_schema | f2            | decimal_param   |                3 | IN             | numeric                     |                          |                   |
 demo_db       | demo_schema | f2            | date_param      |                4 | IN             | date                        |                          |                   |
 demo_db       | demo_schema | f2            | timestamp_param |                5 | IN             | timestamp without time zone |                          |                   |
 demo_db       | demo_schema | f2            | boolean_param   |                6 | IN             | boolean                     |                          |                   |
```

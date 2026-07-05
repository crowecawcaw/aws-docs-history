Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SHOW FUNCTIONS

Shows a list of functions in a schema, along with information about the listed objects.

Each output row has columns database\_name, schema\_name, function\_name, number\_of\_arguments, argument\_list, return\_type, remarks.

If more than 10,000 rows would results from SHOW FUNCTIONS, then the command raises an error.

## Required permissions

To view a function in a Redshift schema, the current user must satisfy one of the following criteria:

- Be a superuser
- Be the owner of the function
- Granted USAGE privilege on the parent schema and granted EXECUTE on the function

## Syntax

```
SHOW FUNCTIONS FROM SCHEMA
[*database\_name*.]*schema\_name*
[LIKE '*filter\_pattern*'] [LIMIT *row\_limit*]
```

## Parameters

_database\_name_

The name of the database that contains the functions to list.

_schema\_name_

The name of the schema that contains the functions to list.

_filter\_pattern_

A valid UTF-8 character expression with a pattern to match function names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:

| Metacharacter | Description                                     |
| ------------- | ----------------------------------------------- |
| %             | Matches any sequence of zero or more characters |
| \_            | Matches any single character                    |

Note that the filter\_pattern only matches the function name.

_row\_limit_

The maximum number of rows to return. The _row\_limit_ can be 0–10,000.

## Examples

The following example shows functions from schema demo\_db.demo\_schema:

```
SHOW FUNCTIONS FROM SCHEMA demo_db.demo_schema;
 database_name | schema_name |    function_name     | number_of_arguments |                                  argument_list                                  |    return_type    | remarks
---------------+-------------+----------------------+---------------------+---------------------------------------------------------------------------------+-------------------+---------
 demo_db       | demo_schema | f2                   |                   6 | integer, character varying, numeric, date, timestamp without time zone, boolean | character varying |
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer                                                                | numeric           |
 demo_db       | demo_schema | f_days_between       |                   2 | date, date                                                                      | integer           |
```

The following example shows functions from schema demo\_schema with names ending in 'discount':

```
SHOW FUNCTIONS FROM SCHEMA demo_schema like '%discount';
 database_name | schema_name |    function_name     | number_of_arguments |  argument_list   | return_type | remarks
---------------+-------------+----------------------+---------------------+------------------+-------------+---------
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer | numeric     |
```

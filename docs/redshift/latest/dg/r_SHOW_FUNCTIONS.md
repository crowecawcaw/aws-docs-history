Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW FUNCTIONS

Shows a list of functions in a schema, along with information about the listed objects.

Each output row has columns database_name, schema_name, function_name, number_of_arguments, argument_list, return_type, remarks.

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

_database_name_

The name of the database that contains the functions to list.

_schema_name_

The name of the schema that contains the functions to list.

_filter_pattern_

A valid UTF-8 character expression with a pattern to match function names. The LIKE option performs a case-sensitive match that supports the following pattern-matching metacharacters:

| Metacharacter | Description                                     |
| ------------- | ----------------------------------------------- |
| %             | Matches any sequence of zero or more characters |
| \_            | Matches any single character                    |

Note that the filter_pattern only matches the function name.

_row_limit_

The maximum number of rows to return. The _row_limit_ can be 0–10,000.

## Examples

The following example shows functions from schema demo_db.demo_schema:

```
SHOW FUNCTIONS FROM SCHEMA demo_db.demo_schema;
 database_name | schema_name |    function_name     | number_of_arguments |                                  argument_list                                  |    return_type    | remarks
---------------+-------------+----------------------+---------------------+---------------------------------------------------------------------------------+-------------------+---------
 demo_db       | demo_schema | f2                   |                   6 | integer, character varying, numeric, date, timestamp without time zone, boolean | character varying |
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer                                                                | numeric           |
 demo_db       | demo_schema | f_days_between       |                   2 | date, date                                                                      | integer           |
```

The following example shows functions from schema demo_schema with names ending in 'discount':

```
SHOW FUNCTIONS FROM SCHEMA demo_schema like '%discount';
 database_name | schema_name |    function_name     | number_of_arguments |  argument_list   | return_type | remarks
---------------+-------------+----------------------+---------------------+------------------+-------------+---------
 demo_db       | demo_schema | f_calculate_discount |                   2 | numeric, integer | numeric     |
```

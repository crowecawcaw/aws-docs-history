Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_REDSHIFT_FUNCTIONS

Use SVV_REDSHIFT_FUNCTIONS to view a list of all functions that a user has access to.
This set of functions includes the functions on the cluster and the functions from
datashares provided by remote clusters.

SVV_REDSHIFT_FUNCTIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name   | Data type    | Description                                                                                                 |
| ------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| database_name | varchar(128) | The name of the database where the cluster that<br>has these functions exists.                              |
| schema_name   | varchar(128) | The name of the schema that specifies a given<br>function.                                                  |
| function_name | varchar(128) | The name of a specified function.                                                                           |
| function_type | varchar(128) | The type of function. Possible values are regular<br>functions, aggregate functions, and stored procedures. |
| argument_type | varchar(512) | A string that represents the type of a<br>function's input argument.                                        |
| result_type   | varchar(128) | The data type of a function's return value.                                                                 |

## Sample query

The following example returns the output of SVV_REDSHIFT_FUNCTIONS.

```
SELECT *
FROM svv_redshift_functions
WHERE database_name = 'tickit_db'
    AND SCHEMA_NAME = 'public'
ORDER BY function_name
LIMIT 5;

database_name | schema_name |      function_name    |  function_type   |   argument_type  | result_type
--------------+-------------+-----------------------+------------------+------------------+-------------
   tickit_db  |    public   |     shared_function   | REGULAR FUNCTION | integer, integer |   integer
```

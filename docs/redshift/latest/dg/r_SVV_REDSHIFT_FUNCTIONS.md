Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SVV\_REDSHIFT\_FUNCTIONS

Use SVV\_REDSHIFT\_FUNCTIONS to view a list of all functions that a user has access to.
This set of functions includes the functions on the cluster and the functions from
datashares provided by remote clusters.

SVV\_REDSHIFT\_FUNCTIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

For more information about best practices when querying system tables and views, see
[Querying System Tables](../mgmt/discovering-metadata-system-tables.md "../mgmt/discovering-metadata-system-tables.md").

###### Note

Use the [SHOW FUNCTIONS](r_SHOW_FUNCTIONS.md "r_SHOW_FUNCTIONS.md") command for function discovery. SHOW FUNCTIONS works consistently across
local, datashare, and external catalog contexts and is updated as new features are released.
For more information, see [Best practices for discovering metadata](../mgmt/best-practices-discovering-metadata.md "../mgmt/best-practices-discovering-metadata.md").

## Table columns

| Column name    | Data type    | Description                                                                                                 |
| -------------- | ------------ | ----------------------------------------------------------------------------------------------------------- |
| database\_name | varchar(128) | The name of the database where the cluster that<br>has these functions exists.                              |
| schema\_name   | varchar(128) | The name of the schema that specifies a given<br>function.                                                  |
| function\_name | varchar(128) | The name of a specified function.                                                                           |
| function\_type | varchar(128) | The type of function. Possible values are regular<br>functions, aggregate functions, and stored procedures. |
| argument\_type | varchar(512) | A string that represents the type of a<br>function's input argument.                                        |
| result\_type   | varchar(128) | The data type of a function's return value.                                                                 |

## Sample query

The following example returns the output of SVV\_REDSHIFT\_FUNCTIONS.

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

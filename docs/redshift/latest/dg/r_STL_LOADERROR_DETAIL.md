Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_LOADERROR_DETAIL

Displays a log of data parse errors that occurred while using a COPY command to load
tables. To conserve disk space, a maximum of 20 errors per node slice are logged for
each load operation.

A parse error occurs when Amazon Redshift cannot parse a field in a data row while loading
it into a table. For example, if a table column is expecting an integer data type and
the data file contains a string of letters in that field, it causes a parse
error.

Query STL_LOADERROR_DETAIL for additional details, such as the exact data row and
column where a parse error occurred, after you query [STL_LOAD_ERRORS](r_STL_LOAD_ERRORS.md "r_STL_LOAD_ERRORS.md") to find out general information about the
error.

The STL_LOADERROR_DETAIL view contains all data columns including and prior to the
column where the parse error occurred. Use the VALUE field to see the data value that
was actually parsed in this column, including the columns that parsed correctly up to
the error.

This view is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_LOADERROR_DETAIL only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_LOAD_ERROR_DETAIL](SYS_LOAD_ERROR_DETAIL.md "SYS_LOAD_ERROR_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name | Data type       | Description                                                                                                                                                                                                 |
| ----------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer         | ID of the user who generated the entry.                                                                                                                                                                     |
| slice       | integer         | Slice where the error occurred.                                                                                                                                                                             |
| session     | integer         | Session ID for the session performing the load.                                                                                                                                                             |
| query       | integer         | Query ID. The query column can be used to join other system tables and views.                                                                                                                               |
| filename    | character(256)  | Complete path to the input file for the load.                                                                                                                                                               |
| line_number | bigint          | Line number in the load file with the error.                                                                                                                                                                |
| field       | integer         | Field with the error.                                                                                                                                                                                       |
| colname     | character(1024) | Column name.                                                                                                                                                                                                |
| value       | character(1024) | Parsed data value of the field. (May be<br>truncated.) Multibyte characters in the load data are replaced with<br>a period.                                                                                 |
| is_null     | integer         | Whether or not the parsed value is null.                                                                                                                                                                    |
| type        | character(10)   | Data type of the field.                                                                                                                                                                                     |
| col_length  | character(10)   | Column length, if applicable. This field is<br>populated when the data type has a limit length. For example, for a<br>column with a data type of "character(3)", this column will contain<br>the value "3". |

## Sample query

The following query joins STL_LOAD_ERRORS to STL_LOADERROR_DETAIL to view the
details of a parse error that occurred while loading the EVENT table, which has a
table ID of 100133:

```
select d.query, d.line_number, d.value,
le.raw_line, le.err_reason
from stl_loaderror_detail d, stl_load_errors le
where
d.query = le.query
and tbl = 100133;
```

The following sample output shows the columns that loaded successfully, including
the column with the error. In this example, two columns successfully loaded before
the parse error occurred in the third column, where a character string was
incorrectly parsed for a field expecting an integer. Because the field expected an
integer, it parsed the string "aaa", which is uninitialized data, as a null and
generated a parse error. The output shows the raw value, parsed value, and error
reason:

```
query  | line_number | value | raw_line | err_reason
-------+-------------+-------+----------+----------------
4      |      3      |  1201 |  1201    | Invalid digit
4      |      3      |   126 |   126    | Invalid digit
4      |      3      |       |   aaa    | Invalid digit
(3 rows)
```

When a query joins STL_LOAD_ERRORS and STL_LOADERROR_DETAIL, it displays an error
reason for each column in the data row, which simply means that an error occurred in
that row. The last row in the results is the actual column where the parse error
occurred.

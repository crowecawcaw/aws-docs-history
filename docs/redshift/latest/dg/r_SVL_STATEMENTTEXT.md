Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_STATEMENTTEXT

Use the SVL_STATEMENTTEXT view to get a complete record of all of the SQL commands
that have been run on the system.

The SVL_STATEMENTTEXT view contains the union of all of the rows in the [STL_DDLTEXT](r_STL_DDLTEXT.md "r_STL_DDLTEXT.md"), [STL_QUERYTEXT](r_STL_QUERYTEXT.md "r_STL_QUERYTEXT.md"), and [STL_UTILITYTEXT](r_STL_UTILITYTEXT.md "r_STL_UTILITYTEXT.md") tables. This view
also includes a join to the STL_QUERY table.

SVL_STATEMENTTEXT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_QUERY_HISTORY](SYS_QUERY_HISTORY.md "SYS_QUERY_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type      | Description                                                                                                                                                                                                |
| ----------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid      | integer        | ID of user who generated entry.                                                                                                                                                                            |
| xid         | bigint         | Transaction ID associated with the statement.                                                                                                                                                              |
| pid         | integer        | Process ID for the statement.                                                                                                                                                                              |
| label       | character(320) | Either the name of the file used to run the query<br>or a label defined with a SET QUERY_GROUP command. If the query is<br>not file-based or the QUERY_GROUP parameter is not set, this field<br>is blank. |
| starttime   | timestamp      | Exact time when the statement started executing,<br>with 6 digits of precision for fractional seconds. For example:<br>`2009-06-12 11:29:19.131358`                                                        |
| endtime     | timestamp      | Exact time when the statement finished executing,<br>with 6 digits of precision for fractional seconds. For example:<br>`2009-06-12 11:29:19.193640`                                                       |
| sequence    | integer        | When a single statement contains more than 200<br>characters, additional rows are logged for that statement. Sequence<br>0 is the first row, 1 is the second, and so on.                                   |
| type        | varchar(10)    | Type of SQL statement:<br>`QUERY`, `DDL`, or<br>`UTILITY`.                                                                                                                                                 |
| text        | character(200) | SQL text, in 200-character increments. This field might contain special characters such as backslash (`\\`) and newline (`\n`).                                                                            |

## Sample query

The following query returns DDL statements that were run on June 16th, 2009:

```
select starttime, type, rtrim(text) from svl_statementtext
where starttime like '2009-06-16%' and type='DDL' order by starttime asc;

starttime                  | type |              rtrim
---------------------------|------|--------------------------------
2009-06-16 10:36:50.625097 | DDL  | create table ddltest(c1 int);
2009-06-16 15:02:16.006341 | DDL  | drop view alltickitjoin;
2009-06-16 15:02:23.65285  | DDL  | drop table sales;
2009-06-16 15:02:24.548928 | DDL  | drop table listing;
2009-06-16 15:02:25.536655 | DDL  | drop table event;
...
```

### Reconstructing stored

SQL

To reconstruct the SQL stored in the `text` column of SVL_STATEMENTTEXT,
run a SELECT statement to create SQL from 1 or more parts in the
`text` column. Before running the reconstructed SQL, replace
any (`\n`) special characters with a new line. The result of the
following SELECT statement is rows of reconstructed SQL in the `query_statement` field.

```
select LISTAGG(CASE WHEN LEN(RTRIM(text)) = 0 THEN text ELSE RTRIM(text) END, '') within group (order by sequence) AS query_statement
from SVL_STATEMENTTEXT where pid=pg_backend_pid();
```

For example, the following query selects 3 columns. The query itself is longer
than 200 characters and is stored in parts in SVL_STATEMENTTEXT.

```
select
1 AS a0123456789012345678901234567890123456789012345678901234567890,
2 AS b0123456789012345678901234567890123456789012345678901234567890,
3 AS b012345678901234567890123456789012345678901234
FROM stl_querytext;
```

In this example, the query is stored in 2 parts (rows) in the `text` column of SVL_STATEMENTTEXT.

```
select sequence, text from SVL_STATEMENTTEXT where pid = pg_backend_pid() order by starttime, sequence;
```

```

 sequence |                                                                                             text
----------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        0 | select\n1 AS a0123456789012345678901234567890123456789012345678901234567890,\n2 AS b0123456789012345678901234567890123456789012345678901234567890,\n3 AS b012345678901234567890123456789012345678901234
        1 | \nFROM stl_querytext;
```

To reconstruct the SQL stored in STL_STATEMENTTEXT, run the following SQL.

```
select LISTAGG(CASE WHEN LEN(RTRIM(text)) = 0 THEN text ELSE RTRIM(text) END, '') within group (order by sequence) AS text
from SVL_STATEMENTTEXT where pid=pg_backend_pid();

```

To use the resulting reconstructed SQL in your client, replace any (`\n`) special characters with a
new line.

```

                                                                                                             text
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 select\n1 AS a0123456789012345678901234567890123456789012345678901234567890,\n2 AS b0123456789012345678901234567890123456789012345678901234567890,\n3 AS b012345678901234567890123456789012345678901234\nFROM stl_querytext;

```

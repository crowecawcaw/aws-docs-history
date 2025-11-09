Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_LOAD_ERRORS

Displays the records of all Amazon Redshift load errors.

STL_LOAD_ERRORS contains a history of all Amazon Redshift load errors. See [Load error reference](r_Load_Error_Reference.md "r_Load_Error_Reference.md") for a
comprehensive list of possible load errors and explanations.

Query [STL_LOADERROR_DETAIL](r_STL_LOADERROR_DETAIL.md "r_STL_LOADERROR_DETAIL.md")
for additional details, such as the exact data row and column where a parse error
occurred, after you query STL_LOAD_ERRORS to find out general information about the
error.

STL_LOAD_ERRORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

###### Note

STL_LOAD_ERRORS only contains queries run on main provisioned clusters. It doesn't contain queries run on concurrency scaling clusters
or on serverless namespaces.
To access explain plans for queries run on both main clusters, concurrency scaling clusters, and serverless namespaces, we recommend that you use the SYS monitoring view
[SYS_LOAD_ERROR_DETAIL](SYS_LOAD_ERROR_DETAIL.md "SYS_LOAD_ERROR_DETAIL.md")
. The data in the SYS monitoring view is formatted to be easier to use and understand.

## Table columns

| Column name     | Data type       | Description                                                                                                                                                                                                                           |
| --------------- | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid          | integer         | ID of the user who generated the entry.                                                                                                                                                                                               |
| slice           | integer         | Slice where the error occurred.                                                                                                                                                                                                       |
| tbl             | integer         | Table ID.                                                                                                                                                                                                                             |
| starttime       | timestamp       | Start time in UTC for the load.                                                                                                                                                                                                       |
| session         | integer         | Session ID for the session performing the load.                                                                                                                                                                                       |
| query           | integer         | Query ID. The query column can be used to join other system tables and views.                                                                                                                                                         |
| filename        | character(256)  | Complete path to the input file for the load.                                                                                                                                                                                         |
| line_number     | bigint          | Line number in the load file with the error. For<br>COPY from JSON, the line number of the last line of the JSON object<br>with the error.                                                                                            |
| colname         | character(127)  | Field with the error.                                                                                                                                                                                                                 |
| type            | character(10)   | Data type of the field.                                                                                                                                                                                                               |
| col_length      | character(10)   | Column length, if applicable. This field is<br>populated when the data type has a limit length. For example, for a<br>column with a data type of "character(3)", this column will contain<br>the value "3".                           |
| position        | integer         | Position of the error in the field.                                                                                                                                                                                                   |
| raw_line        | character(1024) | Raw load data that contains the error. Multibyte<br>characters in the load data are replaced with a period.                                                                                                                           |
| raw_field_value | char(1024)      | The pre-parsing value for the field "colname" that<br>lead to the parsing error.                                                                                                                                                      |
| err_code        | integer         | Error code.                                                                                                                                                                                                                           |
| err_reason      | character(100)  | Explanation for the error.                                                                                                                                                                                                            |
| is_partial      | integer         | Value that if true (1) indicates the input file is<br>split into ranges during a COPY operation. If this value is false<br>(0), the input file isn't split.                                                                           |
| start_offset    | bigint          | Value that, if the input file is split during a<br>COPY operation, indicates the offset value of the split (in bytes). If the line number in the file is unknown, the line number is -1. If<br>the file isn't split, this value is 0. |
| copy_job_id     | bigint          | The copy job identifier. A `0` indicates no job identifier.                                                                                                                                                                           |

## Sample queries

The following query joins STL_LOAD_ERRORS to STL_LOADERROR_DETAIL to view the
details errors that occurred during the most recent load.

```
select d.query, substring(d.filename,14,20),
d.line_number as line,
substring(d.value,1,16) as value,
substring(le.err_reason,1,48) as err_reason
from stl_loaderror_detail d, stl_load_errors le
where d.query = le.query
and d.query = pg_last_copy_id();

 query |    substring      | line |  value   |              err_reason
-------+-------------------+------+----------+----------------------------
    558| allusers_pipe.txt |  251 | 251      | String contains invalid or
                                               unsupported UTF8 code
    558| allusers_pipe.txt |  251 | ZRU29FGR | String contains invalid or
                                               unsupported UTF8 code
    558| allusers_pipe.txt |  251 | Kaitlin  | String contains invalid or
                                               unsupported UTF8 code
    558| allusers_pipe.txt |  251 | Walter   | String contains invalid or
                                               unsupported UTF8 code

```

The following example uses STL_LOAD_ERRORS with STV_TBL_PERM to create a new view,
and then uses that view to determine what errors occurred while loading data into
the EVENT table:

```
create view loadview as
(select distinct tbl, trim(name) as table_name, query, starttime,
trim(filename) as input, line_number, colname, err_code,
trim(err_reason) as reason
from stl_load_errors sl, stv_tbl_perm sp
where sl.tbl = sp.id);
```

Next, the following query actually returns the last error that occurred while
loading the EVENT table:

```
select table_name, query, line_number, colname, starttime,
trim(reason) as error
from loadview
where table_name ='event'
order by line_number limit 1;
```

The query returns the last load error that occurred for the EVENT table. If no
load errors occurred, the query returns zero rows. In this example, the query
returns a single error:

```
 table_name | query | line_number | colname | error | starttime
------+-----+----+----+--------------------------------------------------------+----------------------
event | 309 |  0 |  5 | Error in Timestamp value or format [%Y-%m-%d %H:%M:%S] | 2014-04-22 15:12:44

(1 row)
```

In cases where the COPY command automatically splits large, uncompressed, text-delimited file data to facilitate parallelism, the _line_number_,
_is_partial_, and _start_offset_ columns show information pertaining to splits. (The line number can be unknown in cases where the line number from the original file is unavailable.)

```
--scan ranges information
SELECT line_number, POSITION, btrim(raw_line), btrim(raw_field_value),
btrim(err_reason), is_partial, start_offset FROM stl_load_errors
WHERE query = pg_last_copy_id();

--result
-1,51,"1008771|13463413|463414|2|28.00|38520.72|0.06|0.07|NO|1998-08-30|1998-09-25|1998-09-04|TAKE BACK RETURN|RAIL|ans cajole sly","NO","Char length exceeds DDL length",1,67108864

```

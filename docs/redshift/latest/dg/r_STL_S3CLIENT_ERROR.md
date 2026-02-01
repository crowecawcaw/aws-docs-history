Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_S3CLIENT_ERROR

Records errors encountered by a slice while loading a file from Amazon S3.

Use the STL_S3CLIENT_ERROR to find details for errors encountered while transferring
data from Amazon S3 as part of a COPY command.

STL_S3CLIENT_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name  | Data type       | Description                                                                                                                                                         |
| ------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid       | integer         | ID of the user who generated the entry.                                                                                                                             |
| query        | integer         | Query ID. The query column can be used to join other system tables and views. The query ID -1 is for internal use.                                                  |
| sliceid      | integer         | Number that identifies the slice where the query was running.                                                                                                       |
| recordtime   | timestamp       | Time the record is logged.                                                                                                                                          |
| pid          | integer         | Process ID. All of the queries in a session are<br>run in the same process, so this value remains constant if you run a<br>series of queries in the same session.   |
| http_method  | character(64)   | HTTP method name corresponding to the Amazon S3<br>request.                                                                                                         |
| bucket       | character(64)   | Amazon S3 bucket name.                                                                                                                                              |
| key          | character(256)  | Key corresponding to the Amazon S3 object.                                                                                                                          |
| error        | character(1024) | Error message.                                                                                                                                                      |
| is_partial   | integer         | Value that, if true (1), indicates the input file<br>is split into ranges during a COPY operation. If this value is false<br>(0), the input file isn't split.       |
| start_offset | bigint          | Value that, if the input file is split during a<br>COPY operation, indicates the offset value of the split (in bytes).<br>If the file isn't split, this value is 0. |

## Usage notes

If you see multiple errors with "Connection timed out", you might have a
networking issue. If you're using Enhanced VPC Routing, verify that you have a valid
network path between your cluster's VPC and your data resources. For more
information, see [Amazon Redshift Enhanced
VPC Routing](../mgmt/enhanced-vpc-routing.md "../mgmt/enhanced-vpc-routing.md").

## Sample query

The following query returns the errors from COPY commands completed during the
current session.

```
select query, sliceid, substring(key from 1 for 20) as file,
substring(error from 1 for 35) as error
from stl_s3client_error
where pid = pg_backend_pid()
order by query desc;
```

Result

```

 query  | sliceid |     file           |              error
--------+---------+--------------------+------------------------------------
 362228 |      12 | part.tbl.25.159.gz | transfer closed with 1947655 bytes
 362228 |      24 | part.tbl.15.577.gz | transfer closed with 1881910 bytes
 362228 |       7 | part.tbl.22.600.gz | transfer closed with 700143 bytes r
 362228 |      22 | part.tbl.3.34.gz   | transfer closed with 2334528 bytes
 362228 |      11 | part.tbl.30.274.gz | transfer closed with 699031 bytes r
 362228 |      30 | part.tbl.5.509.gz  | Unknown SSL protocol error in conne
 361999 |      10 | part.tbl.23.305.gz | transfer closed with 698959 bytes r
 361999 |      19 | part.tbl.26.582.gz | transfer closed with 1881458 bytes
 361999 |       4 | part.tbl.15.629.gz | transfer closed with 2275907 bytes
 361999 |      20 | part.tbl.6.456.gz  | transfer closed with 692162 bytes r
(10 rows)

```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STL\_S3CLIENT

Records transfer time and other performance metrics.

Use the STL\_S3CLIENT table to find the time spent transferring data from Amazon S3.

STL\_S3CLIENT is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name           | Data type      | Description                                                                                                                                                         |
| --------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| userid                | integer        | ID of the user who generated the entry.                                                                                                                             |
| query                 | integer        | Query ID. The query column can be used to join other system tables and views.                                                                                       |
| slice                 | integer        | Number that identifies the slice where the query was running.                                                                                                       |
| recordtime            | timestamp      | Time the record is logged.                                                                                                                                          |
| pid                   | integer        | Process ID. All of the queries in a session are<br>run in the same process, so this value remains constant if you run a<br>series of queries in the same session.   |
| http\_method          | character(64)  | HTTP method name corresponding to the Amazon S3<br>request.                                                                                                         |
| bucket                | character(64)  | S3 bucket name.                                                                                                                                                     |
| key                   | character(256) | Key corresponding to the Amazon S3 object.                                                                                                                          |
| transfer\_size        | bigint         | Number of bytes transferred.                                                                                                                                        |
| data\_size            | bigint         | Number of bytes of data. This value is the same as<br>transfer\_size for uncompressed data. If compression was used, this<br>is the size of the uncompressed data.  |
| start\_time           | bigint         | Time when the transfer began (in<br>microseconds since January 1, 2000).                                                                                            |
| end\_time             | bigint         | Time when the transfer ended (in<br>microseconds since January 1, 2000).                                                                                            |
| transfer\_time        | bigint         | Time taken by the transfer (in microseconds).                                                                                                                       |
| compression\_time     | bigint         | Portion of the transfer time that was spent<br>uncompressing data (in microseconds).                                                                                |
| connect\_time         | bigint         | Time from the start until the connect to the<br>remote server was completed (in microseconds).                                                                      |
| app\_connect\_time    | bigint         | Time from the start until the SSL<br>connect/handshake with the remote host was completed (in<br>microseconds).                                                     |
| retries               | bigint         | Number of times the transfer was retried.                                                                                                                           |
| request\_id           | char(32)       | Request ID from Amazon S3 HTTP response header                                                                                                                      |
| extended\_request\_id | char(128)      | Extended request ID from Amazon S3 HTTP header response<br>(x-amz-id-2).                                                                                            |
| ip\_address           | char(64)       | IP address of the server (ip V4 or V6).                                                                                                                             |
| is\_partial           | integer        | Value that if true (1) indicates the input file is<br>split into ranges during a COPY operation. If this value is false<br>(0), the input file isn't split.         |
| start\_offset         | bigint         | Value that, if the input file is split during a<br>COPY operation, indicates the offset value of the split (in bytes).<br>If the file isn't split, this value is 0. |
| query\_uuid           | character(36)  | A globally unique identifier (UUID) of the query.                                                                                                                   |

## Sample query

The following query returns the time taken to load files using a COPY
command.

```
select slice, key, transfer_time
from stl_s3client
where query = pg_last_copy_id();
```

Result

```
 slice |   key                       | transfer_time
 ------+-----------------------------+---------------
     0 | listing10M0003_part_00      |    16626716
     1 | listing10M0001_part_00      |    12894494
     2 | listing10M0002_part_00      |    14320978
     3 | listing10M0000_part_00      |    11293439
  3371 | prefix=listing10M;marker=   |       99395
```

The following query converts the `start_time` and `end_time` to a timestamp.

```
select userid,query,slice,pid,recordtime,start_time,end_time,
'2000-01-01'::timestamp + (start_time/1000000.0)* interval '1 second' as start_ts,
'2000-01-01'::timestamp + (end_time/1000000.0)* interval '1 second' as end_ts
from stl_s3client where query> -1 limit 5;
```

```

 userid | query | slice |  pid  |         recordtime         |   start_time    |    end_time     |          start_ts          |           end_ts
--------+-------+-------+-------+----------------------------+-----------------+-----------------+----------------------------+----------------------------
      0 |     0 |     0 | 23449 | 2019-07-14 16:27:17.207839 | 616436837154256 | 616436837207838 | 2019-07-14 16:27:17.154256 | 2019-07-14 16:27:17.207838
      0 |     0 |     0 | 23449 | 2019-07-14 16:27:17.252521 | 616436837208208 | 616436837252520 | 2019-07-14 16:27:17.208208 | 2019-07-14 16:27:17.25252
      0 |     0 |     0 | 23449 | 2019-07-14 16:27:17.284376 | 616436837208460 | 616436837284374 | 2019-07-14 16:27:17.20846  | 2019-07-14 16:27:17.284374
      0 |     0 |     0 | 23449 | 2019-07-14 16:27:17.285307 | 616436837208980 | 616436837285306 | 2019-07-14 16:27:17.20898  | 2019-07-14 16:27:17.285306
      0 |     0 |     0 | 23449 | 2019-07-14 16:27:17.353853 | 616436837302216 | 616436837353851 | 2019-07-14 16:27:17.302216 | 2019-07-14 16:27:17.353851

```

Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# SYS\_UNLOAD\_DETAIL

Use SYS\_UNLOAD\_DETAIL to view details of an UNLOAD operation. It records one row for
each file created by an UNLOAD statement. For example, if an UNLOAD creates 12 files,
SYS\_UNLOAD\_DETAIL will contain 12 corresponding rows.

SYS\_UNLOAD\_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type        | Description                                                       |
| --------------- | ---------------- | ----------------------------------------------------------------- |
| user\_id        | integer          | The identifier of the user who generated the<br>entry.            |
| query\_id       | integer          | The query identifier of the UNLOAD<br>command.                    |
| session\_id     | integer          | The ID of the process associated with the query<br>statement.     |
| transaction\_id | bigint           | The ID of the transaction associated with the<br>query statement. |
| file\_name      | character (1280) | The complete Amazon S3 object path for the<br>file.               |
| start\_time     | timestamp        | The time when the transaction began.                              |
| end\_time       | timestamp        | The time when the transaction completed.                          |
| line\_count     | bigint           | The number of lines (rows) unloaded to the<br>file.               |
| transfer\_size  | bigint           | The number of bytes transferred.                                  |
| file\_format    | character (10)   | The file format of the unloaded files.                            |

## Sample queries

The following query shows the unloaded query details, including format, rows, and
file count of unload command.

```
select query_id, substring(file_name, 0, 50), transfer_size, file_format from sys_unload_detail;
```

Sample output.

```

 query_id |                     substring                               | transfer_size | file_format
----------+-------------------------------------------------------------+---------------+-------------
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0000_part_00.gz  |        395886 | Text
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0001_part_00.gz  |        406444 | Text
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0002_part_00.gz  |        409431 | Text
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0003_part_00.gz  |        403051 | Text
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0004_part_00.gz  |        413592 | Text
     9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0005_part_00.gz  |        395689 | Text
(6 rows)
```

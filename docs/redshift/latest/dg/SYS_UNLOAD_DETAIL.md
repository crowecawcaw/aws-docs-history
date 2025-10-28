Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_UNLOAD_DETAIL

Use SYS_UNLOAD_DETAIL to view details of an UNLOAD operation. It records one row for
each file created by an UNLOAD statement. For example, if an UNLOAD creates 12 files,
SYS_UNLOAD_DETAIL will contain 12 corresponding rows.

SYS_UNLOAD_DETAIL is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type        | Description                                                    |
| -------------- | ---------------- | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ------ | --------- | ----------------------------------------------------------- | ------ | --------- | ----------------------------------------------------------- | ------ | --------- | ----------------------------------------------------------- | ------ | --------- | ----------------------------------------------------------- | ------ | --------- | ----------------------------------------------------------- | ------ | ----------------- |
| user_id        | integer          | The identifier of the user who generated the entry.            |
| query_id       | integer          | The query identifier of the UNLOAD command.                    |
| session_id     | integer          | The ID of the process associated with the query statement.     |
| transaction_id | bigint           | The ID of the transaction associated with the query statement. |
| file_name      | character (1280) | The complete Amazon S3 object path for the file.               |
| start_time     | timestamp        | The time when the transaction began.                           |
| end_time       | timestamp        | The time when the transaction completed.                       |
| line_count     | bigint           | The number of lines (rows) unloaded to the file.               |
| transfer_size  | bigint           | The number of bytes transferred.                               |
| file_format    | character (10)   | The file format of the unloaded files.                         | ## Sample queries The following query shows the unloaded query details, including format, rows, and file count of unload command. `select query_id, substring(file_name, 0, 50), transfer_size, file_format from sys_unload_detail;` Sample output. ``` query_id | substring | transfer_size | file_format ----------+-------------------------------------------------------------+---------------+------------- 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0000_part_00.gz | 395886 | Text 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0001_part_00.gz | 406444 | Text 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0002_part_00.gz | 409431 | Text 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0003_part_00.gz | 403051 | Text 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0004_part_00.gz | 413592 | Text 9272 | s3://amzn-s3-demo-bucket/my_unload_doc_venue0005_part_00.gz | 395689 | Text (6 rows) ``` |

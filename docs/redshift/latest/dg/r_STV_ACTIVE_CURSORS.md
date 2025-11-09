Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_ACTIVE_CURSORS

STV_ACTIVE_CURSORS displays details for currently open cursors. For more information,
see [DECLARE](declare.md "declare.md").

STV_ACTIVE_CURSORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data"). A user can only view cursors opened by that user.
A superuser can view all cursors.

## Table columns

| Column name  | Data type      | Description                                                     |
| ------------ | -------------- | --------------------------------------------------------------- |
| userid       | integer        | ID of user who generated entry.                                 |
| name         | character(256) | Cursor name.                                                    |
| xid          | bigint         | Transaction context.                                            |
| pid          | integer        | Leader process running the query.                               |
| starttime    | timestamp      | Time when the cursor was declared.                              |
| row_count    | bigint         | Number of rows in the cursor result set.                        |
| byte_count   | bigint         | Number of bytes in the cursor result set.                       |
| fetched_rows | bigint         | Number of rows currently fetched from the cursor<br>result set. |

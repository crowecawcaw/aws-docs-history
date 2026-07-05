Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STV\_ACTIVE\_CURSORS

STV\_ACTIVE\_CURSORS displays details for currently open cursors. For more information,
see [DECLARE](declare.md "declare.md").

STV\_ACTIVE\_CURSORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data"). A user can only view cursors opened by that user.
A superuser can view all cursors.

## Table columns

| Column name   | Data type      | Description                                                     |
| ------------- | -------------- | --------------------------------------------------------------- |
| userid        | integer        | ID of user who generated entry.                                 |
| name          | character(256) | Cursor name.                                                    |
| xid           | bigint         | Transaction context.                                            |
| pid           | integer        | Leader process running the query.                               |
| starttime     | timestamp      | Time when the cursor was declared.                              |
| row\_count    | bigint         | Number of rows in the cursor result set.                        |
| byte\_count   | bigint         | Number of bytes in the cursor result set.                       |
| fetched\_rows | bigint         | Number of rows currently fetched from the cursor<br>result set. |

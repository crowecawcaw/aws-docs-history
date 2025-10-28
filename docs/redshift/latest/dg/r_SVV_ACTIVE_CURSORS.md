Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVV_ACTIVE_CURSORS

SVV_ACTIVE_CURSORS displays details for currently open cursors. For more information,
see [DECLARE](declare.md "declare.md").

SVV_ACTIVE_CURSORS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data"). A user can only view cursors opened by that user.
A superuser can view all cursors.

## Table columns

| Column name                       | Data type    | Description                                                      |
| --------------------------------- | ------------ | ---------------------------------------------------------------- |
| user_id                           | integer      | The ID of the user who created the cursor.                       |
| cursor_name                       | varchar(128) | The name of the cursor.                                          |
| transaction_id                    | bigint(128)  | The ID of the transaction.                                       |
| session_id                        | integer      | The ID of the process with the active cursor.                    |
| declare_time                      | timestamp    | The time the cursor was declared.                                |
| total_bytes                       | bigint       | The size of the cursor result set, in bytes.                     |
| total_rows                        | bigint       | The number of rows in the cursor result set.                     |
| fetched_rows                      | bigint       | The number of rows currently fetched from the cursor result set. |
| cursor_storage_limit_used_percent | integer      | The percentage of disk space currently used by the cursor.       |

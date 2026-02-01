Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_CURSOR_CONFIGURATION

STV_CURSOR_CONFIGURATION displays cursor configuration constraints. For more
information, see [Cursor constraints](declare.md#declare-constraints "declare.md#declare-constraints").

STV_CURSOR_CONFIGURATION is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name            | Data type | Description                                                                                                                                     |
| ---------------------- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| current_cursor_count   | integer   | Number of cursors currently open.                                                                                                               |
| max_diskspace_usable   | integer   | Amount of disk space available for cursors, in<br>megabytes. This constraint is based on the maximum cursor result set<br>size for the cluster. |
| current_diskspace_used | integer   | Amount of disk space currently used by cursors, in<br>megabytes.                                                                                |

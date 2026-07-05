Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# STV\_CURSOR\_CONFIGURATION

STV\_CURSOR\_CONFIGURATION displays cursor configuration constraints. For more
information, see [Cursor constraints](declare.md#declare-constraints "declare.md#declare-constraints").

STV\_CURSOR\_CONFIGURATION is visible only to superusers. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type | Description                                                                                                                                     |
| ------------------------ | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| current\_cursor\_count   | integer   | Number of cursors currently open.                                                                                                               |
| max\_diskspace\_usable   | integer   | Amount of disk space available for cursors, in<br>megabytes. This constraint is based on the maximum cursor result set<br>size for the cluster. |
| current\_diskspace\_used | integer   | Amount of disk space currently used by cursors, in<br>megabytes.                                                                                |

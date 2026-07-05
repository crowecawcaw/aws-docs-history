Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# PG\_LIBRARY

Stores information about user-defined libraries.

PG\_LIBRARY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type | Description                   |
| --------------- | --------- | ----------------------------- |
| name            | name      | Library name.                 |
| language\_oid   | oid       | Reserved for system use.      |
| file\_store\_id | integer   | Reserved for system use.      |
| owner           | integer   | User ID of the library owner. |

## Example

The following example returns information for user-installed libraries.

```
select * from pg_library;

name       | language_oid | file_store_id | owner
-----------+--------------+---------------+------
f_urlparse |       108254 |          2000 |   100
```

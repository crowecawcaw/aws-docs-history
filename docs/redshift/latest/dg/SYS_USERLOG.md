Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_USERLOG

Records details for the following changes to a database user:

- Create user
- Drop user
- Alter user (rename)
- Alter user (alter properties)
  You can query this view to see information about serverless workgroups and provisioned
  clusters.

SYS_USERLOG is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name              | Data type     | Description                                                                             |
| ------------------------ | ------------- | --------------------------------------------------------------------------------------- |
| user_id                  | integer       | The identifier of the user who submitted the<br>unload.                                 |
| user_name                | character(50) | Username of the user affected by the<br>change.                                         |
| original_user_name       | character(50) | The original username in a rename action. This<br>field is empty for all other actions. |
| action                   | character(10) | The action that occurred. Valid values are alter,<br>create, drop, and rename.          |
| has_create_db_privs      | integer       | If true (a value of 1), the user has create<br>database permissions.                    |
| is_superuser             | integer       | If true (a value of 1), the user can update system<br>catalogs.                         |
| has_update_catalog_privs | integer       | If true (a value of 1), the user can update system<br>catalogs.                         |
| password_expiration      | timestamp     | The password expiration date.                                                           |
| session_id               | integer       | The process ID.                                                                         |
| transaction_id           | bigint        | The transaction ID.                                                                     |
| record_time              | timestamp     | Time in UTC of when the query started.                                                  |

## Sample queries

The following example performs four user actions, then queries the SYS_USERLOG
view.

```
`CREATE USER userlog1 password 'Userlog1';
ALTER USER userlog1 createdb createuser;
ALTER USER userlog1 rename to userlog2;
DROP user userlog2;

SELECT user_id, user_name, original_user_name, action, has_create_db_privs, is_superuser from SYS_USERLOG order by record_time desc;`
```

```
`user_id | user_name | original_user_name | action | has_create_db_privs | is_superuser
--------+------------+--------------------+---------+---------------------+------------
 108 | userlog2 | | drop | 1 | 1
 108 | userlog2 | userlog1 | rename | 1 | 1
 108 | userlog1 | | alter | 1 | 1
 108 | userlog1 | | create | 0 | 0
 (4 rows)`
```

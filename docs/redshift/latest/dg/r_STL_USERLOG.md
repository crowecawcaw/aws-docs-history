Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_USERLOG

Records details for the following changes to a database user:

- Create user
- Drop user
- Alter user (rename)
- Alter user (alter properties)
  STL_USERLOG is visible only to superusers. For more information, see [Visibility of data in system tables and
  views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_USERLOG](SYS_USERLOG.md "SYS_USERLOG.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type     | Description                                                                                |
| ----------- | ------------- | ------------------------------------------------------------------------------------------ |
| userid      | integer       | ID of the user affected by the change.                                                     |
| username    | character(50) | User name of the user affected by the<br>change.                                           |
| oldusername | character(50) | For a rename action, the original user name. For<br>any other action, this field is empty. |
| action      | character(10) | Action that occurred. Valid values:<br>• Alter<br>• Create<br>• Drop<br>• Rename           |
| usecreatedb | integer       | If true (1), indicates that the user has create<br>database privileges.                    |
| usesuper    | integer       | If true (1), indicates that the user is a<br>superuser.                                    |
| usecatupd   | integer       | If true (1), indicates that the user can update<br>system catalogs.                        |
| valuntil    | timestamp     | Password expiration date.                                                                  |
| pid         | integer       | Process ID.                                                                                |
| xid         | bigint        | Transaction ID.                                                                            |
| recordtime  | timestamp     | Time in UTC that the query started.                                                        |

## Sample queries

The following example performs four user actions, then queries the STL_USERLOG
view.

```

create user userlog1 password 'Userlog1';
alter user userlog1 createdb createuser;
alter user userlog1 rename  to userlog2;
drop user userlog2;

select userid, username, oldusername, action, usecreatedb, usesuper from stl_userlog order by recordtime desc;

```

```

 userid |  username | oldusername |  action | usecreatedb | usesuper
--------+-----------+-------------+---------+-------------+----------
    108 | userlog2  |             | drop    |           1 |   1
    108 | userlog2  | userlog1    | rename  |           1 |   1
    108 | userlog1  |             | alter   |           1 |   1
    108 | userlog1  |             | create  |           0 |   0
 (4 rows)

```

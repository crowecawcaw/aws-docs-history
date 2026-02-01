Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SVL_USER_INFO

You can retrieve data about Amazon Redshift database users with the SVL_USER_INFO view.

SVL_USER_INFO is visible only to superusers. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name    | Data type | Description                                                                                                                                                                                                                                                                                                                                                                              |
| -------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| usename        | text      | The user name for the role.                                                                                                                                                                                                                                                                                                                                                              |
| usesysid       | integer   | The user ID for the user.                                                                                                                                                                                                                                                                                                                                                                |
| usecreatedb    | boolean   | A value that indicates whether the user has<br>permissions to create databases.                                                                                                                                                                                                                                                                                                          |
| usesuper       | boolean   | A value that indicates whether the user is a<br>superuser.                                                                                                                                                                                                                                                                                                                               |
| usecatupd      | boolean   | A value that indicates whether the user can update<br>system catalogs.                                                                                                                                                                                                                                                                                                                   |
| useconnlimit   | text      | The number of connections that the user can<br>open.                                                                                                                                                                                                                                                                                                                                     |
| syslogaccess   | text      | A value that indicates whether the user has access<br>to the system logs. The two possible values are<br>`RESTRICTED` and `UNRESTRICTED`.<br>`RESTRICTED` means that users that are not superusers<br>can see their own records. `UNRESTRICTED` means that user<br>that are not superusers can see all records in the system views and<br>tables to which they have `SELECT` privileges. |
| last_ddl_ts    | timestamp | The timestamp for the last data definition<br>language (DDL) create statement run by the user.                                                                                                                                                                                                                                                                                           |
| sessiontimeout | integer   | The maximum time in seconds that a session remains<br>inactive or idle before timing out. 0 indicates that no timeout is<br>set. For information about the cluster's idle or inactive timeout<br>setting, see [Quotas and limits in Amazon Redshift](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md") in the<br>_Amazon Redshift Management Guide_.                |
| external_id    | text      | Unique identifier of the user in the third-party identity provider.                                                                                                                                                                                                                                                                                                                      |

## Sample queries

The following command retrieves user information from SVL_USER_INFO.

```
SELECT * FROM SVL_USER_INFO;

```

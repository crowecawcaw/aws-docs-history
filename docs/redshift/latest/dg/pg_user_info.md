Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PG_USER_INFO

PG_USER_INFO is an Amazon Redshift system view that shows user information, such as user ID and password expiration time.

Only superusers can see PG_USER_INFO.

## Table columns

PG_USER_INFO contains the following columns. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/8.0/view-pg-user.html "https://www.postgresql.org/docs/8.0/view-pg-user.html").

| Column name  | Data type | Description                                       |
| ------------ | --------- | ------------------------------------------------- |
| usename      | name      | The username.                                     |
| usesysid     | integer   | The user ID.                                      |
| usecreatedb  | boolean   | True if the user can create databases.            |
| usesuper     | boolean   | True if the user is a superuser.                  |
| usecatupd    | boolean   | True if the user can update system catalogs.      |
| passwd       | text      | The password.                                     |
| valuntil     | abstime   | The password's expiration date and time.          |
| useconfig    | text[]    | The session defaults for run-time variables.      |
| useconnlimit | text      | The number of connections that the user can open. |

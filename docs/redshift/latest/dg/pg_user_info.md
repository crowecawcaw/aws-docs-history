Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# PG\_USER\_INFO

PG\_USER\_INFO is an Amazon Redshift system view that shows user information, such as user ID and password expiration time.

Only superusers can see PG\_USER\_INFO.

## Table columns

PG\_USER\_INFO contains the following columns. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/8.0/view-pg-user.html "https://www.postgresql.org/docs/8.0/view-pg-user.html").

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

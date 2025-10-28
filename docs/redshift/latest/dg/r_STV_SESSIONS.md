Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STV_SESSIONS

Use the STV_SESSIONS table to view information about the active user sessions for
Amazon Redshift.

To view the session history, use the [STL_SESSIONS](r_STL_SESSIONS.md "r_STL_SESSIONS.md") table, rather than STV_SESSIONS.

STV_SESSIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_SESSION_HISTORY](SYS_SESSION_HISTORY.md "SYS_SESSION_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name | Data type     | Description                                                                                                                |
| ----------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | --------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------ | --- | ------------------------ | ----- | ------ | --- | -------------------------- | ----- | ------ | --- | -------------------------- | ----- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| starttime   | timestamp     | Time that the session started.                                                                                             |
| process     | integer       | Process ID for the session.                                                                                                |
| user_name   | character(50) | User associated with the session.                                                                                          |
| db_name     | character(50) | Name of the database associated with the session.                                                                          |
| timeout_sec | int           | The maximum time in seconds that a session remains inactive or idle before timing out. 0 indicates that no timeout is set. | ## Sample queries To perform a quick check to see if any other users are currently logged into Amazon Redshift, type the following query: `select count(*) from stv_sessions;` If the result is greater than one, then at least one other user is currently logged in to the database. To view all active sessions for Amazon Redshift, type the following query: `select * from stv_sessions;` The following result shows four active sessions running on Amazon Redshift: ``` starttime | process | user_name | db_name | timeout_sec -------------------------+---------+----------------------------+----------------------------+------------- 2018-08-06 08:44:07.50 | 13779 | IAMA:aws_admin:admin_grp | dev | 0 2008-08-06 08:54:20.50 | 19829 | dwuser | dev | 120 2008-08-06 08:56:34.50 | 20279 | dwuser | dev | 120 2008-08-06 08:55:00.50 | 19996 | dwuser | tickit | 0 (3 rows) ``` The user name prefixed with IAMA indicates that the user signed on using federated single sign-on. For more information, see [Using IAM authentication to generate database user credentials](../mgmt/generating-user-credentials.md "../mgmt/generating-user-credentials.md"). |

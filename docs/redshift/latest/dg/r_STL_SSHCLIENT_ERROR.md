Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_SSHCLIENT_ERROR

Records all errors seen by the SSH client.

STL_SSHCLIENT_ERROR is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name  | Data type       | Description                                                                   |
| ------------ | --------------- | ----------------------------------------------------------------------------- |
| userid       | integer         | ID of the user who generated the entry.                                       |
| query        | integer         | Query ID. The query column can be used to join other system tables and views. |
| slice        | integer         | Number that identifies the slice where the query was running.                 |
| recordtime   | timestamp       | Time that the error was logged.                                               |
| pid          | integer         | Process that logged the error.                                                |
| ssh_username | character(1024) | The SSH user name.                                                            |
| endpoint     | character(1024) | The SSH endpoint.                                                             |
| command      | character(4096) | The complete SSH command.                                                     |
| error        | character(1024) | The error message.                                                            |

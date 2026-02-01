Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SYS_SESSION_HISTORY

Use the SYS_SESSION_HISTORY to view information about the current active sessions and
session history.

SYS_SESSION_HISTORY is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

## Table columns

| Column name     | Data type | Description                                                                                                                      |
| --------------- | --------- | -------------------------------------------------------------------------------------------------------------------------------- |
| user_id         | char(50)  | The identifier of the user who generated the<br>entry.                                                                           |
| session_id      | integer   | The ID of the session associated with the<br>statement.                                                                          |
| database_name   | char(50)  | The name of the database.                                                                                                        |
| status          | char      | The status of the session. Possible values are<br>`active`, `timed out`, and<br>`closed`.                                        |
| session_timeout | integer   | The maximum time in seconds that a session remains<br>inactive or idle before timing out. 0 indicates that no timeout is<br>set. |
| start_time      | timestamp | The timestamp that the connection was<br>established.                                                                            |
| end_time        | timestamp | The timestamp that the connected stopped.                                                                                        |

### Example

The following is a sample output of SYS_SESSION_HISTORY.

```
select * from sys_session_history;
 user_id | session_id |   database_name  | status | session_timeout |         start_time         |          end_time
---------+------------+------------------+--------+-----------------+----------------------------+----------------------------
       1 | 1073971370 | dev              | closed |        0        | 2023-07-17 15:50:12.030104 | 2023-07-17 15:50:12.123218
       1 | 1073979694 | dev              | closed |        0        | 2023-07-17 15:50:24.117947 | 2023-07-17 15:50:24.131859
       1 | 1073873049 | dev              | closed |        0        | 2023-07-17 15:49:29.067398 | 2023-07-17 15:49:29.070294
       1 | 1073873086 | database18127a4a | closed |        0        | 2023-07-17 15:49:29.119018 | 2023-07-17 15:49:29.125925
       1 | 1073832112 | dev              | closed |        0        | 2023-07-17 15:49:29.164688 | 2023-07-17 15:49:29.179631
       1 | 1073987697 | dev              | closed |        0        | 2023-07-17 15:49:29.26749  | 2023-07-17 15:49:29.273034
       1 | 1073922429 | dev              | closed |        0        | 2023-07-17 15:49:33.35315  | 2023-07-17 15:49:33.367499
       1 | 1073766783 | dev              | closed |        0        | 2023-07-17 15:49:45.38237  | 2023-07-17 15:49:45.396902
       1 | 1073807506 | dev              | active |        0        | 2023-07-17 15:51:48        |
```



 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# STL\_SESSIONS
<a name="r_STL_SESSIONS"></a>

Returns information about user session history.

STL\_SESSIONS differs from STV\_SESSIONS in that STL\_SESSIONS contains session history, where STV\_SESSIONS contains the current active sessions.

STL\_SESSIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and views](cm_chap_system-tables.md#c_visibility-of-data).

Some or all of the data in this table can also be found in the SYS monitoring view [SYS\_SESSION\_HISTORY](SYS_SESSION_HISTORY.md). The data in the SYS monitoring view is formatted to be easier to use and understand. We recommend that you use the SYS monitoring view for your queries.

## Table columns
<a name="r_STL_SESSIONS-table-columns"></a>


| Column name | Data type | Description | 
| --- | --- | --- | 
| userid | integer | ID of the user who generated the entry. | 
| starttime | timestamp | Time in UTC that the session started. | 
| endtime | timestamp | Time in UTC that the session ended. | 
| process | integer | Process ID for the session. | 
| user\_name | character(50) | User name associated with the session. | 
| db\_name | character(50) | Name of the database associated with the session. | 
| timeout\_sec | int | The maximum time in seconds that a session remains inactive or idle before timing out. 0 indicates that no timeout is set. | 
| timed\_out | int | A value that indicates why the connection was terminated. It can have the following values:+  `0`: The connection was terminated due to an unknown error. <br />+  `1`: The connection timed out. <br />+  `2`: The client side terminated the connection. <br />+  `3`: An Amazon Redshift backend internal error terminated the connection.  | 

## Sample queries
<a name="r_STL_SESSIONS-sample-queries"></a>

To view session history for the TICKIT database, type the following query:

```
select starttime, process, user_name, timeout_sec, timed_out
from stl_sessions
where db_name='tickit' order by starttime;
```

This query returns the following sample output:

```
    starttime              | process |  user_name             | timeout_sec | timed_out
---------------------------+---------+------------------------+-------------+-------------
2008-09-15 09:54:06.746705 |   32358 | dwuser                 | 120         | 1
2008-09-15 09:56:34.30275  |   32744 | dwuser                 | 60          | 1
2008-09-15 11:20:34.694837 |   14906 | dwuser                 | 0           | 0
2008-09-15 11:22:16.749818 |   15148 | dwuser                 | 0           | 0
2008-09-15 14:32:44.66112  |   14031 | dwuser                 | 0           | 0
2008-09-15 14:56:30.22161  |   18380 | dwuser                 | 0           | 0
2008-09-15 15:28:32.509354 |   24344 | dwuser                 | 0           | 0
2008-09-15 16:01:00.557326 |   30153 | dwuser                 | 120         | 1
2008-09-15 17:28:21.419858 |   12805 | dwuser                 | 0           | 0
2008-09-15 20:58:37.601937 |   14951 | dwuser                 | 60          | 1
2008-09-16 11:12:30.960564 |   27437 | dwuser                 | 60          | 1
2008-09-16 14:11:37.639092 |   23790 | dwuser                 | 3600        | 1
2008-09-16 15:13:46.02195  |    1355 | dwuser                 | 120         | 1
2008-09-16 15:22:36.515106 |    2878 | dwuser                 | 120         | 1
2008-09-16 15:44:39.194579 |    6470 | dwuser                 | 120         | 1
2008-09-16 16:50:27.02138  |   17254 | dwuser                 | 120         | 1
2008-09-17 12:05:02.157208 |    8439 | dwuser                 | 3600        | 0
(17 rows)
```
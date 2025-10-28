Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# STL_RESTARTED_SESSIONS

To maintain continuous availability following certain internal events, Amazon Redshift might
restart an active session with a new process ID (PID). When Amazon Redshift restarts a session,
STL_RESTARTED_SESSIONS records the new PID and the old PID.

For more information, see the examples following in this section.

STL_RESTARTED_SESSIONS is visible to all users. Superusers can see all rows; regular users can see only their own data. For more information, see [Visibility of data in system tables and
views](cm_chap_system-tables.md#c_visibility-of-data "cm_chap_system-tables.md#c_visibility-of-data").

Some or all of the data in this table can also be found in the SYS monitoring view [SYS_SESSION_HISTORY](SYS_SESSION_HISTORY.md "SYS_SESSION_HISTORY.md"). The data in the SYS monitoring view is formatted to be easier to use and understand.
We recommend that you use the SYS monitoring view for your queries.

## Table columns

| Column name  | Data type       | Description                                       |
| ------------ | --------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| currenttime  | timestamp       | Time of the event.                                |
| dbname       | character(50)   | Name of the database associated with the session. |
| newpid       | integer         | Process ID for the restarted session.             |
| oldpid       | integer         | Process ID for the original session.              |
| username     | character(50)   | Name of the user associated with the session.     |
| remotehost   | character(45)   | Name or IP address of the remote host.            |
| remoteport   | character(32)   | Port number of the remote host.                   |
| parkedtime   | timestamp       | This information is for internal use only.        |
| session_vars | character(2000) | This information is for internal use only.        | ## Sample queries The following example joins STL_RESTARTED_SESSIONS with STL_SESSIONS to show user names for sessions that have been restarted. `select process, stl_restarted_sessions.newpid, user_name from stl_sessions inner join stl_restarted_sessions on stl_sessions.process = stl_restarted_sessions.oldpid order by process; ...` |

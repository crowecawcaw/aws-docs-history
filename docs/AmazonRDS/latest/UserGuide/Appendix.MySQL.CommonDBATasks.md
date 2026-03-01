# Ending a session or query for RDS for MySQL

You can end user sessions or queries on DB instances by using the
`rds_kill` and `rds_kill_query` commands. First connect to
your MySQL DB instance, then issue the appropriate command as shown following. For more
information, see [Connecting to your MySQL DB instance](USER_ConnectToInstance.md "USER_ConnectToInstance.md").

```
CALL mysql.rds_kill(thread-ID)
CALL mysql.rds_kill_query(thread-ID)
```

For example, to end the session that is running on thread 99, you would type the
following:

```
CALL mysql.rds_kill(99);
```

To end the query that is running on thread 99, you would type the following:

```
CALL mysql.rds_kill_query(99);
```

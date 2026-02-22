# Monitoring database activity streams

Database activity streams monitor and report activities. The stream of activity is collected and transmitted to Amazon Kinesis.
From Kinesis, you can monitor the activity stream, or other services and applications can consume
the activity stream for further analysis. You can find the underlying Kinesis stream name by
using the AWS CLI command `describe-db-clusters` or the RDS API
`DescribeDBClusters` operation.

Aurora manages the Kinesis stream for
you as follows:

- Aurora creates the Kinesis stream
  automatically with a 24-hour retention period.
- Aurora scales the Kinesis stream if necessary.
- If you stop the database activity stream or delete the DB cluster, Aurora deletes the Kinesis stream.
  The following categories of activity are monitored and put in the activity stream audit log:

- **SQL commands** – All SQL commands are audited,
  and also prepared statements, built-in functions, and functions in PL/SQL. Calls to stored procedures
  are audited. Any SQL statements issued inside stored procedures or functions are also audited.
- **Other database information** – Activity monitored includes the full SQL statement,
  the row count of affected rows from DML commands, accessed objects, and the unique database name. For Aurora PostgreSQL, database activity streams also monitor the bind variables and stored
  procedure parameters.

###### Important

The full SQL text of each statement is visible in the activity stream audit log,
including any sensitive data. However, database user passwords are redacted if
Aurora can
determine them from the context, such as in the following SQL statement.

```
ALTER ROLE role-name WITH password
```

- **Connection information** – Activity monitored includes session and
  network information, the server process ID, and exit codes.
  If an activity stream has a failure while monitoring your DB instance, you are notified through RDS events.

In the following sections, you can access, audit, and process database activity streams.

###### Topics

- [Accessing an activity stream from Amazon Kinesis](DBActivityStreams.md "DBActivityStreams.md")
- [Audit log contents and examples for database activity streams](DBActivityStreams.md "DBActivityStreams.md")
- [databaseActivityEventList JSON array for database activity streams](DBActivityStreams.AuditLog.md "DBActivityStreams.AuditLog.md")
- [Processing a database activity stream using the AWS SDK](DBActivityStreams.md "DBActivityStreams.md")

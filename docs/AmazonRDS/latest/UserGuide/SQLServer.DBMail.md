# Deleting messages

You use the `rds_sysmail_delete_mailitems_sp` stored procedure to delete messages.

###### Note

RDS automatically deletes mail table items when DBMail history data reaches 1 GB in size, with a retention period of at
least 24 hours.

If you want to keep mail items for a longer period, you can archive them. For more
information, see [Create a SQL Server Agent job to archive Database Mail messages and event
logs](https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/create-a-sql-server-agent-job-to-archive-database-mail-messages-and-event-logs "https://docs.microsoft.com/en-us/sql/relational-databases/database-mail/create-a-sql-server-agent-job-to-archive-database-mail-messages-and-event-logs") in the Microsoft documentation.

###### To delete all email messages

- Use the following SQL statement.

```
DECLARE @GETDATE datetime
SET @GETDATE = GETDATE();
EXECUTE msdb.dbo.rds_sysmail_delete_mailitems_sp @sent_before = @GETDATE;
GO
```

###### To delete all email messages with a particular status

- Use the following SQL statement to delete all failed messages.

```
DECLARE @GETDATE datetime
SET @GETDATE = GETDATE();
EXECUTE msdb.dbo.rds_sysmail_delete_mailitems_sp @sent_status = 'failed';
GO
```

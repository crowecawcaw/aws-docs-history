

# Starting and stopping mail queue
<a name="SQLServer.DBMail.StartStop"></a>

Use the following instructions to start and stop the DB mail queue:

**Topics**
+ [Starting the mail queue](#SQLServer.DBMail.Start)
+ [Stopping the mail queue](#SQLServer.DBMail.Stop)

## Starting the mail queue
<a name="SQLServer.DBMail.Start"></a>

You use the `rds_sysmail_control` stored procedure to start the Database Mail process.

**Note**  
Enabling Database Mail automatically starts the mail queue.

**To start the mail queue**
+ Use the following SQL statement.

  ```
  EXECUTE msdb.dbo.rds_sysmail_control start;
  GO
  ```

## Stopping the mail queue
<a name="SQLServer.DBMail.Stop"></a>

You use the `rds_sysmail_control` stored procedure to stop the Database Mail process.

**To stop the mail queue**
+ Use the following SQL statement.

  ```
  EXECUTE msdb.dbo.rds_sysmail_control stop;
  GO
  ```
# Importing the database

To import the database (DB), follow these steps.

1. Back up your source on-premises database using MS SQL Native backup and restore (see
   [Support for native backup and restore in SQL Server](../../../AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.md "../../../AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.md")). As the result of running that operation, you should have a .bak (backup) file.
2. Upload the .bak file to and existing transit S3 bucket using the AWS S3 CLI or AWS S3 console. For information on transit S3 buckets, see
   [Protecting data using encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md").
3. Import the .bak file into a new DB on your target RDS for SQL Server MS SQL instance (for details on types, see
   [Amazon RDS for MySQL instance types](https://aws.amazon.com/rds/mysql/instance-types/ "https://aws.amazon.com/rds/mysql/instance-types/")):
   1. Log into the EC2 instance (on-premises workstation) and open MS SQL Management Studio
   2. Connect to the target RDS instance created as prerequisite in step #1. Follow this procedure to connect:
      [Connecting to a DB Instance Running the Microsoft SQL Server Database Engine](../../../AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.md "../../../AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.md")
   3. Start the import (restore) job with a new Structured Query Language (SQL) query (for details on SQL queries, see
      [Introduction to SQL](https://www.w3schools.com/sql/sql_intro.asp "https://www.w3schools.com/sql/sql_intro.asp")). The target database name must be new (do not use the same name as the
      database that you previously created). Example without encryption:

   ```
   exec msdb.dbo.rds_restore_database
           @restore_db_name=`TARGET_DB_NAME`,

           @s3_arn_to_restore_from='arn:aws:s3:::`BUCKET_NAME`/`FILENAME`.bak';

   ```

   4. Periodically check the status of the import job by running this query in a separate window:

   ```
   exec msdb.dbo.rds_task_status;
   ```

   If the status changes to Failed, look for the failure details in the message.

# Accessing the tempdb database on Microsoft SQL Server DB

instances on Amazon RDS

You can access the `tempdb` database on your Microsoft SQL Server DB instances on
Amazon RDS. You can run code on `tempdb` by using Transact-SQL through Microsoft SQL
Server Management Studio (SSMS), or any other standard SQL client application. For more
information about connecting to your DB instance, see [Connecting to your Microsoft SQL Server
DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

The master user for your DB instance is granted `CONTROL` access to
`tempdb` so that this user can modify the `tempdb` database
options. The master user isn't the database owner of the `tempdb` database. If
necessary, the master user can grant `CONTROL` access to other users so that they
can also modify the `tempdb` database options.

###### Note

You can't run Database Console Commands (DBCC) on the `tempdb` database.

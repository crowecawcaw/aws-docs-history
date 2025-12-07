# Adding a user to the SQLAgentUser role

To allow an additional login or user to use SQL Server Agent, log in as the master
user and do the following:

1. Create another server-level login by using the `CREATE LOGIN` command.
2. Create a user in `msdb` using `CREATE USER` command, and then link this user to the login
   that you created in the previous step.
3. Add the user to the `SQLAgentUserRole` using the `sp_addrolemember` system stored
   procedure.
   For example, suppose that your master user name is `admin`
   and you want to give access to SQL Server Agent to a user named
   `theirname` with a password
   `theirpassword`. In that case, you can use the following
   procedure.

###### To add a user to the SQLAgentUser role

1. Log in as the master user.
2. Run the following commands:

```
--Initially set context to master database
USE [master];
GO
--Create a server-level login named theirname with password theirpassword
CREATE LOGIN [theirname] WITH PASSWORD = 'theirpassword';
GO
--Set context to msdb database
USE [msdb];
GO
--Create a database user named theirname and link it to server-level login theirname
CREATE USER [theirname] FOR LOGIN [theirname];
GO
--Added database user theirname in msdb to SQLAgentUserRole in msdb
EXEC sp_addrolemember [SQLAgentUserRole], [theirname];

```

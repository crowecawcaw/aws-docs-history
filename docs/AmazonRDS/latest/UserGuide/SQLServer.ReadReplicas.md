# Synchronizing database users and objects with a SQL Server read replica

Any logins, custom server roles, SQL agent jobs, or other server-level objects that exist in the primary DB instance
at the time of creating a read replica are expected to be present in the newly created read replica.
However, any server-level objects that are created in the primary DB instance after the creation of
the read replica will not be automatically replicated, and you must create them manually in the
read replica.

The database users are automatically replicated from the primary DB instance to the read replica.
As the read replica database is in read-only mode, the security identifier (SID) of the database
user cannot be updated in the database. Therefore, when creating SQL logins in the read replica,
it's essential to ensure that the SID of that login matches the SID of the corresponding SQL login
in the primary DB instance. If you don't synchronize the SIDs of the SQL logins, they won't be able to
access the database in the read replica. Windows Active Directory (AD) Authenticated Logins do not
experience this issue because the SQL Server obtains the SID from the Active Directory.

###### To synchronize a SQL login from the primary DB instance to the read replica

1. Connect to the primary DB instance.
2. Create a new SQL login in the primary DB instance.

```
USE [master]
GO
CREATE LOGIN `TestLogin1`
WITH PASSWORD = '`REPLACE WITH PASSWORD`';

```

###### Note

Specify a password other than the prompt shown here as a security best practice. 3. Create a new database user for the SQL login in the database.

```
USE [`REPLACE WITH YOUR DB NAME`]
GO
CREATE USER `TestLogin1` FOR LOGIN `TestLogin1`;
GO

```

4. Check the SID of the newly created SQL login in primary DB instance.

```
SELECT name, sid FROM sys.server_principals WHERE name =  `TestLogin1`;

```

5. Connect to the read replica. Create the new SQL login.

```
CREATE LOGIN `TestLogin1` WITH PASSWORD = '`REPLACE WITH PASSWORD`', SID=[`REPLACE WITH sid FROM STEP #4`];

```

###### Alternately, if you have access to the read replica database, you can fix the orphaned user as follows:

1. Connect to the read replica.
2. Identify the orphaned users in the database.

```
USE [`REPLACE WITH YOUR DB NAME`]
GO
EXEC sp_change_users_login 'Report';
GO

```

3. Create a new SQL login for the orphaned database user.

```
CREATE LOGIN `TestLogin1` WITH PASSWORD = '`REPLACE WITH PASSWORD`', SID=[`REPLACE WITH sid FROM STEP #2`];

```

Example:

```
CREATE LOGIN `TestLogin1` WITH PASSWORD = '`TestPa$$word#1`', SID=[`0x1A2B3C4D5E6F7G8H9I0J1K2L3M4N5O6P`];

```

###### Note

Specify a password other than the prompt shown here as a security best practice.

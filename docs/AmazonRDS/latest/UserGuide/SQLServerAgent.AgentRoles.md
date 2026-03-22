# SQL Server Agent roles

RDS for SQL Server supports the following SQL Server Agent roles with different levels of permissions for managing jobs:

- **SQLAgentUserRole**

Permissions

    + Create and manage their own jobs, schedules, and operators
    + View the properties of their own jobs and schedules
    + Cannot view or manage jobs created by other users

This role is suitable for users who need to create and manage their own jobs but do not require access to jobs created by other users.

- **SQLAgentReaderRole**

Permissions

    + All permissions of SQLAgentUserRole
    + View a list of all jobs and schedules, including those created by others
    + View the properties of all jobs
    + Review job history

This role is suitable for users who need to monitor the status of all jobs but do not need to manage them.

- **SQLAgentOperatorRole**

Permissions

    + All permissions of SQLAgentUserRole and SQLAgentReaderRole
    + Execute, stop, or start jobs
    + Manage job history
    + Enable/disable jobs and schedules
    + View operators and proxies

This role provides the most comprehensive permissions and is suitable for users who need to have full control over all jobs.
Use the following command to assign the roles to your SQL Server login:

```
USE msdb;
EXEC sp_addrolemember 'SQLAgentOperatorRole', '`username`';
```

## Managing SQLAgentOperatorRole in RDS for SQL Server

To view the current jobs, you must add the SQLAgentOperatorRole to your SQL Server login and remove it before disconnecting from your database.

To visualize the SQL Server Agent tree in the SQL Server Management Studio, follow these instructions:

###### View SQL Server Agent on SQL Server Management Studio (SSMS)

1. Using the RDS master credentials, login into the RDS SQL Server instance and grant the desired user the SQLAgentUserRole.

```
USE msdb
GO
IF NOT EXISTS(SELECT name FROM sys.database_principals WHERE name = 'UserName')
BEGIN
CREATE USER UserName FROM LOGIN UserName
END
GO
ALTER ROLE SQLAgentUserRole ADD MEMBER UserName
GO
GRANT ALTER ON ROLE::[SQLAgentOperatorRole] to UserName
GO
```

These commands create the user on the `msdb` database, in case it doesn’t exists.
It also adds the user on the SQLAgentUserRole, so the SQL Server Agent tree on SSMS can be seen.
Finally, it grants alter permissions on the SQLAgentOperatorRole to the user. This allows the user to add/remove itself from that role. 2. To add yourself to the above-mentioned role, connect to the RDS SQL Server instance, with the user that needs to see the jobs, and run the following script.

```
use msdb
go
ALTER ROLE SQLAgentOperatorRole ADD MEMBER UserName
GO
```

After this, right click on the **Jobs** folder, and choose **Refresh**. 3. When you perform this action, the **Jobs** tab displays a **+** (plus) button. Click to expand the the list of SQL Server Agent Jobs. 4. ###### Important

Before you disconnect from the RDS SQL Server instance, you need to remove yourself from the SQLAgentOperatorRole.

To remove your login from the SQLAgentOperatorRole, run the following query before disconnecting or closing the Management Studio:

```
USE msdb
GO
ALTER ROLE SQLAgentOperatorRole DROP MEMBER UserName
GO
```

For more information, see [Leveraging SQLAgentOperatorRole in RDS SQL Server](https://aws.amazon.com/blogs/database/leveraging-sqlagentoperatorrole-in-rds-sql-server/ "https://aws.amazon.com/blogs/database/leveraging-sqlagentoperatorrole-in-rds-sql-server/").

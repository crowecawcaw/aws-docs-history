# Administrative permissions on SSISDB

When the instance is created or modified with the SSIS option, the result is an SSISDB
database with the ssis_admin and ssis_logreader roles granted to the master user. The
master user has the following privileges in SSISDB:

- alter on ssis_admin role
- alter on ssis_logreader role
- alter any user
  Because the master user is a SQL-authenticated user, you can't use the master user for
  executing SSIS packages. The master user can use these privileges to create new SSISDB
  users and add them to the ssis_admin and ssis_logreader roles. Doing this is useful for
  giving access to your domain users for using SSIS.

## Setting up a Windows-authenticated user for SSIS

The master user can use the following code example to set up a Windows-authenticated login
in SSISDB and grant the required procedure permissions. Doing this grants
permissions to the domain user to deploy and run SSIS packages, use S3 file transfer
procedures, create credentials, and work with the SQL Server Agent proxy. For more
information, see [Credentials (database engine)](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/credentials-database-engine?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/credentials-database-engine?view=sql-server-ver15") and [Create a SQL Server Agent proxy](https://docs.microsoft.com/en-us/sql/ssms/agent/create-a-sql-server-agent-proxy?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/ssms/agent/create-a-sql-server-agent-proxy?view=sql-server-ver15") in the Microsoft documentation.

###### Note

You can grant some or all of the following permissions as needed to Windows-authenticated
users.

```
-- Create a server-level SQL login for the domain user, if it doesn't already exist
USE [master]
GO
CREATE LOGIN [`mydomain`\`user_name`] FROM WINDOWS
GO

-- Create a database-level account for the domain user, if it doesn't already exist
USE [SSISDB]
GO
CREATE USER [`mydomain`\`user_name`] FOR LOGIN [`mydomain`\`user_name`]

-- Add SSIS role membership to the domain user
ALTER ROLE [ssis_admin] ADD MEMBER [`mydomain`\`user_name`]
ALTER ROLE [ssis_logreader] ADD MEMBER [`mydomain`\`user_name`]
GO

-- Add MSDB role membership to the domain user
USE [msdb]
GO
CREATE USER [`mydomain`\`user_name`] FOR LOGIN [`mydomain`\`user_name`]

-- Grant MSDB stored procedure privileges to the domain user
GRANT EXEC ON msdb.dbo.rds_msbi_task TO [`mydomain`\`user_name`] with grant option
GRANT SELECT ON msdb.dbo.rds_fn_task_status TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_task_status TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_cancel_task TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_download_from_s3 TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_upload_to_s3 TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_delete_from_filesystem TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_gather_file_details TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_add_proxy TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_update_proxy TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_grant_login_to_proxy TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_revoke_login_from_proxy TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_delete_proxy TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_enum_login_for_proxy to [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.sp_enum_proxy_for_subsystem TO [`mydomain`\`user_name`]  with grant option
GRANT EXEC ON msdb.dbo.rds_sqlagent_proxy TO [`mydomain`\`user_name`] WITH GRANT OPTION


-- Add the SQLAgentUserRole privilege to the domain user
USE [msdb]
GO
ALTER ROLE [SQLAgentUserRole] ADD MEMBER [`mydomain`\`user_name`]
GO

-- Grant the ALTER ANY CREDENTIAL privilege to the domain user
USE [master]
GO
GRANT ALTER ANY CREDENTIAL TO [`mydomain`\`user_name`]
GO
```

# Using SSIS

After deploying the SSIS project into the SSIS catalog, you can run packages directly from
SSMS or schedule them by using SQL Server Agent. You must use a Windows-authenticated
login for executing SSIS packages. For more information, see [Setting up a Windows-authenticated user for SSIS](SSIS.md#SSIS.Use.Auth "SSIS.md#SSIS.Use.Auth").

###### Topics

- [Setting database connection managers for SSIS projects](#SSIS.Use.ConnMgrs "#SSIS.Use.ConnMgrs")
- [Creating an SSIS proxy](#SSIS.Use.Proxy "#SSIS.Use.Proxy")
- [Scheduling an SSIS package using SQL Server Agent](#SSIS.Use.Schedule "#SSIS.Use.Schedule")
- [Revoking SSIS access from the proxy](#SSIS.Use.Revoke "#SSIS.Use.Revoke")

## Setting database connection managers for SSIS projects

When you use a connection manager, you can use these types of authentication:

- For local database connections using AWS Managed Active Directory, you can use SQL authentication or Windows authentication. For Windows authentication, use
  ``DB_instance_name`.`fully_qualified_domain_name`` as the server name of the connection string.

An example is `myssisinstance.corp-ad.example.com`, where
`myssisinstance` is the DB instance name and
`corp-ad.example.com` is the fully qualified domain
name.

- For remote connections, always use SQL authentication.
- For local database connections using self-managed Active Directory,
  you can use SQL authentication or Windows authentication. For Windows authentication,
  use `.` or `LocalHost` as
  the server name of the connection string.

## Creating an SSIS proxy

To be able to schedule SSIS packages using SQL Server Agent, create an SSIS credential and
an SSIS proxy. Run these procedures as a Windows-authenticated user.

###### To create the SSIS credential

- Create the credential for the proxy. To do this, you can use SSMS or the following SQL
  statement.

```
USE [master]
GO
CREATE CREDENTIAL [SSIS_Credential] WITH IDENTITY = N'`mydomain`\`user_name`', SECRET = N'`mysecret`'
GO
```

###### Note

`IDENTITY` must be a domain-authenticated login. Replace
`mysecret` with the
password for the domain-authenticated login.

Whenever the SSISDB primary host is changed, alter the SSIS proxy credentials to allow
the new host to access them.

###### To create the SSIS proxy

1. Use the following SQL statement to create the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_add_proxy @proxy_name=N'SSIS_Proxy',@credential_name=N'SSIS_Credential',@description=N''
GO
```

2. Use the following SQL statement to grant access to the proxy to other
   users.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_grant_login_to_proxy @proxy_name=N'SSIS_Proxy',@login_name=N'`mydomain`\`user_name`'
GO
```

3. Use the following SQL statement to give the SSIS subsystem access to
   the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.rds_sqlagent_proxy @task_type='GRANT_SUBSYSTEM_ACCESS',@proxy_name='SSIS_Proxy',@proxy_subsystem='SSIS'
GO
```

###### To view the proxy and grants on the proxy

1. Use the following SQL statement to view the grantees of the proxy.

```
USE [msdb]
GO
EXEC sp_help_proxy
GO
```

2. Use the following SQL statement to view the subsystem grants.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_enum_proxy_for_subsystem
GO
```

## Scheduling an SSIS package using SQL Server Agent

After you create the credential and proxy and grant SSIS access to the proxy, you can
create a SQL Server Agent job to schedule the SSIS package.

###### To schedule the SSIS package

- You can use SSMS or T-SQL for creating the SQL Server Agent job. The following example
  uses T-SQL.

```
USE [msdb]
GO
DECLARE @jobId BINARY(16)
EXEC msdb.dbo.sp_add_job @job_name=N'MYSSISJob',
@enabled=1,
@notify_level_eventlog=0,
@notify_level_email=2,
@notify_level_page=2,
@delete_level=0,
@category_name=N'[Uncategorized (Local)]',
@job_id = @jobId OUTPUT
GO
EXEC msdb.dbo.sp_add_jobserver @job_name=N'MYSSISJob',@server_name=N'(local)'
GO
EXEC msdb.dbo.sp_add_jobstep @job_name=N'MYSSISJob',@step_name=N'ExecuteSSISPackage',
@step_id=1,
@cmdexec_success_code=0,
@on_success_action=1,
@on_fail_action=2,
@retry_attempts=0,
@retry_interval=0,
@os_run_priority=0,
@subsystem=N'SSIS',
@command=N'/ISSERVER "\"\SSISDB\MySSISFolder\MySSISProject\MySSISPackage.dtsx\"" /SERVER "\"my-rds-ssis-instance.corp-ad.company.com/\""
/Par "\"$ServerOption::LOGGING_LEVEL(Int16)\"";1 /Par "\"$ServerOption::SYNCHRONIZED(Boolean)\"";True /CALLERINFO SQLAGENT /REPORTING E',
@database_name=N'master',
@flags=0,
@proxy_name=N'SSIS_Proxy'
GO
```

## Revoking SSIS access from the proxy

You can revoke access to the SSIS subsystem and delete the SSIS proxy using the following
stored procedures.

###### To revoke access and delete the proxy

1. Revoke subsystem access.

```
USE [msdb]
GO
EXEC msdb.dbo.rds_sqlagent_proxy @task_type='REVOKE_SUBSYSTEM_ACCESS',@proxy_name='SSIS_Proxy',@proxy_subsystem='SSIS'
GO
```

2. Revoke the grants on the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_revoke_login_from_proxy @proxy_name=N'SSIS_Proxy',@name=N'`mydomain`\`user_name`'
GO
```

3. Delete the proxy.

```
USE [msdb]
GO
EXEC dbo.sp_delete_proxy @proxy_name = N'SSIS_Proxy'
GO
```

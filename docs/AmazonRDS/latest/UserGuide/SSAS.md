# Using SSAS on Amazon RDS

After deploying the SSAS project, you can directly process the OLAP database on SSMS.

###### To use SSAS on RDS

1. In SSMS, connect to SSAS using the user name and password for the Active Directory
   domain.
2. Expand **Databases**. The newly deployed SSAS database appears.
3. Locate the connection string, and update the user name and password to give access to the source SQL database. Doing
   this is required for processing SSAS objects.
   1. For Tabular mode, do the following:
      1. Expand the **Connections** tab.
      2. Open the context (right-click) menu for the connection object, and then choose **Properties**.
      3. Update the user name and password in the connection string.

   2. For Multidimensional mode, do the following:
      1. Expand the **Data Sources** tab.
      2. Open the context (right-click) menu for the data source object, and then choose **Properties**.
      3. Update the user name and password in the connection string.

4. Open the context (right-click) menu for the SSAS database that you created and choose **Process Database**.

Depending on the size of the input data, the processing operation might take several minutes to complete.

###### Topics

- [Setting up a Windows-authenticated user for SSAS](#SSAS.Use.Auth "#SSAS.Use.Auth")
- [Adding a domain user as a database administrator](#SSAS.Admin "#SSAS.Admin")
- [Creating an SSAS proxy](#SSAS.Use.Proxy "#SSAS.Use.Proxy")
- [Scheduling SSAS database processing using SQL Server Agent](#SSAS.Use.Schedule "#SSAS.Use.Schedule")
- [Revoking SSAS access from the proxy](#SSAS.Use.Revoke "#SSAS.Use.Revoke")

## Setting up a Windows-authenticated user for SSAS

The main administrator user (sometimes called the master user) can use the
following code example to set up a Windows-authenticated login and grant the
required procedure permissions. Doing this grants permissions to the domain user to
run SSAS customer tasks, use S3 file transfer procedures, create credentials, and
work with the SQL Server Agent proxy. For more information, see [Credentials (database engine)](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/credentials-database-engine?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/credentials-database-engine?view=sql-server-ver15") and [Create a SQL Server Agent proxy](https://docs.microsoft.com/en-us/sql/ssms/agent/create-a-sql-server-agent-proxy?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/ssms/agent/create-a-sql-server-agent-proxy?view=sql-server-ver15") in the Microsoft documentation.

You can grant some or all of the following permissions as needed to
Windows-authenticated users.

```
-- Create a server-level domain user login, if it doesn't already exist
USE [master]
GO
CREATE LOGIN [`mydomain`\`user_name`] FROM WINDOWS
GO

-- Create domain user, if it doesn't already exist
USE [msdb]
GO
CREATE USER [`mydomain`\`user_name`] FOR LOGIN [`mydomain`\`user_name`]
GO

-- Grant necessary privileges to the domain user
USE [master]
GO
GRANT ALTER ANY CREDENTIAL TO [`mydomain`\`user_name`]
GO

USE [msdb]
GO
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
GRANT EXEC ON msdb.dbo.sp_enum_proxy_for_subsystem TO [`mydomain`\`user_name`] with grant option
GRANT EXEC ON msdb.dbo.rds_sqlagent_proxy TO [`mydomain`\`user_name`] with grant option
ALTER ROLE [SQLAgentUserRole] ADD MEMBER [`mydomain`\`user_name`]
GO
```

## Adding a domain user as a database administrator

You can add a domain user as an SSAS database administrator in the following ways:

- A database administrator can use SSMS to create a role with `admin` privileges, then add users to
  that role.
- You can use the following stored procedure.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSAS_ADD_DB_ADMIN_MEMBER',
@database_name='`myssasdb`',
@ssas_role_name='`exampleRole`',
@ssas_role_member='`domain_name`\`domain_user_name`';
```

The following parameters are required:

    + `@task_type` – The type of the MSBI task, in this case
     `SSAS_ADD_DB_ADMIN_MEMBER`.
    + `@database_name` – The name of the SSAS database to which you're granting
     administrator privileges.
    + `@ssas_role_name` – The SSAS database administrator role name. If the role doesn't
     already exist, it's created.
    + `@ssas_role_member` – The SSAS database user that you're adding to the administrator
     role.

## Creating an SSAS proxy

To be able to schedule SSAS database processing using SQL Server Agent, create an SSAS credential and an SSAS proxy.
Run these procedures as a Windows-authenticated user.

###### To create the SSAS credential

- Create the credential for the proxy. To do this, you can use SSMS or the following SQL statement.

```
USE [master]
GO
CREATE CREDENTIAL [SSAS_Credential] WITH IDENTITY = N'`mydomain`\`user_name`', SECRET = N'`mysecret`'
GO
```

###### Note

`IDENTITY` must be a domain-authenticated login. Replace
`mysecret` with the password for the domain-authenticated
login.

###### To create the SSAS proxy

1. Use the following SQL statement to create the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_add_proxy @proxy_name=N'SSAS_Proxy',@credential_name=N'SSAS_Credential',@description=N''
GO
```

2. Use the following SQL statement to grant access to the proxy to other users.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_grant_login_to_proxy @proxy_name=N'SSAS_Proxy',@login_name=N'`mydomain`\`user_name`'
GO
```

3. Use the following SQL statement to give the SSAS subsystem access to the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.rds_sqlagent_proxy @task_type='GRANT_SUBSYSTEM_ACCESS',@proxy_name='SSAS_Proxy',@proxy_subsystem='SSAS'
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

## Scheduling SSAS database processing using SQL Server Agent

After you create the credential and proxy and grant SSAS access to the proxy, you can create a SQL Server Agent job to
schedule SSAS database processing.

###### To schedule SSAS database processing

- Use SSMS or T-SQL for creating the SQL Server Agent job. The following
  example uses T-SQL. You can further configure its job schedule through SSMS
  or T-SQL.

      + The `@command` parameter outlines the XML for Analysis (XMLA) command to be run by the SQL
       Server Agent job. This example configures SSAS Multidimensional database processing.
      + The `@server` parameter outlines the target SSAS server name of the SQL Server Agent
       job.


      To call the SSAS service within the same RDS DB instance where the SQL Server Agent job resides, use
       `localhost:2383`.


      To call the SSAS service from outside the RDS DB instance, use the RDS endpoint. You can also use the
       Kerberos Active Directory (AD) endpoint
       (``your-DB-instance-name`.`your-AD-domain-name``)
       if the RDS DB instances are joined by the same domain. For external DB instances, make sure to properly
       configure the VPC security group associated with the RDS DB instance for a secure connection.

  You can further edit the query to support various XMLA operations. Make
  edits either by directly modifying the T-SQL query or by using the SSMS UI
  following SQL Server Agent job creation.

```
USE [msdb]
GO
DECLARE @jobId BINARY(16)
EXEC msdb.dbo.sp_add_job @job_name=N'SSAS_Job',
    @enabled=1,
    @notify_level_eventlog=0,
    @notify_level_email=0,
    @notify_level_netsend=0,
    @notify_level_page=0,
    @delete_level=0,
    @category_name=N'[Uncategorized (Local)]',
    @job_id = @jobId OUTPUT
GO
EXEC msdb.dbo.sp_add_jobserver
    @job_name=N'SSAS_Job',
    @server_name = N'(local)'
GO
EXEC msdb.dbo.sp_add_jobstep @job_name=N'SSAS_Job', @step_name=N'Process_SSAS_Object',
    @step_id=1,
    @cmdexec_success_code=0,
    @on_success_action=1,
    @on_success_step_id=0,
    @on_fail_action=2,
    @on_fail_step_id=0,
    @retry_attempts=0,
    @retry_interval=0,
    @os_run_priority=0, @subsystem=N'ANALYSISCOMMAND',
    @command=N'<Batch xmlns="http://schemas.microsoft.com/analysisservices/2003/engine">
        <Parallel>
            <Process xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xmlns:ddl2="http://schemas.microsoft.com/analysisservices/2003/engine/2" xmlns:ddl2_2="http://schemas.microsoft.com/analysisservices/2003/engine/2/2"
                xmlns:ddl100\_100="http://schemas.microsoft.com/analysisservices/2008/engine/100/100" xmlns:ddl200="http://schemas.microsoft.com/analysisservices/2010/engine/200"
                xmlns:ddl200\_200="http://schemas.microsoft.com/analysisservices/2010/engine/200/200" xmlns:ddl300="http://schemas.microsoft.com/analysisservices/2011/engine/300"
                xmlns:ddl300\_300="http://schemas.microsoft.com/analysisservices/2011/engine/300/300" xmlns:ddl400="http://schemas.microsoft.com/analysisservices/2012/engine/400"
                xmlns:ddl400\_400="http://schemas.microsoft.com/analysisservices/2012/engine/400/400" xmlns:ddl500="http://schemas.microsoft.com/analysisservices/2013/engine/500"
                xmlns:ddl500\_500="http://schemas.microsoft.com/analysisservices/2013/engine/500/500">
                <Object>
                    <DatabaseID>Your_SSAS_Database_ID</DatabaseID>
                </Object>
                <Type>ProcessFull</Type>
                <WriteBackTableCreation>UseExisting</WriteBackTableCreation>
            </Process>
        </Parallel>
    </Batch>',
    @server=N'localhost:2383',
    @database_name=N'master',
    @flags=0,
    @proxy_name=N'SSAS_Proxy'
GO
```

## Revoking SSAS access from the proxy

You can revoke access to the SSAS subsystem and delete the SSAS proxy using the following stored procedures.

###### To revoke access and delete the proxy

1. Revoke subsystem access.

```
USE [msdb]
GO
EXEC msdb.dbo.rds_sqlagent_proxy @task_type='REVOKE_SUBSYSTEM_ACCESS',@proxy_name='SSAS_Proxy',@proxy_subsystem='SSAS'
GO
```

2. Revoke the grants on the proxy.

```
USE [msdb]
GO
EXEC msdb.dbo.sp_revoke_login_from_proxy @proxy_name=N'SSAS_Proxy',@name=N'`mydomain`\`user_name`'
GO
```

3. Delete the proxy.

```
USE [msdb]
GO
EXEC dbo.sp_delete_proxy @proxy_name = N'SSAS_Proxy'
GO
```

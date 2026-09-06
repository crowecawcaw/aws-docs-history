

# Accessing the SSRS or PBIRS web portal
<a name="SSRS.Access"></a>

Use the following process to access the SSRS or PBIRS web portal:

1. Turn on Secure Sockets Layer (SSL).

1. Grant access to domain users.

1. Access the web portal using a browser and the domain user credentials.

## Using SSL on RDS
<a name="SSRS.Access.SSL"></a>

SSRS uses the HTTPS SSL protocol for its connections. To work with this protocol, import an SSL certificate into the Microsoft Windows operating system on your client computer.

For more information on SSL certificates, see [Using SSL/TLS to encrypt a connection to a DB instance or cluster ](UsingWithRDS.SSL.md). For more information about using SSL with SQL Server, see [Using SSL with a Microsoft SQL Server DB instance](SQLServer.Concepts.General.SSL.Using.md).

## Granting access to domain users
<a name="SSRS.Access.Grant"></a>

In a new SSRS or PBIRS activation, there are no role assignments. To give a domain user or user group access to the web portal, RDS provides a stored procedure.

**To grant access to a domain user on the SSRS web portal**
+ Use the following stored procedure.

  ```
  exec msdb.dbo.rds_msbi_task
  @task_type='SSRS_GRANT_PORTAL_PERMISSION',
  @ssrs_group_or_username=N'{{AD_domain}}\{{user}}';
  ```

**To grant access to a domain user on the PBIRS web portal (SQL Server 2025 and higher)**
+ Use the following stored procedure.

  ```
  exec msdb.dbo.rds_msbi_task
  @task_type='PBIRS_GRANT_PORTAL_PERMISSION',
  @pbirs_group_or_username=N'{{AD_domain}}\{{user}}';
  ```

The domain user or user group is granted the `RDS_SSRS_ROLE` system role for SSRS, or the equivalent role for PBIRS. This role has the following system-level tasks granted to it:
+ Run reports
+ Manage jobs
+ Manage shared schedules
+ View shared schedules

The item-level role of `Content Manager` on the root folder is also granted.

## Accessing the web portal
<a name="SSRS.Access.Portal"></a>

After the `SSRS_GRANT_PORTAL_PERMISSION` or `PBIRS_GRANT_PORTAL_PERMISSION` task finishes successfully, you have access to the portal using a web browser. The web portal URL format and endpoint are the same for both SSRS and PBIRS:

```
https://{{rds_endpoint}}:{{port}}/Reports
```

In this format, the following applies:
+ {{`rds_endpoint`}} – The endpoint for the RDS DB instance. You can find the endpoint on the **Connectivity & security** tab for your DB instance. For more information, see [Connecting to your Microsoft SQL Server DB instance](USER_ConnectToMicrosoftSQLServerInstance.md).
+ `{{port}}` – The listener port that you set in the SSRS or PBIRS option.

**To access the web portal**

1. Enter the web portal URL in your browser. For example:

   ```
   https://myssrsinstance.cg034itsfake.us-east-1.rds.amazonaws.com:8443/Reports
   ```

1. Log in with the credentials for a domain user that you granted access with the `SSRS_GRANT_PORTAL_PERMISSION` task (for SSRS) or the `PBIRS_GRANT_PORTAL_PERMISSION` task (for PBIRS).
# Accessing the SSRS web portal

Use the following process to access the SSRS web portal:

1. Turn on Secure Sockets Layer (SSL).
2. Grant access to domain users.
3. Access the web portal using a browser and the domain user credentials.

## Using SSL on RDS

SSRS uses the HTTPS SSL protocol for its connections. To work with this protocol, import an
SSL certificate into the Microsoft Windows operating system on your client
computer.

For more information on SSL certificates, see [Using SSL/TLS to encrypt a connection to a DB
instance or cluster](UsingWithRDS.md "UsingWithRDS.md"). For more information about using SSL with
SQL Server, see [Using SSL with a Microsoft SQL Server DB instance](SQLServer.Concepts.General.SSL.md "SQLServer.Concepts.General.SSL.md").

## Granting access to domain users

In a new SSRS activation, there are no role assignments in SSRS. To give a domain user or
user group access to the web portal, RDS provides a stored procedure.

###### To grant access to a domain user on the web portal

- Use the following stored procedure.

```
exec msdb.dbo.rds_msbi_task
@task_type='SSRS_GRANT_PORTAL_PERMISSION',
@ssrs_group_or_username=N'`AD_domain`\`user`';
```

The domain user or user group is granted the `RDS_SSRS_ROLE` system role. This
role has the following system-level tasks granted to it:

- Run reports
- Manage jobs
- Manage shared schedules
- View shared schedules

The item-level role of `Content Manager` on the root folder is also
granted.

## Accessing the web portal

After the `SSRS_GRANT_PORTAL_PERMISSION` task finishes successfully, you have
access to the portal using a web browser. The web portal URL has the following
format.

```
https://`rds_endpoint`:`port`/Reports
```

In this format, the following applies:

- `rds_endpoint` – The endpoint for the RDS DB
  instance that you're using with SSRS.

You can find the endpoint on the **Connectivity & security** tab for
your DB instance. For more information, see [Connecting to your Microsoft SQL Server
DB instance](USER_ConnectToMicrosoftSQLServerInstance.md "USER_ConnectToMicrosoftSQLServerInstance.md").

- `port` – The listener port for SSRS that you
  set in the `SSRS` option.

###### To access the web portal

1. Enter the web portal URL in your browser.

```
https://myssrsinstance.cg034itsfake.us-east-1.rds.amazonaws.com:8443/Reports
```

2. Log in with the credentials for a domain user that you granted access with
   the `SSRS_GRANT_PORTAL_PERMISSION` task.

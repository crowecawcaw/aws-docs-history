# Deploying reports and configuring report data sources

Use the following procedures to deploy reports to SSRS and configure the reporting data sources:

###### Topics

- [Deploying reports to SSRS](#SSRS.Deploy "#SSRS.Deploy")
- [Configuring the report data source](#SSRS.ConfigureDataSource "#SSRS.ConfigureDataSource")

## Deploying reports to SSRS

After you have access to the web portal, you can deploy reports to it. You can use the Upload tool in the web portal to upload reports, or deploy directly from
[SQL Server data tools (SSDT)](https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt "https://docs.microsoft.com/en-us/sql/ssdt/download-sql-server-data-tools-ssdt").
When deploying from SSDT, ensure the following:

- The user who launched SSDT has access to the SSRS web portal.
- The `TargetServerURL` value in the SSRS project properties is set to the HTTPS endpoint of the RDS DB instance suffixed with
  `ReportServer`, for example:

```
https://myssrsinstance.cg034itsfake.us-east-1.rds.amazonaws.com:8443/ReportServer
```

## Configuring the report data source

After you deploy a report to SSRS, you should configure the report data source. When configuring the report data source, ensure the following:

- For RDS for SQL Server DB instances joined to AWS Directory Service for Microsoft Active Directory, use the fully qualified domain name (FQDN) as the data source name of the connection string.
  An example is `myssrsinstance.corp-ad.example.com`,
  where `myssrsinstance` is the DB instance name and `corp-ad.example.com` is the fully qualified domain name.
- For RDS for SQL Server DB instances joined to self-managed Active Directory, use `.`,
  or `LocalHost` as the data source name of the connection string.

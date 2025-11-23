# Features not supported and features with limited support

The following Microsoft SQL Server features aren't supported on Amazon RDS:

- Backing up to Microsoft Azure Blob Storage
- Buffer pool extension
- Custom password policies
- Data Quality Services
- Database Log Shipping
- Database snapshots (Amazon RDS supports only DB instance snapshots)
- Extended stored procedures, including xp_cmdshell
- FILESTREAM support
- File tables
- Machine Learning and R Services (requires OS access to install it)
- Maintenance plans
- Performance Data Collector
- Policy-Based Management
- PolyBase
- Replication
- Resource Governor

In a multi-tenancy environment, we recommend understanding performance
requirements and considerations to minimize problems due to workload
competition for resources.

- Server-level triggers
- Service Broker endpoints
- Stretch database
- TRUSTWORTHY database property (requires sysadmin role)
- T-SQL endpoints (all operations using CREATE ENDPOINT are unavailable)
- WCF Data Services
  The following Microsoft SQL Server features have limited support on Amazon RDS:

- Distributed queries/linked servers. For more information, see [Implement linked servers with
  Amazon RDS for Microsoft SQL Server](https://aws.amazon.com/blogs/database/implement-linked-servers-with-amazon-rds-for-microsoft-sql-server/ "https://aws.amazon.com/blogs/database/implement-linked-servers-with-amazon-rds-for-microsoft-sql-server/").
- Common Runtime Language (CLR). On RDS for SQL Server 2016 and lower versions, CLR is supported in `SAFE` mode and
  using assembly bits only. CLR isn't supported on RDS for SQL Server 2017 and higher versions. For more information, see [Common Runtime Language Integration](https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-integration-overview "https://docs.microsoft.com/en-us/sql/relational-databases/clr-integration/common-language-runtime-integration-overview") in the Microsoft documentation.
- Link servers with Oracle OLEDB in Amazon RDS for SQL Server. For more information,
  see [Support for Linked
  Servers with Oracle OLEDB in Amazon RDS for SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").
  The following features aren't supported on Amazon RDS with SQL Server 2022:

- Suspend database for snapshot
- External Data Source
- Backup and restore to S3 compatible object storage
- Object store integration
- TLS 1.3 and MS-TDS 8.0
- Backup compression offloading with QAT
- SQL Server Analysis Services (SSAS)
- Database mirroring with Multi-AZ deployments. SQL Server Always On is the only supported method with Multi-AZ deployments.

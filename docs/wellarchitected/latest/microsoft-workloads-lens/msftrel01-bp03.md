# MSFTREL01-BP03 Safeguard the continuous accessibility of

essential data from your Microsoft workload

Microsoft workloads encompass diverse technologies including SQL
Server databases, Active Directory domain controllers, Exchange
Server mailbox databases, SharePoint content databases, IIS web
applications, and Windows file servers, each requiring specialized
backup and recovery approaches. A comprehensive data accessibility
strategy must address the unique backup requirements of each
Microsoft technology while using AWS services to maintain business
continuity and data protection.

**Desired outcome:** The organization
maintains comprehensive data accessibility by implementing a robust
strategy that maintains continuous access to Microsoft SQL Server
databases, Active Directory System State and SYSVOL, Exchange
mailbox databases and transaction logs, SharePoint content databases
and search indexes, IIS configurations and application pools, and
Windows system components including certificates and registry
settings. This strategy aligns with AWS best practices for Microsoft
workload management, enabling reliable data recovery and business
continuity while using AWS infrastructure and services.

**Common anti-patterns:**

- Focusing solely on SQL Server databases while ignoring critical
  Active Directory System State backups, Exchange transaction
  logs, SharePoint service applications, and IIS configuration
  files.
- Implementing generic backup strategies without considering
  Microsoft-specific requirements such as VSS integration,
  application-consistent snapshots, and service dependencies.
- Migrating to AWS without adapting backup strategies to utilize
  AWS-native tools for comprehensive Microsoft workload protection
  including AWS Backup, FSx for Windows File Server, and
  application-aware backup solutions.

**Benefits of establishing this best
practice:**

- Verifies complete Microsoft workload restoration by protecting
  databases, system configurations, application states, and
  supporting components across Microsoft technologies, minimizing
  business disruption.
- Using AWS-specific tools and services for Microsoft workload
  management reduces operational costs, improves resource
  efficiency, and provides centralized backup management across
  diverse Microsoft technologies.
- Maintains consistent access to critical data while enabling
  quick recovery of complex Microsoft environments, supporting
  uninterrupted business operations and improved adherence across
  Microsoft services.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a comprehensive inventory of Microsoft workload
components, including: - SQL Server databases and transaction logs

- Active Directory System State and SYSVOL folders - Exchange
  mailbox databases and transport queues - SharePoint content
  databases and service applications - IIS application pools and web
  configurations, Windows certificates and registry settings - FSx for Windows File Server shares

Implement AWS Backup with VSS integration for
application-consistent snapshots, configure Amazon RDS for SQL
Server automated backups, establish AWS Managed Microsoft AD
backup procedures, and use AWS Systems Manager for Windows system
configuration backup.

Regularly test recovery procedures across your Microsoft
technologies, and train staff on AWS best practices for
comprehensive Microsoft workload management.

### Implementation steps

1. Create a complete inventory of Microsoft workload components
   requiring continuous accessibility, including:
   1. SQL Server databases
   2. Active Directory System State and SYSVOL,
   3. Exchange mailbox databases,
   4. SharePoint content databases,
   5. IIS configurations,
   6. Windows system settings,
   7. and FSx for Windows File Server data

2. Configure AWS Backup with VSS integration for
   application-consistent snapshots of Microsoft workloads,
   implement Amazon RDS automated backups for managed SQL
   Server instances, establish AWS Managed Microsoft AD backup
   procedures, and set up FSx for Windows File Server backup
   policies.
3. Establish and document comprehensive recovery procedures
   including restoration order and dependencies between
   Microsoft services, Active Directory domain controller
   recovery, SQL Server Always On Availability Group
   restoration, Exchange Database Availability Group recovery,
   and SharePoint farm restoration procedures.
4. Schedule regular recovery testing and validation exercises
   across your Microsoft technologies to check the
   effectiveness of the comprehensive data accessibility
   strategy, including cross-service dependency validation and
   disaster recovery scenario testing.

## Resources

**Related documents:**

- [Migrating
  Microsoft SQL Server databases to the AWS Cloud](../../../prescriptive-guidance/latest/migration-sql-server/welcome.md "../../../prescriptive-guidance/latest/migration-sql-server/welcome.md")
- [Optimize
  SQL Server backup strategies](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-backup.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-backup.md")
- [How
  to simplify Microsoft SQL Server backup using AWS Backup and
  VSS](https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/ "https://aws.amazon.com/blogs/storage/how-to-simplify-microsoft-sql-server-backup-using-aws-backup-and-vss/")
- [Automating
  SQL Server Point-in-Time Recovery Using EBS Snapshots](https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/ "https://aws.amazon.com/blogs/modernizing-with-aws/automating-sql-server-point-in-time-recovery-using-ebs-snapshots/")

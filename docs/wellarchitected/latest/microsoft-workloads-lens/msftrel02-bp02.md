# MSFTREL02-BP02 Develop a strategic plan for quickly reinstating

service availability during outages

Microsoft workloads require specialized disaster recovery strategies
due to their unique architectural dependencies and state management
requirements. SQL Server Always On Availability Groups, Active
Directory domain controllers, Exchange Database Availability Groups,
and Windows Failover Clusters each have specific recovery procedures
that differ from generic cloud workload restoration, requiring
tailored approaches for rapid service reinstatement.

**Desired outcome:** Implement a
comprehensive service restoration strategy specifically designed for
Microsoft workloads that includes automated recovery procedures for
SQL Server Always On configurations, Active Directory hybrid
scenarios, and Windows-based clustering services. This plan should
use AWS Elastic Disaster Recovery (DRS) for block-level replication
while addressing Microsoft-specific challenges such as cluster
reformation, domain controller restoration, and
application-consistent recovery.

**Common anti-patterns:**

- Treating Microsoft workloads as generic applications during DR
  planning, failing to account for Active Directory dependencies,
  SQL Server cluster requirements, or Windows-specific services
  that require specialized recovery procedures.
- Relying on AWS DRS replication alone without planning for
  Microsoft cluster reformation, resulting in standalone SQL
  Server instances instead of properly configured Always On
  Availability Groups at the DR site.

**Benefits of establishing this best
practice:**

- Verifies that complex Microsoft services like SQL Server
  clusters and Active Directory maintain their intended
  architecture and functionality after disaster recovery events.
- Pre-planned procedures for reforming Windows Failover Clusters
  and reestablishing Always On Availability Groups minimize manual
  intervention and potential errors during critical recovery
  operations.
- Maintains integration between on-premises Active Directory and
  AWS-hosted domain controllers, preserving authentication
  services and trust relationships during outages.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop Microsoft workload-specific disaster recovery procedures
that address SQL Server Always On Availability Groups restoration
using AWS DRS, Active Directory domain controller recovery with
proper site configuration, and Windows Failover Cluster
reformation at DR sites.

Implement AWS Backup for Active Directory System State backups and
configure cross-region replication for critical Microsoft
services.

Establish automated procedures for reestablishing trust
relationships, cluster quorum, and application dependencies
specific to Microsoft environments.

### Implementation steps

1. Configure AWS Elastic Disaster Recovery (DRS) for SQL Server
   Always On primary nodes with plans for cluster reformation
   and secondary replica establishment at the DR site.
2. Implement Active Directory disaster recovery using AWS DRS
   for domain controllers combined with AWS Backup for System
   State backups, providing a proper site and subnet
   configuration for hybrid scenarios.
3. Establish Windows Failover Cluster recovery procedures
   including shared storage configuration using Amazon FSx for Windows File Server and cluster quorum reestablishment.
4. Create automated runbooks for Microsoft-specific recovery
   tasks including SQL Server Always On listener
   reconfiguration, Active Directory trust relationship
   validation, and Exchange Database Availability Group
   restoration.
5. Configure cross-Region backup strategies for Microsoft
   workloads using AWS Backup with application-consistent
   snapshots and coordinate with AWS DRS replication schedules.
6. Implement regular testing procedures that validate Microsoft
   service dependencies, cluster functionality, and hybrid
   Active Directory connectivity after DR scenarios.

## Resources

**Related documents:**

- [Set
  up high availability for SQL Server at DR site using AWS
  Elastic Disaster Recovery](https://aws.amazon.com/blogs/modernizing-with-aws/set-up-high-availability-for-sql-server-at-dr-site-using-aws-elastic-disaster-recovery/ "https://aws.amazon.com/blogs/modernizing-with-aws/set-up-high-availability-for-sql-server-at-dr-site-using-aws-elastic-disaster-recovery/")
- [Hybrid
  Active Directory disaster recovery solutions on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/hybrid-active-directory-disaster-recovery-cyber-resiliency-and-high-availability-solutions-on-aws/ "https://aws.amazon.com/blogs/modernizing-with-aws/hybrid-active-directory-disaster-recovery-cyber-resiliency-and-high-availability-solutions-on-aws/")
- [Choose
  a high availability and disaster recovery solution](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-hadr.md")

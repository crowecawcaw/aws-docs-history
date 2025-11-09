# Best Practice 10.3 – Define an

approach to help ensure the availability of critical SAP data

The business data for an SAP application is primarily stored within the database, but
may also include file-based data or binaries (for example, executables, libraries, scripts,
configuration, and interface files).

**Suggestion 10.3.1 – Evaluate MTTR requirements and identify how they
can be met**

In [Reliability] [Suggestion 10.1.5 – Define
minimum acceptable percentage uptime](best-practice-10-1.md "best-practice-10-1.md"), you will have defined the MTTR requirements
for each of your applications. Having assessed the risk of failures and the mechanisms for
protecting system availability, confirm your requirements can be met, and document the
expectations for MTTR against each failure scenario. If compromises need to be made for
cost, complexity, or consistency, consult with the business owners to reach an agreement.

**Suggestion 10.3.2 – Determine in which failure scenarios a recovery
from backup would be necessary**

Backup is often a secondary mechanism for ensuring or recovering availability, but
most architectures will have some reliance on backups. The following are examples of
failure scenarios that could be used to guide your analysis. The granularity of the
scenarios, classification, and impact will vary depending on your requirements and
architecture.

|                                                                                                                 | Comparative Risk of Occurrence | Backup Required | Potential Data Loss | Estimated Recovery Time |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------ | --------------- | ------------------- | ----------------------- |
| Planned / Controlled Maintenance                                                                                | Planned                        |                 |                     |                         |
| Resource exhausted or compromised (High CPU utilization /<br>File system full / Out of memory / Storage issues) | Medium                         |                 |                     |                         |
| Distributed stateless component failure (for example, Web<br>Dispatchers)                                       | Medium                         |                 |                     |                         |
| Distributed stateful component failure (for example,<br>application servers)                                    | Medium                         |                 |                     |                         |
| Single Point of Failure (Database / SAP Central<br>Services)                                                    | Medium                         |                 |                     |                         |
| AZ / Network Failure                                                                                            | Low                            |                 |                     |                         |
| Core service failure (DNS / Amazon EFS / API<br>calls)                                                          | Low / Medium                   |                 |                     |                         |
| Corruption / Accidental deletion / Malicious activities /<br>Faulty code deployment                             | Low                            |                 |                     |                         |
| Region failure                                                                                                  | Very low                       |                 |                     |                         |

**Suggestion 10.3.3 – Determine where data replication is
required**

Data replication is used to improve reliability by having copies of the same data in
multiple locations and is often a requirement for systems with a low RPO. When determining
whether replication is required for availability or recovery, consider whether the service
is Zonal (for example, Amazon EC2 and Amazon EBS and the databases they support) or Regional (for
example, shared storage and Amazon S3).

| Database replication | Database                | Replication Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Guidance |
| -------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| SAP HANA             | HANA System Replication | SAP Documentation: [HANA System Replication](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/676844172c2442f0bf6c8b080db05ae7.html "https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/676844172c2442f0bf6c8b080db05ae7.html")                                                                                                                                                                                                                                                                          |
| SAP ASE              | SAP Replication Server  | SAP Documentation: [SAP Replication<br>Server](https://help.sap.com/viewer/product/SAP_REPLICATION_SERVER "https://help.sap.com/viewer/product/SAP_REPLICATION_SERVER")                                                                                                                                                                                                                                                                                                                                                                                  |
| Oracle               | Oracle Data Guard       | SAP Note: [105047<br>• Support for<br>Oracle functions in the SAP environment](https://launchpad.support.sap.com/#/notes/105047 "https://launchpad.support.sap.com/#/notes/105047") [Requires SAP Portal Access]                                                                                                                                                                                                                                                                                                                                         |
| Microsoft SQL Server | SQL Server Always ON    | • SAP Documentation: [Database High-Availability with SQL Server AlwaysOn](https://help.sap.com/viewer/34ba60e8526d4110921c9c0fd05b4b6d/LATEST/en-US/483523b4fd7c433998ec38dadcd67d3c.html "https://help.sap.com/viewer/34ba60e8526d4110921c9c0fd05b4b6d/LATEST/en-US/483523b4fd7c433998ec38dadcd67d3c.html")<br>• AWS Documentation: [SQL Server Deployment for High Availability](../../../sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.md "../../../sap/latest/sap-netweaver/sql-server-deployment-for-high-availability.md") |
| SAP MaxDB            | MaxDb Standby Database  | SAP Note: [952783<br>• FAQ: SAP MaxDB<br>high availability](https://launchpad.support.sap.com/#/notes/952783 "https://launchpad.support.sap.com/#/notes/952783") [Requires SAP Portal Access]                                                                                                                                                                                                                                                                                                                                                            |
| IBM Db2              | HADR                    | SAP Note: [1612105<br>• DB6: FAQ on<br>Db2 High Availability Disaster Recovery (HADR)](https://launchpad.support.sap.com/#/notes/1612105 "https://launchpad.support.sap.com/#/notes/1612105") [Requires SAP Portal<br>Access]                                                                                                                                                                                                                                                                                                                            |

| AWS service replication options    | Service      | Operating level                                                                              | Replication options available                                                                                                                                                       | Guidance |
| ---------------------------------- | ------------ | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| Amazon EFS                         | File system  | Continuous asynchronous replication within a Region and cross Region                         | [Amazon EFS Replication](../../../efs/latest/ug/efs-replication.md "../../../efs/latest/ug/efs-replication.md")                                                                     |
| Amazon FSx for Windows File Server | File system  | Scheduled asynchronous replication within a Region and cross Region using<br>AWS DataSync    | [Scheduled replication using AWS DataSync](../../../fsx/latest/WindowsGuide/scheduled-replication-datasync.md "../../../fsx/latest/WindowsGuide/scheduled-replication-datasync.md") |
| Amazon FSx for NetApp ONTAP        | File system  | Scheduled asynchronous replication within a region and cross region via NetApp<br>SnapMirror | [Scheduled replication using NetApp SnapMirror](../../../fsx/latest/ONTAPGuide/scheduled-replication.md "../../../fsx/latest/ONTAPGuide/scheduled-replication.md")                  |
| Amazon S3                          | S3 bucket    | Continuous asynchronous replication within a Region and cross Region                         | [Amazon S3 Replicating objects](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md")                                              |
| AWS Elastic Disaster Recovery      | EC2 instance | Continuous asynchronous replication within a Region and cross Region                         | [AWS Elastic Disaster Recovery](../../../drs/latest/userguide/what-is-drs.md "../../../drs/latest/userguide/what-is-drs.md")                                                        |

**Suggestion 10.3.4 – Build a strategy to ensure consistent
configuration data and binaries**

It is important to have consistent configuration data and binaries to help ensure
predictable behavior and a tested setup following a failure. This can include operating
system packages, application parameters, and cluster configuration. Determine how you
could ensure alignment across all instances for an application, including those which are
there for resilience (for example, additional application servers, secondary database
nodes).

Amazon EFS, Amazon FSx, and Amazon S3 provide a durable location for shared binaries
or configuration that can be managed centrally.

Refer to [Operational Excellence] [Best Practice 2.1

- Use version control and configuration management](best-practice-2-1.md "best-practice-2-1.md") pillar for mechanisms to
  control versions and manage configuration.

**Suggestion 10.3.5 – Have a holistic approach to data
consistency**

The approach to ensuring the consistency of critical SAP data should not only focus on
a single set of data but also should consider the dependencies within and between datasets
and systems. For example, if you need to recover an SAP BW system, but not the source
systems it pulls from, what would be the impact on change pointers and what mechanisms are
in place to ensure a consistent recovery?

**Suggestion 10.3.6 – Build a strategy for interfaces that permits
data to be replayed or re-sent**

For data exchange between systems, determine whether the integration is loosely
coupled and if data can be replayed or re-sent, either at the source or target. Review if
there are queuing capabilities to allow the scenario to be suspended or cached during an
outage.

**Suggestion 10.3.7 – Evaluate the use of a data bunker**

Failure scenarios that result in the online data becoming unusable or unavailable due
to situations such as accidental deletion or a malicious act might require a different
approach to help ensure that data is protected or recoverable.

Although prevention is the best defense through a security framework covering network
isolation and access control, the impact should be considered in the context of recovery
and resilience.

Using a _write only_ backup account with a reduced retention
period is a common approach for this rare but potentially high impact scenario.

- SAP Lens [Security]: [Best Practice 8.3 - Secure
  your data recovery mechanisms to protect against threats](best-practice-8-3.md "best-practice-8-3.md")



# Best Practice 15.4 – Consider performance tuning for recovery and availability options
<a name="best-practice-15-4"></a>

In alignment with both the Well-Architected Reliability and Operational Excellence pillars, tuning of the SAP system given your chosen recovery and resiliency requirements should be evaluated to minimize any performance impact. Take into consideration items such as system performance during a backup, clustering options for the chosen database (for example, synchronous vs. asynchronous SAP HANA System Replication), and the distribution of load across multiple SAP application server instances.

 **Suggestion 15.4.1 – Review performance recommendations for backup and recovery solutions** 

Each supported database has different recommendations to optimize the performance of backups and recovery operations, and these often work in conjunction with your chosen software solution for managing backups and restores, including third-party offerings. 

In general, following the guidelines for improving throughput between an EC2 instance and the storage target of your backup (such as, EBS volumes, S3 buckets, and EFS file systems) can improve the performance of your backup and recovery.

For example, when using Amazon S3 as a repository for backups and AWS Backint Agent for SAP HANA, you can enable performance improvements via changing configuration parameters, such as the maximum concurrency settings. Another common way to improve backup performance is to increase EBS volume performance characteristics, such as maximizing GP3 throughput configuration to 1,000 MB/s. 

 For more information, refer to the following: 
+  AWS Documentation: [AWS Backint Agent for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-installing-configuring.html#aws-backint-agent-performance-tuning) 
+  AWS Documentation: [SAP NetWeaver on AWS – Backup and Recovery](https://docs.aws.amazon.com/sap/latest/sap-netweaver/backup-and-recovery.html) 
+ AWS Documentation: [S3 Configuration Parameters](https://awscli.amazonaws.com/v2/documentation/api/latest/topic/s3-config.html)
+  SAP on AWS Blog: [Build for availability and reliability](https://aws.amazon.com/blogs/awsforsap/sap-on-aws-build-for-availability-and-reliability/) 


| Database | Guidance | 
| --- | --- | 
| SAP HANA |  +   AWS Documentation: [SAP HANA on AWS – Storage Configuration for SAP HANA](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-storage-config.html) <br />+   SAP Note: [1842096 - HANA Backup & Restore Performance](https://launchpad.support.sap.com/#/notes/1842096) [Requires SAP Portal Access]  <br />+   SAP Note: [2945518 - Performance issues encountered on HANA when a data backup is running](https://launchpad.support.sap.com/#/notes/2945518) [Requires SAP Portal Access]    | 
| SAP ASE | (Consult SAP or Vendor documentation for guidance) | 
| IBM Db2 | (Consult SAP or Vendor documentation for guidance) | 
| Oracle |  SAP Note: [2084077 - How to plan backup cycle for Oracle database](https://launchpad.support.sap.com/#/notes/2084077) [Requires SAP Portal Access]  | 
| Microsoft SQL Server |  SAP Note: [1420452 - FAQ: Restore and recovery with MS SQL Server](https://launchpad.support.sap.com/#/notes/1420452) [Requires SAP Portal Access]  | 
| SAP MaxDB |  SAP Note: [1377148 - FAQ: SAP MaxDB backup / recovery](https://launchpad.support.sap.com/#/notes/1377148) [Requires SAP Portal Access]  | 

 **Suggestion 15.4.2 – Review configuration of clustering parameters** 

 Clustering options for SAP HANA and other databases often rely on a confirmed connection in a cluster (that is, a heartbeat) between the primary instance and the failover instance. SAP administrators must balance the speed with which an action can occur in the system with the potential for any failover side effects that may occur if there is a false negative interruption in communication. Follow recommendations for timeout parameters and related settings. 
+  AWS Documentation: [SAP HANA on AWS: High Availability Configuration Guide for SLES and RHEL](https://docs.aws.amazon.com/sap/latest/sap-hana/sap-hana-on-aws-ha-configuration.html) 
+  AWS Documentation: [SAP HANA on AWS Operations Guide: Networking](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-networking.html) 
+  AWS Documentation: [SAP on AWS – IBM Db2 HADR with Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-AnyDB/sap-ibm-pacemaker.html) 
+  SAP Note: 1612105 - [DB6: FAQ on Db2 High Availability Disaster Recovery (HADR)](https://launchpad.support.sap.com/#/notes/1612105) [Requires SAP Portal Access] 
+  Operating System-specific Documentation: [SUSE Linux SAP HSR Scale-up Performance Optimized Scenario](https://documentation.suse.com/sbp/all/html/SLES4SAP-hana-sr-guide-PerfOpt-12/index.html) 
+  Operating System-specific Documentation: [Automated SAP HANA System Replication in Scale-Up in pacemaker cluster](https://access.redhat.com/articles/3004101) 
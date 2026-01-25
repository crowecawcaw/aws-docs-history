# Databases for SAP on AWS with Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed service that provides highly reliable, scalable, high-performing, and feature-rich file storage built on NetApp’s popular ONTAP file system. You can now deploy and operate SAP applications using IBM Db2, SAP MaxDB, SAP ASE, Oracle, and MSSQL on AWS with FSx for ONTAP. For more information, see [Amazon FSx for NetApp ONTAP](https://aws.amazon.com/fsx/netapp-ontap/ "https://aws.amazon.com/fsx/netapp-ontap/").

If you are a first-time user, see [How Amazon FSx for NetApp ONTAP works](../../../fsx/latest/ONTAPGuide/how-it-works-fsx-ontap.md "../../../fsx/latest/ONTAPGuide/how-it-works-fsx-ontap.md").

###### Topics

- [Instances and sizing](#rules "#rules")
- [Supported instance types](#instance-types "#instance-types")
- [Sizing](#sizing "#sizing")
- [Create storage virtual machines (SVM)](#svm-sap "#svm-sap")
- [Volume configuration and layout](#volume-configuration "#volume-configuration")
- [File system setup](#filesystem-setup "#filesystem-setup")
- [Architecture diagrams for databases with Amazon FSx for NetApp ONTAP](architecture.md "architecture.md")
- [Host setup for databases with Amazon FSx for NetApp ONTAP](host.md "host.md")
- [Installing the databases](installation.md "installation.md")

## Instances and sizing

The following rules and limitations are applicable for deploying SAP applications on AWS using IBM Db2, SAP MaxDB, SAP ASE, Oracle, and MSSQL with FSx for ONTAP.

- Amazon EC2 instance where you plan to deploy the database and FSx for ONTAP must be in the same subnet.
- Use separate storage virtual machines (SVM) for binarie, data, and log volumes of the database. This ensures that your I/O traffic flows through different IP addresses and TCP sessions.
- The following file systems must have their separate FSx for ONTAP volumes. See the following tabs.

IBM Db2

    + `/db2/<DBSID>/sapdata1`
    + `/db2/<DBSID>/sapdata1`
    + `/db2/<DBSID>/log_dir`
    + `/db2/<DBSID>/saptmp<x>`
    + `/db2/<DBSID>/log_arch`
    + `/usr/sap`

SAP MaxDB

    + `/sapdb/<SID>/sapdata`
    + `/sapdb/<SID>/saplog`
    + `/sapdb/<SID>/backup`
    + `/usr/sap`

SAP ASE

    + `/sybase/<SID>/sapdata_1`
    + `/sybase/<SID>/sapdata_n`
    + `/sybase/<SID>/saplog_1`
    + `/sybase/<SID>/saptmp`
    + `/sybase/<SID>/sapdiag`
    + `/sybasebackup`
    + `/usr/sap`

Oracle

    + `/oracle/<DBSID>`
    + `/oracle/<DBSID>/oraarch`
    + `/oracle/<DBSID>/saparch`
    + `/oracle/<DBSID>/sapreorg`
    + `/oracle/<DBSID>/sapbackup`
    + `/oracle/<DBSID>/saptrace`
    + `/oracle/<DBSID>/sapdata<x>`
    + `/oracle/<DBSID>/origlogA`
    + `/oracle/<DBSID>>/origlogB`
    + `/oracle/<DBSID>/mirrlogA`
    + `/oracle/<DBSID>/mirrlogB`

MSSQL

    + `MSSQL data`
    + `MSSQL log`
    + `MSSQL tempdb`
    + SQL binaries (including SQL Server system databases)
    + Backup directories

- FSx for ONTAP creates endpoints for accessing your file system in a Amazon VPC route table. FSx for ONTAP uses your Amazon VPC main route table. We recommend configuring your file system to use all of your Amazon VPC route tables that are associated with the subnets in which your clients are located. Alternatively, you can specify one or more route tables for Amazon FSx to use when you create your file system.
- _Oracle_ – SAP with Oracle Database is supported on Amazon EC2 instances with Amazon FSx for NetApp ONTAP only using Oracle Direct NFS (dNFS) with NFSv3, NFSv4 and NFSv4.1. Kernel NFS mounted filesystems are not supported by SAP for any Oracle files, such as database files, redo logs, and control files. For more information, see [SAP Note 2358420 - Oracle Database Support for Amazon Web Services EC2](https://me.sap.com/notes/2358420 "https://me.sap.com/notes/2358420") (requires SAP portal access).

## Supported instance types

See the following tabs for details.

IBM Db2
FSx for ONTAP is supported for SAP applications using IBM Db2 database in a Single or Multi-Availability Zone deployment. You can use FSx for ONTAP as the primary storage solution for IBM Db2 database devices and backup volumes with supported Amazon EC2 instances.

SAP MaxDB
FSx for ONTAP is supported for SAP MaxDB version 7.9.10 or higher (including liveCache) with SAP applications in a Single or Multi-Availability Zone deployment. You can use FSx for ONTAP as the primary storage solution for SAP MaxDB `data`, `log`, `binary`, and `backup` volumes with supported Amazon EC2 instances.

SAP ASE
FSx for ONTAP is supported for SAP ASE version 16.0 for Business Suite and higher with SAP NetWeaver based applications in a Single or Multi-Availability Zone deployment. You can use FSx for ONTAP as the primary storage solution for SAP ASE `data`, `log`, `sapdiag`, `saptmp`, and `backup` volumes with supported Amazon EC2 instances.

Oracle
FSx for ONTAP is supported for Oracle 19c (minimum 19.5.0) for Business Suite and higher with SAP NetWeaver based applications in a Single or Multi-Availability Zone deployment. You can use FSx for ONTAP as the primary storage solution for Oracle `data`, `log`, `binaries`, `archive`, `backup`, and other volumes volumes with supported Amazon EC2 instances.

You can use the Quick Sizer tool from SAP to calculate the compute requirement in SAPS for a greenfield (new) Oracle deployment. It enables you to choose an instance type that meets your business requirements and is cost-efficient. You can use source system utilisation and workload patterns, such as SAP EarlyWatch alert reports, source system specification: CPU+ memory and source system SAPS rating for migrations.

MSSQL
FSx for ONTAP is supported for SAP applications using MSSQL database in a Single or Multi-Availability Zone deployment. You can use FSx for ONTAP as the primary storage solution for MSSQL `data`, `log`, `tempdb`, `SQL binaries`, and `backup` volumes with supported Amazon EC2 instances.

For a complete list of supported Amazon EC2 instances for the databases, see [SAP Note 1656099 - SAP Applications on Amazon EC2: Supported DB/OS and Amazon EC2 products](https://launchpad.support.sap.com/#/notes/1656099 "https://launchpad.support.sap.com/#/notes/1656099") (requires SAP portal access).

## Sizing

A single FSx for ONTAP file system can provide a maximum output of 80,000 IOPS. Select multiple FSx for ONTAP file systems if your I/O requirement exceeds 80,000 IOPS.

You can configure the throughput capacity of FSx for ONTAP when you create a new file system by scaling up to 4 GB/s of read throughput and 1000 MB/s of write throughput in a single Availability Zone deployment. In a multi-Availability Zone deployment, you can create a file system by scaling up to 4 GB/s of read throughput and 1800 MB/s of write throughput. For more information, see [Performance details](../../../fsx/latest/ONTAPGuide/performance.md#performance-details-fsxw "../../../fsx/latest/ONTAPGuide/performance.md#performance-details-fsxw").

**_Oracle_**

You can calculate the IOPS required by your database by querying the system tables over a period of time and selecting the highest value. You can get this information from the GV$SYSSTAT dynamic performance view from Oracle. This view is continuously updated while the database is open and in use. IOPS requirements can also be validated through Oracle Enterprise Manager and Automatic Workload Repository reports which use these views to gather data. For more information, see [Estimating IOPS for an existing database](../../../whitepapers/latest/determining-iops-needs-oracle-db-on-aws/estimating-iops-for-an-existing-database.md "../../../whitepapers/latest/determining-iops-needs-oracle-db-on-aws/estimating-iops-for-an-existing-database.md").

**_MSSQL_**

For migrating your existing SAP applications based on SQL Server to AWS, use Windows Performance Monitor to get information about IOPS and throughput required for FSx for ONTAP file system. To open Windows Performance Monitor, run `perfmon` at command prompt. IOPS and throughput data is provided by the following performance counters:

- Peak Disk reads/sec + Peak disk writes/sec = IOPS
- Peak Disk read bytes/sec + Peak disk write bytes/sec = throughput

We also recommend that you get the IOPS and throughput data over a typical workload cycle to get a good estimate for your requirements. Ensure that the FSx for ONTAP file system you provision for SQL server supports these I/O and throughput requirements.

For sizing your SAP on SQL environment, you can use:

- SAP Quick Sizer (for new implementations)
- SAP Early Watch Alerts reports

Running MSSQL with FSx for ONTAP file system separates compute and storage. Therefore, SQL server running on smaller EC2 instances connected to FSx for ONTAP can perform the same as SQL server running on a much larger EC2 instance. A smaller instance can also lower the total cost of ownership for your SAP landscape on AWS. For standard database workloads, you can run memory optimized instance classes, such as `r6i`, `r6in`, `r6a`, `r7i`, and `r7a`. For a complete list of supported instances, see [Amazon EC2 instance types for SAP on AWS](../general/ec2-instance-types-sap.md "../general/ec2-instance-types-sap.md").

## Create storage virtual machines (SVM)

You get one SVM per FSx for ONTAP file system by default. You can create additional SVMs at any time. We recommend a separate SVM for each volume. You don’t need to join your file system to Active Directory for the database. For more information, see [Managing FSx for ONTAP storage virtual machines](../../../fsx/latest/ONTAPGuide/managing-svms.md "../../../fsx/latest/ONTAPGuide/managing-svms.md").

## Volume configuration and layout

Before you create an FSx for ONTAP file system, determine the total storage space you need for your system. You can increase the storage size later. To decrease the storage size, you must create a new file system.

The storage capacity of your file system should align with the needs of your database’s system volumes. You must also consider the capacity required for snapshots, if applicable.

The following lists the example volume layout for databases.

IBM Db2| **Volume name** | **Junction name** | **Linux mount points** |
| <SID>-usrsap | /<SID>-usrsap | /usr/sap |
| <SID>-sapmnt | /<SID>-sapmnt | /sapmnt |
| <DBSID>-db2dbsid | /<DBSID>-db2dbsid | /db2/db2<db2sid> |
| <DBSID>-dbpath | /<DBSID>-dbpath | /db2/<DBSID> |
| <DBSID>-sapdata1 | /<DBSID>-sapdata1 | /db2/<DBSID>/sapdata1 |
| <DBSID>-sapdata<x> | /<DBSID>-sapdata<x> | /db2/<DBSID>/sapdata<x> |
| <DBSID>-saptmp1 | /<DBSID>-saptmp1 | /db2/<DBSID>/saptmp1 |
| <DBSID>-saptmp<x> | /<DBSID>-saptmp<x> | /db2/<DBSID>/saptmp<x> |
| <DBSID>-logdir | /<DBSID>-logdir | /db2/<DBSID>/log_dir |
| <DBSID>-logarch | /<DBSID>-logarch | /db2/<DBSID>/log_arch |
| <DBSID>-db2dump | /<DBSID>-db2dump | /db2/<DBSID>/db2dump |
| <DBSID>-backup | /<DBSID>-backup | /db2backup |

SAP MaxDB| **Volume name** | **Junction name** | **Linux mount points** |
| <DBSID>-sapmnt | <DBSID>-sapmnt | /sapmnt/ |
| <DBSID>-usrsap | <DBSID>-usrsap | /usr/sap |
| <DBSID>-sapdata | <DBSID>-sapdata | /sapdb/<DBSID>/sapdata |
| <DBSID>-saplog | <DBSID>-saplog | /sapdb/<DBSID>/saplog |
| <DBSID>-backup | <DBSID>-backup | /sapdb/<DBSID>/backup |
| <DBSID>-sapdb | <DBSID>-sapdb | /sapdb |

SAP ASE| **Volume name** | **Junction name** | **Linux mount points** |
| <SID>-sapmnt | <SID>-sapmnt | /sapmnt/ |
| <SID>-usrsap | <SID>-usrsap | /usr/sap |
| <SID>-sysbase | <SID>-sysbase | /sysbase |
| <SID>-sapdata_1 | <SID>-sapdata_1 | /sysbase/<SID>/sapdata_1 |
| <SID>-saplog_1 | <SID>-saplog_1 | /sysbase/<SID>/saplog_1 |
| <SID>-sapdiag | <SID>-sapdiag | /sysbase/<SID>/sapdiag |
| <SID>-saptmp | <SID>-saptmp | /sysbase/<SID>/saptmp |
| <SID>-backup | <SID>-backup | /sysbasebackup |

Oracle| **Volume name** | **Junction name** | **Linux mount points** |
| <DBSID>-oracle | /<DBSID>-oracle | /oracle |
| <DBSID>-oracle-<DBSID> | /<DBSID>-oracle-<DBSID> | /oracle/<DBSID> |
| <DBSID>-oraarch | /<DBSID>-oraarch | /oracle/<DBSID>/oraarch |
| <DBSID>-saparch | /<DBSID>-saparch | /oracle/<DBSID>/saparch |
| <DBSID>-sapreorg | /<DBSID>-sapreorg | /oracle/<DBSID>/sapreorg |
| <DBSID>-sapbackup | /<DBSID>-sapbackup | /oracle/<DBSID>/sapbackup |
| <DBSID>-saptrace | /<DBSID>-saptrace | /oracle/<DBSID>/saptrace |
| <DBSID>-sapdata1 | /<DBSID>-sapdata1 | /oracle/<DBSID>/sapdata1 |
| <DBSID>-sapdata<x> | /<DBSID>-sapdata<x> | /oracle/<DBSID>/sapdata<x> |
| <DBSID>-origlogA | /<DBSID>-origlogA | /oracle/<DBSID>/origlogA |
| <DBSID>-origlogB | /<DBSID>-origlogB | /oracle/<DBSID>/origlogB |
| <DBSID>-mirrlogB | /<DBSID>-mirrlogB | /oracle/<DBSID>/mirrlogB |
| <DBSID>-mirrlogA | /<DBSID>-mirrlogA | /oracle/<DBSID>/mirrlogA |

MSSQL| **Volume name** | **Directory** | **Description** |
| <SID>-sapdata | <drive>:\<SAPSID>DATA0<br><drive>:\<SAPSID>DATA1<br><drive>:\<SAPSID>DATA<N> | Directory for SAP database data files |
| <SID>-saplog | <drive>:\<SAPSID>log<N> | Directory for SAP database transaction log |
| <SID>-tempdb | <drive>:\Tempdb | Directory for temporary database data files |
| <SID>-sqldbexe | <drive>:\Program Files\Microsoft SQL Server | Directory for SQL server program files, and `master`, `msdb`, and `model` data files |
| <SID>-backup | <drive>:\Backup | SQL server data and log backup directory |

It is recommended to switch on Storage Efficiency, but to keep inactive data compression disabled.

## File system setup

To create a FSx for ONTAP file system, see [Step 1: Create an Amazon FSx for NetApp ONTAP file system](../../../fsx/latest/ONTAPGuide/getting-started-step1.md "../../../fsx/latest/ONTAPGuide/getting-started-step1.md"). For more information, see [Managing FSx for ONTAP file systems](../../../fsx/latest/ONTAPGuide/managing-file-systems.md "../../../fsx/latest/ONTAPGuide/managing-file-systems.md").

After creating a FSx for ONTAP file system, you must complete additional file system setup.

###### Topics

- [Set administrative password](#admin-password "#admin-password")
- [Sign in to the management endpoint via SSH](#ssh "#ssh")
- [Set TCP max transfer size](#tcp-transfer "#tcp-transfer")
- [Disable snapshots](#disable-snapshots "#disable-snapshots")
- [Configuration settings for dynamically allocating storage – MSSQL](#dynamic-storage "#dynamic-storage")

### Set administrative password

If you did not create an administrative password during FSx for ONTAP file system creation, you must set an ONTAP administrative password for `fsxadmin` user.

The administrative password enables you to access the file system via SSH, the ONTAP CLI, and REST API. To use tools like NetApp SnapCenter, you must have an administrative password.

### Sign in to the management endpoint via SSH

Get the DNS name of the management endpoint from AWS console. Sign in to the management endpoint via SSH, using the `fsxadmin` user and administrative password.

```
ssh fsxadmin@management.<file-system-id>.fsx.<aws-region>.amazonaws.com Password:
```

### Set TCP max transfer size

We recommend a TCP max transfer size of 262,144 for your database systems. Elevate the privilege level to _advanced_ and use the following command on each SVM.

```
set advanced
nfs modify -vserver <svm> -tcp-max-xfer-size 262144
set admin
```

### Disable snapshots

FSx for ONTAP automatically enables a snapshot policy for volumes that take hourly snapshots. The default policy offers limited value due to missing application awareness. We recommend disabling the automatic snapshots by setting the policy to none.

```
volume modify -vserver <vserver-name> -volume <volume-name> -snapshot-policy none
```

You can use SnapCenter, a backup management software offered by NetApp to automate backup and restore of your workloads. SnapCenter provides a plug-in for Oracle and MSSQL databases.

### Configuration settings for dynamically allocating storage – MSSQL

This section only applies to MSSQL database.

NetApp recommends that storage space be dynamically allocated to each volume or logical unit number as data is written, instead of allocating space upfront. The following table provides the configuration settings for dynamically allocating storage.

| Setting               | Configuration         |
| --------------------- | --------------------- |
| Volume guarantee      | None (set by default) |
| LUN reservation       | Enabled               |
| fractional_reserve    | 0% (set by default)   |
| snap reserve          | 0%                    |
| Autodelete            | volume/oldest_first   |
| Autosize              | On                    |
| try_first             | Autogrow              |
| Volume tiering policy | Snapshot only         |
| Snapshot policy       | None                  |
| space allocation      | Enabled               |

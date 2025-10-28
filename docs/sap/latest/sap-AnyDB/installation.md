# Installing the databases

See the following tabs for more information.

IBM Db2
You must install the IBM Db2 system as per the instructions provided by SAP. For more information, see [Installation of SAP Systems Based on the Application Server ABAP of SAP NetWeaver 7.3 EHP1 to 7.52 on UNIX: IBM Db2 for Linux, UNIX, and Windows](https://help.sap.com/doc/4f95f7ac741a1014956dd879c2537334/CURRENT_VERSION/en-US/db6_inst_71x_unix_abap.pdf "https://help.sap.com/doc/4f95f7ac741a1014956dd879c2537334/CURRENT_VERSION/en-US/db6_inst_71x_unix_abap.pdf").

SAP MaxDB
You must install the SAP MaxDB as per the instructions provided by SAP. For more information, see [Installation of SAP Systems Based on the Application Server ABAP of SAP NetWeaver 7.3 EHP1 to 7.52 on UNIX: SAP MaxDB](https://help.sap.com/doc/4f96bbba741a101490e5e2c6b8cdf8a6/CURRENT_VERSION/en-US/NW7XX_Inst_Max_UX_ABAP.pdf "https://help.sap.com/doc/4f96bbba741a101490e5e2c6b8cdf8a6/CURRENT_VERSION/en-US/NW7XX_Inst_Max_UX_ABAP.pdf").

**Backup and restore**

Backup and restore operations are supported by standard SAP MaxDB tools. For more information, see [SAP Note 1928060 - Data backup and recovery with file system backup](https://launchpad.support.sap.com/#/notes/1928060 "https://launchpad.support.sap.com/#/notes/1928060")(requires access to the SAP portal).

SAP ASE
You must install the SAP ASE as per the instructions provided by SAP. You can select the relevant guide from the [Guide Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US "https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US") on SAP website.

**Backup and restore**

FSx for ONTAP snapshot is a read-only image of an FSx for ONTAP volume at a point-in-time. Snapshots offer protection against accidental deletion or modification of files in your volumes. Your users can easily view and/or restore individual files or folders from an earlier snapshot. For more information, see [Working with snapshots](../../../fsx/latest/ONTAPGuide/snapshots-ontap.md "../../../fsx/latest/ONTAPGuide/snapshots-ontap.md").

Backup and restore operations are also supported by standard SAP ASE tools. You can check the following SAP Notes (requires SAP portal access) to learn more.

- [SAP Note 1585981 - SYB: Ensuring Recoverability for SAP ASE](https://launchpad.support.sap.com/#/notes/1585981 "https://launchpad.support.sap.com/#/notes/1585981")
- [SAP Note 1588316 - SYB: Configure automatic database and log backups](https://launchpad.support.sap.com/#/notes/1588316 "https://launchpad.support.sap.com/#/notes/1588316")
- [SAP Note 1618817 - SYB: How to restore an SAP ASE database server (UNIX)](https://launchpad.support.sap.com/#/notes/1618817 "https://launchpad.support.sap.com/#/notes/1618817")
- [SAP Note 1887068 - SYB: Using external backup and restore with SAP ASE](https://launchpad.support.sap.com/#/notes/1887068 "https://launchpad.support.sap.com/#/notes/1887068")

Oracle
You must install the Oracle database as per the instructions provided by SAP. You can select the relevant guide from the [Guide Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US "https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US") on SAP website.

**Backup and restore**

FSx for ONTAP snapshot is a read-only image of an FSx for ONTAP volume at a point-in-time. Snapshots offer protection against accidental deletion or modification of files in your volumes. Your users can easily view and/or restore individual files or folders from an earlier snapshot. For more information, see [Working with snapshots](../../../fsx/latest/ONTAPGuide/snapshots-ontap.md "../../../fsx/latest/ONTAPGuide/snapshots-ontap.md").

You can also use the plug-in for Oracle database offered by NetApp SnapCenter. The plug-in takes application-consistent backups using NetApp snapshots and Oracle Recovery Manager.

Backup and restore operations are also supported by standard Oracle database for SAP tools, such as BRTools. You can check the following resources from SAP and Oracle to learn more.

- [SAP Database Guide: Oracle](https://help.sap.com/doc/f63a5adfa5de4d4b8ddf7c5bf7d41c06/129/en-US/0b5daf09b03344ad97338f838e09b9ee.pdf "https://help.sap.com/doc/f63a5adfa5de4d4b8ddf7c5bf7d41c06/129/en-US/0b5daf09b03344ad97338f838e09b9ee.pdf")
- [Oracle Database Backup To Cloud: Amazon Simple Storage Service (S3)](https://www.oracle.com/technetwork/database/features/availability/twp-oracledbcloudbackup-130129.pdf "https://www.oracle.com/technetwork/database/features/availability/twp-oracledbcloudbackup-130129.pdf")
- [SAP Note 2358420 - Oracle Database Support for Amazon Web Services EC2](https://me.sap.com/notes/2358420 "https://me.sap.com/notes/2358420") (requires SAP portal access)
- [SAP Note 1656250 - SAP on AWS: Support prerequisites](https://me.sap.com/notes/1656250 "https://me.sap.com/notes/1656250") (requires SAP portal access)

MSSQL
You must install the MSSQL database as per the instructions provided by SAP. You can select the relevant guide from the [Guide Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US "https://help.sap.com/docs/SAP_NETWEAVER/9e41ead9f54e44c1ae1a1094b0f80712/576f5c1808de4d1abecbd6e503c9ba42.html?language=en-US") on SAP website.

**Backup and restore**

FSx for ONTAP snapshot is a read-only image of an FSx for ONTAP volume at a point-in-time. Snapshots offer protection against accidental deletion or modification of files in your volumes. Your users can easily view and/or restore individual files or folders from an earlier snapshot. For more information, see [Working with snapshots](../../../fsx/latest/ONTAPGuide/snapshots-ontap.md "../../../fsx/latest/ONTAPGuide/snapshots-ontap.md").

Backup and restore operations are also supported by standard SQL server tools. For further details, see [Back Up and Restore of SQL Server Databases](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16 "https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver16").

For point-in-time resilient restores and immutable backups, we storing 3 days of snapshots on a local disk, and replicating older backups via SnapVault. Replicate older backups to a secondary (different Availability Zone) FSx for ONTAP filesystem with capacity pool enabled. For more information, see [Managing storage capacity](../../../fsx/latest/ONTAPGuide/managing-storage-capacity.md "../../../fsx/latest/ONTAPGuide/managing-storage-capacity.md").

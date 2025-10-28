# Best Practice 12.1 – Establish a

method for consistent recovery of business data

Define data recovery plans that can help ensure business data consistency for an
individual system in the event of data loss or corruption.

**Suggestion 12.1.1 - Ensure that database backups are consistent by
using backup mechanisms that are aware of database state**

SAP provides mechanisms for integrating with a database vendor’s backup capability
(for example, brtools) and providing visibility within SAP transactions or management
consoles. In addition, there are options to integrate with third-party backup providers or
storage solutions including [AWS Backint Agent for SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md"). These supported options have awareness of
database state, continuously capturing changes or quiescing the database (pausing or
reducing activity) while a consistent copy is taken, for example using storage snapshots.

Review the SAP guides for individual database vendors as well as AWS documentation:

- AWS Documentation: [AWS Backint Agent for SAP HANA](../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md "../../../sap/latest/sap-hana/aws-backint-agent-sap-hana.md")
- SAP Documentation: [Guide
  Finder for SAP NetWeaver and ABAP Platform](https://help.sap.com/viewer/nwguidefinder "https://help.sap.com/viewer/nwguidefinder")
- SAP on AWS Blog: [How to back up Microsoft SQL Server databases for SAP with VSS Snapshots](https://aws.amazon.com/blogs/awsforsap/how-to-back-up-microsoft-sql-server-databases-for-sap-with-vss-snapshots/ "https://aws.amazon.com/blogs/awsforsap/how-to-back-up-microsoft-sql-server-databases-for-sap-with-vss-snapshots/")
- AWS Blog: [Taking crash-consistent snapshots across multiple Amazon EBS volumes on an Amazon
  EC2 instance](https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/#:~:text=AWS%20Storage%20Blog-,Taking%20crash%2Dconsistent%20snapshots%20across%20multiple%20Amazon%20EBS,on%20an%20Amazon%20EC2%20instance&text=Snapshots%20retain%20the%20data%20from,to%20as%20crash%2Dconsistency). "https://aws.amazon.com/blogs/storage/taking-crash-consistent-snapshots-across-multiple-amazon-ebs-volumes-on-an-amazon-ec2-instance/#:~:text=AWS%20Storage%20Blog-,Taking%20crash%2Dconsistent%20snapshots%20across%20multiple%20Amazon%20EBS,on%20an%20Amazon%20EC2%20instance&text=Snapshots%20retain%20the%20data%20from,to%20as%20crash%2Dconsistency).")

**Suggestion 12.1.2 – Evaluate the durability and recoverability of
file-based data critical to your business**

Business data that is not stored within a database might require a separate backup
strategy.

In a standard SAP NetWeaver system, this often includes file-based interface files,
SAP transport directory contents, and logs including batch logs, job logs, and work process
directory logs. Non-SAP NetWeaver and supporting systems, such as document management
solutions, might have other file-based business data which should be evaluated. Evaluate
[Amazon EFS](https://aws.amazon.com/efs/ "https://aws.amazon.com/efs/") or [Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/") to increase availability and durability of
such file systems.

File system backups can be performed using snapshots, [AWS Backup](https://aws.amazon.com/backup/ "https://aws.amazon.com/backup/"), or third-party backup solutions.

Business data should be evaluated independently from binaries and configuration data,
which might be able to be re-provisioned via SAP download, re-install, or infrastructure as
code.

- SAP Lens [Operational Excellence]: [Suggestion
  12.2.1 - Define infrastructure as code approach to the creation and change of
  configuration](best-practice-12-2.md "best-practice-12-2.md")
- SAP Lens [Operational Excellence]: [Suggestion
  12.2.2 - Define an approach for backups of file system contents, including the root
  volume](best-practice-12-2.md "best-practice-12-2.md")

**Suggestion 12.1.3 – Evaluate the durability and location of database
backups and logs**

Backups and logs contain a record of your live data, but can themselves be
susceptible to failure. Consider how you minimize the impact of a failure by evaluating
the location of your backups in relation to your active data copies. It’s important to
consider the following:

- The time it takes to secure the backups – impacting your recovery point
- The time it takes to retrieve/recover the backups – impacting your recovery
  time
  Additional information:

- AWS Documentation: [AWS
  Backint Agent for HANA](https://aws.amazon.com/backint-agent/ "https://aws.amazon.com/backint-agent/")
- AWS Documentation: [FSR (Fast Snapshot Restores)](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md")
- AWS Documentation: [Amazon S3
  Replication options](../../../AmazonS3/latest/dev/replication.md "../../../AmazonS3/latest/dev/replication.md")

**Suggestion 12.1.4 – Evaluate your requirements for a point-in-time
recovery**

If you have a requirement to recover to any particular point in time, does your backup
design allow for this? Is the backup method database-aware and can you roll your database
forward to a consistent recovery point? Have you considered any file-based recovery
required for consistency?

Consider the following:

- The log interval and how quickly logs are secured
- Incremental or differential backups to improve the recovery time
- If a backup catalog or other mechanism is required
- Is it possible to use database or storage options to go back in time?

**Suggestion 12.1.5 – Review mechanisms for recovery caused by data
loss**

Determine the implications of recovering from a significant data loss situation, such
as data corruption, deletion, or a faulty code deployment that is unable to be reverted.
Evaluate the propagation of data loss when using database or storage-based replication,
and the RTO and RPO impact of using a secondary restore mechanism, such as backups.

**Suggestion 12.1.6 – Create a data bunker**

Following the guidance in [Suggestion 10.3.7 -
Determine in which failure scenarios a recovery from backup would be necessary](best-practice-10-3.md "best-practice-10-3.md"),
create a data bunker to secure your backups from accidental deletion or malicious
activities.

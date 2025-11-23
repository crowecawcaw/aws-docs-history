# Microsoft SQL Server on Amazon EC2 backup with the AWS VSS solution

You can use the AWS VSS solution to create snapshots of the volumes attached to your EC2 instance,
including data from your Microsoft SQL Server database. The AWS VSS solution uses Amazon managed command documents
with the [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md").
The snapshot process uses the Windows [Volume Shadow Copy Service (VSS)](https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service "https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service") to create EBS volume-level backups without
requiring you to shut down or pause your SQL Server application or disconnect active connections.

There is no additional cost to use the AWS VSS solution to create EBS snapshots. You only pay for
EBS snapshots created by the backup process. For more information, see [How am I billed
for my Amazon EBS snapshots?](https://repost.aws/knowledge-center/ebs-snapshot-billing/ "https://repost.aws/knowledge-center/ebs-snapshot-billing/")

To restore your SQL Server databases from AWS VSS solution based EBS snapshots, see [Use an automation runbook to restore your database from AWS VSS solution snapshots](ms-ssdb-ec2-restore-vss.md "ms-ssdb-ec2-restore-vss.md").

## AWS VSS solution based snapshot prerequisites

To start backing up your SQL Server databases with AWS VSS solution based EBS snapshots, you must
meet all of the prerequisites.

- Your instance must satisfy the system requirements, and have the appropriate
  IAM permissions attached to your instance profile role. If you use Systems Manager to run
  the recommended command document (`AWSEC2-VssInstallAndSnapshot`), you
  can skip the component install prerequisite. That command document automatically
  installs the VSS components as needed on your instance.

For more information, see [Prerequisites to create
Windows VSS based EBS snapshots](../../../index.md "../../../index.md") in the
_Amazon EC2 User Guide_.

- To enable the restore process for your SQL Server database, you must set your
  database to full recovery mode before you take the snapshot. To configure
  recovery mode, see [View or change the recovery model of a database (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/view-or-change-the-recovery-model-of-a-database-sql-server "https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/view-or-change-the-recovery-model-of-a-database-sql-server") on the _Microsoft Learn_
  website.

## Create AWS VSS solution based EBS snapshots

To create EBS snapshots that you can use to restore your database instance, see
[Use Systems Manager
command documents to create VSS based snapshots](../../../AWSEC2/latest/UserGuide/create-vss-snapshots-ssm.md "../../../AWSEC2/latest/UserGuide/create-vss-snapshots-ssm.md"). We recommend that you run the
**AWSEC2-VssInstallAndSnapshot** command document, which automatically installs
the VSS components as needed on your instance.

###### Note

To ensure that you can use the AWS VSS solution snapshots to restore your database, set the
`SaveVssMetadata` parameter to `True` for your command document
before you run it.

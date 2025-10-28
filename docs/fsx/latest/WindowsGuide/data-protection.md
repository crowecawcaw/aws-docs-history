# Protecting your data with backups, shadow copies, and scheduled replication

Beyond automatically replicating your file system's data to ensure high durability, Amazon FSx provides you with
the following options to further protect the data stored on your file systems:

- Native Amazon FSx backups support your backup retention and compliance needs within Amazon FSx.
- AWS Backup backups of your Amazon FSx file systems are part of a centralized and automated backup
  solution across AWS services in the cloud and on premises.
- Windows shadow copies enable your users to easily undo file changes and compare file
  versions by restoring files to previous versions.
- AWS DataSync scheduled replication of your Amazon FSx file system to a second file system
  provides data protection and recovery.

###### Topics

- [Protecting your data with backups](using-backups.md "using-backups.md")
- [Protecting your data with shadow copies](shadow-copies-fsxW.md "shadow-copies-fsxW.md")
- [Scheduled replication using AWS DataSync](#scheduled-replication-datasync "#scheduled-replication-datasync")

## Scheduled replication using AWS DataSync

You can use AWS DataSync to schedule periodic replication of your FSx for Windows File Server file system
to a second file system. This capability is available for both in-Region and cross-Region
deployments. To learn more, see [Migrating existing files to FSx for Windows File Server using
AWS DataSync](migrate-files-to-fsx-datasync.md "migrate-files-to-fsx-datasync.md") in this guide and [Data transfer between AWS storage services](../../../datasync/latest/userguide/how-datasync-works.md#in-cloud-transfer "../../../datasync/latest/userguide/how-datasync-works.md#in-cloud-transfer")
in the _AWS DataSync User Guide_.

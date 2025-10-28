This is version 2.18 of the AWS Elemental Conductor File documentation. This is the
latest version. For prior versions, see the _Archive_ section of
[AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Work with Database Backups for

AWS Elemental Conductor File

###### Important

To set up database backup for the entire cluster, you need perform this setup only on the Conductor node. If you have two Conductor nodes, you need perform this setup only on the primary Conductor node.

All nodes in the cluster – Conductor and worker nodes – share the same database. The AWS Elemental Conductor File node is automatically configured to back up the database to a local disk. The following sections describe how to work with the backup.

###### Topics

- [View Folder for Database Backups](config-cond-cf-cg-bkup-view.md "config-cond-cf-cg-bkup-view.md")
- [Change Folder for Database Backups](config-cond-cf-cg-bkup-change.md "config-cond-cf-cg-bkup-change.md")
- [Restore a Database Backup](config-cond-cf-cg-bkup-restore.md "config-cond-cf-cg-bkup-restore.md")

This is version 2.20 of the AWS Elemental Statmux documentation.
This is the latest version. For prior versions, see the
_Previous Versions_ section of [AWS Elemental Statmux
and AWS Elemental Live Documentation](../../../elemental-live.md "../../../elemental-live.md").

# Configure Database Backups for AWS Elemental Statmux

During a database backup, AWS Elemental Statmux copies the data that's
related to your framework
(channels, profiles, nodes, MPTS outputs, and redundancy groups) from the Statmux node to
another server. You can use this backup to restore the data to the node in case of a major
hardware failure or if you have to re-install the software for any reason.

Backup files are named in this format:
`elemental-db-backup_`yyyy`-`mm`-
 `dd`_`hh`-`mm`-`ss`.tar.bz2`

AWS Elemental Statmux is configured by default to create database backups and store them on a
local disk. This section describes how to view the backup configuration and modify it for your
needs.

For steps to restore a database backup, see [Database Backups for AWS Elemental Statmux](config-wrkr-sm-cg-bkup-chg.md "config-wrkr-sm-cg-bkup-chg.md")

###### To view and change the backup configuration

1. On the AWS Elemental Statmux web interface, go to the **Settings** page and
   choose **General**.
2. In the **Cluster Tasks** section, the following fields configure the
   database backups:
   - **Minutes between management database backups** indicates how often
     AWS Elemental Statmux creates backups.
   - **Management database backups to keep** indicates how many backups
     Statmux keeps. When this number is reached, the oldest backup is removed so that
     the newest backup can be saved.
   - **Path to store management database backups** indicates where
     Statmux stores backups.

   The folder to receive backups must be the local disk or on a remote server that is mounted to the node. For assistance,
   see [Add Mount Points to AWS Elemental Statmux Nodes](config-wrkr-cf-cg-mount.md "config-wrkr-cf-cg-mount.md").

3. Change any of these values as you need and choose **Save**.

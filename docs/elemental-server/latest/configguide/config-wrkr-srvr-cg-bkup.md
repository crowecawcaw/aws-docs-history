This is version 2.18 of the AWS Elemental Server documentation.
This is the latest version. For prior versions, see
the _Previous Versions_ section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](../../../elemental-server.md "../../../elemental-server.md").

# Configure Database Backups for

AWS Elemental Server

During a database backup, AWS Elemental Server copies the data that's
related to your framework
(channels, profiles, nodes, MPTS outputs, and redundancy groups) from the AWS Elemental Server node to
another server. You can use this backup to restore the data to the node in case of a major
hardware failure or if you have to re-install the software for any reason.

Backup files are named in this format:
`elemental-db-backup_`yyyy`-`mm`-
 `dd`_`hh`-`mm`-`ss`.tar.bz2`

AWS Elemental Server is configured by default to create database backups and store them on a
local disk. This section describes how to view the backup configuration and modify it for your
needs.

For steps to restore a database backup, see [Database Backups for AWS Elemental Server](config-wrkr-srvr-cg-bkup-chg.md "config-wrkr-srvr-cg-bkup-chg.md")

###### To view and change the backup configuration

1. On the AWS Elemental Server web interface, go to the **Settings** page and
   choose **General**.
2. In the **Cluster Tasks** section, the following fields configure the
   database backups:
   - **Minutes between management database backups** indicates how often
     AWS Elemental Server creates backups.
   - **Management database backups to keep** indicates how many backups
     AWS Elemental Server keeps. When this number is reached, the oldest backup is removed so that
     the newest backup can be saved.
   - **Path to store management database backups** indicates where
     AWS Elemental Server stores backups.

   The folder to receive backups must be the local disk or on a remote server that is mounted to the node. For assistance,
   see [Add Mount Points to AWS Elemental ServerNodes](config-wrkr-cf-cg-mount.md "config-wrkr-cf-cg-mount.md").

3. Change any of these values as you need and choose **Save**.

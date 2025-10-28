# Configuring backup and

restore on Conductor Live

AWS Elemental Conductor Live is configured by default to create database backups to a directory on the node.
We recommend that you modify the configuration to back up to a remote server. This section
describes how to modify the configuration.

The Conductor Live backup command copies the following data to a backup server:
profiles, channels, MPTS outputs, nodes, and redundancy groups. Backup files
are named in the following format:

`elemental-db-backup_`yyyy`-`mm`-`dd`_`hh`-`mm`-`ss`.tar.bz2`

Backup when a Conductor Live node fails

If the primary Conductor Live fails, the other Conductor Live node (the new primary)
takes over backups. The new primary stores the backups in the same location
as the failed primary. You don't have to manage two backup files.

###### Topics

- [Configuring for
  backup](conductor-live-config-bkup.md "conductor-live-config-bkup.md")
- [Disabling database
  backups](conductor-live-config-bkup-dis.md "conductor-live-config-bkup-dis.md")
- [Restoring a backup](conductor-live-config-bkup-restore.md "conductor-live-config-bkup-restore.md")

# Backup window in Neptune

Automated backups occur daily during the preferred backup window. If the backup requires
more time than allotted to the backup window, the backup continues after the window ends,
until it finishes. The backup window can't overlap with the weekly maintenance window for the
DB instance.

During the automatic backup window, storage I/O might be suspended briefly while the
backup process initializes (typically under a few seconds). You might experience elevated
latencies for a few minutes during backups for Multi-AZ deployments.

The backup window is normally selected at random from an eight-hour block of time per
Region by the Amazon RDS control plane underlying Neptune. The time blocks for each
Region from which the default backups windows are assigned is documented in the [Backup
Window](../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow "../../../AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.md#USER_WorkingWithAutomatedBackups.BackupWindow") section of the Amazon RDS User Guide.

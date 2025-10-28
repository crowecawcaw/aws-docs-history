# Managing automated backups

This section shows how to manage automated backups for DB instances and Multi-AZ DB clusters.

###### Topics

- [Backup window](#USER_WorkingWithAutomatedBackups.BackupWindow "#USER_WorkingWithAutomatedBackups.BackupWindow")
- [Backup retention period](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md")
- [Enabling automated
  backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md")
- [Retaining automated backups](USER_WorkingWithAutomatedBackups.md "USER_WorkingWithAutomatedBackups.md")
- [Deleting retained automated backups](USER_WorkingWithAutomatedBackups-Deleting.md "USER_WorkingWithAutomatedBackups-Deleting.md")
- [Automated backups with unsupported MySQL storage engines](Overview.md "Overview.md")
- [Automated backups with unsupported MariaDB storage engines](Overview.md "Overview.md")
- [Replicating automated backups to another AWS Region](USER_ReplicateBackups.md "USER_ReplicateBackups.md")

## Backup window

Automated backups occur daily during the preferred backup window. If the backup
requires more time than allotted to the backup window, the backup continues after the
window ends until it finishes. The backup window can't overlap with the weekly
maintenance window for the DB instance or Multi-AZ DB cluster.

During the automatic backup window, storage I/O might be suspended briefly while the
backup process initializes (typically under a few seconds). You might experience
elevated latencies for a few minutes during backups for Multi-AZ deployments. For
MariaDB, MySQL, Oracle, and PostgreSQL, I/O activity isn't suspended on your primary
during backup for Multi-AZ deployments because the backup is taken from the standby. For
SQL Server, I/O activity is suspended briefly during backup for both Single-AZ and
Multi-AZ deployments because the backup is taken from the primary.

For Db2, I/O activity is also suspended briefly during backup even though the backup is
taken from the standby.

Automated backups might occasionally be skipped if the DB instance or cluster has a
heavy workload at the time a backup is supposed to start. If a backup is skipped, you
can still do a point-in-time-recovery (PITR), and a backup is still attempted during the
next backup window. For more information on PITR, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

If you don't specify a preferred backup window when you create the DB instance or
Multi-AZ DB cluster, Amazon RDS assigns a default 30-minute backup window. This window is
selected at random from an 8-hour block of time for each AWS Region. The following
table lists the time blocks for each AWS Region from which the default backup windows
are assigned.

| Region Name                | Region         | Time Block      |
| -------------------------- | -------------- | --------------- |
| US East (N. Virginia)      | us-east-1      | 03:00–11:00 UTC |
| US East (Ohio)             | us-east-2      | 03:00–11:00 UTC |
| US West (N. California)    | us-west-1      | 06:00–14:00 UTC |
| US West (Oregon)           | us-west-2      | 06:00–14:00 UTC |
| Africa (Cape Town)         | af-south-1     | 03:00–11:00 UTC |
| Asia Pacific (Hong Kong)   | ap-east-1      | 06:00–14:00 UTC |
| Asia Pacific (Hyderabad)   | ap-south-2     | 06:30–14:30 UTC |
| Asia Pacific (Jakarta)     | ap-southeast-3 | 08:00–16:00 UTC |
| Asia Pacific (Malaysia)    | ap-southeast-5 | 09:00–17:00 UTC |
| Asia Pacific (Melbourne)   | ap-southeast-4 | 11:00–19:00 UTC |
| Asia Pacific (Mumbai)      | ap-south-1     | 16:30–00:30 UTC |
| Asia Pacific (New Zealand) | ap-southeast-6 | 13:00–21:00 UTC |
| Asia Pacific (Osaka)       | ap-northeast-3 | 00:00–08:00 UTC |
| Asia Pacific (Seoul)       | ap-northeast-2 | 13:00–21:00 UTC |
| Asia Pacific (Singapore)   | ap-southeast-1 | 14:00–22:00 UTC |
| Asia Pacific (Sydney)      | ap-southeast-2 | 12:00–20:00 UTC |
| Asia Pacific (Taipei)      | ap-east-2      | 9:00–17:00 UTC  |
| Asia Pacific (Thailand)    | ap-southeast-7 | 8:00–16:00 UTC  |
| Asia Pacific (Tokyo)       | ap-northeast-1 | 13:00–21:00 UTC |
| Canada (Central)           | ca-central-1   | 03:00–11:00 UTC |
| Canada West (Calgary)      | ca-west-1      | 18:00–02:00 UTC |
| China (Beijing)            | cn-north-1     | 06:00–14:00 UTC |
| China (Ningxia)            | cn-northwest-1 | 06:00–14:00 UTC |
| Europe (Frankfurt)         | eu-central-1   | 20:00–04:00 UTC |
| Europe (Ireland)           | eu-west-1      | 22:00–06:00 UTC |
| Europe (London)            | eu-west-2      | 22:00–06:00 UTC |
| Europe (Milan)             | eu-south-1     | 02:00–10:00 UTC |
| Europe (Paris)             | eu-west-3      | 07:29–14:29 UTC |
| Europe (Spain)             | eu-south-2     | 02:00–10:00 UTC |
| Europe (Stockholm)         | eu-north-1     | 23:00–07:00 UTC |
| Europe (Zurich)            | eu-central-2   | 02:00–10:00 UTC |
| Israel (Tel Aviv)          | il-central-1   | 03:00–11:00 UTC |
| Mexico (Central)           | mx-central-1   | 19:00–03:00 UTC |
| Middle East (Bahrain)      | me-south-1     | 06:00–14:00 UTC |
| Middle East (UAE)          | me-central-1   | 05:00–13:00 UTC |
| South America (São Paulo)  | sa-east-1      | 23:00–07:00 UTC |
| AWS GovCloud (US-East)     | us-gov-east-1  | 17:00–01:00 UTC |
| AWS GovCloud (US-West)     | us-gov-west-1  | 06:00–14:00 UTC |

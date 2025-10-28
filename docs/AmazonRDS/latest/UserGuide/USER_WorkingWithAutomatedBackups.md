# Backup retention period

You can set the backup retention period when you create a DB instance or Multi-AZ DB cluster.
If you create a DB instance using the Amazon RDS API or the AWS CLI and if you don't set
the backup retention period, the default backup retention period is one day.
If you create a DB instance using the console, the default backup retention period is
seven days.

After you create a DB instance or cluster, you can modify the backup retention period.
You can set the backup retention period of a DB instance to between 0 and 35 days. Setting the backup
retention period to 0 disables automated backups. For a Multi-AZ DB cluster, you can set the backup retention period
to between 1 and 35 days. Manual snapshot limits (100 per
Region) don't apply to automated backups.

###### Important

An outage occurs if you change the backup retention period of a DB instance from 0 to a nonzero value or
from a nonzero value to 0.

RDS doesn't include time spent in the `stopped` state when the
backup retention period is calculated. Automated backups aren't created while a DB instance or cluster is stopped.
Backups can be retained longer than the backup retention period if a DB instance has been
stopped.

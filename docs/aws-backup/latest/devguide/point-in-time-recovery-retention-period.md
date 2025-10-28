# Changing your retention

period

You can use AWS Backup to increase or decrease the retention period for your existing
continuous backup rule. The minimum retention period is 1 day. The maximum retention period
is 35 days. The change in retention period will take effect when the next backup is completed
following this change.

## Retention period by service

The retention behavior can be specific to the resource type
that is backed up in the recovery point.

###### Amazon S3

When a retention period of an Amazon S3 continuous recovery point has changed (increased
or decreased), that recovery point status will become `STOPPED`. A new
continuous recovery point with the altered retention settings will be created.

###### Amazon Aurora and Amazon RDS

For recovery points of Aurora and Amazon RDS resources, only one recovery point is
possible at a time. No new recovery points are created when a retention period is
changed; instead, AWS Backup updates the existing recovery point with the retention
specifications within the backup plan.

Ensure that you set the retention period for these backups to be
greater than the backup frequency to avoid a scenario where the recovery point
transitions to `EXPIRED` state.

###### Tip

A backup frequency rule for a continuous backup is not the same as a
periodic backup snapshot. Each backup plan, even one that doesn't create a snapshot,
has a frequency you set (hourly, daily, weekly, or monthly as examples) for
maintenance and syncing purposes.

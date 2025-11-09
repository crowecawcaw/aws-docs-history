Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift snapshots and backups

Snapshots are point-in-time backups of a cluster. There are two types of snapshots:
_automated_ and _manual_. Amazon Redshift stores these
snapshots internally in Amazon S3 by using an encrypted Secure Sockets Layer (SSL) connection.

Amazon Redshift automatically takes incremental snapshots that track changes to the cluster since
the previous automated snapshot. Automated snapshots retain all of the data required to
restore a cluster from a snapshot. You can create a snapshot schedule to control when
automated snapshots are taken, or you can take a manual snapshot any time.

When you restore from a snapshot, Amazon Redshift creates a new cluster and makes the new cluster
available before all of the data is loaded, so you can begin querying the new cluster
immediately. The cluster streams data on demand from the snapshot in response to active
queries, then loads the remaining data in the background.

When you launch a cluster, you can set the retention period for automated and manual
snapshots. You can change the default retention period for automated and manual snapshots by
modifying the cluster. You can change the retention period for a manual snapshot when you
create the snapshot or by modifying the snapshot.

You can monitor the progress of snapshots by viewing the snapshot details in the AWS Management Console,
or by calling [describe-cluster-snapshots](../../../cli/latest/reference/redshift/describe-cluster-snapshots.md "../../../cli/latest/reference/redshift/describe-cluster-snapshots.md") in the CLI or the [DescribeClusterSnapshots](../APIReference/API_DescribeClusterSnapshots.md "../APIReference/API_DescribeClusterSnapshots.md") API action. For an in-progress snapshot, these display
information such as the size of the incremental snapshot, the transfer rate, the elapsed time,
and the estimated time remaining.

To ensure that your backups are always available to your cluster, Amazon Redshift stores snapshots in
an internally managed Amazon S3 bucket that is managed by Amazon Redshift. To manage storage charges,
evaluate how many days you need to keep automated snapshots and configure their retention
period accordingly. Delete any manual snapshots that you no longer need. For more information
about the cost of backup storage, see the [Amazon Redshift pricing](https://aws.amazon.com/redshift/pricing/ "https://aws.amazon.com/redshift/pricing/") page.

You can also create and restore snapshots using AWS Backup, a fully managed service that
helps you centralize and automate data protection across AWS services, in the cloud,
and on premises. For more information, see [AWS Backup integration with Amazon Redshift](managing-aws-backup.md "managing-aws-backup.md").
For information on AWS Backup, see
[What is AWS Backup?](../../../aws-backup/latest/devguide/whatisbackup.md "../../../aws-backup/latest/devguide/whatisbackup.md") in the _AWS Backup Developer Guide_.

## Working with snapshots and backups in

Amazon Redshift Serverless

Amazon Redshift Serverless, like a provisioned cluster, enables you to take a backup as a
point-in-time representation of the objects and data in the namespace. There are two types
of backups in Amazon Redshift Serverless: snapshots that are manually created and recovery points
that Amazon Redshift Serverless creates automatically. You can find more information about working
with snapshots for Amazon Redshift Serverless at [Snapshots and recovery
points](serverless-snapshots-recovery-points.md "serverless-snapshots-recovery-points.md").

You can also restore a snapshot from a provisioned cluster to a serverless namespace.
For more information, see [Restoring a serverless namespace from a snapshot](serverless-snapshot-restore.md "serverless-snapshot-restore.md").

## Automated snapshots

When automated snapshots are enabled for a cluster, Amazon Redshift periodically takes
snapshots of that cluster. By default Amazon Redshift takes a snapshot about every eight
hours or following every 5 GB per node of data changes, or whichever comes first. If your
data is larger than 5 GB \* the number of nodes, the shortest amount of time in between
automated snapshot creation is 15 minutes. Alternatively, you can create a snapshot
schedule to control when automated snapshots are taken. If you're using custom
schedules, the minimum amount of time between automated snapshots is one hour. Automated
snapshots are enabled by default when you create a cluster.

Automated snapshots are deleted at the end of a retention period. The default retention
period is one day, but you can modify it by using the Amazon Redshift console or programmatically
by using the Amazon Redshift API or CLI.

To disable automated snapshots, set the retention period to zero. If you disable
automated snapshots, Amazon Redshift stops taking snapshots and deletes any existing automated
snapshots for the cluster. You can't disable automated
snapshots for RA3 node types. You can set an RA3 node type automated retention period from
1–35 days.

Only Amazon Redshift can delete an automated snapshot; you cannot delete them manually.
Amazon Redshift deletes automated snapshots at the end of a snapshot's retention period, when
you disable automated snapshots for the cluster, or when you delete the cluster. Amazon Redshift retains the latest automated snapshot until you disable automated
snapshots or delete the cluster.

If you want to keep an automated snapshot for a longer period, you can create a copy of
it as a manual snapshot. The automated snapshot is retained until the end of the retention
period, but the corresponding manual snapshot is retained until you manually delete it or
until the end of the retention period.

## Automated snapshot schedules

To precisely control when snapshots are taken, you can create a snapshot schedule and
attach it to one or more clusters. When you modify a snapshot schedule, the schedule is
modified for all associated clusters. If a cluster doesn't have a snapshot schedule
attached, the cluster uses the default automated snapshot schedule.

A _snapshot schedule_ is a set of schedule rules. You can define a
simple schedule rule based on a specified interval, such as every 8 hours or every 12
hours. You can also add rules to take snapshots on certain days of the week, at specific
times, or during specific periods. Rules can also be defined using Unix-like cron
expressions.

## Snapshot schedule format

On the Amazon Redshift console, you can create a snapshot schedule. Then, you can attach a schedule
to a cluster to trigger the creation of a system snapshot. A schedule can be attached to
multiple clusters, and you can create multiple cron definitions in a schedule to trigger a
snapshot.

You can define a schedule for your snapshots using a cron syntax. The definition of
these schedules uses a modified Unix-like
[cron](http://en.wikipedia.org/wiki/Cron "http://en.wikipedia.org/wiki/Cron") syntax. You specify time in
[Coordinated
universal time (UTC)](http://en.wikipedia.org/wiki/Coordinated_Universal_Time "http://en.wikipedia.org/wiki/Coordinated_Universal_Time"). You can create schedules with a maximum frequency of one
hour and minimum precision of one minute.

Amazon Redshift modified cron expressions have 3 required fields, which are separated by white
space.

**Syntax**

```
cron(`Minutes` `Hours` `Day-of-month` `Month` `Day-of-week` `Year`)
```

| **Fields**   | **Values**      | **Wildcards**         |
| ------------ | --------------- | --------------------- |
| Minutes      | 0–59            | ,<br>• \<br>• /       |
| Hours        | 0–23            | ,<br>• \<br>• /       |
| Day-of-month | 1–31            | ,<br>• \<br>• ? / L W |
| Month        | 1–12 or JAN-DEC | ,<br>• \<br>• /       |
| Day-of-week  | 1–7 or SUN-SAT  | ,<br>• \<br>• ? L #   |
| Year         | 1970–2199       | ,<br>• \<br>• /       |

###### Wildcards

- The **,** (comma) wildcard includes additional values. In the
  `Day-of-week` field, `MON,WED,FRI` would include Monday,
  Wednesday, and Friday. Total values are limited to 24 per field.
- The **-** (dash) wildcard specifies ranges. In the
  `Hour` field, 1–15 would include hours 1 through 15 of the
  specified day.
- The **\*** (asterisk) wildcard includes all values in the field.
  In the `Hours` field, **\*** would include every
  hour.
- The **/** (forward slash) wildcard specifies increments. In the
  `Hours` field, you could enter `1/10` to specify
  every 10th hour, starting from the first hour of the day (for example, the 01:00,
  11:00, and 21:00).
- The **?** (question mark) wildcard specifies one or another. In
  the `Day-of-month` field you could enter **7**, and if
  you didn't care what day of the week the seventh was, you could enter
  **?** in the Day-of-week field.
- The **L** wildcard in the `Day-of-month` or
  `Day-of-week` fields specifies the last day of the month or
  week.
- The **W** wildcard in the `Day-of-month` field
  specifies a weekday. In the `Day-of-month` field, `3W`
  specifies the day closest to the third weekday of the month.
- The **#** wildcard in the Day-of-week field specifies a certain
  instance of the specified day of the week within a month. For example, 3#2 would be
  the second Tuesday of the month: the 3 refers to Tuesday because it is the third day
  of each week, and the 2 refers to the second day of that type within the
  month.

###### Note

If you use a '#' character, you can define only one expression in the
day-of-week field. For example, "3#1,6#3" is not valid because it is interpreted
as two expressions.

###### Limits

- You can't specify the `Day-of-month` and `Day-of-week`
  fields in the same cron expression. If you specify a value in one of the fields, you
  must use a **?** (question mark) in the other.
- Snapshot schedules don't support the following frequencies:

      + Snapshots scheduled more frequently than 1 per hour.
      + Snapshots scheduled less frequently than 1 per day (24 hours).

  If you have overlapping schedules that result in scheduling snapshots within a 1
  hour window, a validation error results.

When creating a schedule, you can use the following sample cron strings.

| Minutes | Hours   | Day of week | Meaning                                                                                                                                                                              |
| ------- | ------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0       | 14-20/1 | TUE         | Every hour between 2pm and 8pm on Tuesday.                                                                                                                                           |
| 0       | 21      | MON-FRI     | Every night at 9pm Monday–Friday.                                                                                                                                                    |
| 30      | 0/6     | SAT-SUN     | Every 6 hour increment on Saturday and Sunday starting at 30 minutes<br>after midnight (00:30) that day. This results in a snapshot at [00:30,<br>06:30, 12:30, and 18:30] each day. |
| 30      | 12/4    | \*          | Every 4 hour increment starting at 12:30 each day. This resolves to<br>[12:30, 16:30, 20:30].                                                                                        |

For example to run on a schedule on an every 2 hour increment starting at 15:15 each
day. This resolves to [15:15, 17:15, 19:15, 21:15, 23:15] , specify:

```

cron(15 15/2 *)

```

You can create multiple cron schedule definitions within as schedule. For example the
following AWS CLI command contains two cron schedules in one schedule.

```

create-snapshot-schedule --schedule-identifier "my-test" --schedule-definition "cron(0 17 SAT,SUN)" "cron(0 9,17 MON-FRI)"

```

## Manual snapshots

You can take a manual snapshot any time. By default, manual snapshots are retained
indefinitely, even after you delete your cluster. You can specify the retention period when
you create a manual snapshot, or you can change the retention period by modifying the
snapshot. For more information about changing the retention period, see [Modifying the manual snapshot retention
period](snapshot-manual-retention-period.md "snapshot-manual-retention-period.md").

If a snapshot is deleted, you can't start any new operations that reference that
snapshot. However, if a restore operation is in progress, that restore operation will run
to completion.

Amazon Redshift has a quota that limits the total number of manual snapshots that you can
create; this quota is per AWS account per AWS Region. The default quota is listed at
[Quotas and limits in Amazon Redshift](amazon-redshift-limits.md "amazon-redshift-limits.md").

## Snapshot storage

Because snapshots accrue storage charges, it's important that you delete them when
you no longer need them. Amazon Redshift deletes automated and manual snapshots at the end of their
respective snapshot retention periods. You can also delete manual snapshots using the
AWS Management Console or with the [batch-delete-cluster-snapshots](../../../cli/latest/reference/redshift/batch-delete-cluster-snapshots.md "../../../cli/latest/reference/redshift/batch-delete-cluster-snapshots.md") CLI command.

You can change the retention period for a manual snapshot by modifying the manual
snapshot settings.

You can get information about how much storage your snapshots are consuming using the
Amazon Redshift Console or using the [describe-storage](../../../cli/latest/reference/redshift/describe-storage.md "../../../cli/latest/reference/redshift/describe-storage.md") CLI command.

## Excluding tables from snapshots

By default, all user-defined permanent tables are included in snapshots. If a table,
such as a staging table, doesn't need to be backed up, you can significantly reduce
the time needed to create snapshots and restore from snapshots. You also reduce storage
space on Amazon S3 by using a no-backup table. To create a no-backup table, include the
BACKUP NO parameter when you create the table. For more information, see [CREATE TABLE](../dg/r_CREATE_TABLE_NEW.md "../dg/r_CREATE_TABLE_NEW.md") and [CREATE TABLE AS](../dg/r_CREATE_TABLE_AS.md "../dg/r_CREATE_TABLE_AS.md") in the
_Amazon Redshift Database Developer Guide_.

###### Note

No-backup tables aren't supported for RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot. To avoid snapshot costs for no-backup tables,
truncate them before taking a snapshot.

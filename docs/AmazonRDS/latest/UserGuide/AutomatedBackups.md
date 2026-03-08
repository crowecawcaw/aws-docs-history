# Restoring to a specified time from a replicated backup for Amazon RDS

You can restore a DB instance to a specific point in time from a replicated backup using the Amazon RDS console. You can also use
the `restore-db-instance-to-point-in-time` AWS CLI command or the `RestoreDBInstanceToPointInTime` RDS API
operation.

For general information on point-in-time recovery (PITR), see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

###### Note

Note the following DB engine restrictions when automated backups are replicated across
AWS Regions:

- On RDS for SQL Server, option groups aren't copied.
- On RDS for Oracle, the following options aren't copied:
  `NATIVE_NETWORK_ENCRYPTION`, `OEM`,
  `OEM_AGENT`, and `SSL`.
  If you've associated a custom option group with your DB instance, you can
  re-create that option group in the destination Region. Then restore the DB instance
  in the destination Region and associate the custom option group with it. For more
  information, see [Working with option groups](USER_WorkingWithOptionGroups.md "USER_WorkingWithOptionGroups.md").

###### To restore a DB instance to a specified time from a replicated backup

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose the destination Region (where backups are replicated to) from the Region selector.
3. In the navigation pane, choose **Automated backups**.
4. On the **Replicated backups** tab, choose the DB instance that you want to restore.
5. For **Actions**, choose **Restore to point in time**.
6. Choose **Latest restorable time** to restore to the latest possible time, or choose
   **Custom** to choose a time.

If you chose **Custom**, enter the date and time that you want to restore the instance to.

###### Note

Times are shown in your local time zone, which is indicated by an offset from Coordinated Universal Time
(UTC). For example, UTC-5 is Eastern Standard Time/Central Daylight Time. 7. For **DB instance identifier**, enter the name of the target restored DB instance. 8. (Optional) Choose other options as needed, such as enabling autoscaling. 9. Choose **Restore to point in time**.
Use the [`restore-db-instance-to-point-in-time`](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") AWS CLI command
to create a new DB instance.

###### To restore a DB instance to a specified time from a replicated backup

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-to-point-in-time \
    --source-db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:`ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`" \
    --target-db-instance-identifier `mytargetdbinstance` \
    --restore-time `2020-10-14T23:45:00.000Z`
```

For Windows:

```
aws rds restore-db-instance-to-point-in-time ^
    --source-db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:`ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE`" ^
    --target-db-instance-identifier `mytargetdbinstance` ^
    --restore-time `2020-10-14T23:45:00.000Z`
```

To restore a DB instance to a specified time, call the
[`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md")
Amazon RDS API operation with the following parameters:

- `SourceDBInstanceAutomatedBackupsArn`
- `TargetDBInstanceIdentifier`
- `RestoreTime`

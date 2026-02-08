# Deleting replicated backups for Amazon RDS

You can delete replicated backups for DB instances using the Amazon RDS console. You can also use the `delete-db-instance-automated-backups` AWS CLI
command or the `DeleteDBInstanceAutomatedBackup` RDS API operation.

Delete replicated backups in the destination Region from the
**Automated backups** page.

###### To delete replicated backups

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose the destination Region from the **Region selector**.
3. In the navigation pane, choose **Automated backups**.
4. On the **Replicated backups** tab, choose the DB instance for which you want to delete the
   replicated backups.
5. For **Actions**, choose **Delete**.
6. On the confirmation page, enter `delete me` and choose
   **Delete**.
   Delete replicated backups by using the [`delete-db-instance-automated-backup`](../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md "../../../cli/latest/reference/rds/delete-db-instance-automated-backup.md") AWS CLI command.

You can use the [`describe-db-instances`](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")
CLI command to find the Amazon Resource Names (ARNs) of the replicated backups. For more information, see [Finding information about replicated backups for Amazon RDS](AutomatedBackups.Replicating.md "AutomatedBackups.Replicating.md").

###### To delete replicated backups

- Run one of the following commands.

For Linux, macOS, or Unix:

```
aws rds delete-db-instance-automated-backup \
--db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE"
```

For Windows:

```
aws rds delete-db-instance-automated-backup ^
--db-instance-automated-backups-arn "arn:aws:rds:us-east-1:`123456789012`:auto-backup:ab-L2IJCEXJP7XQ7HOJ4SIEXAMPLE"
```

Delete replicated backups by using the [`DeleteDBInstanceAutomatedBackup`](../APIReference/API_DeleteDBInstanceAutomatedBackup.md "../APIReference/API_DeleteDBInstanceAutomatedBackup.md") RDS API operation with the
`DBInstanceAutomatedBackupsArn` parameter.

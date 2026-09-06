

# Copying continuous backups
<a name="point-in-time-recovery-copying"></a>

If a continuous backup rule also specifies a cross-account or cross-Region copy and AWS Backup supports the operation for the resource type, AWS Backup takes a snapshot of the resource and copies the snapshot to the destination vault. To learn more about copying your recovery points across accounts and Regions, see [Copying a backup ](https://docs.aws.amazon.com/aws-backup/latest/devguide/recov-point-create-a-copy.html).

Continuous backups create a periodic backups in accordance with the frequency set in the backup plan rule in the destination account and/or Region.

AWS Backup does not support on-demand copies of continuous backups.

**Note**  
For database resources, ensure that your IAM role has the `rds:DeleteDBSnapshot` permission. AWS Backup temporarily creates a source snapshot during a point-in-time recovery (PITR) copy. After the copy completes, the service removes the snapshot. If the role lacks this permission, AWS Backup cannot remove the temporary snapshot. Instead, it creates an expired recovery point to prevent a snapshot leak. You must manually delete any expired recovery points that result from insufficient permissions.
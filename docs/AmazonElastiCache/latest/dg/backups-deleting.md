# Deleting a backup

An automatic backup is automatically deleted when its retention limit expires. If
you delete a cluster, all of its automatic backups are also deleted. If you delete a
replication group, all of the automatic backups from the clusters in that group are also
deleted.

ElastiCache provides a deletion API operation that lets you delete a backup at any time,
regardless of whether the backup was created automatically or manually. Because manual
backups don't have a retention limit, manual deletion is the only way to remove them.

You can delete a backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.

The following procedure deletes a backup using the ElastiCache console.

###### To delete a backup

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. In the navigation pane, choose **Backups**.

The Backups screen appears with a list of your backups. 3. Choose the box to the left of the name of the backup you want to
delete. 4. Choose **Delete**. 5. If you want to delete this backup, choose **Delete** on the
**Delete Backup** confirmation screen.
The status changes to _deleting_.
Use the delete-snapshot AWS CLI operation with the following parameter to delete a serverless backup.

- `--serverless-cache-snapshot-name` – Name of the backup to be deleted.
  The following code deletes the backup `myBackup`.

```
aws elasticache delete-serverless-cache-snapshot --serverless-cache-snapshot-name `myBackup`
```

For more information, see [delete-serverless-cache-snapshot](../../../cli/latest/reference/elasticache/delete-serverless-cache-snapshot.md "../../../cli/latest/reference/elasticache/delete-serverless-cache-snapshot.md") in the _AWS CLI Command Reference_.

Use the delete-snapshot AWS CLI operation with the following parameter to delete a node-based cluster backup.

- `--snapshot-name` – Name of the backup to be deleted.
  The following code deletes the backup `myBackup`.

```
aws elasticache delete-snapshot --snapshot-name `myBackup`
```

For more information, see [delete-snapshot](../../../cli/latest/reference/elasticache/delete-snapshot.md "../../../cli/latest/reference/elasticache/delete-snapshot.md") in the _AWS CLI Command Reference_.

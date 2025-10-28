# Copying backups

You can create a copy of any backup, whether it was created automatically or manually.

You can also export your backup so you can access it from outside ElastiCache.
For guidance on exporting your backup, see [Exporting a backup](backups-exporting.md "backups-exporting.md").

The following steps show you how to copy a backup.

###### To copy a backup (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. To see a list of your backups,
   from the left navigation pane choose **Backups**.
3. From the list of backups, choose the box to the left of the name of the backup you want to copy.
4. Choose **Actions** then **Copy**.
5. In the **New backup name** box, type a name for your new backup.
6. Choose **Copy**.
   To copy a backup of a serverless cache, use the `copy-serverless-cache-snapshot` operation.

###### Parameters

- `--source-serverless-cache-snapshot-name` –
  Name of the backup to be copied.
- `--target-serverless-cache-snapshot-name` –
  Name of the backup's copy.
  The following example makes a copy of an automatic backup.

For Linux, macOS, or Unix:

```
aws elasticache copy-serverless-cache-snapshot \
    --source-serverless-cache-snapshot-name `automatic.my-cache-2023-11-27-03-15` \
    --target-serverless-cache-snapshot-name `my-backup-copy`
```

For Windows:

```
aws elasticache copy-serverless-cache-snapshot ^
    --source-serverless-cache-snapshot-name `automatic.my-cache-2023-11-27-03-15` ^
    --target-serverless-cache-snapshot-name `my-backup-copy`
```

For more information, see [`copy-serverless-cache-snapshot`](../../../cli/latest/reference/elasticache/copy-serverless-cache-snapshot.md "../../../cli/latest/reference/elasticache/copy-serverless-cache-snapshot.md") in the _AWS CLI_.

To copy a backup of a node-based cluster, use the `copy-snapshot` operation.

###### Parameters

- `--source-snapshot-name` –
  Name of the backup to be copied.
- `--target-snapshot-name` –
  Name of the backup's copy.
- `--target-bucket` –
  Reserved for exporting a backup. Do not use this parameter when making a copy of a backup.

For more information, see [Exporting a backup](backups-exporting.md "backups-exporting.md").
The following example makes a copy of an automatic backup.

For Linux, macOS, or Unix:

```
aws elasticache copy-snapshot  \
    --source-snapshot-name `automatic.my-redis-primary-2014-03-27-03-15` \
    --target-snapshot-name `amzn-s3-demo-bucket`
```

For Windows:

```
aws elasticache copy-snapshot ^
    --source-snapshot-name `automatic.my-redis-primary-2014-03-27-03-15` ^
    --target-snapshot-name `amzn-s3-demo-bucket`
```

For more information, see [`copy-snapshot`](../../../cli/latest/reference/elasticache/copy-snapshot.md "../../../cli/latest/reference/elasticache/copy-snapshot.md") in the _AWS CLI_.

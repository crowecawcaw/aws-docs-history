# Restoring from a backup into a new cache

You can restore an existing backup from Valkey into a new Valkey cache or node-based cluster, and
restore an existing Redis OSS backup into a new Redis OSS cache or node-based cluster.
You can also restore an existing Memcached serverless cache backup into a new Memcached serverless cache.

###### Note

ElastiCache Serverless supports RDB files compatible with Valkey 7.2 and above, and Redis OSS versions between 5.0 and the latest version available.

###### To restore a backup to a serverless cache (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Backups**.
3. In the list of backups, choose the box to the left of the backup name that you want to restore.
4. Choose **Actions** and then **Restore**.
5. Enter a name for the new serverless cache, and an optional description.
6. Click **Create** to create your new cache and import data from your backup.

###### To restore a backup to a node-based cluster (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. From the navigation pane, choose **Backups**.
3. In the list of backups, choose the box to the left of the backup name you want to restore from.
4. Choose **Actions** and then **Restore**.
5. Choose **Node-based cache** and customize the cluster settings, such as node type, sizes, number of shards, replicas, AZ placement, and security settings.
6. Choose **Create** to create your new node-based cluster and import data from your backup.

###### Note

ElastiCache Serverless supports RDB files compatible with Valkey 7.2 and above, and Redis OSS versions between 5.0 and the latest version available.

**To restore a backup to a new serverless cache (AWS CLI)**

The following AWS CLI example creates a new cache using `create-serverless-cache` and imports data from a backup.

For Linux, macOS, or Unix:

```
aws elasticache create-serverless-cache \

    --serverless-cache-name CacheName \
    --engine redis
    --snapshot-arns-to-restore Snapshot-ARN
```

For Windows:

```
aws elasticache create-serverless-cache ^

    --serverless-cache-name CacheName ^
    --engine redis ^
    --snapshot-arns-to-restore Snapshot-ARN
```

**To restore a backup to a node-based cluster (AWS CLI)**

You can restore a backup to a node-based cluster using the `create-replication-group` operation with the
`--snapshot-name` parameter (for an ElastiCache backup) or the `--snapshot-arns` parameter (for an RDB file stored in Amazon S3).

The following example restores from an ElastiCache backup:

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
    --replication-group-id `my-cluster` \
    --replication-group-description "`Restore from backup`" \
    --snapshot-name `my-backup`
```

For Windows:

```
aws elasticache create-replication-group ^
    --replication-group-id `my-cluster` ^
    --replication-group-description "`Restore from backup`" ^
    --snapshot-name `my-backup`
```

The following example restores from an RDB file stored in Amazon S3:

For Linux, macOS, or Unix:

```
aws elasticache create-replication-group \
    --replication-group-id `my-cluster` \
    --replication-group-description "`Restore from S3`" \
    --snapshot-arns `arn:aws:s3:::my-bucket/my-backup.rdb`
```

For Windows:

```
aws elasticache create-replication-group ^
    --replication-group-id `my-cluster` ^
    --replication-group-description "`Restore from S3`" ^
    --snapshot-arns `arn:aws:s3:::my-bucket/my-backup.rdb`
```

For more information on seeding a new node-based cluster from a backup, see
[Tutorial: Seeding a new node-based cluster with an externally created backup](backups-seeding-redis.md "backups-seeding-redis.md").

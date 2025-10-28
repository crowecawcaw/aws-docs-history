# Creating a final backup

You can create a final backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.

You can create a final backup when you delete a Valkey, Memcached, or Redis OSS serverless cache, or a Valkey or Redis OSS node-based cluster, by using the ElastiCache console.

To create a final backup when deleting a cache, on the delete dialog box
choose **Yes** under **Create backup** and give the backup a name.

###### Related topics

- [Using the AWS Management Console](Clusters.md#Clusters.Delete.CON "Clusters.md#Clusters.Delete.CON")
- [Deleting a Replication Group (Console)](Replication.md#Replication.DeletingRepGroup.CON "Replication.md#Replication.DeletingRepGroup.CON")
  You can create a final backup when deleting a cache using the AWS CLI.

###### Topics

- [When deleting a Valkey cache, Memcached serverless cache, or Redis OSS cache](#w30aac24b7c29b7b1b7 "#w30aac24b7c29b7b1b7")
- [When deleting a Valkey or Redis OSS cluster with no read replicas](#w30aac24b7c29b7b1b9 "#w30aac24b7c29b7b1b9")
- [When deleting a Valkey or Redis OSS cluster with read replicas](#w30aac24b7c29b7b1c11 "#w30aac24b7c29b7b1c11")

### When deleting a Valkey cache, Memcached serverless cache, or Redis OSS cache

To create a final backup, use the `delete-serverless-cache` AWS CLI operation with
the following parameters.

- `--serverless-cache-name` – Name of the cache being deleted.
- `--final-snapshot-name` – Name of the backup.

The following code creates the final backup `bkup-20231127-final` when deleting the
cache `myserverlesscache`.

For Linux, macOS, or Unix:

```
aws elasticache delete-serverless-cache \
        --serverless-cache-name `myserverlesscache` \
        --final-snapshot-name `bkup-20231127-final`
```

For Windows:

```
aws elasticache delete-serverless-cache ^
        --serverless-cache-name `myserverlesscache` ^
        --final-snapshot-name `bkup-20231127-final`
```

For more information, see [delete-serverless-cache](../../../cli/latest/reference/elasticache/delete-serverless-cache.md "../../../cli/latest/reference/elasticache/delete-serverless-cache.md") in the _AWS CLI Command Reference_.

### When deleting a Valkey or Redis OSS cluster with no read replicas

To create a final backup for a node-based cluster with no read replicas, use the `delete-cache-cluster` AWS CLI operation with
the following parameters.

- `--cache-cluster-id` – Name of the cluster being deleted.
- `--final-snapshot-identifier` – Name of the backup.

The following code creates the final backup `bkup-20150515-final` when deleting the
cluster `myRedisCluster`.

For Linux, macOS, or Unix:

```
aws elasticache delete-cache-cluster \
        --cache-cluster-id `myRedisCluster` \
        --final-snapshot-identifier `bkup-20150515-final`
```

For Windows:

```
aws elasticache delete-cache-cluster ^
        --cache-cluster-id `myRedisCluster` ^
        --final-snapshot-identifier `bkup-20150515-final`
```

For more information, see [delete-cache-cluster](../../../cli/latest/reference/elasticache/delete-cache-cluster.md "../../../cli/latest/reference/elasticache/delete-cache-cluster.md") in the _AWS CLI Command Reference_.

### When deleting a Valkey or Redis OSS cluster with read replicas

To create a final backup when deleting a replication group, use the
`delete-replication-group` AWS CLI operation, with the following
parameters:

- `--replication-group-id` – Name of the replication group being deleted.
- `--final-snapshot-identifier` – Name of the final backup.

The following code takes the final backup `bkup-20150515-final` when deleting the
replication group `myReplGroup`.

For Linux, macOS, or Unix:

```
aws elasticache delete-replication-group \
        --replication-group-id `myReplGroup` \
        --final-snapshot-identifier `bkup-20150515-final`
```

For Windows:

```
aws elasticache delete-replication-group ^
        --replication-group-id `myReplGroup` ^
        --final-snapshot-identifier `bkup-20150515-final`
```

For more information, see [delete-replication-group](../../../cli/latest/reference/elasticache/delete-replication-group.md "../../../cli/latest/reference/elasticache/delete-replication-group.md") in the _AWS CLI Command Reference_.

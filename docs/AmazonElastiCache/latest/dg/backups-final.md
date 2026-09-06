

# Creating a final backup
<a name="backups-final"></a>

You can create a final backup using the ElastiCache console, the AWS CLI, or the ElastiCache API.

## Creating a final backup (Console)
<a name="backups-final-CON"></a>

You can create a final backup when you delete a Valkey, Memcached, or Redis OSS serverless cache, or a Valkey or Redis OSS node-based cluster, by using the ElastiCache console.

To create a final backup when deleting a cache, on the delete dialog box choose **Yes** under **Create backup** and give the backup a name.

**Related topics**
+ [Using the AWS Management Console](Clusters.Delete.md#Clusters.Delete.CON)
+ [Deleting a Replication Group (Console)](Replication.DeletingRepGroup.md#Replication.DeletingRepGroup.CON)

## Creating a final backup (AWS CLI)
<a name="backups-final-CLI"></a>

You can create a final backup when deleting a cache using the AWS CLI.

**Topics**
+ [When deleting a Valkey cache, Memcached serverless cache, or Redis OSS cache](#w2aac27b7c29b7b1b7)
+ [When deleting a Valkey or Redis OSS cluster with no read replicas](#w2aac27b7c29b7b1b9)
+ [When deleting a Valkey or Redis OSS cluster with read replicas](#w2aac27b7c29b7b1c11)

### When deleting a Valkey cache, Memcached serverless cache, or Redis OSS cache
<a name="w2aac27b7c29b7b1b7"></a>

To create a final backup, use the `delete-serverless-cache` AWS CLI operation with the following parameters.
+ `--serverless-cache-name` – Name of the cache being deleted.
+ `--final-snapshot-name` – Name of the backup.

The following code creates the final backup `bkup-20231127-final` when deleting the cache `myserverlesscache`.

For Linux, macOS, or Unix:

```
aws elasticache delete-serverless-cache \
        --serverless-cache-name {{myserverlesscache}} \
        --final-snapshot-name {{bkup-20231127-final}}
```

For Windows:

```
aws elasticache delete-serverless-cache ^
        --serverless-cache-name {{myserverlesscache}} ^
        --final-snapshot-name {{bkup-20231127-final}}
```

For more information, see [delete-serverless-cache](https://docs.aws.amazon.com/cli/latest/reference/elasticache/delete-serverless-cache.html) in the *AWS CLI Command Reference*.

### When deleting a Valkey or Redis OSS cluster with no read replicas
<a name="w2aac27b7c29b7b1b9"></a>

To create a final backup for a node-based cluster with no read replicas, use the `delete-cache-cluster` AWS CLI operation with the following parameters.
+ `--cache-cluster-id` – Name of the cluster being deleted.
+ `--final-snapshot-identifier` – Name of the backup.

The following code creates the final backup `bkup-20150515-final` when deleting the cluster `myRedisCluster`.

For Linux, macOS, or Unix:

```
aws elasticache delete-cache-cluster \
        --cache-cluster-id {{myRedisCluster}} \
        --final-snapshot-identifier {{bkup-20150515-final}}
```

For Windows:

```
aws elasticache delete-cache-cluster ^
        --cache-cluster-id {{myRedisCluster}} ^
        --final-snapshot-identifier {{bkup-20150515-final}}
```

For more information, see [delete-cache-cluster](https://docs.aws.amazon.com/cli/latest/reference/elasticache/delete-cache-cluster.html) in the *AWS CLI Command Reference*.

### When deleting a Valkey or Redis OSS cluster with read replicas
<a name="w2aac27b7c29b7b1c11"></a>

To create a final backup when deleting a replication group, use the `delete-replication-group` AWS CLI operation, with the following parameters:
+ `--replication-group-id` – Name of the replication group being deleted.
+ `--final-snapshot-identifier` – Name of the final backup.

The following code takes the final backup `bkup-20150515-final` when deleting the replication group `myReplGroup`.

For Linux, macOS, or Unix:

```
aws elasticache delete-replication-group \
        --replication-group-id {{myReplGroup}} \
        --final-snapshot-identifier {{bkup-20150515-final}}
```

For Windows:

```
aws elasticache delete-replication-group ^
        --replication-group-id {{myReplGroup}} ^
        --final-snapshot-identifier {{bkup-20150515-final}}
```

For more information, see [delete-replication-group](https://docs.aws.amazon.com/cli/latest/reference/elasticache/delete-replication-group.html) in the *AWS CLI Command Reference*.
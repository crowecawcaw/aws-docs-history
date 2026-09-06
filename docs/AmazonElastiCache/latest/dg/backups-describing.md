

# Describing backups
<a name="backups-describing"></a>

The following procedures show you how to display a list of your backups. If you desire, you can also view the details of a particular backup.

## Describing backups (Console)
<a name="backups-describing-CON"></a>

**To display backups using the AWS Management Console**

1. Sign in to the AWS Management Console and open the ElastiCache console at [ https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/).

1. From the navigation pane, choose **Backups**.

1. To see the details of a particular backup, choose the box to the left of the backup's name.

## Describing serverless backups (AWS CLI)
<a name="backups-describing-serverless-CLI"></a>

To display a list of serverless backups and optionally details about a specific backup, use the `describe-serverless-cache-snapshots` CLI operation. 

**Examples**

The following operation uses the parameter `--max-records` to list up to 20 backups associated with your account. Omitting the parameter `--max-records` lists up to 50 backups.

```
aws elasticache describe-serverless-cache-snapshots --max-records {{20}}
```

The following operation uses the parameter `--serverless-cache-name` to list only the backups associated with the cache `my-cache`.

```
aws elasticache describe-serverless-cache-snapshots --serverless-cache-name {{my-cache}}
```

The following operation uses the parameter `--serverless-cache-snapshot-name` to display the details of the backup `my-backup`.

```
aws elasticache describe-serverless-cache-snapshots --serverless-cache-snapshot-name {{my-backup}}
```

For more information, see [describe-serverless-cache-snapshots](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-serverless-cache-snapshots.html) in the AWS CLI Command Reference.

## Describing node-based cluster backups (AWS CLI)
<a name="backups-describing-CLI"></a>

To display a list of node-based cluster backups and optionally details about a specific backup, use the `describe-snapshots` CLI operation. 

**Examples**

The following operation uses the parameter `--max-records` to list up to 20 backups associated with your account. Omitting the parameter `--max-records` lists up to 50 backups.

```
aws elasticache describe-snapshots --max-records {{20}}
```

The following operation uses the parameter `--cache-cluster-id` to list only the backups associated with the cluster `my-cluster`.

```
aws elasticache describe-snapshots --cache-cluster-id {{my-cluster}}
```

The following operation uses the parameter `--snapshot-name` to display the details of the backup `my-backup`.

```
aws elasticache describe-snapshots --snapshot-name {{my-backup}}
```

For more information, see [describe-snapshots](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-snapshots.html) in the AWS CLI Command Reference.
# Promoting a read replica to primary, for Valkey or Redis OSS (cluster mode disabled) replication groups

Information in the following topic applies to
only Valkey or Redis OSS (cluster mode disabled) replication groups.

You can promote a Valkey or Redis OSS (cluster mode disabled) read replica to primary using the AWS Management Console, the AWS CLI,
or the ElastiCache API. You can't promote a read replica to primary while Multi-AZ with
Automatic Failover is enabled on the replication group. To promote a
Valkey or Redis OSS (cluster mode disabled) replica to primary on a Multi-AZ enabled replication group, do the
following:

1. Modify the replication group to disable Multi-AZ (doing this doesn't require
   that all your clusters be in the same Availability Zone). For more information, see
   [Modifying a replication group](Replication.md "Replication.md").
2. Promote the read replica to primary.
3. Modify the replication group to re-enable Multi-AZ.
   Multi-AZ is not available on replication groups running Redis OSS 2.6.13 or earlier.

## Using the AWS Management Console

The following procedure uses the console to promote a replica node to primary.

###### To promote a read replica to primary (console)

1. Sign in to the AWS Management Console and open the ElastiCache console at
   [https://console.aws.amazon.com/elasticache/](https://console.aws.amazon.com/elasticache/ "https://console.aws.amazon.com/elasticache/").
2. If the replica you want to promote is a member of a Valkey or Redis OSS (cluster mode disabled) replication
   group where Multi-AZ is enabled, modify the replication group to disable Multi-AZ
   before you proceed. For more information, see [Modifying a replication group](Replication.md "Replication.md").
3. Choose **Valkey** or **Redis OSS**, then from the list of clusters, choose the
   replication group that you want to modify. This replication group must be running
   the "Redis" engine, not the "Clustered Redis" engine, and must have two or more
   nodes.
4. From the list of nodes, choose the replica node you want to promote to primary,
   then for **Actions**, choose **Promote**.
5. In the **Promote Read Replica** dialog box, do the
   following:
   1. For **Apply Immediately**, choose
      **Yes** to promote the read replica immediately, or
      **No** to promote it at the cluster's next maintenance
      window.
   2. Choose **Promote** to promote the read replica or **Cancel**
      to cancel the operation.

6. If the cluster was Multi-AZ enabled before you began the promotion process,
   wait until the replication group's status is **available**, then modify the cluster to
   re-enable Multi-AZ. For more information, see [Modifying a replication group](Replication.md "Replication.md").

## Using the AWS CLI

You can't promote a read replica to primary if the replication group is Multi-AZ
enabled. In some cases, the replica that you want to promote might be a member of a
replication group where Multi-AZ is enabled. In these cases, you must modify the
replication group to disable Multi-AZ before you proceed. Doing this doesn't require
that all your clusters be in the same Availability Zone. For more information on
modifying a replication group, see [Modifying a replication group](Replication.md "Replication.md").

The following AWS CLI command modifies the replication group `sample-repl-group`,
making the read replica `my-replica-1` the primary in the replication group.

For Linux, macOS, or Unix:

```
aws elasticache modify-replication-group \
   --replication-group-id `sample-repl-group` \
   --primary-cluster-id `my-replica-1`
```

For Windows:

```
aws elasticache modify-replication-group ^
   --replication-group-id `sample-repl-group` ^
   --primary-cluster-id `my-replica-1`
```

For more information on modifying a replication group, see modify-replication-group in the _Amazon ElastiCache Command Line Reference._

## Using the ElastiCache API

You can't promote a read replica to primary if the replication group is Multi-AZ
enabled. In some cases, the replica that you want to promote might be a member of a
replication group where Multi-AZ is enabled. In these cases, you must modify the
replication group to disable Multi-AZ before you proceed. Doing this doesn't require
that all your clusters be in the same Availability Zone. For more information on
modifying a replication group, see [Modifying a replication group](Replication.md "Replication.md").

The following ElastiCache API action modifies the replication group `myReplGroup`,
making the read replica `myReplica-1` the primary in the replication group.

```
https://elasticache.us-west-2.amazonaws.com/
   ?Action=ModifyReplicationGroup
   &ReplicationGroupId=myReplGroup
   &PrimaryClusterId=myReplica-1
   &Version=2014-12-01
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Timestamp=20141201T220302Z
   &X-Amz-Algorithm=&AWS;4-HMAC-SHA256
   &X-Amz-Date=20141201T220302Z
   &X-Amz-SignedHeaders=Host
   &X-Amz-Expires=20141201T220302Z
   &X-Amz-Credential=<credential>
   &X-Amz-Signature=<signature>
```

For more information on modifying a replication group, see ModifyReplicationGroup in the _Amazon ElastiCache API Reference._

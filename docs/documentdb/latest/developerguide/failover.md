# Amazon DocumentDB Failover

In certain cases, such as certain types of planned maintenance, or in
the unlikely event of a primary node or Availability Zone failure, Amazon DocumentDB (with MongoDB compatibility) detects the failure and replaces the primary node.
During a failover, write down time is minimized. This is because the role of primary node fails over to one of the read replicas instead of having to create and provision a new primary node.
This failure detection and replica promotion ensure that you can resume writing to the new primary as soon as promotion is complete.

For failover to function, your cluster must have at least two instances
— a primary and at least one replica instance.

###### Note

This topic only applies to original Amazon DocumentDB instance-based clusters. It does not apply to elastic or global clusters.

## Controlling the failover target

Amazon DocumentDB provides you with failover tiers as a means to control which
replica instance is promoted to primary when a failover occurs.

###### Failover Tiers

Each replica instance is associated with a failover tier (0–15). When a failover occurs due to maintenance or an unlikely hardware failure, the primary instance fails over to a replica with the highest priority (the lowest numbered tier). If multiple replicas have the same priority tier, the primary fails over to that tier's replica that is the closest in size to the previous primary.

By setting the failover tier for a group of select replicas to `0` (the highest priority), you can ensure that a failover will promote one of the replicas in that group. You can effectively prevent specific replicas from being promoted to primary in case of a failover by assigning a low-priority tier (high number) to these replicas. This is useful in cases where specific replicas are receiving heavy use by an application and failing over to one of them would negatively impact a critical application.

You can set the failover tier of an instance when you create it or
later by modifying it. Setting an instance failover tier by modifying the instance does not trigger a failover. For more information see the following topics:

- [Adding an Amazon DocumentDB instance to a cluster](db-instance-add.md "db-instance-add.md")
- [Modifying an Amazon DocumentDB instance](db-instance-modify.md "db-instance-modify.md")

When manually initiating a failover, you have two means to control
which replica instance is promoted to primary: the failover tiers as
previously described, and the `--target-db-instance-identifier` parameter.

###### --`target-db-instance-identifier`

For testing, you can force a failover event using the `failover-db-cluster` operation. You can use the `--target-db-instance-identifier` parameter to specify which replica to promote to primary. Using the `--target-db-instance-identifier` parameter supersedes the failover priority tier. If you do not specify the `--target-db-instance-identifier` parameter, the primary failover is in accordance with the failover priority tier.

## What happens during a failover

Failover is automatically handled by Amazon DocumentDB so that your applications can resume database operations as quickly as possible without administrative intervention.

- If you have an Amazon DocumentDB replica instance in the same or different Availability Zone when failing over: Amazon DocumentDB flips the canonical name record (CNAME) for your instance to point at the healthy replica, which is, in turn, promoted to become the new primary. Failover typically completes within 30 seconds from start to finish.
- If you don't have an Amazon DocumentDB replica instance (for example, a
  single instance cluster): Amazon DocumentDB will attempt to create a new
  instance in the same Availability Zone as the original instance.
  This replacement of the original instance is done on a best-effort
  basis and may not succeed if, for example, there is an issue that
  is broadly affecting the Availability Zone.

Your application should retry database connections in the event of a
connection loss.

## Testing failover

A failover for a cluster promotes one of the Amazon DocumentDB replicas
(read-only instances) in the cluster to be the primary instance (the
cluster writer).

When the primary instance fails, Amazon DocumentDB automatically fails over to
an Amazon DocumentDB replica, if one exists. You can force a failover when you want
to simulate a failure of a primary instance for testing. Each instance
in a cluster has its own endpoint address. Therefore, you need to clean
up and re-establish any existing connections that use those endpoint
addresses when the failover is complete.

To force a failover, use the `failover-db-cluster`
operation with these parameters.

- `--db-cluster-identifier`—Required.
  The name of the cluster to fail over.
- `--target-db-instance-identifier`—Optional.
  The name of the instance to be promoted to the primary
  instance.

The following operation forces a failover of the `sample-cluster`
cluster. It does not specify which instance to make the new primary
instance, so Amazon DocumentDB chooses the instance according to failover tier
priority.

For Linux, macOS, or Unix:

```
aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster
```

For Windows:

```
aws docdb failover-db-cluster ^
   --db-cluster-identifier sample-cluster
```

The following operation forces a failover of the `sample-cluster`
cluster, specifying that `sample-cluster-instance` is to
be promoted to the primary role. (Notice `"IsClusterWriter": true`
in the output.)

For Linux, macOS, or Unix:

```
aws docdb failover-db-cluster \
   --db-cluster-identifier sample-cluster \
   --target-db-instance-identifier sample-cluster-instance
```

For Windows:

```
aws docdb failover-db-cluster ^
   --db-cluster-identifier sample-cluster ^
   --target-db-instance-identifier sample-cluster-instance
```

Output from this operation looks something like the following (JSON format).

```
{
    "DBCluster": {
        "HostedZoneId": "Z2SUY0A1719RZT",
        "Port": 27017,
        "EngineVersion": "3.6.0",
        "PreferredMaintenanceWindow": "thu:04:05-thu:04:35",
        "BackupRetentionPeriod": 1,
        "ClusterCreateTime": "2018-06-28T18:53:29.455Z",
        "AssociatedRoles": [],
        "DBSubnetGroup": "default",
        "MasterUsername": "master-user",
        "Engine": "docdb",
        "ReadReplicaIdentifiers": [],
        "EarliestRestorableTime": "2018-08-21T00:04:10.546Z",
        "DBClusterIdentifier": "sample-cluster",
        "ReaderEndpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "DBClusterMembers": [
            {
                "DBInstanceIdentifier": "sample-cluster-instance",
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1,
                `"IsClusterWriter": true`
            },
            {
                "DBInstanceIdentifier": "sample-cluster-instance-00",
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1,
                "IsClusterWriter": false
            },
            {
                "DBInstanceIdentifier": "sample-cluster-instance-01",
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1,
                "IsClusterWriter": false
            }
        ],
        "AvailabilityZones": [
            "us-east-1b",
            "us-east-1c",
            "us-east-1a"
        ],
        "DBClusterParameterGroup": "default.docdb3.6",
        "Endpoint": "sample-cluster.node.us-east-1.docdb.amazonaws.com",
        "IAMDatabaseAuthenticationEnabled": false,
        "AllocatedStorage": 1,
        "LatestRestorableTime": "2018-08-22T21:57:33.904Z",
        "PreferredBackupWindow": "00:00-00:30",
        "StorageEncrypted": false,
        "MultiAZ": true,
        "Status": "available",
        "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster",
        "VpcSecurityGroups": [
            {
                "Status": "active",
                "VpcSecurityGroupId": "sg-12345678"
            }
        ],
        "DbClusterResourceId": "cluster-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }
}
```

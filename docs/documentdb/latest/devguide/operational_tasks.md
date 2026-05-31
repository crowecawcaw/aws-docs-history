# Amazon DocumentDB Operational tasks overview

This section covers operational tasks for your Amazon DocumentDB cluster, and
how to accomplish these tasks using the AWS CLI.

###### Topics

- [Adding a replica to an Amazon DocumentDB cluster](#operational_tasks-add_replica "#operational_tasks-add_replica")
- [Describing clusters and instances](#operational_tasks-list_clusters_and_instances "#operational_tasks-list_clusters_and_instances")
- [Creating a cluster snapshot](#operational_tasks-creating_snapshot "#operational_tasks-creating_snapshot")
- [Restoring from a snapshot](#operational_tasks-restore_from_snapshot "#operational_tasks-restore_from_snapshot")
- [Removing an instance from a cluster](#operational_tasks-remove_instance_from_cluster "#operational_tasks-remove_instance_from_cluster")
- [Deleting a cluster](#operational_tasks-delete_cluster "#operational_tasks-delete_cluster")

## Adding a replica to an Amazon DocumentDB cluster

After you create the primary instance for your Amazon DocumentDB cluster, you
can add one or more _replicas_. A replica is a
read-only instance that serves two purposes:

- **Scalability** — If you
  have a large number of clients that require concurrent access,
  you can add more replicas for read-scaling.
- **High availability** — If
  the primary instance fails, Amazon DocumentDB automatically fails over to a
  replica instance and designates it as the new primary. If a
  replica fails, other instances in the cluster can still serve
  requests until the failed node can be recovered.

Each Amazon DocumentDB cluster can support up to 15 replicas.

###### Note

For maximum fault tolerance, you should deploy replicas in
separate Availability Zones. This helps ensure that your Amazon DocumentDB
cluster can continue to function, even if an entire Availability
Zone becomes unavailable.

The following AWS CLI example shows how to add a new replica. The
`--availability-zone` parameter places the replica in the
specified Availability Zone.

```
aws docdb create-db-instance \
    --db-instance-identifier sample-instance \
    --db-cluster-identifier sample-cluster \
    --engine docdb \
    --db-instance-class db.r5.large \
    --availability-zone us-east-1a

```

## Describing clusters and instances

The following AWS CLI example lists all Amazon DocumentDB clusters in a Region.
For certain management features such as cluster and instance lifecycle
management, Amazon DocumentDB leverages operational technology that is shared with
Amazon RDS. The `filterName=engine,Values=docdb` filter parameter
returns only Amazon DocumentDB clusters.

For more information on describing and modifying clusters, see the [Amazon DocumentDB cluster lifecycle](db-cluster-life-cycle.md "db-cluster-life-cycle.md").

```
aws docdb describe-db-clusters --filter Name=engine,Values=docdb
```

Output from this operation looks something like the following.

```
{
    "DBClusters": [
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-1",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        },
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-2",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        },
        {
            "AvailabilityZones": [
                "us-east-1c",
                "us-east-1b",
                "us-east-1a"
            ],
            "BackupRetentionPeriod": 1,
            "DBClusterIdentifier": "sample-cluster-3",
            "DBClusterParameterGroup": "sample-parameter-group",
            "DBSubnetGroup": "default",
            "Status": "available",
            ...
        }
    ]
}

```

The following AWS CLI example lists the instances in an Amazon DocumentDB cluster.
For more information on describing and modifying clusters, see the [Amazon DocumentDB instance lifecycle](db-instance-life-cycle.md "db-instance-life-cycle.md").

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].[DBClusterMembers]'
```

The output looks like something like below. In this output, there are
two instances. The primary instance is `sample-instance-1`
(`"IsClusterWriter": true`). There is also a replica instance,
`sample-instance2` (`"IsClusterWriter: false"`).

```
[
    [
        [
            {
                "DBInstanceIdentifier": "sample-instance-1",
                "IsClusterWriter": true,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            },
            {
                "DBInstanceIdentifier": "sample-cluster-2",
                "IsClusterWriter": false,
                "DBClusterParameterGroupStatus": "in-sync",
                "PromotionTier": 1
            }
        ]
    ]
]
```

## Creating a cluster snapshot

A _cluster snapshot_ is a complete backup of the
data in your Amazon DocumentDB cluster. When the snapshot is being created,
Amazon DocumentDB reads your data directly from the cluster volume. Because of
this, you can create a snapshot even if your cluster doesn't have any
instances running at the time. The amount of time it takes to create a
snapshot depends on the size of your cluster volume.

Amazon DocumentDB supports automatic backups, which occur daily during the
preferred backup window — a 30-minute period of time during the
day. The following AWS CLI example shows how to view the backup window
for your cluster:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].PreferredBackupWindow'
```

The output shows the backup window (in UTC):

```
[
    "00:18-00:48"
]

```

You can define the backup window when you create your Amazon DocumentDB cluster.
You can also change the backup window, as shown in the following example.
If you don't define a backup window, Amazon DocumentDB automatically assigns one
to your cluster.

```
aws docdb modify-db-cluster \
    --db-cluster-identifier sample-cluster \
    --preferred-backup-window "02:00-02:30"
```

In addition to automatic backups, you can manually create a cluster
snapshot at any time. When you do this, you specify which cluster you
want to back up, and a unique name for your snapshot so that you can
restore from it later.

The following AWS CLI example shows how to create a snapshot of your
data.

```
aws docdb create-db-cluster-snapshot \
    --db-cluster-identifier sample-cluster \
    --db-cluster-snapshot-identifier sample-cluster-snapshot
```

## Restoring from a snapshot

You can restore a cluster snapshot to a new Amazon DocumentDB cluster. To do
this, you provide the name of the snapshot and the name of a new cluster.
You can't restore from a snapshot to an existing cluster; instead,
Amazon DocumentDB creates a new cluster when you restore and then populates it
with your snapshot data.

The following example shows all the snapshots for the cluster
`sample-cluster`.

```
aws docdb describe-db-cluster-snapshots \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusterSnapshots[*].[DBClusterSnapshotIdentifier,SnapshotType,Status]'
```

The output looks something like the following. A manual snapshot is
one that you created manually, whereas an automated snapshot is created
by Amazon DocumentDB within the cluster backup window.

```
[
        "sample-cluster-snapshot",
        "manual",
        "available"
    ],
    [
        "rds:sample-cluster",
        "automated",
        "available"
    ]
]
```

The following example shows how to restore an Amazon DocumentDB cluster from
a snapshot.

```
aws docdb restore-db-cluster-from-snapshot \
    --engine docdb \
    --db-cluster-identifier new-sample-cluster \
    --snapshot-identifier sample-cluster-snapshot
```

The new cluster does not have any instances associated with it; so
if you want to interact with the cluster, you must add an instance to it.

```
aws docdb create-db-instance \
    --db-instance-identifier new-sample-instance \
    --db-instance-class db.r5.large \
    --engine docdb \
    --db-cluster-identifier new-sample-cluster
```

You can use the following AWS CLI operations to monitor the progress of
cluster and instance creation. When the cluster and instance statuses
are available, you can connect to the new cluster's endpoint and access
your data.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier new-sample-cluster  \
    --query 'DBClusters[*].[Status,Endpoint]'
```

```
aws docdb describe-db-instances \
    --db-instance-identifier new-sample-instance \
    --query 'DBInstances[*].[DBInstanceStatus]'
```

## Removing an instance from a cluster

Amazon DocumentDB stores all of your data in the cluster volume. The data
persists in that cluster volume, even if you remove all the instances
from your cluster. If you need to access the data again, you can add an
instance to the cluster at any time, and pick up where you left off.

The following example shows how to remove an instance from your
Amazon DocumentDB cluster.

```
aws docdb delete-db-instance \
    --db-instance-identifier sample-instance
```

## Deleting a cluster

Before you can delete an Amazon DocumentDB cluster, you must first remove all
of its instances. The following AWS CLI example returns information about
the instances in a cluster. If this operation returns any instance
identifiers, you have to delete each of the instances. For more
information, see [Removing an instance from a cluster](#operational_tasks-remove_instance_from_cluster "#operational_tasks-remove_instance_from_cluster").

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].DBClusterMembers[*].DBInstanceIdentifier'
```

When there are no more instances remaining, you can delete the
cluster. At that time, you must choose one of the following options:

- Create a final snapshot —
  Capture all the cluster data in a snapshot so that you can
  re-create a new instance with that data later. The following
  example shows how to do this:

```
aws docdb delete-db-cluster \
    --db-cluster-identifier sample-cluster \
    **--final-db-snapshot-identifier sample-cluster-snapshot**
```

- Skip the final snapshot —
  Permanently discard all the cluster data. This cannot be reversed.
  The following example shows how to do this:

```
aws docdb delete-db-cluster \
    --db-cluster-identifier sample-cluster \
    **--skip-final-snapshot**
```

# Restoring to a point in time

You can restore a cluster to any point in time that is within the
cluster's backup retention period using the AWS Management Console or AWS Command Line Interface
(AWS CLI).

###### Note

You cannot conduct a point-in-time restore of a 3.6 cluster to a 4.0 cluster but you can migrate from one cluster version to another. For more information, go to [Migrating to Amazon DocumentDB](docdb-migration.md "docdb-migration.md").

Keep the following in mind when restoring a cluster to a point in
time.

- The new cluster is created with the same configuration as the
  source cluster, except that the new cluster is created with the
  default parameter group. To set the new cluster's parameter group
  to the source cluster's parameter group, modify the cluster after
  it is _available_. For more information on
  modifying a cluster, see [Modifying an Amazon DocumentDB cluster](db-cluster-modify.md "db-cluster-modify.md").

Using the AWS Management Console
You can restore a cluster to a point-in-time within its backup
retention period by completing the following using the AWS Management Console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.
   In the list of clusters, choose the button to the left of the
   cluster that you want to restore.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. On the **Actions** menu, choose
**Restore to point in time**. 4. Complete the **Restore time** section,
which specifies the date and time to restore to.

    1. **Restore date**—Choose or
     enter a date that is between the **Earliest
     restore time** and the **Latest restore
     time**.
    2. **Restore time**—Choose or
     enter the hour, minute, and seconds that are between the
     **Earliest restore time** and the
     **Latest restore time**.

5.  Complete the **Configuration** section.
    1. **Cluster identifier** —
       Accept the default identifier, or enter an identifier
       that you prefer.

    Cluster naming constraints:

        * Length is [1—63] letters, numbers, or
         hyphens.
        * First character must be a letter.
        * Cannot end with a hyphen or contain two
         consecutive hyphens.
        * Must be unique for all clusters across Amazon RDS,
         Neptune and Amazon DocumentDB per AWS account, per Region.

    2. **Instance class** — From the
       drop-down list, choose the instance class that you want
       for the cluster's instances.
    3. **Number of instances** —
       From the drop-down list, choose the number of instances
       that you want created when the cluster is restored.

6.  For **Cluster storage configuration**, choose a storage option.

###### Note

**Amazon DocumentDB I/O-Optimized** storage configuration is only available on the Amazon DocumentDB 5.0 engine version. 7. Optional. To configure the network settings, cluster options,
and enable log exports, choose **Show advanced
settings**, and then complete the following sections.
Otherwise, continue with the next step.

    * **Network settings**




    	1. **Virtual Private Cloud (VPC)**
    	 — From the drop-down list, choose the VPC
    	 that you want to use for this cluster.
    	2. **Subnet group** — From
    	 the drop-down list, choose the subnet group for
    	 this cluster.
    	3. **VPC security groups**
    	 — From the drop-down list, choose the VPC
    	 security groups for this cluster.
    * **Cluster options**




    	1. **Port** — Accept the
    	 default port (27017), or use the up and down
    	 arrows to set the port for communicating with this
    	 cluster.
    * **Log exports**




    	1. **Audit logs** — Select
    	 this option to enable exporting audit logs to
    	 Amazon CloudWatch Logs. If you select this option, you must
    	 enable `audit_logs` in the cluster's
    	 custom parameter group. For more information, see
    	 [Auditing Amazon DocumentDB events](event-auditing.md "event-auditing.md").
    	2. **Profiler logs** —
    	 Select this option to enable exporting operation
    	 profiler logs to Amazon CloudWatch Logs. If you select this
    	 option, you must also modify the following
    	 parameters in the cluster's custom parameter group:




    		+ `profiler` — Set to
    		 `enabled`.
    		+ `profiler_threshold_ms`
    		 — Set to a value
    		 `[0-INT_MAX]` to set the
    		 threshold for profiling operations.
    		+ `profiler_sampling_rate`
    		 — Set to a value
    		 `[0.0-1.0]` to set the percentage
    		 of slow operations to profile.
    	For more information, see [Profiling Amazon DocumentDB operations](profiling.md "profiling.md").
    	3. **Profiler logs** —
    	 Export profiler logs to Amazon CloudWatch
    	4. **IAM role** — From
    	 the drop-down list, choose *RDS Service
    	 Linked Role*.
    * **Tags**




    	1. **Add Tag**
    	 — In the *Key* box,
    	 enter the name for the tag for your cluster. In
    	 the *Value* box, optionally
    	 enter the tag value. Tags are used with AWS Identity and Access Management
    	 (IAM) policies to manage access to Amazon DocumentDB
    	 resources and to control what actions can be
    	 applied to the resources.
    * **Deletion protection**





    	1. **Enable deletion
    	 protection** — Protects the
    	 cluster from being accidentally deleted. While
    	 this option is enabled, you can't delete the
    	 cluster.

8. To restore the cluster, choose **Create
   cluster**. Alternatively, you can choose
   **Cancel** to cancel the operation.

Using the AWS CLI
To restore a cluster to a point in time using the snapshot's
backup retention period, use the `restore-db-cluster-to-point-in-time` operation with the following parameters.

- `--db-cluster-identifier`— Required. The name of the new cluster to be created. This cluster cannot exist before the operation. The parameter value must meet the following constraints.

Cluster naming constraints:

    + Length is [1—63] letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive
     hyphens.
    + Must be unique for all clusters across Amazon RDS,
     Neptune and Amazon DocumentDB per AWS account, per Region.

- `--restore-to-time`
  — The UTC date and time to restore the cluster to. For
  example, `2018-06-07T23:45:00Z`.

Time Constraints:

    + Must be before the latest restorable time for the
     cluster.
    + Must be specified if the
     `--use-latest-restorable-time` parameter is
     not provided.
    + Cannot be specified if the
     `--use-latest-restorable-time` parameter is
     `true`.
    + Cannot be specified if the `--restore-type`
     parameter value is `copy-on-write`.

- `--source-db-cluster-identifier`
  — The name of the source cluster from which to restore.
  This cluster must exist and be available.
- `--use-latest-restorable-time`
  or `--no-use-latest-restorable-time`
  — Whether to restore to the latest restorable backup
  time. Cannot be specified if the `--restore-to-time`
  parameter is provided.
- `--storage-type standard | iopt1` —
  Optional. Default: `standard`.

The AWS CLI operation `restore-db-cluster-to-point-in-time`
only restores the cluster, not the instances for that cluster. You
must invoke the `create-db-instance` operation to create
instances for the restored cluster, specifying the identifier of the
restored cluster in `--db-cluster-identifier`. You can
create instances only after the
`restore-db-cluster-to-point-in-time` operation has
completed and the restored cluster is _available_.

###### Example

The following example creates `sample-cluster-restored`
from the snapshot `sample-cluster-snapshot` to the
latest restorable time.

For Linux, macOS, or Unix:

```
aws docdb restore-db-cluster-to-point-in-time \
    --db-cluster-identifier sample-cluster-restored \
    --source-db-cluster-identifier sample-cluster-snapshot \
    --use-latest-restorable-time
```

For Windows:

```
aws docdb restore-db-cluster-to-point-in-time ^
    --db-cluster-identifier sample-cluster-restored ^
    --source-db-cluster-identifier sample-cluster-snapshot ^
    --use-latest-restorable-time
```

###### Example

The following example creates `sample-cluster-restored`
from the snapshot `sample-cluster-snapshot` to 03:15
on December 11, 2018 (UTC), which is within the backup retention
period of `sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb restore-db-cluster-to-point-in-time \
    --db-cluster-identifier sample-cluster-restore \
    --source-db-cluster-identifier sample-cluster \
    --restore-to-time 2020-05-12T03:15:00Z
```

For Windows:

```
aws docdb restore-db-cluster-to-point-in-time ^
    --db-cluster-identifier sample-cluster-restore ^
    --source-db-cluster-identifier sample-cluster ^
    --restore-to-time 2020-05-12T03:15:00Z
```

Output from this operation looks something like the following.

```
{
    "DBCluster": {
        "AvailabilityZones": [
            "us-east-1c",
            "us-west-2b",
            "us-west-2a"
        ],
        "BackupRetentionPeriod": 1,
        "DBClusterIdentifier": "sample-cluster-restored",
        "DBClusterParameterGroup": "sample-parameter-group",
        "DBSubnetGroup": "default",
        "Status": "creating",
        "Endpoint": "sample-cluster-restored.node.us-east-1.docdb.amazonaws.com",
        "ReaderEndpoint": "sample-cluster-restored.node.us-east-1.docdb.amazonaws.com",
        "MultiAZ": false,
        "Engine": "docdb",
        "EngineVersion": "4.0.0",
        "Port": 27017,
        "MasterUsername": "master-user",
        "PreferredBackupWindow": "02:00-02:30",
        "PreferredMaintenanceWindow": "tue:09:50-tue:10:20",
        "DBClusterMembers": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abc0123",
                "Status": "active"
            }
        ],
        "HostedZoneId": "ABCDEFGHIJKLM",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID^>:key/sample-key",
        "DbClusterResourceId": "cluster-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "DBClusterArn": "arn:aws:rds:us-east-1:<accountID>:cluster:sample-cluster-restored",
        "AssociatedRoles": [],
        "ClusterCreateTime": "2020-04-24T20:14:36.713Z",
        "DeletionProtection": false
    }
}

```

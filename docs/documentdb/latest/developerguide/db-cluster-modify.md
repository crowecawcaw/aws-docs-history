# Modifying an Amazon DocumentDB cluster

To modify a cluster, the cluster must be in the
_available_ state. You cannot modify a cluster
that is stopped. If the cluster is stopped, first start the cluster,
wait for the cluster to become _available_, and
then make the desired modifications. For more information, see [Stopping and starting an
Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

Using the AWS Management Console
Use the following procedure to modify a specific Amazon DocumentDB
cluster using the console.

###### To modify an Amazon DocumentDB cluster

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. Specify the cluster that you want to modify by choosing
the button to the left of the cluster's name. 4. Choose **Actions**, and then choose
**Modify**. 5. In the **Modify Cluster: <cluster-name>**
pane, make the changes that you want. You can make changes
in the following areas:

    * **Cluster specifications**—The
     cluster's name, security groups, and credentials management.
    * **Cluster storage configuration**—The
     cluster's data storage mode. Choose between Standard and I/O-Optimized configuration.
    * **Cluster options**—The
     cluster's port and parameter group.
    * **Backup**—The
     cluster's backup retention period and backup window.
    * **Log exports**—Enable
     or disable exporting audit or profiler logs.
    * **Maintenance**—Set
     the cluster's maintenance window.
    * **Deletion protection**—Enable
     or disable deletion protection on the cluster. Deletion
     protection is enabled by default.

6. When you're finished, choose **Continue**
   to view a summary of your changes.
7. If you are satisfied with your changes, you can choose
   **Modify cluster** to modify your cluster.
   Alternatively, you can choose **Back** or
   **Cancel** to edit or cancel your changes,
   respectively.

It takes a few minutes for your changes to be applied. You can
use the cluster only when its status is _available_.
You can monitor the cluster's status using the console or AWS CLI.
For more information, see [Monitoring an Amazon DocumentDB cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md").

Using the AWS CLI
Use the `modify-db-cluster` operation to modify the
specified cluster using the AWS CLI. For more information, see [`ModifyDBCluster`](API_ModifyDBCluster.md "API_ModifyDBCluster.md")
in the _Amazon DocumentDB API Reference_.

###### Parameters

- `--db-cluster-identifier`—Required.
  The identifier of the Amazon DocumentDB cluster that you are going to
  modify.
- `--backup-retention-period`—Optional.
  The number of days for which automated backups are retained.
  Valid values are 1–35.
- `--storage-type`—Optional.
  The cluster's storage configuration.
  Valid values are `standard` (Standard) or `iopt1` (I/O-optimized).
- `--db-cluster-parameter-group-name`—Optional.
  The name of the cluster parameter group to use for the
  cluster.
- `--manage-master-user-password`—Optional.
  Amazon DocumentDB generates the master user password and manages it throughout its lifecycle in Secrets Manager.
- `--rotate-master-user-password`—Optional.
  Secrets Manager generates a new secret version for the existing secret.
  The new version of the secret contains the new primary user password.
  Amazon DocumentDB changes the primary user password for the cluster to match the password for the new secret version.

You must specify the `--apply-immediately` option when you rotate the primary password.

- `--master-user-password`—Optional.
  The new password for the primary database user.

Password constraints:

    + Length is [8—100] printable ASCII characters.
    + Can use any printable ASCII characters except for
     the following:




    	- `/`
    	 (forward slash)
    	- `"`
    	 (double quotation mark)
    	- `@`
    	 (at symbol)

- `--new-db-cluster-identifier`—Optional.
  The new cluster identifier for the cluster when renaming a
  cluster. This value is stored as a lowercase string.

Naming constraints:

    + Length is [1—63] letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive
     hyphens.
    + Must be unique for all clusters across Amazon RDS, Amazon Neptune, and Amazon DocumentDB per AWS account, per region.

- `--preferred-backup-window`—Optional.
  The daily time range during which automated backups are
  created, in Universal Coordinated Time (UTC).
  - Format: `hh24:mm-hh24:mm`

- `--preferred-maintenance-window`—Optional.
  The weekly time range during which system maintenance can
  occur, in UTC.
  - Format: `ddd:hh24:mm-ddd:hh24:mm`
  - Valid days: `Sun`, `Mon`,
    `Tue`, `Wed`, `Thu`,
    `Fri`, and `Sat`.

- `--deletion-protection`
  or `--no-deletion-protection`—Optional.
  Whether deletion protection should be enabled on this cluster.
  Deletion protection prevents a cluster from being accidentally
  deleted until the cluster is modified to disable deletion
  protection. For more information, see [Deleting an Amazon DocumentDB cluster](db-cluster-delete.md "db-cluster-delete.md").
- `--apply-immediately`
  or `--no-apply-immediately`—Use
  `--apply-immediately` to make the change immediately.
  Use `--no-apply-immediately` to make the change
  during your cluster's next maintenance window.

The following code changes the backup retention period for
the cluster `sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb modify-db-cluster \
       --db-cluster-identifier sample-cluster \
       --apply-immediately \
       --backup-retention-period 7
```

For Windows:

```
aws docdb modify-db-cluster ^
       --db-cluster-identifier sample-cluster ^
       --apply-immediately ^
       --backup-retention-period 7
```

Output from this operation looks something like the following.

```
{
    "DBCluster": {
        **"BackupRetentionPeriod": 7**,
        "DbClusterResourceId": "cluster-VDP53QEWST7YHM36TTXOPJT5YE",
        "Status": "available",
        "DBClusterMembers": [
            {
                "PromotionTier": 1,
                "DBClusterParameterGroupStatus": "in-sync",
                "DBInstanceIdentifier": "sample-cluster-instance",
                "IsClusterWriter": true
            }
        ],
        "ReadReplicaIdentifiers": [],
        "AvailabilityZones": [
            "us-east-1b",
            "us-east-1c",
            "us-east-1a"
        ],
        "ReaderEndpoint": "sample-cluster.cluster-ro-ctevjxdlur57.us-east-1.rds.amazonaws.com",
        "DBClusterArn": "arn:aws:rds:us-east-1:123456789012:cluster:sample-cluster",
        "PreferredMaintenanceWindow": "sat:09:51-sat:10:21",
        "EarliestRestorableTime": "2018-06-17T00:06:19.374Z",
        "StorageEncrypted": false,
        "MultiAZ": false,
        "AssociatedRoles": [],
        "MasterUsername": "`<your-master-user-name>`",
        "DBClusterIdentifier": "sample-cluster",
        "VpcSecurityGroups": [
            {
                "Status": "active",
                "VpcSecurityGroupId": "sg-77186e0d"
            }
        ],
        "HostedZoneId": "Z2SUY0A1719RZT",
        "LatestRestorableTime": "2018-06-18T21:17:05.737Z",
        "AllocatedStorage": 1,
        "Port": 27017,
        "Engine": "docdb",
        "DBClusterParameterGroup": "default.docdb3.4",
        "Endpoint": "sample-cluster.cluster-ctevjxdlur57.us-east-1.rds.amazonaws.com",
        "DBSubnetGroup": "default",
        "PreferredBackupWindow": "00:00-00:30",
        "EngineVersion": "3.4",
        "ClusterCreateTime": "2018-06-06T19:25:47.991Z",
        "IAMDatabaseAuthenticationEnabled": false
    }
}
```

It takes a few minutes for your changes to be applied. You can
use the cluster only when its status is _available_.
You can monitor the cluster's status using the console or AWS CLI.
For more information, see [Monitoring an Amazon DocumentDB cluster's status](monitoring_docdb-cluster_status.md "monitoring_docdb-cluster_status.md").

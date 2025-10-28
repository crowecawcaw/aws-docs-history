# Deleting an Amazon DocumentDB instance

You can delete your Amazon DocumentDB instance using either the AWS Management Console or the AWS CLI. To delete an instance, the instance must be in the _available_ state. You cannot delete an
instance that is stopped. If the Amazon DocumentDB cluster that contains
your instance is stopped, first start the cluster, wait for the
instance to become _available_, and then
delete the instance. For more information, see [Stopping and starting an
Amazon DocumentDB cluster](db-cluster-stop-start.md "db-cluster-stop-start.md").

###### Note

Amazon DocumentDB stores all of your data in the cluster volume. The
data persists in that cluster volume, even if you remove
all the instances from your cluster. If you need to access
the data again, you can add an instance to the cluster at
any time and pick up where you left off.

Using the AWS Management Console
The following procedure deletes a specified Amazon DocumentDB instance
using the console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters** .

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the Clusters navigation box, you’ll see the column **Cluster Identifier**. Your instances are listed under clusters, similar to the screenshot below.

![Clusters table showing list of clusters under Cluster identifier column, with instances nested inside clusters.](images/choose-clusters.png) 4. Check the box to the left of the instance you wish to delete. 5. Select **Actions**, and then
choose **Delete**.

    1. If you are deleting the last instance in your
     cluster:




    	* **Create final cluster
    	 snapshot?** — Choose
    	 **Yes** if you want
    	 to create a final snapshot before the
    	 cluster is deleted. Otherwise, choose
    	 **No**.
    	* **Final snapshot name**
    	 — If you choose to create a
    	 final snapshot, enter the cluster
    	 snapshot identifier of the new cluster
    	 snapshot created.
    	* **Delete <instance-name>
    	 instance?** — Enter
    	 the phrase **delete entire
    	 cluster** into the field to
    	 confirm the deletion.
    2. If you are not deleting the last instance
     in your cluster:




    	* **Delete <instance-name>
    	 instance?** — Enter
    	 the phrase **delete me**
    	 into the field to confirm the deletion.

6. Select **Delete** to delete the
   instance.

It takes several minutes for an instance to be deleted.
To monitor the status of an instance, see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

Using the AWS CLI
The following procedure deletes an Amazon DocumentDB instance using
the AWS CLI.

1. **First, determine how many
   instances are in your Amazon DocumentDB cluster:**

To determine how many instances are in your cluster,
run the `describe-db-clusters` command, as
follows.

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster \
    --query 'DBClusters[*].[DBClusterIdentifier,DBClusterMembers[*].DBInstanceIdentifier]'
```

Output from this operation looks something like the
following.

```
[
    [
        "sample-cluster",
        [
            "sample-instance-1",
            "sample-instance-2"
        ]
    ]
]
```

2. **If there are more than one
   instances in your Amazon DocumentDB cluster:**

To delete a specified Amazon DocumentDB instance, use the
`delete-db-instance` command with the
`--db-instance-identifier` parameter, as
shown below. It takes several minutes for an instance
to be deleted. To monitor the status of an instance,
see [Monitoring an Amazon DocumentDB instance's status](monitoring_docdb-instance_status.md "monitoring_docdb-instance_status.md").

```
aws docdb delete-db-instance \
       --db-instance-identifier sample-instance-2
```

Output from this operation looks something like
the following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "sample-instance-2",
        "DBInstanceClass": "db.r5.large",
        "Engine": "docdb",
        "DBInstanceStatus": "deleting",
        "Endpoint": {
            "Address": "sample-instance-2.node.us-east-1.docdb.amazonaws.com",
            "Port": 27017,
            "HostedZoneId": "ABCDEFGHIJKLM"
        },
        "InstanceCreateTime": "2020-03-27T08:05:56.314Z",
        "PreferredBackupWindow": "02:00-02:30",
        "BackupRetentionPeriod": 1,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcd0123",
                "Status": "active"
            }
        ],
        "AvailabilityZone": "us-east-1c",
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-6242c31a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-abcd0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    "SubnetIdentifier": "subnet-wxyz0123",
                    "SubnetAvailabilityZone": {
                        "Name": "us-east-1b"
                    },
                    "SubnetStatus": "Active"
                }
            ]
        },
        "PreferredMaintenanceWindow": "sun:06:53-sun:07:23",
        "PendingModifiedValues": {},
        "EngineVersion": "3.6.0",
        "AutoMinorVersionUpgrade": true,
        "PubliclyAccessible": false,
        "DBClusterIdentifier": "sample-cluster",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "CACertificateIdentifier": "rds-ca-2019",
        "PromotionTier": 1,
        "DBInstanceArn": "arn:aws:rds:us-east-1:<accountID>:db:sample-instance-2",
        "EnabledCloudwatchLogsExports": [
            "profiler"
        ]
    }
}

```

3. **If the instance your want to
   delete is the last instance in your Amazon DocumentDB cluster:**

If you delete the last instance in an Amazon DocumentDB
cluster, you also delete that cluster and the
automatic snapshots and continuous backups associated
with that cluster.

To delete the last instance in your cluster, you
can delete the cluster and optionally create a final
snapshot. For more information, see [Deleting an Amazon DocumentDB cluster](db-cluster-delete.md "db-cluster-delete.md").

## Deletion protection

Deleting the last instance of an Amazon DocumentDB cluster will also
delete the cluster, as well as the automatic snapshots and
continuous backups associated with that cluster. Amazon DocumentDB
enforces deletion protection for a cluster whether you
perform the delete operation using the AWS Management Console or the
AWS CLI. If deletion protection is enabled, you can't delete a
cluster.

To delete a cluster that has deletion protection enabled,
you must first modify the cluster and disable deletion
protection. For more information, see [Deleting an Amazon DocumentDB cluster](db-cluster-delete.md "db-cluster-delete.md").

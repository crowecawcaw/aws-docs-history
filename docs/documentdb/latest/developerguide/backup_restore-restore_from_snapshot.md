# Restoring from a cluster snapshot

Amazon DocumentDB (with MongoDB compatibility) creates a cluster snapshot of your storage volume. You
can create a new cluster by restoring from a cluster snapshot. When you
restore the cluster, you provide the name of the cluster snapshot to
restore from and a name for the new cluster that is created by the
restore. You can't restore from a snapshot to an existing cluster
because a new cluster is created when you restore.

When you are restoring a cluster from a cluster snapshot:

- This action restores only the cluster, and not the instances for that cluster. You must invoke the `create-db-instance` action to create instances for the restored cluster, specifying the identifier of the restored cluster in `--db-cluster-identifier`. You can create instances only after the cluster is _available_.
- You cannot restore an encrypted snapshot to an unencrypted
  cluster. However, you can restore an unencrypted snapshot to an
  encrypted cluster by specifying the AWS KMS key.
- To restore a cluster from an encrypted snapshot, you must have
  access to the AWS KMS key.

###### Note

You cannot restore a 3.6 cluster to a 4.0 cluster but you can migrate from one cluster version to another. For more information, go to [Migrating to Amazon DocumentDB](docdb-migration.md "docdb-migration.md").

Using the AWS Management Console
The following procedure shows how to restore an Amazon DocumentDB cluster
from a cluster snapshot using the Amazon DocumentDB Management Console.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Snapshots**, and then choose the button to the left of the snapshot that you want to use to restore a cluster.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. On the **Actions** menu, choose
**Restore**. 4. On the **Restore snapshot** page, complete
the **Configuration** section.

    1. **Cluster identifier** — The name for the new cluster. You can accept the Amazon DocumentDB supplied name or type a name that you prefer. The Amazon DocumentDBsupplied name is in the format of `docdb-` plus a UTC timestamp; for example, `docdb-*yyyy-mm-dd-hh-mm-ss*`.
    2. **Instance class** — The
     instance class for the new cluster. You can accept the
     default instance class or choose an instance class from
     the drop-down list.
    3. **Number of instances** — The
     number of instances you want created with this cluster.
     You can accept the default of 3 instances (1 primary
     read/write and 2 read-only replicas) or choose the
     number of instances from the drop-down list.

5. For **Cluster storage configuration**, choose a storage option.

###### Note

**Amazon DocumentDB I/O-Optimized** storage configuration is only available on the Amazon DocumentDB 5.0 engine version. 6. If you are satisfied with the cluster configuration, choose
**Restore cluster** and wait while your
cluster is restored. 7. If you prefer to change some configurations, such as
specifying a non-default Amazon VPC or security group, choose
**Show advanced settings** from the bottom
left of the page, and then continue with the following steps.

    1. Complete the **Network settings**
     section.




    	* **Virtual Private Cloud (VPC)**
    	 — Accept the current VPC, or choose a VPC
    	 from the drop-down list.
    	* **Subnet Group** —
    	 Accept the `default` subnet group, or
    	 choose one from the drop-down list.
    	* **VPC Security Groups**
    	 — Accept the `default (VPC)`
    	 security group, or choose one from the list.
    2. Complete the **Cluster options**
     section.




    	* **Database port** —
    	 Accept the default port, `27017`, or
    	 use the up or down arrow to set the port that you
    	 want to use for application connections.
    3. Complete the **Encryption** section.





    	* **Encryption at rest** — If your snapshot is encrypted, these options are not available to you. If it is not encrypted, you can choose one of the following:




    		+ To encrypt all your cluster's data, choose **Enable encryption-at-rest**. If you choose this option, you must designate a KMS key.
    		+ To not encrypt your cluster's data, choose **Disable encryption-at-rest**. If you choose this option, you are finished with the encryption section.
    	* **AWS KMS Key** — Choose one of the following from the drop-down list:




    		+ **(default) aws/rds**
    		 — The account number and AWS KMS key ID are listed following this option.
    		+ **Customer-managed key** — This option is available only if you created an IAM encryption key in the AWS Identity and Access Management (IAM) console. You can choose the key to encrypt your cluster.
    		+ **Enter a key ARN**
    		 — In the **ARN** box, enter the Amazon Resource Name (ARN) for your AWS KMS key. The format of the ARN is `arn:aws:kms:<region>:<accountID>:key/<key-id>`.
    4. Complete the **Log exports** section.





    	* **Select the log types to publish to
    	 CloudWatch** — Choose one of the
    	 following:




    		+ **Enabled** —
    		 Enables your cluster to export DDL logging
    		 to Amazon CloudWatch Logs.
    		+ **Disabled** —
    		 Prevents your cluster from exporting DDL logs to Amazon CloudWatch Logs. **Disabled** is the default.
    	* **IAM role**—From the
    	 list, choose *RDS Service Linked Role*.
    5. Complete the **Tags** section.




    	* **Add Tag** — In the
    	 *Key* box, enter the name for
    	 the tag for your cluster. In the
    	 *Value* box, optionally enter
    	 the tag value. Tags are used with AWS Identity and Access Management (IAM)
    	 policies to manage access to Amazon DocumentDB resources and
    	 to control what actions can be applied to the
    	 resources.
    6. Complete the **Deletion protection**
     section.




    	* **Enable deletion protection**
    	 — Protects the cluster from being
    	 accidentally deleted. While this option is enabled,
    	 you can't delete the cluster.

8. Choose **Restore cluster**.

Using the AWS CLI
To restore a cluster from a snapshot using the AWS CLI, use the
`restore-db-cluster-from-snapshot` operation with the
following parameters. For more information, see [RestoreDBClusterFromSnapshot](API_RestoreDBClusterFromSnapshot.md "API_RestoreDBClusterFromSnapshot.md").

- `--db-cluster-identifier`
  — Required. The name of the cluster that is created by
  the operation. A cluster by this name cannot exist before this
  operation.

Cluster naming constraints:

    + Length is [1—63] letters, numbers, or hyphens.
    + First character must be a letter.
    + Cannot end with a hyphen or contain two consecutive
     hyphens.
    + Must be unique for all clusters across Amazon RDS, Neptune,
     and Amazon DocumentDB per AWS account, per Region.

- `--snapshot-identifier`
  — Required. The name of the snapshot used to restore
  from. A snapshot by this name must exist and be in the
  _available_ state.
- `--engine` —
  Required. Must be `docdb`.
- `--storage-type standard | iopt1` —
  Optional. Default: `standard`.
- `--kms-key-id` —
  Optional. The ARN of the AWS KMS key identifier to use when
  restoring an encrypted snapshot or encrypting a cluster when
  restoring from an unencrypted snapshot. Supplying the AWS KMS
  key ID results in the restored cluster being encrypted with
  the AWS KMS key, whether or not the snapshot was encrypted.

The format of the `--kms-key-id` is
`arn:aws:kms:<region>:<accountID>:key/<key-id>`.
If you do not specify a value for the `--kms-key-id`
parameter, then the following occurs:

    + If the snapshot in `--snapshot-identifier`
     is encrypted, then the restored cluster is encrypted
     using the same AWS KMS key that was used to encrypt the
     snapshot.
    + If the snapshot in `--snapshot-identifier`
     is not encrypted, then the restored cluster is not
     encrypted.

For Linux, macOS, or Unix:

```
aws docdb restore-db-cluster-from-snapshot \
    --db-cluster-identifier sample-cluster-restore \
    --snapshot-identifier sample-cluster-snapshot \
    --engine docdb \
    --kms-key-id arn:aws:kms:us-east-1:123456789012:key/SAMPLE-KMS-KEY-ID
```

For Windows:

```
aws docdb restore-db-cluster-from-snapshot ^
    --db-cluster-identifier sample-cluster-restore ^
    --snapshot-identifier sample-cluster-snapshot ^
    --engine docdb ^
    --kms-key-id arn:aws:kms:us-east-1:123456789012:key/SAMPLE-KMS-KEY-ID
```

Output from this operation looks something like the following.

```
{
    "DBCluster": {
        "AvailabilityZones": [
            "us-east-1c",
            "us-east-1b",
            "us-east-1a"
        ],
        "BackupRetentionPeriod": 1,
        "DBClusterIdentifier": "sample-cluster-restore",
        "DBClusterParameterGroup": "default.docdb4.0",
        "DBSubnetGroup": "default",
        "Status": "creating",
        "Endpoint": "sample-cluster-restore.cluster-node.us-east-1.docdb.amazonaws.com",
        "ReaderEndpoint": "sample-cluster-restore.cluster-node.us-east-1.docdb.amazonaws.com",
        "MultiAZ": false,
        "Engine": "docdb",
        "EngineVersion": "4.0.0",
        "Port": 27017,
        "MasterUsername": "<master-user>",
        "PreferredBackupWindow": "02:00-02:30",
        "PreferredMaintenanceWindow": "tue:09:50-tue:10:20",
        "DBClusterMembers": [],
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcdefgh",
                "Status": "active"
            }
        ],
        "HostedZoneId": "ABCDEFGHIJKLM",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/<sample-key-id>",
        "DbClusterResourceId": "cluster-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "DBClusterArn": "arn:aws:rds:us-east-1:<accountID>:cluster:sample-cluster-restore",
        "AssociatedRoles": [],
        "ClusterCreateTime": "2020-04-01T01:43:40.871Z",
        "DeletionProtection": true
    }
}

```

After the cluster status is _available_,
create at least one instance for the cluster.

For Linux, macOS, or Unix:

```
aws docdb create-db-instance \
    --db-cluster-identifier sample-cluster-restore  \
    --db-instance-identifier sample-cluster-restore-instance \
    --availability-zone us-east-1b \
    --promotion-tier 2 \
    --db-instance-class db.r5.large \
    --engine docdb
```

For Windows:

```
aws docdb create-db-instance ^
    --db-cluster-identifier sample-cluster-restore  ^
    --db-instance-identifier sample-cluster-restore-instance ^
    --availability-zone us-east-1b ^
    --promotion-tier 2 ^
    --db-instance-class db.r5.large ^
    --engine docdb
```

Output from this operation looks something like the following.

```
{
    "DBInstance": {
        "DBInstanceIdentifier": "sample-cluster-restore-instance",
        "DBInstanceClass": "db.r5.large",
        "Engine": "docdb",
        "DBInstanceStatus": "creating",
        "PreferredBackupWindow": "02:00-02:30",
        "BackupRetentionPeriod": 1,
        "VpcSecurityGroups": [
            {
                "VpcSecurityGroupId": "sg-abcdefgh",
                "Status": "active"
            }
        ],
        "AvailabilityZone": "us-west-2b",
        "DBSubnetGroup": {
            "DBSubnetGroupName": "default",
            "DBSubnetGroupDescription": "default",
            "VpcId": "vpc-6242c31a",
            "SubnetGroupStatus": "Complete",
            "Subnets": [
                {
                    "SubnetIdentifier": "subnet-abcdefgh",
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    },
                    "SubnetStatus": "Active"
                },
                {
                    ...
                }
            ]
        },
        "PreferredMaintenanceWindow": "fri:09:43-fri:10:13",
        "PendingModifiedValues": {},
        "EngineVersion": "4.0.0",
        "AutoMinorVersionUpgrade": true,
        "PubliclyAccessible": false,
        "DBClusterIdentifier": "sample-cluster-restore",
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/<sample-key-id>",
        "DbiResourceId": "db-ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "CACertificateIdentifier": "rds-ca-2019",
        "PromotionTier": 2,
        "DBInstanceArn": "arn:aws:rds:us-east-1:<accountID>:db:sample-cluster-restore-instance"
    }
}

```

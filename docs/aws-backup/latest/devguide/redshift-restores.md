# Restore an Amazon Redshift cluster

You can restore automated and manual snapshots in the AWS Backup console or through
CLI.

When you restore a Amazon Redshift cluster, the original cluster settings are input into the
console by default. You can specify different settings for the configurations below. When
restoring a table, you must specify the source and target databases. For more information on
these configurations, see [Restoring a cluster from a snapshot](../../../redshift/latest/mgmt/working-with-snapshots.md#working-with-snapshot-restore-cluster-from-snapshot "../../../redshift/latest/mgmt/working-with-snapshots.md#working-with-snapshot-restore-cluster-from-snapshot") in the _Amazon Redshift Management
Guide_.

- **Single table or cluster**: You can choose to restore an entire
  cluster or a single table. If you choose to restore a single table, the source database,
  source schema, and source table name are needed, as well as the target cluster, schema,
  and new table name.
- **Node type**: Each Amazon Redshift cluster consists of a leader node and at
  least one compute node. When you restore a cluster, you need to specify the node type
  that meets your requirements for CPU, RAM, storage capacity, and drive type.
- **Number of nodes**: When restoring a cluster, you need to specify
  the number of nodes needed.
- **Configuration summary**
- **Cluster Permissions**

## To restore an Amazon Redshift cluster or table using the AWS Backup console

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the navigation pane, choose **Settings** and the Amazon Redshift
   resource ID that you want to restore.
3. On the **Resource details** page, a list of recovery points for
   the selected resource ID is shown. To restore a resource, in the **Recovery
   Points** pane, choose the radio button next to the recovery point ID of the
   resource. In the upper-right corner of the pane, choose
   **Restore**.
4. Restore Options
   1. Restore cluster from snapshot, or
   2. Restore single table within a snapshot to new cluster. If you choose this
      options, then you must configure the following:
      1. Toggle on or off case-sensitive names.
      2. Input the source table values, including the database, the schema, and the
         table. The source table information can be found in the [Amazon Redshift console](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
      3. Input the target table values, including the database, the schema, and the
         new table name.

5. Specify your new cluster configuration settings.
   1. For cluster restore: choose Cluster identifier, Node type, and number of
      nodes.
   2. Specify availability zone and maintenance windows.
   3. You can associate additional roles by clicking **Associate IAM
      roles**.

6. _Optional:_ Additional configurations:
   1. **Use defaults** is toggled on by default.
   2. Use the dropdown menus to select settings for Networking and security, VPC
      security groups, Cluster subnet group, and Availability zone.
   3. Toggle **Enhanced VPC routing** on or off.
   4. Determine if you want to make your cluster endpoint **publicly
      accessible**. If it is, instances and devices outside the VPC can
      connect to your database through the cluster endpoint. If this is toggled on,
      input the elastic IP address.

7. _Optional:_ Database configuration. You may choose to input
   1. Database port (by typing into the text field)
   2. Parameter groups

8. Maintenance: You can choose the
   1. Maintenance window
   2. Maintenance track, from among current, trailing, or preview. This controls
      which cluster version is applied during a maintenance window.

9. Automated snapshot is set to default.
   1. Automated snapshot retention period. Retention period must be 0 to 35 days.
      Choose 0 to not create automated snapshots.
   2. The manual snapshot retention period is 1 to 3653 days.
   3. There is an optional checkbox for cluster relocation. If this is checked, it
      permits the ability to relocate your cluster in another Availability Zone. After
      you enable relocation, you can use the VPC endpoint.

10. Monitoring: After a cluster is restored, you can set up monitoring through
    CloudWatch or Amazon Redshift.
11. Choose IAM role to be passed to perform restores. You can use the default role, or
    you can specify a different one.

Your restore jobs will be visible under **Jobs**. You can see the
current status of your restore job by clicking the refresh button or CTRL-R.

## Restore an Amazon Redshift cluster using API, CLI, or SDK

Use [`StartRestoreJob`](API_StartRestoreJob.md "API_StartRestoreJob.md") to restore an Amazon Redshift cluster.

To restore a Amazon Redshift using the AWS CLI, use the command `start-restore-job` and
specify the following metadata:

```
ClusterIdentifier // required string
AdditionalInfo // optional string
AllowVersionUpgrade // optional Boolean
AquaConfigurationStatus // optional string
AutomatedSnapshotRetentionPeriod // optional integer 0 to 35
AvailabilityZone // optional string
AvailabilityZoneRelocation // optional Boolean
ClusterParameterGroupName // optional string
ClusterSecurityGroups // optional array of strings
ClusterSubnetGroupName // optional strings
DefaultIamRoleArn // optional string
ElasticIp // optional string
Encrypted // *Optional* TRUE or FALSE
EnhancedVpcRouting // optional Boolean
HsmClientCertificateIdentifier // optional string
HsmConfigurationIdentifier // optional string
IamRoles // optional array of strings
KmsKeyId // *optional* string
MaintenanceTrackName // optional string
ManageMasterPassword // optional Boolean
ManualSnapshotRetentionPeriod // optional integer
MasterPasswordSecretKmsKeyId // optional string
NodeType // optional string
NumberOfNodes // optional integer
OwnerAccount // optional string
Port // optional integer
PreferredMaintenanceWindow // optional string
PubliclyAccessible // optional Boolean
ReservedNodeId // optional string
SnapshotClusterIdentifier // optional string
SnapshotScheduleIdentifier // optional string
TargetReservedNodeOfferingId // optional string
VpcSecurityGroupIds // optional array of strings
RestoreType // CLUSTER_RESTORE or TABLE_RESTORE or NAMESPACE_RESTORE
```

For more information, see [`RestoreFromClusterSnapshot`](../../../redshift/latest/APIReference/API_RestoreFromClusterSnapshot.md "../../../redshift/latest/APIReference/API_RestoreFromClusterSnapshot.md") in the _Amazon Redshift API
Reference_ and [`restore-from-cluster-snapshot`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift/restore-from-cluster-snapshot.html") in the _AWS CLI
guide_.

Here is an example template:

```
aws backup start-restore-job \
-\-recovery-point-arn "arn:aws:backup:`region`:`account`:snapshot:`name`
-\-iam-role-arn "arn:aws:iam:`account`:role/`role-name`" \
-\-metadata
-\-resource-type Redshift \
-\-region `AWS Region`
-\-endpoint-url `URL`
```

Here is an example:

```
aws backup start-restore-job \
-\-recovery-point-arn "arn:aws:redshift:us-west-2:123456789012:snapshot:redshift-cluster-1/awsbackup:job-c40dda3c-fdcc-b1ba-fa56-234d23209a40" \
-\-iam-role-arn "arn:aws:iam::974288443796:role/Backup-Redshift-Role" \
-\-metadata 'RestoreType=CLUSTER_RESTORE,ClusterIdentifier=redshift-cluster-restore-78,Encrypted=true,KmsKeyId=45e261e4-075a-46c7-9261-dfb91e1c739c' \
-\-resource-type Redshift \
-\-region us-west-2 \
```

You can also use [`DescribeRestoreJob`](API_DescribeRestoreJob.md "API_DescribeRestoreJob.md") to assist with restore information.

In the AWS CLI, use the operation `describe-restore-job` and use the
following metadata:

```
Region
```

Here is an example template:

```
aws backup describe-restore-job —restore-job-id `restore job ID`
-\-region `AWS Region`
```

Here is an example:

```
aws backup describe-restore-job -\-restore-job-id BEA3B353-576C-22C0-9E99-09632F262620 \
-\-region us-west-2 \
```

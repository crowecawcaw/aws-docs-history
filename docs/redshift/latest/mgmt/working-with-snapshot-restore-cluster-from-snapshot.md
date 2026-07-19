Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Restoring a cluster from a snapshot

A snapshot contains data from any databases that are running on your cluster. It also
contains information about your cluster, including the number of nodes, node type, and
admin user name. If you restore your cluster from a snapshot, Amazon Redshift uses the cluster
information to create a new cluster. Then it restores all the databases from the snapshot
data.

###### Note

No-backup tables aren't supported for RG or RA3 provisioned clusters and Amazon Redshift Serverless workgroups.
A table marked as no-backup in an RG or RA3 cluster or serverless workgroup is treated as a permanent table that will
always be backed up while taking a snapshot, and always restored when restoring from a snapshot.

For the new cluster created from the original snapshot, you can choose the
configuration, such as node type and number of nodes. The cluster is restored in the same
AWS Region and a random, system-chosen Availability Zone, unless you specify another
Availability Zone in your request. When you restore a cluster from a snapshot, you can
optionally choose a compatible maintenance track for the new cluster.

###### Note

When you restore a snapshot to a cluster with a different configuration, the snapshot
must have been taken on a cluster with cluster version 1.0.10013, or later.

When a restore is in progress, events are typically emitted in the following
order:

1. RESTORE\_STARTED – REDSHIFT-EVENT-2008 sent when the restore process begins.
2. RESTORE\_SUCCEEDED – REDSHIFT-EVENT-3003 sent when the new cluster has been
   created.

The cluster is available for queries. 3. DATA\_TRANSFER\_COMPLETED – REDSHIFT-EVENT-3537 sent when data transfer
complete.

###### Note

RG and RA3 clusters only emit RESTORE\_STARTED and RESTORE\_SUCCEEDED events. There is no
explicit data transfer to be done after a RESTORE succeeds because RG and RA3 node types store
data in Amazon Redshift managed storage. With RG and RA3 nodes, data is continuously transferred between
RG and RA3 nodes and Amazon Redshift managed storage as part of normal query processing. RG and RA3 nodes cache
hot data locally and keep less frequently queried blocks in Amazon Redshift managed storage
automatically.

You can monitor the progress of a restore by either calling the [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md") API operation, or
viewing the cluster details in the AWS Management Console. For an in-progress restore, these display
information such as the size of the snapshot data, the transfer rate, the elapsed time, and
the estimated time remaining. For a description of these metrics, see [RestoreStatus](../APIReference/API_RestoreStatus.md "../APIReference/API_RestoreStatus.md").

You can't use a snapshot to revert an active cluster to a previous state.

###### Note

When you restore a snapshot into a new cluster, the default security group and
parameter group are used unless you specify different values.

You might want to restore a snapshot to a cluster with a different configuration for
these reasons:

- When a cluster is made up of smaller node types and you want to consolidate it
  into a larger node type with fewer nodes.
- When you have monitored your workload and determined the need to move to a node
  type with more CPU and storage.
- When you want to measure performance of test workloads with different node types.
  Restore has the following constraints:

- The new node configuration must have enough storage for existing data. Even when
  you add nodes, your new configuration might not have enough storage because of the
  way that data is redistributed.
- The restore operation checks if the snapshot was created on a cluster version that
  is compatible with the cluster version of the new cluster. If the new cluster has a
  version level that is too early, then the restore operation fails and reports more
  information in an error message.
- The possible configurations (number of nodes and node type) you can restore to is
  determined by the number of nodes in the original cluster and the target node type of
  the new cluster. To determine the possible configurations available, you can use the
  Amazon Redshift console or the `describe-node-configuration-options` AWS CLI command
  with `action-type restore-cluster`. For more information about the
  restoring using the Amazon Redshift console, see Restoring a cluster from a snapshot.
  The following steps take a cluster with many nodes and consolidate it into a bigger node
  type with a smaller number of nodes using the AWS CLI. For this example, we start with a
  source cluster of 24 nodes. In this case, suppose that we
  already created a snapshot of this cluster and want to restore it into a bigger node
  type.

1. Run the following command to get the details of our 24-node
   cluster.

```
aws redshift describe-clusters --region eu-west-1 --cluster-identifier mycluster-123456789012
```

2. Run the following command to get the details of the snapshot.

```
aws redshift describe-cluster-snapshots --region eu-west-1 --snapshot-identifier mycluster-snapshot
```

3. Run the following command to describe the options available for this snapshot.

```
aws redshift describe-node-configuration-options --snapshot-identifier mycluster-snapshot --region eu-west-1 --action-type restore-cluster
```

This command returns an option list with recommended node types, number of nodes,
and disk utilization for each option. For this example, the preceding command lists
the following possible node configurations. We choose to restore into a four-node
cluster.

```
{
    "NodeConfigurationOptionList": [
        {
            "NodeType": "ra3.16xlarge",
            "NumberOfNodes": 2,
            "EstimatedDiskUtilizationPercent": 0.1
        },
        **{
 "NodeType": "ra3.16xlarge",
 "NumberOfNodes": 4,
 "EstimatedDiskUtilizationPercent": 0.05
 },**
        {
            "NodeType": "ra3.4xlarge",
            "NumberOfNodes": 8,
            "EstimatedDiskUtilizationPercent": 0.03
        },
        {
            "NodeType": "ra3.4xlarge",
            "NumberOfNodes": 10,
            "EstimatedDiskUtilizationPercent": 0.02
        },
        {
            "NodeType": "ra3.4xlarge",
            "NumberOfNodes": 12,
            "EstimatedDiskUtilizationPercent": 0.02
        },
        {
            "NodeType": "ra3.xlplus",
            "NumberOfNodes": 8,
            "EstimatedDiskUtilizationPercent": 0.11
        },
        {
            "NodeType": "ra3.xlplus",
            "NumberOfNodes": 16,
            "EstimatedDiskUtilizationPercent": 0.06
        }
    ]
}
```

4. Run the following command to restore the snapshot into the cluster configuration
   that we chose. After this cluster is restored, we have the same content as the source
   cluster, but the data has been consolidated into four `ra3.16xlarge`
   nodes.

```
aws redshift restore-from-cluster-snapshot --region eu-west-1 --snapshot-identifier mycluster-snapshot --cluster-identifier mycluster-123456789012-x --node-type ra3.16xlarge --number-of-nodes 4
```

If you have reserved nodes, for example
RA3
reserved nodes, you can upgrade to RG reserved nodes. You can do this when you restore
from a snapshot or perform an elastic resize. You can use the console to guide you through
this process. For more information about upgrading to RG nodes, see [Upgrading to RG or RA3 node
types](managing-cluster-considerations.md#rs-upgrading-to-ra3 "managing-cluster-considerations.md#rs-upgrading-to-ra3").

###### To restore a cluster from a snapshot on the console

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   **Snapshots**, then choose the snapshot to restore.
3. Choose **Restore from snapshot** to view the **Cluster
   configuration** and **Cluster details** values of the
   new cluster to be created using the snapshot information.
4. Update the properties of the new cluster, then choose **Restore cluster
   from snapshot**.
   After restoring your cluster snapshot, the restored data warehouse is encrypted with the same custom
   AWS KMS key that it was using at the time that the snapshot was taken. If the snapshot didn't
   have a custom KMS key, Amazon Redshift's backup encryption logic depends on the following factors:

- The type of Amazon Redshift data warehouse you're restoring the snapshot to.
- The encryption type of the cluster at the time the snapshot was taken.
  To learn how your data warehouse is encrypted after you
  restore it from your cluster snapshot, see the following table:

| Destination type     | Snapshot encryption type          | Destination encryption type       |
| -------------------- | --------------------------------- | --------------------------------- |
| Provisioned cluster  | Encrypted with an AWS managed key | Encrypted with an AWS managed key |
| Provisioned cluster  | Encrypted with an AWS owned key   | Encrypted with an AWS owned key   |
| Serverless namespace | Encrypted with an AWS managed key | Encrypted with an AWS owned key   |
| Serverless namespace | Encrypted with an AWS owned key   | Encrypted with an AWS owned key   |

If AWS Secrets Manager managed your cluster's admin password at the time the snapshot was taken,
you must continue using AWS Secrets Manager to manage the admin password. You can opt out of using a
secret after restoring the cluster by updating the cluster's admin credentials in the
cluster detail page.

If you have reserved nodes, you can upgrade to RG reserved nodes. You can do this when
you restore from a snapshot or perform an elastic resize. You can use the console to guide
you through this process. For more information about upgrading to RG nodes, see [Upgrading to RG or RA3 node
types](managing-cluster-considerations.md#rs-upgrading-to-ra3 "managing-cluster-considerations.md#rs-upgrading-to-ra3").

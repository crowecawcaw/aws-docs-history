

# Adding / Removing nodes from a cluster
<a name="clusters.deletenode"></a>

You can add or remove nodes from a cluster using the AWS Management Console, the AWS CLI, or the MemoryDB API.

## Using the AWS Management Console
<a name="clusters.deletenodeclusters.viewdetails"></a>

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/).

1. From the list of clusters, choose the cluster name from which you want to add or remove a node.

1. Under the **Shards and nodes** tab, choose **Add/Delete nodes**

1. In **New number of nodes**, enter the the number of nodes you want. 

1. Choose **Confirm**.
**Important**  
If you set the number of nodes to 1, you will no longer be Multi-AZ enabled. You can also to choose to enable **Auto failover**.

## Using the AWS CLI
<a name="clusters.deletenode.cli"></a>

1. Identify the names of the nodes that you want to remove. For more information, see [Viewing a cluster's details](clusters.viewdetails.md).

1. Use the `update-cluster` CLI operation with a list of the nodes to remove, as in the following example.

   To remove nodes from a cluster using the command-line interface, use the command `update-cluster` with the following parameters:
   + `--cluster-name` The ID of the cluster that you want to remove nodes from.
   + `--replica-configuration` – Allows you to set the number of replicas:
     + `ReplicaCount` – Set this property to specify the number of replica nodes you want. 
   + `--region` Specifies the AWS Region of the cluster that you want to remove nodes from.

   For Linux, macOS, or Unix:

   ```
   aws memorydb update-cluster \
       --cluster-name {{my-cluster}} \
       --replica-configuration \
           ReplicaCount={{1}} \
       --region {{us-east-1}}
   ```

   For Windows:

   ```
   aws memorydb update-cluster ^
       --cluster-name {{my-cluster}} ^
       --replica-configuration ^
           ReplicaCount={{1}} ^
       --region {{us-east-1}}
   ```

For more information, see the AWS CLI topics [`update-cluster`](https://docs.aws.amazon.com/cli/latest/reference/memorydb/update-cluster.html).

## Using the MemoryDB API
<a name="clusters.deletenode.api"></a>

To remove nodes using the MemoryDB API, call the `UpdateCluster` API operation with the cluster name and a list of nodes to remove, as shown:
+ `ClusterName` The ID of the cluster that you want to remove nodes from.
+ `ReplicaConfiguration` – Allows you to set the number of replicas:
  + `ReplicaCount` – Set this property to specify the number of replica nodes you want. 
+ `Region` Specifies the AWS Region of the cluster that you want to remove a node from.

For more information, see [UpdateCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_UpdateCluster.html).
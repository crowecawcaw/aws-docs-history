# Aurora DSQL cluster lifecycle

Understanding the Aurora DSQL cluster lifecycle helps you manage your clusters effectively. This section covers cluster status definitions and the scale to zero feature that optimizes costs.

## Defining Aurora DSQL cluster status

The Aurora DSQL cluster status provides critical information about cluster health and
connectivity. You can view the status of clusters and cluster instances by using the AWS Management Console,
AWS CLI, or Aurora DSQL API.

The following table describes each possible status for a Aurora DSQL cluster and what each
status means.

| Status             | Description                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Creating**       | Aurora DSQL is attempting to create or configure resources for the cluster. Any<br>connection attempts will fail while a cluster is in this state.                                                                                                                                                                                                                                                      |
| **Active**         | The cluster is operational and ready to use.                                                                                                                                                                                                                                                                                                                                                            |
| **Idle**           | A cluster becomes idle when it's idle long enough for Aurora DSQL to scale down<br>running resources to reduce capacity and costs. When you connect to an idle cluster,<br>Aurora DSQL transitions the cluster back to the \*_Active_<br>• state.                                                                                                                                                       |
| **Inactive**       | An Idle cluster becomes Inactive when there's been no activity on the cluster for a<br>prolonged period. In this suspended state, running resources are scaled to zero while<br>your data is preserved. When you attempt to connect to an inactive cluster, Aurora DSQL<br>automatically transitions the cluster back to the \*_Active_<br>• state.<br>The time to restore depends on the cluster size. |
| **Updating**       | A cluster transitions to the \*_Updating_<br>• status when you make<br>changes to the cluster configuration.                                                                                                                                                                                                                                                                                            |
| **Deleting**       | A cluster transitions to the \*_Deleting_<br>• status when you submit<br>a request to delete it.                                                                                                                                                                                                                                                                                                        |
| **Deleted**        | The cluster has been successfully deleted.                                                                                                                                                                                                                                                                                                                                                              |
| **Failed**         | Aurora DSQL couldn't create the cluster because it encountered an error.                                                                                                                                                                                                                                                                                                                                |
| **Pending Setup**  | For multi-Region clusters only. A multi-Region cluster enters the<br>\*_Pending Setup_<br>• status when you create a multi-Region cluster in<br>your first Region with a witness Region. Cluster creation pauses until you create<br>another cluster in a secondary Region and peer the two clusters together.                                                                                          |
| **Pending Delete** | For multi-Region clusters only. A multi-Region cluster enters the<br>**Pending Delete\*<br>• status when you delete a cluster from it. The<br>cluster moves to the **Deleting\*<br>• state after you delete the last peer<br>cluster.                                                                                                                                                                   |

### Working with Idle and Inactive clusters

When Aurora DSQL detects no connection activity on a cluster for some period of time, it transitions
the cluster to the **Idle** state, reducing running resources to minimize capacity and costs. If
connection activity remains absent for a prolonged period, the **Idle** cluster automatically
transitions to the **Inactive** state, where running resources are scaled to zero while your data
is preserved.

To resume normal operations, simply connect to the cluster as usual.
When you successfully connect to the cluster, Aurora Aurora DSQL automatically transitions the cluster to Active state.

###### Note

The first connection attempt to an **Idle** or **Inactive** cluster will be
slower than usual.

#### Operations requiring Active cluster state

Some operations require your cluster to be in an Active state. To perform these
operations on an **Idle** or **Inactive** cluster,
you need to transition your cluster back to Active by connecting to your cluster.

###### Backup operations

Taking a backup requires an Active cluster state. If your cluster is **Idle** or **Inactive**,
backups fail with the following error:

```
"Error": {
    "Code": "FailedPrecondition",
    "Message": "Cluster 'cluster-id' is in state 'IDLE' and can't be backed up.
    In order to take a backup of your cluster, it must be in Active state. Please
    connect to your cluster to transition it to Active to perform the backup."
}
```

To proceed with a backup:

1. Connect to the cluster using your preferred database client or the Aurora DSQL console to wake it up.
2. Wait for automatic transition to **Active** state.
3. Initiate the backup after the cluster is fully operational.

###### Note

Existing backups taken before the cluster was Idle or Inactive remain valid and unaffected. New backup attempts on the cluster will fail until the cluster is connected to for auto wake up.

## Viewing your Aurora DSQL cluster status

To view the status of your cluster, use the AWS Management Console, AWS CLI, or Aurora DSQL API.

Follow these steps to view cluster status in the AWS Management Console:

###### To view cluster status in the console

1. Open the Aurora DSQL console at [https://console.aws.amazon.com/dsql](https://console.aws.amazon.com/dsql "https://console.aws.amazon.com/dsql").
2. Choose **Clusters** in the navigation pane.
3. View the status for each cluster in the dashboard.
   Use the following AWS CLI command to check the status of a single cluster.

```
aws dsql get-cluster --identifier `cluster-id` --query status --output text
```

Run the following command to list the status of all clusters.

```
for id in $(aws dsql list-clusters --query 'clusters[*].identifier' --output text); do
  cluster_status=$(aws dsql get-cluster --identifier "$id" --query 'status' --output text)
  echo "$id    $cluster_status"
done
```

This sample output shows two active clusters and one cluster in the process of being
deleted.

```
aaabbb2bkx555xa7p42qd5cdef    ACTIVE
abcde123efghi77t35abcdefgh    ACTIVE
12abc6lqasc5bbbbbbbbbbbbbb    DELETING
```

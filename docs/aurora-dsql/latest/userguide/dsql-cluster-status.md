# Viewing Aurora DSQL cluster status

The Aurora DSQL cluster status provides critical information about cluster health and
connectivity. You can view the status of clusters and cluster instances by using the AWS Management Console,
AWS CLI, or Aurora DSQL API.

## Aurora DSQL cluster statuses and definitions

The following table describes each possible status for a Aurora DSQL cluster and what each
status means.

| Status             | Description                                                                                                                                                                                                                                                                                                    |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Creating**       | Aurora DSQL is attempting to create or configure resources for the cluster. Any<br>connection attempts will fail while a cluster is in this state.                                                                                                                                                             |
| **Active**         | The cluster is operational and ready to use.                                                                                                                                                                                                                                                                   |
| **Idle**           | A cluster becomes idle when it's idle long enough for Aurora DSQL to reclaim the<br>resources configured for it. When you connect to an idle cluster, Aurora DSQL transitions<br>the cluster back to the \*_Active_<br>• state.                                                                                |
| **Inactive**       | A cluster becomes inactive when there's been no activity on the cluster for a<br>prolonged period. When you attempt to connect to an inactive cluster, Aurora DSQL<br>automatically transitions the cluster back to the **Active**<br>state.                                                                   |
| **Updating**       | A cluster transitions to the \*_Updating_<br>• status when you make<br>changes to the cluster configuration.                                                                                                                                                                                                   |
| **Deleting**       | A cluster transitions to the \*_Deleting_<br>• status when you submit<br>a request to delete it.                                                                                                                                                                                                               |
| **Deleted**        | The cluster has been successfully deleted.                                                                                                                                                                                                                                                                     |
| **Failed**         | Aurora DSQL could not create the cluster because it encountered an error.                                                                                                                                                                                                                                      |
| **Pending Setup**  | For multi-Region clusters only. A multi-Region cluster enters the<br>\*_Pending Setup_<br>• status when you create a multi-Region cluster in<br>your first Region with a witness Region. Cluster creation pauses until you create<br>another cluster in a secondary Region and peer the two clusters together. |
| **Pending Delete** | For multi-Region clusters only. A multi-Region cluster enters the<br>**Pending Delete\*<br>• status when you delete a cluster from it. The<br>cluster moves to the **Deleting\*<br>• state once you delete the last peer<br>cluster.                                                                           |

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

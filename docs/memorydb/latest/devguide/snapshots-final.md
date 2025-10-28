# Creating a final snapshot

You can create a final snapshot using the MemoryDB console, the AWS CLI, or the MemoryDB API.

You can create a final snapshot when you delete a MemoryDB cluster using the MemoryDB console.

To create a final snapshot when deleting a MemoryDB cluster, on the delete page, choose **Yes** and give the snapshot a name at [Step 5: Deleting a cluster](getting-started.md#clusters.delete "getting-started.md#clusters.delete").

You can create a final snapshot when deleting a MemoryDB cluster using the AWS CLI.

### When deleting a MemoryDB cluster

To create a final snapshot when deleting a cluster, use the
`delete-cluster` AWS CLI operation, with the following
parameters:

- `--cluster-name` – Name of the cluster being deleted.
- `--final-snapshot-name` – Name of the final snapshot.

The following code takes the final snapshot `bkup-20210515-final` when deleting the
cluster `myCluster`.

For Linux, macOS, or Unix:

```
aws memorydb delete-cluster \
        --cluster-name `myCluster` \
        --final-snapshot-name `bkup-20210515-final`
```

For Windows:

```
aws memorydb delete-cluster ^
        --cluster-name `myCluster` ^
        --final-snapshot-name `bkup-20210515-final`
```

For more information, see [delete-cluster](../../../cli/latest/reference/memorydb/delete-cluster.md "../../../cli/latest/reference/memorydb/delete-cluster.md") in the _AWS CLI Command Reference_.

You can create a final snapshot when deleting a MemoryDB cluster using the MemoryDB API.

### When deleting a MemoryDB cluster

To create a final snapshot, use the `DeleteCluster` MemoryDB API operation with
the following parameters.

- `ClusterName` – Name of the cluster being deleted.
- `FinalSnapshotName` – Name of the snapshot.

The following MemoryDB API operation creates the snapshot `bkup-20210515-final` when deleting the
cluster `myCluster`.

```
https://memory-db.us-east-1.amazonaws.com/
    ?Action=DeleteCluster
    &ClusterName=myCluster
    &FinalSnapshotName=bkup-20210515-final
    &Version=2021-01-01
    &SignatureVersion=4
    &SignatureMethod=HmacSHA256
    &Timestamp=20210515T192317Z
    &X-Amz-Credential=<credential>
```

For more information, see [DeleteCluster](../APIReference/API_DeleteCluster.md "../APIReference/API_DeleteCluster.md").

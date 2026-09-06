

# Creating a final snapshot
<a name="snapshots-final"></a>

You can create a final snapshot using the MemoryDB console, the AWS CLI, or the MemoryDB API.

## Creating a final snapshot (Console)
<a name="snapshots-final-CON"></a>

You can create a final snapshot when you delete a MemoryDB cluster using the MemoryDB console.

To create a final snapshot when deleting a MemoryDB cluster, on the delete page, choose **Yes** and give the snapshot a name at [Step 5: Deleting a cluster](getting-started.md#clusters.delete).

## Creating a final snapshot (AWS CLI)
<a name="snapshots-final-CLI"></a>

You can create a final snapshot when deleting a MemoryDB cluster using the AWS CLI.

### When deleting a MemoryDB cluster
<a name="w2ab1c18c23c29b7b1b5"></a>

To create a final snapshot when deleting a cluster, use the `delete-cluster` AWS CLI operation, with the following parameters:
+ `--cluster-name` – Name of the cluster being deleted.
+ `--final-snapshot-name` – Name of the final snapshot.

The following code takes the final snapshot `bkup-20210515-final` when deleting the cluster `myCluster`.

For Linux, macOS, or Unix:

```
aws memorydb delete-cluster \
        --cluster-name {{myCluster}} \
        --final-snapshot-name {{bkup-20210515-final}}
```

For Windows:

```
aws memorydb delete-cluster ^
        --cluster-name {{myCluster}} ^
        --final-snapshot-name {{bkup-20210515-final}}
```

For more information, see [delete-cluster](https://docs.aws.amazon.com/cli/latest/reference/memorydb/delete-cluster.html) in the *AWS CLI Command Reference*.

## Creating a final snapshot (MemoryDB API)
<a name="snapshots-final-API"></a>

You can create a final snapshot when deleting a MemoryDB cluster using the MemoryDB API.

### When deleting a MemoryDB cluster
<a name="snapshots-final-API-cluster"></a>

To create a final snapshot, use the `DeleteCluster` MemoryDB API operation with the following parameters.
+ `ClusterName` – Name of the cluster being deleted.
+ `FinalSnapshotName` – Name of the snapshot.

The following MemoryDB API operation creates the snapshot `bkup-20210515-final` when deleting the cluster `myCluster`.

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

For more information, see [DeleteCluster](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DeleteCluster.html).
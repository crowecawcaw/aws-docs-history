# Making manual snapshots

In addition to automatic snapshots, you can create a _manual_ snapshot
at any time. Unlike automatic snapshots, which are automatically deleted after a specified
retention period, manual snapshots do not have a retention period after which they are
automatically deleted. You must manually delete any manual snapshot. Even if you delete a
cluster or node, any manual snapshots from that cluster or node are retained. If you no
longer want to keep a manual snapshot, you must explicitly delete it yourself.

Manual snapshots are useful for testing and archiving. For example, suppose that you've
developed a set of baseline data for testing purposes. You can create a manual snapshot of
the data and restore it whenever you want. After you test an application that modifies
the data, you can reset the data by creating a new cluster and restoring from your
baseline snapshot. When the cluster is ready, you can test your applications against the
baseline data again—and repeat this process as often as needed.

In addition to directly creating a manual snapshot,
you can create a manual snapshot in one of the following ways:

- [Copying a snapshot](snapshots-copying.md "snapshots-copying.md") – It does not matter whether the source
  snapshot was created automatically or manually.
- [Creating a final snapshot](snapshots-final.md "snapshots-final.md") – Create a snapshot immediately before deleting a cluster.

###### Other topics of importance

- [Snapshot constraints](snapshots-constraints.md "snapshots-constraints.md")
- [Snapshot costs](snapshots-costs.md "snapshots-costs.md")
  You can create a manual snapshot of a node using the AWS Management Console, the AWS CLI, or the MemoryDB API.

###### To create a snapshot of a cluster (console)

1. Sign in to the AWS Management Console and open the MemoryDB console at [https://console.aws.amazon.com/memorydb/](https://console.aws.amazon.com/memorydb/ "https://console.aws.amazon.com/memorydb/").
2. from the left navigation pane, choose **Clusters**.

The MemoryDB clusters screen appears. 3. choose the radio button to the left of the name of the MemoryDB cluster you want
to back up. 4. Choose **Actions** and then **Take snapshot**. 5. In the **Snapshot** window, type in a name for your
snapshot in the **Snapshot Name** box. We recommend that the
name indicate which cluster was backed up and the date and time the snapshot
was made.

Cluster naming constraints are as follows:

    * Must contain 1–40 alphanumeric characters or hyphens.
    * Must begin with a letter.
    * Can't contain two consecutive hyphens.
    * Can't end with a hyphen.

6. Under **Encryption**, choose whether to use a default encryption key or a customer managed key. For more information, see
   [In-transit encryption (TLS) in MemoryDB](in-transit-encryption.md "in-transit-encryption.md").
7. Under **Tags**, optionally add tags to search and filter your snapshots or track your AWS costs.
8. Choose **Take snapshot**.

The status of the cluster changes to _snapshotting_.
When the status returns to _available_ the snapshot is complete.
To create a manual snapshot of a cluster using the AWS CLI, use the
`create-snapshot` AWS CLI operation with the following parameters:

- `--cluster-name` – Name of the MemoryDB
  cluster to use as the source for the snapshot.
  Use this parameter when backing up a MemoryDB cluster.

Cluster naming constraints are as follows:

    + Must contain 1–40 alphanumeric characters or hyphens.
    + Must begin with a letter.
    + Can't contain two consecutive hyphens.
    + Can't end with a hyphen.

- `--snapshot-name` – Name of the snapshot to be
  created.

### Related topics

For more information, see `create-snapshot` in the _AWS CLI Command Reference_.

To create a manual snapshot of a cluster using the MemoryDB API, use the
`CreateSnapshot` MemoryDB API operation with the following parameters:

- `ClusterName` – Name of the MemoryDB
  cluster to use as the source for the snapshot.
  Use this parameter when backing up a MemoryDB cluster.

 

Cluster naming constraints are as follows:

    + Must contain 1–40 alphanumeric characters or hyphens.
    + Must begin with a letter.
    + Can't contain two consecutive hyphens.
    + Can't end with a hyphen.

- `SnapshotName` – Name of the snapshot to be
  created.

### Related topics

For more information, see [CreateSnapshot](../APIReference/API_CreateSnapshot.md "../APIReference/API_CreateSnapshot.md").

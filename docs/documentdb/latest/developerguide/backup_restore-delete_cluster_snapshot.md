# Deleting a cluster snapshot

A manual snapshot is a full backup that is deleted only when you
manually delete it using the AWS Management Console or AWS CLI. You cannot manually
delete an automatic snapshot because automatic snapshots are deleted
only when the snapshot's retention period expires or you delete the
snapshot's cluster.

Using the AWS Management Console
To delete a manual cluster snapshot using the AWS Management Console, complete
the following steps.

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Snapshots**.

###### Tip

If you don't see the navigation pane on the left side of your screen, choose the menu icon
(![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
in the upper-left corner of the page. 3. In the list of snapshots, choose the button to the left of
the snapshot that you want to delete. The snapshot's type must
be **manual**.

    1. You can verify that that the snapshot's type is
     **manual** by checking if it is listed
     as `manual` or `automatic` under
     the **Type** column.

4. From the **Actions** menu, choose
   **Delete**. If the **Delete**
   option is unavailable, you probably chose an automatic snapshot.
5. On the delete confirmation screen, to delete the snapshot,
   choose **Delete**. To keep the snapshot,
   choose **Cancel**.

Using the AWS CLI
An Amazon DocumentDB manual cluster snapshot is a full backup that you can
manually delete using the AWS CLI. You cannot manually delete an
automatic snapshot.

To delete a manual cluster snapshot using the AWS CLI, use the
`delete-db-cluster-snapshot` operation with the following
parameters.

###### Parameters

- `--db-cluster-snapshot-identifier`
  — Required. The name of the manual snapshot to delete.

The following example deletes the cluster snapshot
`sample-cluster-snapshot`.

For Linux, macOS, or Unix:

```
aws docdb delete-db-cluster-snapshot \
    --db-cluster-snapshot-identifier sample-cluster-snapshot
```

For Windows:

```
aws docdb delete-db-cluster-snapshot ^
    --db-cluster-snapshot-identifier sample-cluster-snapshot
```

Output from this operation lists the details of the cluster
snapshot you deleted.

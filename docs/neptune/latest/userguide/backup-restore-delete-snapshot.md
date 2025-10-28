# Deleting a Neptune Snapshot

You can delete a DB snapshot using the AWS Management Console, the AWS CLI, or the Neptune management API:

## Deleting Using the Console

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home "https://console.aws.amazon.com/neptune/home").
2. In the navigation pane, choose **Snapshots**.
3. Choose the DB snapshot that you want to delete.
4. For **Actions**, choose **Delete Snapshot**.
5. Choose **Delete** on the confirmation page.

## Deleting Using the AWS CLI

You can also delete a DB snapshot using the AWS CLI
[delete_db_cluster_snapshot](api-snapshots.md#DeleteDBClusterSnapshot "api-snapshots.md#DeleteDBClusterSnapshot") command,
using the `--db-snapshot-identifier` parameter to identify the snapshot
you want to delete:

For Linux, OS X, or Unix:

```
aws neptune delete-db-cluster-snapshot \
    --db-snapshot-identifier `<name-of-the-snapshot-to-delete>`
```

For Windows:

```
aws neptune delete-db-cluster-snapshot ^
    --db-snapshot-identifier `<name-of-the-snapshot-to-delete>`
```

## Deleting Using the Neptune Management API

You can use one of the SDKs to delete a DB snapshot by calling the [DeleteDBClusterSnapshot](api-snapshots.md#DeleteDBClusterSnapshot "api-snapshots.md#DeleteDBClusterSnapshot") API and use the `DBSnapshotIdentifier`
parameters to identify the DB snapshot to be deleted.

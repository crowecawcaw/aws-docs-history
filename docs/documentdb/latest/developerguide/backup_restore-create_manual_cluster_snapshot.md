# Creating a manual cluster snapshot

You can create a manual snapshot using either the AWS Management Console or
AWS CLI. The amount of time it takes to create a snapshot varies with the
size of your databases. When you create a snapshot, you must do the
following:

1. Identify which cluster to back up.
2. Give your snapshot a name. This allows you to restore from it
   later.

Using the AWS Management Console
To create a manual snapshot using the AWS Management Console, you can follow
either method below.

1.  **Method 1:**
    1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
    2. In the navigation pane, choose
       **Snapshots**.

    ###### Tip

    If you don't see the navigation pane on the left side of your screen, choose the menu icon
    (![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
    in the upper-left corner of the page. 3. On the **Snapshots** page, choose
    **Create**. 4. On the **Create cluster snapshot**
    page:

        1. **Cluster identifier**
         — From the drop-down list of clusters,
         choose the cluster that you want to create a
         snapshot of.
        2. **Snapshot identifier**
         — Enter a name for your snapshot.


        Snapshot naming constraints:




        	* Length is [1–255] letters, numbers,
        	 or hyphens.
        	* First character must be a letter.
        	* Cannot end with a hyphen or contain two
        	 consecutive hyphens.
        	* Must be unique for all clusters (across
        	 Amazon RDS, Amazon Neptune, and Amazon DocumentDB) per AWS
        	 account, per Region.
        3. Choose **Create**.

2.  **Method 2:**
    1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
    2. In the navigation pane, choose
       **Clusters**.

    ###### Tip

    If you don't see the navigation pane on the left side of your screen, choose the menu icon
    (![Hamburger menu icon with three horizontal lines.](images/docdb-menu-icon.png))
    in the upper-left corner of the page. 3. On the **Clusters** page, choose the
    button to the left of the cluster that you want to
    snapshot. 4. From the **Actions** menu, choose
    **Take snapshot**. 5. On the **Create cluster snapshot**
    page:

        1. **Snapshot identifier**
         — Enter a name for your snapshot.


        Snapshot naming constraints:




        	* Length is [1–63] letters, numbers,
        	 or hyphens.
        	* First character must be a letter.
        	* Cannot end with a hyphen or contain two
        	 consecutive hyphens.
        	* Must be unique for all clusters (across
        	 Amazon RDS, Amazon Neptune, and Amazon DocumentDB) per AWS
        	 account, per Region.
        2. Choose **Create**.

Using the AWS CLI
To create a cluster snapshot using the AWS CLI, use the
`create-db-cluster-snapshot` operation with the following
parameters.

###### Parameters

- `--db-cluster-identifier`
  — Required. The name of the cluster that you are taking a snapshot of. This cluster must exist and be _available_.
- `--db-cluster-snapshot-identifier` — Required. The name of the manual snapshot that you are creating.

The following example creates a snapshot named
`sample-cluster-snapshot` for a cluster named
`sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb create-db-cluster-snapshot \
    --db-cluster-identifier sample-cluster \
    --db-cluster-snapshot-identifier sample-cluster-snapshot
```

For Windows:

```
aws docdb create-db-cluster-snapshot ^
    --db-cluster-identifier sample-cluster ^
    --db-cluster-snapshot-identifier sample-cluster-snapshot
```

Output from this operation looks something like the following.

```
{
    "DBClusterSnapshot": {
        "AvailabilityZones": [
            "us-east-1a",
            "us-east-1b",
            "us-east-1c"
        ],
        "DBClusterSnapshotIdentifier": "sample-cluster-snapshot",
        "DBClusterIdentifier": "sample-cluster",
        "SnapshotCreateTime": "2020-04-24T04:59:08.475Z",
        "Engine": "docdb",
        "Status": "creating",
        "Port": 0,
        "VpcId": "vpc-abc0123",
        "ClusterCreateTime": "2020-01-10T22:13:38.261Z",
        "MasterUsername": "master-user",
        "EngineVersion": "4.0.0",
        "SnapshotType": "manual",
        "PercentProgress": 0,
        "StorageEncrypted": true,
        "KmsKeyId": "arn:aws:kms:us-east-1:<accountID>:key/sample-key",
        "DBClusterSnapshotArn": "arn:aws:rds:us-east-1:<accountID>:cluster-snapshot:sample-cluster-snapshot"
    }
}
```

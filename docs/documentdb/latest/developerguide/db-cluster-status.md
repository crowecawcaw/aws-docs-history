# Determining a cluster's status

You can determine a cluster's status using the AWS Management Console or AWS CLI.

Using the AWS Management Console
Use the following procedure to see the status of your Amazon DocumentDB
cluster using the AWS Management Console

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. In the navigation pane, choose **Clusters**.
3. In the **Cluster identifier** column, find
   the name of the cluster that you are interested in. Then, to
   find the status of the cluster, read across that row to the
   **Status** column, as shown below.

![Screenshot of clusters page with sample-cluster showing active status.](images/db-cluster-status-con.png)

Using the AWS CLI
Use the `describe-db-clusters` operation to see the
the status of your Amazon DocumentDB cluster using the AWS CLI.

The following code finds the status of the cluster
`sample-cluster`.

For Linux, macOS, or Unix:

```
aws docdb describe-db-clusters \
    --db-cluster-identifier sample-cluster  \
    --query 'DBClusters[*].[DBClusterIdentifier,Status]'
```

For Windows:

```
aws docdb describe-db-clusters ^
    --db-cluster-identifier sample-cluster  ^
    --query 'DBClusters[*].[DBClusterIdentifier,Status]'
```

Output from this operation looks something like the following (JSON format).

```
[
    [
        "sample-cluster",
        "available"
    ]
]
```

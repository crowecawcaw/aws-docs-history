# Getting the status of a database activity stream

You can get the status of an activity stream using the console or AWS CLI.

###### To get the status of a database activity stream

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB cluster link.
3. Choose the **Configuration** tab, and check **Database activity stream**
   for status.
   You can get the activity stream configuration for a DB cluster as the response to a [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md")
   CLI
   request.

The following example describes `my-cluster`.

```
aws rds --region `my-region` describe-db-clusters --db-cluster-identifier `my-cluster`
```

The following example shows a JSON response. The following fields are shown:

- `ActivityStreamKinesisStreamName`
- `ActivityStreamKmsKeyId`
- `ActivityStreamStatus`
- `ActivityStreamMode`
- These fields are the same for Aurora PostgreSQL and Aurora MySQL, except that `ActivityStreamMode` is
  always `async` for Aurora MySQL, while for Aurora PostgreSQL it might be `sync` or `async`.

```
{
    "DBClusters": [
        {
      "DBClusterIdentifier": "`my-cluster`",
            ...
            "ActivityStreamKinesisStreamName": "aws-rds-das-cluster-A6TSYXITZCZXJHIRVFUBZ5LTWY",
            "ActivityStreamStatus": "starting",
            "ActivityStreamKmsKeyId": "12345678-abcd-efgh-ijkl-bd041f170262",
            "ActivityStreamMode": "async",
            "DbClusterResourceId": "cluster-ABCD123456"
            ...
        }
    ]
}
```

You can get the activity stream configuration for a DB cluster as the response to a [DescribeDBClusters](../APIReference/API_DescribeDBClusters.md "../APIReference/API_DescribeDBClusters.md")
operation.

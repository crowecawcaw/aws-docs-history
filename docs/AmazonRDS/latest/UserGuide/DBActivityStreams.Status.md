# Getting the status of a database activity stream

You can get the status of an activity stream for your Amazon RDS
database instance using the console or AWS CLI.

###### To get the status of a database activity stream

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the DB instance link.
3. Choose the **Configuration** tab, and check **Database activity stream**
   for status.
   You can get the activity stream configuration for a
   database instance as the response to a
   [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") CLI
   request.

The following example describes `my-instance`.

```
aws rds --region `my-region` describe-db-instances --db-instance-identifier `my-db`
```

The following example shows a JSON response. The following fields are shown:

- `ActivityStreamKinesisStreamName`
- `ActivityStreamKmsKeyId`
- `ActivityStreamStatus`
- `ActivityStreamMode`
- `ActivityStreamPolicyStatus`

```
{
    "DBInstances": [
        {
            ...
            "Engine": "oracle-ee",
            ...
            "ActivityStreamStatus": "starting",
            "ActivityStreamKmsKeyId": "ab12345e-1111-2bc3-12a3-ab1cd12345e",
            "ActivityStreamKinesisStreamName": "aws-rds-das-db-AB1CDEFG23GHIJK4LMNOPQRST",
            "ActivityStreamMode": "async",
            "ActivityStreamEngineNativeAuditFieldsIncluded": true,
            "ActivityStreamPolicyStatus": locked",
            ...
        }
    ]
}
```

You can get the activity stream configuration for a database as the response to a
[DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md") operation.

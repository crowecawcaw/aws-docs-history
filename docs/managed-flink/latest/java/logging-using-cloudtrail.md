

# Log Managed Service for Apache Flink API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Managed Service for Apache Flink is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Managed Service for Apache Flink. CloudTrail captures all API calls for Managed Service for Apache Flink as events. The calls captured include calls from the Managed Service for Apache Flink console and code calls to the Managed Service for Apache Flink API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Managed Service for Apache Flink. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Managed Service for Apache Flink, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## Managed Service for Apache Flink information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Managed Service for Apache Flink, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for Managed Service for Apache Flink, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail Supported Services and Integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations)
+ [Configuring Amazon SNS Notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html)
+ [Receiving CloudTrail Log Files from Multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail Log Files from Multiple Accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

All Managed Service for Apache Flink actions are logged by CloudTrail and are documented in the [Managed Service for Apache Flink API reference](/managed-flink/latest/apiv2/Welcome.html). For example, calls to the `[CreateApplication](/managed-flink/latest/apiv2/API_CreateApplication.html)` and ` [UpdateApplication](/managed-flink/latest/apiv2/API_UpdateApplication.html)` actions generate entries in the CloudTrail log files. 

CloudTrail also logs the following enhanced snapshot API actions:
+ [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html)
+ [`DescribeSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshot.html)
+ [`ListSnapshots`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshots.html)
+ [`DeleteSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteSnapshot.html)
+ [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html)
+ [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html)
+ [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html)
+ [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity Element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understand Managed Service for Apache Flink log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the [AddApplicationCloudWatchLoggingOption](/managed-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html) and [DescribeApplication](/managed-flink/latest/apiv2/API_DescribeApplication.html) actions.

```
{
    "Records": [
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:user/MaryMajor",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "MaryMajor"
            },
            "eventTime": "2019-03-07T01:19:47Z",
            "eventSource": "kinesisanalytics.amazonaws.com",
            "eventName": "AddApplicationCloudWatchLoggingOption",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "{{source-ip-address}}",
            "userAgent": "aws-sdk-java/unknown-version Linux/x.xx",
            "requestParameters": {
                "applicationName": "cloudtrail-test",
                "currentApplicationVersionId": 1,
                "cloudWatchLoggingOption": {
                    "logStreamARN": "arn:aws:logs:us-east-1:111122223333:log-group:cloudtrail-test:log-stream:flink-cloudwatch"
                }
            },
            "responseElements": {
                "cloudWatchLoggingOptionDescriptions": [
                    {
                        "cloudWatchLoggingOptionId": "2.1",
                        "logStreamARN": "arn:aws:logs:us-east-1:111122223333:log-group:cloudtrail-test:log-stream:flink-cloudwatch"
                    }
                ],
                "applicationVersionId": 2,
                "applicationARN": "arn:aws:kinesisanalytics:us-east-1:111122223333:application/cloudtrail-test"
            },
            "requestID": "18dfb315-4077-11e9-afd3-67f7af21e34f",
            "eventID": "d3c9e467-db1d-4cab-a628-c21258385124",
            "eventType": "AwsApiCall",
            "apiVersion": "2018-05-23",
            "recipientAccountId": "111122223333"
        },
        {
            "eventVersion": "1.05",
            "userIdentity": {
                "type": "IAMUser",
                "principalId": "EX_PRINCIPAL_ID",
                "arn": "arn:aws:iam::111122223333:user/MaryMajor",
                "accountId": "111122223333",
                "accessKeyId": "EXAMPLE_KEY_ID",
                "userName": "MaryMajor"
            },
            "eventTime": "2019-03-12T02:40:48Z",
            "eventSource": "kinesisanalytics.amazonaws.com",
            "eventName": "DescribeApplication",
            "awsRegion": "us-east-1",
            "sourceIPAddress": "{{source-ip-address}}",
            "userAgent": "aws-sdk-java/unknown-version Linux/x.xx",
            "requestParameters": {
                "applicationName": "sample-app"
            },
            "responseElements": null,
            "requestID": "3e82dc3e-4470-11e9-9d01-e789c4e9a3ca",
            "eventID": "90ffe8e4-9e47-48c9-84e1-4f2d427d98a5",
            "eventType": "AwsApiCall",
            "apiVersion": "2018-05-23",
            "recipientAccountId": "111122223333"
        }
    ]
}
```

The following example shows a CloudTrail log entry for the [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) action. The `resources` field lists the ARN of the application and the ARN of the enhanced snapshot.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::111122223333:user/MaryMajor",
        "accountId": "111122223333",
        "userName": "MaryMajor"
    },
    "eventTime": "2026-10-01T12:00:00Z",
    "eventSource": "kinesisanalytics.amazonaws.com",
    "eventName": "CreateSnapshot",
    "awsRegion": "aa-example-1",
    "sourceIPAddress": "{{source-ip-address}}",
    "userAgent": "aws-cli/2.0.0",
    "requestParameters": {
        "applicationName": "MyApplication",
        "snapshotName": "MyApplication-snapshot-1"
    },
    "responseElements": {
        "snapshotArn": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1",
        "snapshotStatus": "CREATING",
        "snapshotOperationId": "a1B2c3D4e5F6",
        "snapshotOperationStatus": "IN_PROGRESS"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
    "readOnly": false,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KinesisAnalyticsV2::Application",
            "ARN": "arn:aws:kinesisanalytics:aa-example-1:111122223333:application/MyApplication"
        },
        {
            "accountId": "111122223333",
            "type": "AWS::KinesisAnalyticsV2::Snapshot",
            "ARN": "arn:aws:kinesisanalytics:aa-example-1:111122223333:snapshot/MyApplication-snapshot-1"
        }
    ],
    "eventType": "AwsApiCall",
    "apiVersion": "2018-05-23",
    "recipientAccountId": "111122223333"
}
```

The following rules apply to CloudTrail events for enhanced snapshot actions:
+ CloudTrail logs all enhanced snapshot actions as management events, which are control plane API calls.
+ For `DescribeSnapshot`, `ListSnapshots`, `DescribeSnapshotOperation`, and `ListSnapshotOperations`, `responseElements` is null.
+ `ListSnapshots` events have no `resources` field. For the other enhanced snapshot actions, `resources` lists the ARN of the enhanced snapshot. For `CreateSnapshot`, `resources` also lists the ARN of the application.
+ CloudTrail logs the full request parameters. Do not put sensitive data in the snapshot description or in tags.

## Audit enhanced snapshot operations across an account
<a name="logging-using-cloudtrail-audit-snapshot-operations"></a>

Use CloudTrail and the enhanced snapshot operation records together to audit enhanced snapshot activity:
+ **CloudTrail**: CloudTrail keeps the account-level history of the enhanced snapshot API calls. Each event shows the caller, the time, and the request.
+ **Operation records**: [`DescribeSnapshotOperation`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DescribeSnapshotOperation.html) and [`ListSnapshotOperations`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ListSnapshotOperations.html) return the record of each operation for 90 days after the operation ends.

Managed Service for Apache Flink creates a system snapshot without an API call from you. A system snapshot does not create a CloudTrail event of its own. CloudTrail logs only the `UpdateApplication` or `StopApplication` call that starts the system snapshot. In enhanced snapshot mode, to trace a system snapshot that succeeded, call `ListSnapshotOperations` and find the `SystemCreateSnapshot` operation. For more information, see [Operations that CloudTrail does not log](snapshots-monitor-operations.md#snapshots-monitor-operations-cloudtrail).
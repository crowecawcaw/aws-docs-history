# Amazon CloudWatch logging for AWS Transfer Family servers

Amazon CloudWatch is a powerful monitoring and observability service that provides comprehensive
visibility into your AWS resources, including AWS Transfer Family.

- Real-time monitoring: CloudWatch monitors Transfer Family resources and applications in real-time,
  allowing you to track and analyze their performance.
- Metrics collection: CloudWatch collects and tracks various metrics for your resources
  and applications, which are variables you can measure and use for analysis.
- CloudWatch home page: The CloudWatch home page automatically displays metrics about Transfer Family and
  other AWS services you use, providing a centralized view of your monitoring
  data.
- Custom dashboards: You can create custom dashboards in CloudWatch to display metrics
  specific to your custom applications and the resources you choose to monitor.
- Alarms and notifications: CloudWatch allows you to create alarms that monitor your
  metrics and trigger notifications or automated actions when certain thresholds are
  breached. This can be useful for monitoring file transfer activity in your Transfer Family
  servers and scaling resources accordingly.
- Cost optimization: You can use the data collected by CloudWatch to identify
  under-utilized resources and take actions, such as stopping or deleting instances,
  to optimize your costs.
  Overall, the comprehensive monitoring capabilities in CloudWatch make it a valuable tool for
  managing and optimizing your Transfer Family infrastructure and the applications running on it.

Details for CloudWatch logging for Transfer Family web apps is available in [CloudTrail logging for Transfer Family web apps](webapp-cloudtrail.md "webapp-cloudtrail.md").

## Types of CloudWatch logging for Transfer Family

Transfer Family provides two ways to log events to CloudWatch:

- JSON structured logging
- Logging via a logging role

For Transfer Family servers, you can choose the logging mechanism that you prefer. For connectors
and workflows, only logging roles are supported.

**JSON structured logging**

For logging server events, we recommend using JSON structured logging. This provides a
more comprehensive logging format that enables CloudWatch log querying. For this type of
logging, the IAM policy for the user that creates the server (or edits the server's
logging configuration) must contain the following permissions:

- `logs:CreateLogDelivery`
- `logs:DeleteLogDelivery`
- `logs:DescribeLogGroups`
- `logs:DescribeResourcePolicies`
- `logs:GetLogDelivery`
- `logs:ListLogDeliveries`
- `logs:PutResourcePolicy`
- `logs:UpdateLogDelivery`

The following is an example policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogDelivery",
                "logs:GetLogDelivery",
                "logs:UpdateLogDelivery",
                "logs:DeleteLogDelivery",
                "logs:ListLogDeliveries",
                "logs:PutResourcePolicy",
                "logs:DescribeResourcePolicies",
                "logs:DescribeLogGroups"
            ],
            "Resource": "*"
        }
    ]
}
```

For details on setting up JSON structured logging, see [Creating, updating, and viewing logging for
servers](log-server-manage.md "log-server-manage.md").

**Logging role**

To log events for a managed workflow that is attached to a server, as well as for
connectors, you need to specify a logging role. To set access, you create a
resource-based IAM policy and an IAM role that provides that access information. The
following is an example policy for an AWS account that can log server events.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:DescribeLogStreams",
                "logs:CreateLogGroup",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:log-group:/aws/transfer/*"
        }
    ]
}
```

For details on configuring a logging role to log workflow events see [Managing logging for workflows](cloudwatch-workflows.md "cloudwatch-workflows.md").

## Creating Amazon CloudWatch alarms

The following example shows how to create Amazon CloudWatch alarms using the AWS Transfer Family metric,
`FilesIn`.

CDK

```
new cloudwatch.Metric({
  namespace: "AWS/Transfer",
  metricName: "FilesIn",
  dimensionsMap: { ServerId: "s-00000000000000000" },
  statistic: "Average",
  period: cdk.Duration.minutes(1),
}).createAlarm(this, "AWS/Transfer FilesIn", {
  threshold: 1000,
  evaluationPeriods: 10,
  datapointsToAlarm: 5,
  comparisonOperator: cloudwatch.ComparisonOperator.GREATER_THAN_OR_EQUAL_TO_THRESHOLD,
});
```

CloudFormation

```
Type: AWS::CloudWatch::Alarm
Properties:
  Namespace: AWS/Transfer
  MetricName: FilesIn
  Dimensions:
    - Name: ServerId
      Value: s-00000000000000000
  Statistic: Average
  Period: 60
  Threshold: 1000
  EvaluationPeriods: 10
  DatapointsToAlarm: 5
  ComparisonOperator: GreaterThanOrEqualToThreshold
```

## Logging Amazon S3 API operations to S3 access

logs

###### Note

This section does not apply to Transfer Family web apps.

If you are [using Amazon S3
access logs to identify S3 requests](../../../AmazonS3/latest/dev/using-s3-access-logs-to-identify-requests.md "../../../AmazonS3/latest/dev/using-s3-access-logs-to-identify-requests.md") made on behalf of your file transfer
users, `RoleSessionName` is used to display which IAM role was assumed to
service the file transfers. It also displays additional information such as the user
name, session id, and server-id used for the transfers. The format is `[AWS:Role
 Unique Identifier]/username.sessionid@server-id` and is contained in the
Requester field. For example, the following are the contents for a sample Requester
field from an S3 access log for a file that was copied to the S3 bucket.

`arn:aws:sts::AWS-Account-ID:assumed-role/*IamRoleName*/username.sessionid@server-id`

In the Requester field above, it shows the IAM Role called `IamRoleName`.
For more information about IAM role unique identifiers, see [Unique
identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids") in the _AWS Identity and Access Management User Guide_.

## Using AWS User Notifications with AWS Transfer Family

To get notified about AWS Transfer Family events, you can use [AWS User Notifications](../../../notifications/latest/userguide/what-is.md "../../../notifications/latest/userguide/what-is.md") to set up
various delivery channels. When an event matches a rule that you specify, you receive a
notification.

You can receive notifications for events through multiple channels, including email,
[Amazon Q Developer in chat applications](../../../chatbot/latest/adminguide/what-is.md "../../../chatbot/latest/adminguide/what-is.md") chat notifications, or [AWS Console Mobile Application](../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md "../../../consolemobileapp/latest/userguide/what-is-consolemobileapp.md") push notifications. You can also see notifications in the [Console Notifications Center](https://console.aws.amazon.com/notifications/ "https://console.aws.amazon.com/notifications/"). User Notifications
supports aggregation, which can reduce the number of notifications that you receive
during specific events.

For more information, see the [Customize file delivery notifications using AWS Transfer Family managed workflows](https://aws.amazon.com/blogs/storage/customize-file-delivery-notifications-using-aws-transfer-family-managed-workflows/ "https://aws.amazon.com/blogs/storage/customize-file-delivery-notifications-using-aws-transfer-family-managed-workflows/") blog
post, and [What is AWS User Notifications?](../../../notifications/latest/userguide/what-is.md "../../../notifications/latest/userguide/what-is.md") in the _AWS User Notifications User
Guide_.

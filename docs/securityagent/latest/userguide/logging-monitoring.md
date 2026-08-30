# Logging and monitoring in AWS Security Agent

Monitoring is an important part of maintaining the reliability, availability, and performance of AWS Security Agent and your other AWS solutions. AWS provides the following monitoring tools to watch AWS Security Agent, report when something is wrong, and take automatic actions when appropriate:

- **AWS CloudTrail** captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
- **Amazon CloudWatch** monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For more information, see the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

## Logging AWS Security Agent API calls with AWS CloudTrail

AWS Security Agent is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Security Agent. CloudTrail captures all API calls for AWS Security Agent as events. The calls captured include calls from the AWS Security Agent console and code calls to the AWS Security Agent API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Security Agent. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Security Agent, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

### AWS Security Agent information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Security Agent, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Security Agent, create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All AWS Security Agent actions are logged by CloudTrail and are documented in the [AWS Security Agent API Reference](../../../security-agent/latest/api.md "../../../security-agent/latest/api.md"). For example, calls to the `CreatePentest`, `StartPentestExecution`, and `ListFindings` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

### Understanding AWS Security Agent log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren’t an ordered stack trace of the public API calls, so they don’t appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `CreatePentest` action:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/Alice",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "Alice"
    },
    "eventTime": "2025-01-15T10:30:00Z",
    "eventSource": "securityagent.amazonaws.com",
    "eventName": "CreatePentest",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.12",
    "userAgent": "aws-cli/2.13.0",
    "requestParameters": {
        "pentestName": "WebApp-Security-Test",
        "targetUrl": "https://example.com",
        "testScope": "OWASP-Top-10"
    },
    "responseElements": {
        "pentestId": "pt-1234567890abcdef0",
        "pentestArn": "arn:aws:securityagent:us-east-1:123456789012:pentest/pt-1234567890abcdef0"
    },
    "requestID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "eventID": "12345678-1234-1234-1234-123456789012",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

The following example shows a CloudTrail log entry that demonstrates the `StartPentestExecution` action:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID:session-name",
        "arn": "arn:aws:sts::123456789012:assumed-role/SecurityTeamRole/session-name",
        "accountId": "123456789012",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID",
                "arn": "arn:aws:iam::123456789012:role/SecurityTeamRole",
                "accountId": "123456789012",
                "userName": "SecurityTeamRole"
            },
            "attributes": {
                "creationDate": "2025-01-15T09:00:00Z",
                "mfaAuthenticated": "true"
            }
        }
    },
    "eventTime": "2025-01-15T11:00:00Z",
    "eventSource": "securityagent.amazonaws.com",
    "eventName": "StartPentestExecution",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "203.0.113.45",
    "userAgent": "console.amazonaws.com",
    "requestParameters": {
        "pentestId": "pt-1234567890abcdef0"
    },
    "responseElements": {
        "executionId": "exec-abcdef1234567890",
        "status": "RUNNING"
    },
    "requestID": "b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "eventID": "23456789-2345-2345-2345-234567890123",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789012",
    "eventCategory": "Management"
}
```

## Monitoring AWS Security Agent with Amazon CloudWatch

You can monitor AWS Security Agent using CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your security testing is performing. You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met.

### AWS Security Agent metrics

AWS Security Agent sends the following metrics to CloudWatch:

| Metric                     | Description                                       | Unit    |
| -------------------------- | ------------------------------------------------- | ------- |
| `PentestExecutions`        | The number of penetration test executions started | Count   |
| `PentestExecutionDuration` | The duration of penetration test executions       | Seconds |
| `FindingsGenerated`        | The number of security findings generated         | Count   |
| `CriticalFindings`         | The number of critical severity findings          | Count   |
| `HighFindings`             | The number of high severity findings              | Count   |
| `MediumFindings`           | The number of medium severity findings            | Count   |
| `LowFindings`              | The number of low severity findings               | Count   |
| `CodeReviews`              | The number of code reviews performed              | Count   |
| `DesignReviews`            | The number of design reviews performed            | Count   |

### Dimensions for AWS Security Agent metrics

AWS Security Agent metrics use the following dimensions:

| Dimension     | Description                                                              |
| ------------- | ------------------------------------------------------------------------ |
| `PentestId`   | Filters metrics by specific penetration test                             |
| `ExecutionId` | Filters metrics by specific test execution                               |
| `Severity`    | Filters findings metrics by severity level (Critical, High, Medium, Low) |
| `FindingType` | Filters metrics by type of security finding                              |

### Creating CloudWatch alarms for AWS Security Agent

You can create a CloudWatch alarm that sends an Amazon SNS message when the alarm changes state. An alarm watches a single metric over a time period you specify, and performs one or more actions based on the value of the metric relative to a given threshold over a number of time periods.

For example, you can create an alarm that monitors the number of critical findings and sends a notification when the number exceeds a threshold:

1. Open the CloudWatch console at https://console.aws.amazon.com/cloudwatch/.
2. In the navigation pane, choose **Alarms**, **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select metric**.
5. Choose **SecurityAgent**, then choose the metric category you want to monitor.
6. Select the metric you want to monitor, then choose **Select metric**.
7. Configure the alarm conditions, notification, and other settings.
8. Choose **Create alarm**.

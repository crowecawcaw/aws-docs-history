# Accessing audit logs in AWS CloudTrail

AWS CloudTrail is enabled on your AWS account when you create it. CloudTrail logs the activity taken by an IAM entity or an AWS service, such as Amazon Managed Workflows for Apache Airflow, which is recorded as a CloudTrail event.
You can view, search, and download the past 90 days of event history in the CloudTrail console. CloudTrail captures all events on the Amazon MWAA console and all calls to Amazon MWAA APIs. It doesn't capture read-only actions,
such as `GetEnvironment`, or the `PublishMetrics` action. This page describes how to use CloudTrail to monitor events for Amazon MWAA.

###### Contents

- [Creating a trail in CloudTrail](monitoring-cloudtrail.md#monitoring-cloudtrail-create "monitoring-cloudtrail.md#monitoring-cloudtrail-create")
- [Logging data plane events](monitoring-cloudtrail.md#monitoring-cloudtrail-invoke-rest-api "monitoring-cloudtrail.md#monitoring-cloudtrail-invoke-rest-api")
- [Accessing events with CloudTrail Event History](monitoring-cloudtrail.md#monitoring-cloudtrail-view "monitoring-cloudtrail.md#monitoring-cloudtrail-view")
- [Example trail for CreateEnvironment](monitoring-cloudtrail.md#monitoring-cloudtrail-logs-ex "monitoring-cloudtrail.md#monitoring-cloudtrail-logs-ex")
- [InvokeRestApi log entry example](monitoring-cloudtrail.md#monitoring-cloudtrail-logs-invoke-rest-api "monitoring-cloudtrail.md#monitoring-cloudtrail-logs-invoke-rest-api")
- [What's next?](monitoring-cloudtrail.md#monitoring-cloudtrail-next-up "monitoring-cloudtrail.md#monitoring-cloudtrail-next-up")

## Creating a trail in CloudTrail

You need to create a trail to access an ongoing record of events in your AWS account, including events for Amazon MWAA. A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. If you don't create a trail, you can still access available event history in the CloudTrail console. For example, using the information collected by CloudTrail, you can determine the request that was made to Amazon MWAA, the IP address from which the request was made, who made the request, when it was made, and additional details. To learn more, refer to the [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md").

## Logging data plane events

The following Amazon MWAA API actions are data plane events: `InvokeRestApi`, `CreateWebLoginToken`, and `CreateCliToken`. Unlike management events, AWS CloudTrail does not log data events by default, and they do not appear in CloudTrail Event History. You must configure a trail that explicitly includes data events. Additional charges apply. For more information, see [Logging data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the AWS CloudTrail User Guide.

###### To log data plane events

1. Open the CloudTrail console.
2. In the navigation pane, choose **Trails**, and then choose **Create trail**.
3. Enter a trail name and configure an Amazon S3 bucket for log files.
4. On the **Choose log events** page, select **Data events**.
5. Under **Data event type**, choose **Managed Apache Airflow**.
6. Review your settings and choose **Create trail**.

After the trail is active, CloudTrail delivers data plane events such as `InvokeRestApi`, `CreateWebLoginToken`, and `CreateCliToken` to your Amazon S3 bucket within approximately 15 minutes. If you configured Amazon CloudWatch Logs, use the following filter pattern to find these events:

```
{ ($.eventName = "InvokeRestApi") || ($.eventName = "CreateWebLoginToken") || ($.eventName = "CreateCliToken") }
```

###### Response payload is not logged

CloudTrail redacts the `RestApiResponse` field in log entries. CloudTrail records the call and its status code but does not log the response payload.

## Accessing events with CloudTrail Event History

You can troubleshoot operational and security incidents over the past 90 days in the CloudTrail console by viewing event history. For example, you can access events related to the creation, modification, or deletion of resources (such as IAM users or other AWS resources) in your AWS account on a per-region basis. To learn more, refer to the [Accessing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

1. Open the [CloudTrail](https://console.aws.amazon.com/cloudtrail/home# "https://console.aws.amazon.com/cloudtrail/home#") console.
2. Choose **Event history**.
3. Select the events you want to view, and then choose **Compare event details**.

## Example trail for `CreateEnvironment`

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, such as the date and time of the action, or request parameters. CloudTrail log files are not an ordered stack trace of the public API calls, and aren't listed in any specific order. The following example is a log entry for the `CreateEnvironment` action that is denied due to lacking permissions. The values in `AirflowConfigurationOptions` have been redacted for privacy.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "00123456ABC7DEF8HIJK",
    "arn": "arn:aws:sts::012345678901:assumed-role/root/myuser",
    "accountId": "012345678901",
    "accessKeyId": "",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "00123456ABC7DEF8HIJK",
        "arn": "arn:aws:iam::012345678901:role/user",
        "accountId": "012345678901",
        "userName": "user"
      },
      "webIdFederationData": {},
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2020-10-07T15:51:52Z"
      }
    }
  },
  "eventTime": "2020-10-07T15:52:58Z",
  "eventSource": "airflow.amazonaws.com",
  "eventName": "CreateEnvironment",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "205.251.233.178",
  "userAgent": "PostmanRuntime/7.26.5",
  "errorCode": "AccessDenied",
  "requestParameters": {
    "SourceBucketArn": "arn:aws:s3:::my-bucket",
    "ExecutionRoleArn": "arn:aws:iam::012345678901:role/AirflowTaskRole",
    "AirflowConfigurationOptions": "***",
    "DagS3Path": "sample_dag.py",
    "NetworkConfiguration": {
      "SecurityGroupIds": [
      "sg-01234567890123456"
      ],
      "SubnetIds": [
        "subnet-01234567890123456",
        "subnet-65432112345665431"
      ]
    },
    "Name": "test-cloudtrail"
  },
  "responseElements": {
    "message": "Access denied."
  },
  "requestID": "RequestID",
  "eventID": "EventID",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "recipientAccountId": "012345678901"
}
```

## InvokeRestApi log entry example

The following is a complete log entry example for the `InvokeRestApi` action. CloudTrail redacts the `RestApiResponse` field.

###### Use temporary credentials in production

This example shows temporary credentials from an assumed role, which is the recommended approach. For production workloads, use temporary credentials from or AWS Security Token Service (AWS STS) instead of long-term access keys.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "00123456ABC7DEF8HIJK:MySession",
    "arn": "arn:aws:sts::012345678901:assumed-role/MyRole/MySession",
    "accountId": "012345678901",
    "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "00123456ABC7DEF8HIJK",
        "arn": "arn:aws:iam::012345678901:role/MyRole",
        "accountId": "012345678901",
        "userName": "MyRole"
      },
      "attributes": {
        "creationDate": "2024-01-20T12:00:00Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2024-01-20T12:15:00Z",
  "eventSource": "airflow.amazonaws.com",
  "eventName": "InvokeRestApi",
  "awsRegion": "us-west-2",
  "sourceIPAddress": "203.0.113.10",
  "userAgent": "Boto3/1.28.0 Python/3.11.0",
  "requestParameters": {
    "Name": "MyAirflowEnvironment",
    "Path": "/dags",
    "Method": "GET"
  },
  "responseElements": {
    "RestApiStatusCode": 200,
    "RestApiResponse": "***"
  },
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "resources": [
    {
      "accountId": "012345678901",
      "type": "AWS::MWAA::Environment",
      "ARN": "arn:aws:airflow:us-west-2:012345678901:environment/MyAirflowEnvironment"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "012345678901",
  "eventCategory": "Data"
}
```

## What's next?

- Learn how to configure other AWS services for the event data collected in CloudTrail logs in [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations").
- Learn how to be notified when CloudTrail publishes new log files to an Amazon S3 bucket in [Configuring Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md").

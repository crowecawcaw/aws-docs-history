# AWS CloudTrail logging for AWS Transfer Family

AWS Transfer Family integrates with both AWS CloudTrail and Amazon CloudWatch. CloudTrail and CloudWatch serve different but
complementary purposes.

- This topic covers integration with CloudTrail , an AWS service that creates a record of
  actions taken within your AWS account. It continuously monitors and records API operations for
  activities like console sign-ins, AWS Command Line Interface commands, and SDK/API operations. This allows you to
  keep a log of who took what action, when, and from where. CloudTrail helps with auditing, access
  management, and regulatory compliance by providing a history of all activity in your AWS
  environment. For details, see the [AWS CloudTrail User
  Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").
- [Amazon CloudWatch logging for AWS Transfer Family servers](structured-logging.md "structured-logging.md") covers integration with CloudWatch, a monitoring service for AWS resources and applications. It collects metrics
  and logs to provide visibility into resource utilization, application performance, and
  overall system health. CloudWatch helps with operational tasks like troubleshooting issues,
  setting alarms and autoscaling. For details, see the [Amazon CloudWatch User
  Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md").
  A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
  that you specify. CloudTrail log files contain one or more log entries. An event represents a
  single request from any source and includes information about the requested action, the date
  and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered
  stack trace of the public API operations, so they don't appear in any specific order.

For an ongoing record of events in your AWS account, including events for AWS Transfer Family,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon
  SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving
  CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")
  All AWS Transfer Family actions are logged by CloudTrail and are documented in the [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")
  [API reference](../APIReference/api_welcome.md "../APIReference/api_welcome.md"). For example, calls to the
  `CreateServer`, `ListUsers` and `StopServer` actions
  generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail userIdentity
  element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3
bucket, including events for AWS Transfer Family. If you don't configure a trail, you can still
view the most recent events in the CloudTrail console in **Event
history**.

Using the information collected by CloudTrail, you can determine the request that was made to
AWS Transfer Family, the IP address from which the request was made, who made the request, when it was
made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

###### Topics

- [Enable AWS CloudTrail logging](#monitoring-enable-cloudtrail "#monitoring-enable-cloudtrail")
- [Example log entry for creating a server](#create-server-ct-example "#create-server-ct-example")
- [Data access log examples](#data-access-log-examples "#data-access-log-examples")

## Enable AWS CloudTrail logging

You can monitor AWS Transfer Family API operations using AWS CloudTrail. By monitoring API operations, you can
get useful security and operational information. If you have [Amazon S3 object level
logging enabled](../../../AmazonS3/latest/user-guide/enable-cloudtrail-events.md "../../../AmazonS3/latest/user-guide/enable-cloudtrail-events.md"), `RoleSessionName` is contained in the Requester
field as `[AWS:Role Unique Identifier]/username.sessionid@server-id`. For
more information about AWS Identity and Access Management (IAM) role unique identifiers, see [Unique
identifiers](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-unique-ids") in the _AWS Identity and Access Management User Guide_.

###### Important

The maximum length of the `RoleSessionName` is 64 characters. If the
`RoleSessionName` is longer, the `server-id`
gets truncated.

### Enabling Amazon S3 data events

To track file operations performed through AWS Transfer Family on your Amazon S3 buckets, you need to enable data events for those buckets. Data events provide object-level API activity and are particularly useful for tracking file uploads, downloads, and other operations performed by AWS Transfer Family users.

To enable Amazon S3 data events for your AWS Transfer Family server:

1. Open the CloudTrail console at [https://console.aws.amazon.com/cloudtrail/](https://console.aws.amazon.com/cloudtrail/ "https://console.aws.amazon.com/cloudtrail/").
2. In the navigation pane, choose **Trails**, and then select an existing trail or create a new one.
3. Under **Data events**, choose **Edit**.
4. For **Data event type**, select **S3**.
5. Choose the Amazon S3 buckets to log data events for. You can log data events for all buckets or specify individual buckets.
6. Choose whether to log **Read** events, **Write** events, or both.
7. Choose **Save changes**.

After enabling data events, you can access these logs in the Amazon S3 bucket configured for your CloudTrail trail. The logs include details such as the user who performed the action, the action timestamp, the specific object affected, and the `onBehalfOf` field that helps trace the `userId` for actions performed through AWS Transfer Family.

## Example log entry for creating a server

The following example shows a CloudTrail log entry (in JSON format) that demonstrates the
`CreateServer` action.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AAAA4FFF5HHHHH6NNWWWW:user1",
        "arn": "arn:aws:sts::123456789102:assumed-role/Admin/user1",
        "accountId": "123456789102",
        "accessKeyId": "AAAA52C2WWWWWW3BB4Z",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2018-12-18T20:03:57Z"
            },
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AAAA4FFF5HHHHH6NNWWWW",
                "arn": "arn:aws:iam::123456789102:role/Admin",
                "accountId": "123456789102",
                "userName": "Admin"
            }
        }
    },
    "eventTime": "2024-02-05T19:18:53Z",
    "eventSource": "transfer.amazonaws.com",
    "eventName": "CreateServer",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "11.22.1.2",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "requestParameters": {
        "domain": "S3",
        "hostKey": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "protocols": [
            "SFTP"
        ],
        "protocolDetails": {
            "passiveIp": "AUTO",
            "tlsSessionResumptionMode": "ENFORCED",
            "setStatOption": "DEFAULT"
        },
        "securityPolicyName": "TransferSecurityPolicy-2020-06",
        "s3StorageOptions": {
            "directoryListingOptimization": "ENABLED"
        }
    },
    "responseElements": {
        "serverId": "s-1234abcd5678efghi"
    },
    "requestID": "6fe7e9b1-72fc-45b0-a7f9-5840268aeadf",
    "eventID": "4781364f-7c1e-464e-9598-52d06aa9e63a",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789102",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "transfer.us-east-1.amazonaws.com"
    },
    "sessionCredentialFromConsole": "true"
}
```

## Data access log examples

When you enable Amazon S3 data events for your CloudTrail trail, you can track file operations performed through AWS Transfer Family. These logs help you monitor who accessed what data, when, and how.

### Example log entry for successful data access

The following example shows a CloudTrail log entry for a successful file download operation through AWS Transfer Family.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID:TransferSessionUser",
        "arn": "arn:aws:sts::123456789012:assumed-role/TransferS3AccessRole/TransferSessionUser",
        "accountId": "123456789012",
        "accessKeyId": "ASIAEXAMPLEKEY",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID",
                "arn": "arn:aws:iam::123456789012:role/TransferS3AccessRole",
                "accountId": "123456789012",
                "userName": "TransferS3AccessRole"
            },
            "attributes": {
                "creationDate": "2025-07-15T16:12:05Z",
                "mfaAuthenticated": "true"
            }
        },
        "invokedBy": "transfer.amazonaws.com"
    },
    "eventTime": "2025-07-15T16:15:22Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "GetObject",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "transfer.amazonaws.com",
    "userAgent": "transfer.amazonaws.com",
    "requestParameters": {
        "bucketName": "my-transfer-bucket",
        "key": "users/john.doe/reports/quarterly-report-2025-Q2.pdf",
        "Host": "my-transfer-bucket.s3.amazonaws.com",
        "x-amz-request-payer": "requester"
    },
    "responseElements": null,
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "bytesTransferredIn": 0,
        "bytesTransferredOut": 2458732,
        "x-amz-id-2": "EXAMPLE123456789+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ="
    },
    "requestID": "EXAMPLE123456789",
    "eventID": "example12-3456-7890-abcd-ef1234567890",
    "readOnly": true,
    "resources": [
        {
            "type": "AWS::S3::Object",
            "ARN": "arn:aws:s3:::my-transfer-bucket/users/john.doe/reports/quarterly-report-2025-Q2.pdf"
        },
        {
            "accountId": "123456789012",
            "type": "AWS::S3::Bucket",
            "ARN": "arn:aws:s3:::my-transfer-bucket"
        }
    ],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "123456789012",
    "eventCategory": "Data",
    "requestParameters": {
        "x-amz-onBehalfOf": "john.doe.sessionid@s-abcd1234efgh5678"
    }
}
```

In this example, note the following important fields:

- `eventName`: Indicates the S3 API operation that was performed (GetObject for a file download).
- `requestParameters.bucketName` and `requestParameters.key`: Show which S3 object was accessed.
- `additionalEventData.bytesTransferredOut`: Shows the size of the downloaded file in bytes.
- `requestParameters.x-amz-onBehalfOf`: Contains the AWS Transfer Family username and session ID, allowing you to trace which AWS Transfer Family user performed the action.

The `x-amz-onBehalfOf` field is particularly important as it links the S3 API call back to the specific AWS Transfer Family user who initiated the action. This field follows the format `username.sessionid@server-id`, where:

- `username` is the AWS Transfer Family username.
- `sessionid` is a unique identifier for the user's session.
- `server-id` is the ID of the AWS Transfer Family server.

### Common data access operations

When monitoring data access through AWS Transfer Family, you'll typically see the following S3 API operations in your CloudTrail logs:

| Common S3 operations in AWS Transfer Family logs | S3 API Operation  | AWS Transfer Family Action             | Description                                                                                                                                                                                                           |
| ------------------------------------------------ | ----------------- | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GetObject                                        | File download     | User downloaded a file from the server |
| PutObject                                        | File upload       | User uploaded a file to the server     |
| DeleteObject                                     | File deletion     | User deleted a file from the server    |
| ListObjects or ListObjectsV2                     | Directory listing | User listed files in a directory       |
| CopyObject                                       | File copy         | User copied a file within the server   | By monitoring these operations in your CloudTrail logs, you can track all file activities performed through your AWS Transfer Family server, helping you meet compliance requirements and detect unauthorized access. |

# Logging Amazon MWAA Serverless APIs with CloudTrail

Amazon MWAA Serverless is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in the Amazon MWAA Serverless.
AWS CloudTrail captures API calls for Amazon MWAA Serverless as events including calls from Amazon MWAA Serverless console and code calls to the Amazon MWAA Serverless API operations. If you create a trail, you can enable continuous delivery of
AWS CloudTrail events to an Amazon S3 bucket, including events for Amazon MWAA Serverless. If you don't configure a trail, you can still view the most recent events in the AWS CloudTrail console in Event history. Using the information collected by
AWS CloudTrail, you can determine the request that was made to Amazon MWAA Serverless, the IP address it was made from, who made it, when it was made, and additional details.

To learn more about AWS CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Data encryption

AWS CloudTrailis enabled on your AWS account when you create it. AWS CloudTrail logs the activity taken by an IAM entity or an AWS service, such as , which is recorded as a CloudTrail event.
You can view, search, and download the past 90 days of event history in the AWS CloudTrail console. AWS CloudTrail captures all events on the Amazon MWAA Serverless console and all calls to Amazon MWAA Serverless APIs.

###### Topics

- [Creating a trail in CloudTrail](#trail-in-cloudtrail "#trail-in-cloudtrail")
- [Accessing events with CloudTrail Event History](#access-events-history "#access-events-history")
- [Accessing events with CloudTrail Event History](#example-create-workflow-trail "#example-create-workflow-trail")

### Creating a trail in CloudTrail

You need to create a trail to access an ongoing record of events in your AWS account, including events for Amazon MWAA Serverless. A trail enables AWS CloudTrail to deliver log files to an Amazon S3 bucket.
If you don't create a trail, you can still access available event history in the AWS CloudTrail console. For example, using the information collected by AWS CloudTrail, you can determine the request that was made to Amazon MWAA Serverless,
the IP address from which the request was made, who made the request, when it was made, and additional details. To learn more, refer to the Creating a trail for your AWS account.

### Accessing events with CloudTrail Event History

You can troubleshoot operational and security incidents over the past 90 days in the AWS CloudTrail console by viewing event history. For example, you can access events related to the creation,
modification, or deletion of resources (such as IAM users or other AWS resources) in your AWS account on a per-region basis. To learn more, refer to the
[Accessing Events with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

1. Open the [AWS CloudTrail console](https://console.aws.amazon.com/cloudtrail/home "https://console.aws.amazon.com/cloudtrail/home").
2. Choose **Event history**.
3. Select the events you want to view, and then choose **Compare event details**.

### Accessing events with CloudTrail Event History

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify.

CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, such as the date and time of the action, or request parameters.
CloudTrail log files are not an ordered stack trace of the public API calls, and aren't listed in any specific order. The following example is a log entry for the `CreateWorkflow` action that is denied due to lacking permissions.

CLI

```

{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "`AIDACKCEVSQ6C2EXAMPLE`",
    "arn": "arn:aws:iam::`111122223333`:role/`mwaa-serverless-role`",
    "accountId": "`111122223333`",
    "accessKeyId": "`ASIAIOSFODNN7EXAMPLE`",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "`AIDA123456789EXAMPLE`",
        "arn": "arn:aws:iam::`111122223333`:role/Admin",
        "accountId": "`111122223333`",
        "userName": "Admin"
      },
      "attributes": {
        "creationDate": "2025-11-03T23:30:24Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2025-11-03T23:31:54Z",
  "eventSource": "airflow-serverless.amazonaws.com",
  "eventName": "CreateWorkflow",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-cli/2.28.17",
  "requestParameters": {
    "name": "`my-mwaa-serverless-workflow`",
    "clientToken": "`c52de4a9-4f0f-4c87-af44-0fc9417e0765`",
    "definitionS3Location": {
      "bucket": "`amzn-s3-demo-bucket`",
      "objectKey": "`my-mwaa-serverless-workflow.yml`"
    },
    "roleArn": "arn:aws:iam::`111122223333`:role/`mwaa-serverless-workflow-role"`,
    "encryptionConfiguration": {
      "type": "CUSTOMER_MANAGED_KEY",
      "kmsKeyId": "arn:aws:kms:us-east-1:`111122223333`:key/`37edb8d7-ff19-4456-9b65-cbef9c61b53f`"
    },
    "loggingConfiguration": {
      "logGroupName": "`my-mwaa-serverless-workflow-log-group`"
    },
    "triggerMode": "manual_only"
  },
  "responseElements": {
    "workflowArn": "arn:aws:airflow-serverless:us-east-1:`111122223333`:workflow/`my-mwaa-serverless-workflow-Tc2lQzso0N`",
    "createdAt": "2025-11-03T23:31:54.406Z",
    "revisionId": "41f42323-f8cb-463b-a7d7-3d1a9d16cdea",
    "workflowVersion": "7a1bf53101df1c62969f81221c58c5f7"
  },
  "requestID": "14f37e54-e6f3-49f7-97fb-bd32b578c68d",
  "eventID": "a82b4d5f-74f6-4817-9591-066488a63859",
  "readOnly": "false",
  "resources": [
    {
      "accountId": "`111122223333`",
      "type": "AWS::MWAAServerless::Workflow",
      "ARN": "arn:aws:airflow-serverless:us-east-1:`111122223333`:workflow/`my-mwaa-serverless-workflow-Tc2lQzso0N`"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": "true",
  "recipientAccountId": "`111122223333`",
  "eventCategory": "Management"
}

```

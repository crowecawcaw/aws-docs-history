

# Logging AWS Startups API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

 AWS Startups is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Startups. CloudTrail captures all API calls for AWS Startups as events. The calls captured include calls from the AWS Startups console and code calls to the AWS Startups API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Startups. If you don’t configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Startups, the IP address from which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

## AWS Startups information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Startups, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for AWS Startups, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following:
+  [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html#cloudtrail-aws-service-specific-topics-integrations) 
+  [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/getting_notifications_top_level.html) 
+  [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) 
+  [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

 AWS Startups logs API calls to CloudTrail as management events. For example, calls to the `GetSpendSummary` action generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding AWS Startups log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren’t an ordered stack trace of the public API calls, so they don’t appear in any specific order.

The following examples show CloudTrail log entries that demonstrate the `GetSpendSummary` action. In both entries, the event source is `startups.amazonaws.com`, and `GetSpendSummary` is a read-only management event.

The following example shows a successful `GetSpendSummary` call.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID123456:jane-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/aws-startup-advisor-user/jane-doe",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID123456",
                "arn": "arn:aws:iam::111122223333:role/aws-startup-advisor-user",
                "accountId": "111122223333",
                "userName": "aws-startup-advisor-user"
            },
            "attributes": { "creationDate": "2026-01-01T00:00:00Z", "mfaAuthenticated": "false" }
        }
    },
    "eventTime": "2026-01-01T00:00:05Z",
    "eventSource": "startups.amazonaws.com",
    "eventName": "GetSpendSummary",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-sdk-js/3.x",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "eventID": "b2c3d4e5-6789-01bc-defa-EXAMPLE22222",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "startups.global.api.aws"
    }
}
```

The following example shows a failed `GetSpendSummary` call. This entry shows an action-level authorization failure for `startups:GetSpendSummary`, where no identity-based policy allows the caller to perform the action. This action-level failure differs from the partial-response behavior. In that case, a successful call returns `ACCESS_DENIED` in individual response sections when the caller lacks the downstream Cost Explorer or Billing permissions.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAEXAMPLEID123456:jane-doe",
        "arn": "arn:aws:sts::111122223333:assumed-role/aws-startup-advisor-user/jane-doe",
        "accountId": "111122223333",
        "accessKeyId": "ASIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAEXAMPLEID123456",
                "arn": "arn:aws:iam::111122223333:role/aws-startup-advisor-user",
                "accountId": "111122223333",
                "userName": "aws-startup-advisor-user"
            },
            "attributes": { "creationDate": "2026-01-01T00:00:00Z", "mfaAuthenticated": "false" }
        }
    },
    "eventTime": "2026-01-01T00:00:05Z",
    "eventSource": "startups.amazonaws.com",
    "eventName": "GetSpendSummary",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-sdk-js/3.x",
    "errorCode": "AccessDenied",
    "errorMessage": "User: arn:aws:sts::111122223333:assumed-role/aws-startup-advisor-user/jane-doe is not authorized to perform: startups:GetSpendSummary because no identity-based policy allows the startups:GetSpendSummary action",
    "requestParameters": null,
    "responseElements": null,
    "requestID": "c3d4e5f6-7890-12cd-efab-EXAMPLE33333",
    "eventID": "d4e5f6a7-8901-23de-fabc-EXAMPLE44444",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_128_GCM_SHA256",
        "clientProvidedHostHeader": "startups.global.api.aws"
    }
}
```
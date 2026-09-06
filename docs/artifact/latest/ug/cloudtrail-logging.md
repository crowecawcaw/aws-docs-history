

# Logging AWS Artifact API calls with AWS CloudTrail
<a name="cloudtrail-logging"></a>

AWS Artifact is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in AWS Artifact. CloudTrail captures API calls for AWS Artifact as events. The calls captured include calls from the AWS Artifact console and code calls to the AWS Artifact API operations. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Artifact. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to AWS Artifact, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html). 

## AWS Artifact information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in AWS Artifact, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html). 

For an ongoing record of events in your AWS account, including events for AWS Artifact, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+  [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) 
+  [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html) 
+  [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html) 
+  [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html) 

AWS Artifact supports logging the following actions as events in CloudTrail log files:
+  [ListReports](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListReports.html) 
+  [GetAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAccountSettings.html) 
+  [GetReportMetadata](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReportMetadata.html) 
+  [GetReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetReport.html) 
+  [GetTermForReport](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetTermForReport.html) 
+  [PutAccountSettings](https://docs.aws.amazon.com/artifact/latest/APIReference/API_PutAccountSettings.html) 
+  [AcceptAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptAgreement.html) 
+  [AcceptNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_AcceptNdaForAgreement.html) 
+  [GetAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetAgreement.html) 
+  [GetCustomerAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetCustomerAgreement.html) 
+  [GetNdaForAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_GetNdaForAgreement.html) 
+  [ListAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListAgreements.html) 
+  [ListCustomerAgreements](https://docs.aws.amazon.com/artifact/latest/APIReference/API_ListCustomerAgreements.html) 
+  [TerminateAgreement](https://docs.aws.amazon.com/artifact/latest/APIReference/API_TerminateAgreement.html) 

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html). 

## Understanding AWS Artifact log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the GetReportMetadata action. 

```
{
  "Records": [
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::999999999999:user/myUserName",
        "accountId": "999999999999",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:03:36Z",
      "eventSource": "artifact.amazonaws.com",
      "eventName": "GetReportMetadata",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "errorCode": "AccessDenied",
      "errorMessage": "User: arn:aws:iam::999999999999:user/myUserName is not authorized to perform: artifact:GetReportMetadata on resource: arn:aws:artifact:us-east-1::report/report-f1DIWBmGa2Lhsadg",
      "requestParameters": null,
      "responseElements": null,
      "requestID": "7aebcd0f-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "e92a3e85-8ecd-4d23-8074-843aabfe89bf",
      "eventType": "AwsApiCall",
      "recipientAccountId": "999999999999"
    },
    {
      "eventVersion": "1.03",
      "userIdentity": {
        "type": "IAMUser",
        "principalId": "A1B2C3D4E5F6G7EXAMPLE",
        "arn": "arn:aws:iam::999999999999:user/myUserName",
        "accountId": "999999999999",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "myUserName"
      },
      "eventTime": "2015-03-18T19:04:42Z",
      "eventSource": "artifact.amazonaws.com",
      "eventName": "GetReportMetadata",
      "awsRegion": "us-east-1",
      "sourceIPAddress": "127.0.0.1",
      "userAgent": "Python-httplib2/0.8 (gzip)",
      "requestParameters": {
        "reportId": "report-f1DIWBmGa2Lhsadg"
      },
      "responseElements": null,
      "requestID": "a2198ecc-cda1-11e4-aaa2-e356da31e4ff",
      "eventID": "20b84ce5-730f-482e-b2b2-e8fcc87ceb22",
      "eventType": "AwsApiCall",
      "recipientAccountId": "999999999999"
    }
  ]
}
```
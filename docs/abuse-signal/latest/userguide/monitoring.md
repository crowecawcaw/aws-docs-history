

# Monitoring AWS Abuse Signal API

You can monitor API activity for AWS Abuse Signal API using AWS CloudTrail, which records the API calls made in your AWS account. CloudTrail captures these calls as events that you can view, search, and deliver to storage for an ongoing record. Use this record to understand which requests were made, who made them, and when.

**Note**  
AWS Abuse Signal API does not publish Amazon CloudWatch metrics to your AWS account. AWS CloudTrail provides monitoring for AWS Abuse Signal API.

**Topics**
+ [Logging AWS Abuse Signal API calls using AWS CloudTrail](#monitoring-cloudtrail)

## Logging AWS Abuse Signal API calls using AWS CloudTrail
<a name="monitoring-cloudtrail"></a>

AWS Abuse Signal API is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures API calls for AWS Abuse Signal API as events. For more information, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/).

CloudTrail is enabled on your AWS account when you create the account. With Event history, you can view recent management events for your account with no additional setup. For an ongoing record of activity, create a trail to deliver events to an Amazon S3 bucket that you specify. Using the information that CloudTrail collects, you can determine the request that was made to AWS Abuse Signal API, the source IP address from which the request was made, who made the request, and when it was made.

### AWS Abuse Signal API management events in CloudTrail
<a name="monitoring-management-events"></a>

Management events provide information about management operations that are performed in your AWS account. CloudTrail logs management events by default, and they appear in Event history with no additional configuration and no additional charge.

AWS Abuse Signal API logs `ListAbuseReportStatuses` as a management event.

For more information, see [Logging management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

### AWS Abuse Signal API data events in CloudTrail
<a name="monitoring-data-events"></a>

Data events provide information about the resource operations performed on or in a resource. CloudTrail does not log data events by default. To record them, configure advanced event selectors on a trail or event data store that include the resource type `AWS::Abuse::Report`.

AWS Abuse Signal API logs `CreateAbuseReport` and `GetAbuseReportStatus` as data events.

**Important**  
Additional charges apply for logging data events. For more information, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

For more information about enabling data events, see [Logging data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) in the *AWS CloudTrail User Guide*.

**Note**  
To protect the privacy of report content, the `report` field is redacted in the logged `CreateAbuseReport` event and appears as `"*"`.

**Note**  
CloudTrail records each event in the AWS Region that served the request, which is the Regional endpoint you called or the Region that the global endpoint routed to.

### AWS Abuse Signal API event examples
<a name="monitoring-event-examples"></a>

A CloudTrail event represents a single request from any source and includes information about the requested operation, the date and time of the operation, request parameters, and so on. CloudTrail events are not an ordered stack trace of the public API calls, so they don’t appear in any specific order.

The following example shows a CloudTrail data event for the `CreateAbuseReport` operation. The `report` field in `requestParameters` is redacted to protect report content.

```json
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE",
    "arn": "arn:aws:iam::111122223333:user/Mary_Major",
    "accountId": "111122223333",
    "userName": "Mary_Major"
  },
  "eventTime": "2024-11-18T15:04:21Z",
  "eventSource": "abuse.amazonaws.com",
  "eventName": "CreateAbuseReport",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-sdk-java/2.25.0",
  "requestParameters": {
    "report": "***"
  },
  "responseElements": {
    "reportId": "EXAMPLE11-2222-3333-4444-555566667777"
  },
  "resources": [
    {
      "type": "AWS::Abuse::Report",
      "ARN": "arn:aws:abuse:us-east-1:111122223333:report/EXAMPLE11-2222-3333-4444-555566667777"
    }
  ],
  "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "eventID": "b2c3d4e5-6789-01ab-cdef-EXAMPLE22222",
  "readOnly": false,
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "eventCategory": "Data",
  "recipientAccountId": "111122223333"
}
```

The following example shows a CloudTrail management event for the `ListAbuseReportStatuses` operation. Because the operation is read-only, `responseElements` is `null`.

```json
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE",
    "arn": "arn:aws:iam::111122223333:user/Mary_Major",
    "accountId": "111122223333",
    "userName": "Mary_Major"
  },
  "eventTime": "2024-11-18T15:06:48Z",
  "eventSource": "abuse.amazonaws.com",
  "eventName": "ListAbuseReportStatuses",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "192.0.2.1",
  "userAgent": "aws-sdk-java/2.25.0",
  "requestParameters": null,
  "responseElements": null,
  "requestID": "c3d4e5f6-7890-12ab-cdef-EXAMPLE33333",
  "eventID": "d4e5f6a7-8901-23ab-cdef-EXAMPLE44444",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "eventCategory": "Management",
  "recipientAccountId": "111122223333"
}
```
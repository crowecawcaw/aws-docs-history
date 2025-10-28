Amazon Lookout for Metrics is no longer available to new customers. Existing Amazon Lookout for Metrics customers will be able to use the service until September 12, 2025, when we will end support for Amazon Lookout for Metrics. To help transition off of Amazon Lookout for Metrics, please read [Transitioning off Amazon Lookout for Metrics](https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/ "https://aws.amazon.com/blogs/machine-learning/transitioning-off-amazon-lookout-for-metrics/").

# Viewing Amazon Lookout for Metrics API activity in CloudTrail

Amazon Lookout for Metrics is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an
AWS service in Lookout for Metrics. CloudTrail captures all API calls for Lookout for Metrics as events. Captured calls include calls from the Lookout for Metrics
console and code calls to the Lookout for Metrics API operations.

Using the information collected by CloudTrail, you can determine the request that was made to Lookout for Metrics, the IP address
from which the request was made, who made the request, when it was made, and additional details.

All [Lookout for Metrics calls](../api/API_Operations.md "../api/API_Operations.md") are logged by CloudTrail. Log entries contain
information about who generated the request. The identity information helps you determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a role or federated user.
- Whether the request was made by another AWS service.
  For more information, see the [CloudTrail
  userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Topics

- [Storing Lookout for Metrics information in CloudTrail](#services-cloudtrail-logs "#services-cloudtrail-logs")
- [Example: Lookout for Metrics log file entry](#services-cloudtrail-format "#services-cloudtrail-format")

## Storing Lookout for Metrics information in CloudTrail

AWS CloudTrail is activated on your AWS account when you create it. When activity occurs in Lookout for Metrics, it is
automatically recorded in a CloudTrail event. You can view, search, and download recent events in the **Event
history** in the CloudTrail console. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Lookout for Metrics, create a trail. A
_trail_ enables CloudTrail to send log files to an Amazon S3 bucket. When you create a trail in the
console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition. It
sends the log files to the Amazon S3 bucket that you specify. For more information, see [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md").

You can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs.
For more information, see the following:

- [CloudTrail supported services and
  integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS
  notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files
  from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from
  multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Example: Lookout for Metrics log file entry

AWS CloudTrail log files contain one or more log entries, one entry for every event. An event represents a single
request from any source and includes information about the requested action, the date and time of the action,
request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't
appear in any specific order.

The following example is a CloudTrail log entry for a `DescribeAnomalyDetector` call. Specific
information about the call appears in the `eventName` and `requestParameters` fields. The
remaining fields record details about the caller and tracking information such as the request ID, which you can
use to find information about the request in places like logs and [AWS X-Ray](../../../xray/latest/devguide.md "../../../xray/latest/devguide.md")
traces.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AKIAI44QH8DHBEXAMPLE",
        "arn": "arn:aws:iam::123456789012:user/fred",
        "accountId": "123456789012",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "fred",
        "sessionContext": {
            "sessionIssuer": {},
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-01-09T00:14:34Z"
            }
        }
    },
    "eventTime": "2021-01-09T00:18:12Z",
    "eventSource": "lookoutmetrics.amazonaws.com",
    "eventName": "DescribeAnomalyDetector",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "205.256.256.182",
    "userAgent": "aws-sdk-java/1.11.930 Linux/4.9.230-0.1.ac.223.84.332.metal1.x86_64 OpenJDK_64-Bit_Server_VM/25.275-b01 java/1.8.0_275 vendor/Oracle_Corporation",
    "requestParameters": {
        "AnomalyDetectorArn": "arn:aws:lookoutmetrics:us-east-2:123456789012:AnomalyDetector:my-detector-5m"
    },
    "responseElements": null,
    "requestID": "f587ee3c-xmpl-406b-b573-66100bb14b61",
    "eventID": "f2f879f8-xmpl-4475-9c0c-4291a389e14a",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "eventCategory": "Management",
    "recipientAccountId": "123456789012"
}
```

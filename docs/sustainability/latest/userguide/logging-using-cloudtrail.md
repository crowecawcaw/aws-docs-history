# Logging AWS Sustainability API calls using AWS CloudTrail

AWS Sustainability is integrated with AWS CloudTrail, a service that provides a record of actions
taken by a user, role, or an AWS service in AWS Sustainability. CloudTrail captures all API calls for
AWS Sustainability as events. The calls captured include calls from the AWS Sustainability console and
code calls to the AWS Sustainability API operations. If you create a trail, you can enable
continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Sustainability. If
you don't configure a trail, you can still view the most recent events in the CloudTrail console
in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to AWS Sustainability, the IP address from which the request
was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

###### Note

For resiliency purposes, AWS Sustainability can fail over to a secondary region. During a fail-over event, CloudTrail logs can be found in region us-west-2.

## AWS Sustainability information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs
in AWS Sustainability, that activity is recorded in a CloudTrail event along with other AWS service events
in **Event history**. You can view, search, and download recent events in
your AWS account. For more information, see [Viewing events with CloudTrail Event
history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for AWS Sustainability,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket.
By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail
logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket
that you specify. Additionally, you can configure other AWS services to further analyze and act
upon the event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications
  for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log
  files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log
  files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All AWS Sustainability actions are logged by CloudTrail and are documented in the [AWS Sustainability API Reference](../APIReference.md "../APIReference.md"). For example,
calls to the
`GetEstimatedCarbonEmissions` and `GetEstimatedCarbonEmissionsDimensionValues` actions generate
entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity
element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS Sustainability log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`GetEstimatedCarbonEmissions` action.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "accountId": "111122223333",
    "accessKeyId": "AIDACKCEVSQ6C2EXAMPLE",
    "sessionContext": {
      "sessionIssuer": {},
      "attributes": {
        "creationDate": "2026-03-11T21:15:59Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2026-03-11T21:22:23Z",
  "eventSource": "sustainability.amazonaws.com",
  "eventName": "GetEstimatedCarbonEmissions",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "123.123.123.123",
  "requestParameters": {
    "EmissionsTypes": [
      "TOTAL_LBM_CARBON_EMISSIONS",
      "TOTAL_MBM_CARBON_EMISSIONS",
      "TOTAL_SCOPE_1_CARBON_EMISSIONS",
      "TOTAL_SCOPE_2_LBM_CARBON_EMISSIONS",
      "TOTAL_SCOPE_2_MBM_CARBON_EMISSIONS",
      "TOTAL_SCOPE_3_LBM_CARBON_EMISSIONS",
      "TOTAL_SCOPE_3_MBM_CARBON_EMISSIONS"
    ],
    "GroupBy": [
      "SERVICE"
    ],
    "TimePeriod": {
      "Start": "2025-03-01T00:00:00Z",
      "End": "2026-02-28T23:59:59.999Z"
    },
    "MaxResults": 5000,
    "Granularity": "MONTHLY"
  },
  "responseElements": null,
  "requestID": "abfb58f2-96c0-496c-9b95-9896d6482193",
  "eventID": "36316506-78f7-430d-8e16-fc49da7fb7f5",
  "readOnly": true,
  "eventType": "AwsApiCall",
  "managementEvent": true,
  "recipientAccountId": "111122223333",
  "eventCategory": "Management",
  "sessionCredentialFromConsole": "true"
}
```

# Logging AWS Service Catalog API calls using

AWS CloudTrail

AWS Service Catalog is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in AWS Service Catalog. CloudTrail captures all API calls for
AWS Service Catalog as events. The calls captured include calls from the AWS Service Catalog
console and code calls to the AWS Service Catalog API operations. If you create a trail, you
can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for AWS Service Catalog. If you don't configure a trail, you can still view the most recent events
in the CloudTrail console in Event history. Using the information collected by CloudTrail, you can
determine the request that was made to AWS Service Catalog, the IP address from which the
request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail
User Guide.](logging-using-cloudtrail.md "logging-using-cloudtrail.md")

## AWS Service Catalog information

in CloudTrail

CloudTrail is enabled on your AWS account when you create it. When
activity occurs in AWS Service Catalog, that activity is recorded in a CloudTrail event
along with other AWS service events in Event history. You can view, search, and
download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including
events for AWS Service Catalog, create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the
console, the trail applies to all AWS Regions. The trail logs events from all Regions in
the AWS partition and delivers the log files to the Amazon S3 bucket that you specify.
Additionally, you can configure other AWS services to further analyze and act upon the
event data collected in CloudTrail logs. For more information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [AWS CloudTrail supported services and
  integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for
  AWS CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving AWS CloudTraillog files from multiple
  regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving AWS CloudTrail log files from multiple
  accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

CloudTrail [logs](../dg/logging-using-cloudtrail.md "../dg/logging-using-cloudtrail.md") all AWS Service Catalog actions. For example, calls to the
`CreatePortfolio`, `CreateProduct` and `UpdateProvisionedProduct` actions generate entries in the CloudTrail log files.

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding AWS Service Catalog log file

entries

A trail is a configuration that enables delivery of events as log
files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log
entries. An event represents a single request from any source and includes information
about the requested action, the date and time of the action, request parameters, and so
on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they
don't appear in any specific order. The following example shows an CloudTrail log entry
that demonstrates the `CreateApplication` API.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "account",
        "arn": "arn:aws:iam::12345789012:user/dev-haw",
        "accountId": "12345789012",
        "accessKeyId": "keyId",
        "userName": "dev-haw"
    },
    "eventTime": "2020-09-23T21:07:58Z",
    "eventSource": "servicecatalog-appregistry.amazonaws.com",
    "eventName": "CreateApplication",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "205.251.233.48",
    "userAgent": "aws-cli/1.18.140 Python/3.6.11 Linux/4.9.217-0.1.ac.205.84.332.metal1.x86_64 botocore/1.17.63",
    "requestParameters": {
        "name": "hawTestCT",
        "clientToken": "6f36d650-a086-47cf-810a-fbfab2f8ad33"
    },
    "responseElements": {
        "application": {
            "applicationArn": "arn:aws:servicecatalog:us-east-1:12345789012:application/app-02ocuq2cie2328pv64ya78e22f",
            "applicationId": "app-02ocuq2cie2328pv64ya78e22f",
            "creationTime": 1600895277.775,
            "lastUpdateTime": 1600895277.775,
            "name": "hawTestCT",
            "tags": {}
        }
    },
    "requestID": "1b6ad353-3b06-421b-bcb4-00075a782762",
    "eventID": "0a2ca224-cdfd-4c4b-a4ed-163218ff5e2d",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "recipientAccountId": "12345789012"
}
```

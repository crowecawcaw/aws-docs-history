The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Logging AWS Marketplace Deployment API calls with CloudTrail

The AWS Marketplace Deployment Service is integrated with AWS CloudTrail, a service that provides a
record of actions taken by a user, role, or an AWS service.

If you create a trail, you can enable continuous delivery of CloudTrail events to an
Amazon Simple Storage Service (Amazon S3) bucket. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**. Using the
information collected by CloudTrail, you can determine the request, the IP address from which
the request was made, who made the request, when it was made, and additional
details.

## AWS Marketplace Deployment Service information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity
occurs in the AWS Marketplace Deployment Service, that activity is recorded in a CloudTrail event
along with other AWS service events in **Event history**. You can
view, search, and download recent events in your AWS account. For more
information, see [Viewing Events
with CloudTrail Event History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the
_AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, create a trail. A trail
enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a
trail in the console, the trail applies to all AWS Regions. The trail logs events
from all AWS Regions in the AWS partition and delivers the log files to the Amazon S3
bucket that you specify. Additionally, you can configure other AWS services to
further analyze and act upon the event data collected in CloudTrail logs. For more
information, see:

- [Overview for Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring
  Amazon SNS Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md")
- [Receiving CloudTrail Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

All Deployment Service actions are logged by CloudTrail and are documented in this API
reference. For example, calls to the `PutDeploymentParameter`API action
generates entries in the CloudTrail log files. Every event or log entry contains
information about who generated the request. The identity information helps you
determine the following:

- Whether the request was made with root or user credentials.
- Whether the request was made with temporary security credentials for a
  role or federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail
userIdentity Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.

## Understanding AWS Marketplace log file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3
bucket that you specify. CloudTrail log files contain one or more log entries. An event
represents a single request from any source and includes information about the
requested action, the date and time of the action, request parameters, and so on.
CloudTrail log files are not an ordered stack trace of the public API calls, so they do
not appear in any specific order.

###### Note

These examples have been formatted for improved readability. In a CloudTrail log
file, all entries and events are concatenated into a single line. In addition,
this example has been limited to a single Deployment Service entry. In a real
CloudTrail log file, you see entries and events from multiple AWS services.

The following example shows a Deployment Service log entry that demonstrates the
`PutDeploymentParameter` action:

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "Unknown",
        "principalId": "ABCDEFGHIJKLMNOP12345",
        "arn": "arn:aws:iam::123456789010:user/CloudTrailTestUser",
        "accountId": "123456789010",
        "accessKeyId": "ABCDEFGHIJKLMNOP123"
    },
    "eventTime": "2023-11-16T16:32:48Z",
    "eventSource": "deployment-marketplace.amazonaws.com",
    "eventName": "PutDeploymentParameter",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-sdk-java/2.20.162 Mac_OS_X/13.5.2 OpenJDK_64-Bit_Server_VM/18.0.1+10-FR Java/18.0.1 vendor/Amazon.com_Inc. io/sync http/UrlConnection cfg/retry-mode/legacy",
    "requestParameters": {
        "productId": "prod-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "catalog": "AWSMarketplace",
        "clientToken": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "agreementId": "agmt-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "deploymentParameter": {
            "name": "PutDeploymentParameterCloudTrailTest-secret",
            "secretString": "***"
        },
        "expirationDate": "2023-11-30T03:02:26.779241Z"
        }
    },
    "responseElements": {
        "agreementId": "agmt-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "deploymentParametersId": "dp-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
        "resourceArn": "arn:aws:aws-marketplace:us-east-1:123456789010:DeploymentParameter:catalogs/AWSMarketplace/products/prod-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1/dp-fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1"
    },
    "requestID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
    "eventID": "fEXAMPLE-cb3e-4e21-86fd-6b3EXAMPLEd1",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "123456789010",
    "eventCategory": "Management"
}
```

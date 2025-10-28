# Logging AWS Control Tower Actions with AWS CloudTrail

AWS Control Tower is integrated with AWS CloudTrail, a service that provides a record of actions taken by a
user, role, or an AWS service in AWS Control Tower. CloudTrail captures actions for AWS Control Tower as events. If
you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for AWS Control Tower.

If you don't configure a trail, you can still view the most recent events in the CloudTrail
console in **Event history**. Using the information collected by CloudTrail, you can
determine the request that was made to AWS Control Tower, the IP address from which the request was made,
who made the request, when it was made, and additional details.

To learn more about CloudTrail, including how to configure and enable it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

## AWS Control Tower Information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When supported event
activity occurs in AWS Control Tower, that activity is recorded in a CloudTrail event along with other AWS
service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing Events with CloudTrail Event
History](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

###### Note

In AWS Control Tower releases before landing zone version 3.0, AWS Control Tower created a member account
trail. When you update to release 3.0, your CloudTrail trail is updated to become an organization
trail. For best practices when moving between trails, see [Creating an organizational trail](../../../awscloudtrail/latest/userguide/creating-trail-organization.md#creating-an-organizational-trail-best-practice "../../../awscloudtrail/latest/userguide/creating-trail-organization.md#creating-an-organizational-trail-best-practice") in the CloudTrail User Guide.

**Recommended: Create a trail**

For an ongoing record of events in your AWS account, including events for AWS Control Tower,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all AWS
Regions. The trail logs events from all Regions in the AWS partition and delivers the log
files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for
  Creating a Trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [Prepare for creating a trail](../../../awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.md "../../../awscloudtrail/latest/userguide/creating-an-organizational-trail-prepare.md")
- [Managing CloudTrail
  costs](../../../awscloudtrail/latest/userguide/cloudtrail-trail-manage-costs.md "../../../awscloudtrail/latest/userguide/cloudtrail-trail-manage-costs.md")
- [CloudTrail Supported Services and Integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md#cloudtrail-aws-service-specific-topics-integrations")
- [Configuring Amazon SNS
  Notifications for CloudTrail](../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md "../../../awscloudtrail/latest/userguide/getting_notifications_top_level.md")
- [Receiving CloudTrail Log Files from Multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail
  Log Files from Multiple Accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

AWS Control Tower logs the following actions as events in CloudTrail log files:

###### Public APIs

- For a full list of the AWS Control Tower public APIs and details about each one, see [The AWS Control Tower
  API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md"). Calls to these public APIs are logged by AWS CloudTrail.

###### Other APIs

- `SetupLandingZone`
- `UpdateAccountFactoryConfig`
- `ManageOrganizationalUnit`
- `CreateManagedAccount`
- `GetLandingZoneStatus`
- `GetHomeRegion`
- `ListManagedAccounts`
- `DescribeManagedAccount`
- `DescribeAccountFactoryConfig`
- `DescribeGuardrailForTarget`
- `DescribeManagedOrganizationalUnit`
- `ListEnabledGuardrails`
- `ListGuardrailViolations`
- `ListGuardrails`
- `ListGuardrailsForTarget`
- `ListManagedAccountsForGuardrail`
- `ListManagedAccountsForParent`
- `ListManagedOrganizationalUnits`
- `ListManagedOrganizationalUnitsForGuardrail`
- `GetGuardrailComplianceStatus`
- `DescribeGuardrail`
- `ListDirectoryGroups`
- `DescribeSingleSignOn`
- `DescribeCoreService`
- `GetAvailableUpdates`

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.
- Whether the request was rejected as access denied or processed successfully.

For more information, see the [CloudTrail userIdentity
Element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Example: AWS Control Tower Log File

Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail events don't appear in any specific order
in the log files.

The following example shows a CloudTrail log entry that shows the structure of a typical log
file entry for a `SetupLandingZone` AWS Control Tower event, including a record of the
identity of the user who initiated the action.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:backend-test-assume-role-session",
    "arn": "arn:aws:sts::76543EXAMPLE;:assumed-role/AWSControlTowerTestAdmin/backend-test-assume-role-session",
    "accountId": "76543EXAMPLE",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2018-11-20T19:36:11Z"
      },
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam::AKIAIOSFODNN7EXAMPLE:role/AWSControlTowerTestAdmin",
        "accountId": "AIDACKCEVSQ6C2EXAMPLE",
        "userName": "AWSControlTowerTestAdmin"
      }
    }
  },
  "eventTime": "2018-11-20T19:36:15Z",
  "eventSource": "controltower.amazonaws.com",
  "eventName": "SetupLandingZone",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "AWS Internal",
  "userAgent": "Coral/Netty4",
  "errorCode": "InvalidParametersException",
  "errorMessage": "Home region EU_CENTRAL_1 is unsupported",
  "requestParameters": {
    "homeRegion": "EU_CENTRAL_1",
    "logAccountEmail": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "sharedServiceAccountEmail": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "securityAccountEmail": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "securityNotificationEmail": "HIDDEN_DUE_TO_SECURITY_REASONS"
  },
  "responseElements": null,
  "requestID": "96f47b68-ed5f-4268-931c-807cd1f89a96",
  "eventID": "4ef5cf08-39e5-4fdf-9ea2-b07ced506851",
  "eventType": "AwsApiCall",
  "recipientAccountId": "76543EXAMPLE"
}

```

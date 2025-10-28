AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Logging Strategy Recommendations API calls with AWS CloudTrail

Migration Hub Strategy Recommendations is integrated with AWS CloudTrail, a service that provides a record of actions taken
by a user, role, or an AWS service in Strategy Recommendations. CloudTrail captures API calls for Strategy Recommendations as
events. The calls captured include calls from the Strategy Recommendations console and code calls to the
Strategy Recommendations API operations.

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket,
including events for Strategy Recommendations. If you don't configure a trail, you can still view the most
recent events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Strategy Recommendations, the IP address from
which the request was made, who made the request, when it was made, and additional details.

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Strategy Recommendations information in CloudTrail

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in
Strategy Recommendations, that activity is recorded in a CloudTrail event along with other AWS service events in
**Event history**. You can view, search, and download recent events in your
AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md").

For an ongoing record of events in your AWS account, including events for Strategy Recommendations,
create a trail. A _trail_ enables CloudTrail to deliver log files to an Amazon S3
bucket. By default, when you create a trail in the console, the trail applies to all
AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the
log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS
services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following:

- [Overview for creating a trail](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

Strategy Recommendations supports logging the following actions as events in CloudTrail log files:

- [GetApplicationComponentStrategies](../APIReference/API_GetApplicationComponentStrategies.md "../APIReference/API_GetApplicationComponentStrategies.md")
- [GetApplicationComponentDetails](../APIReference/API_GetApplicationComponentDetails.md "../APIReference/API_GetApplicationComponentDetails.md")
- [GetAssesment](../APIReference/API_GetAssessment.md "../APIReference/API_GetAssessment.md")
- [GetImportFileTask](../APIReference/API_GetImportFileTask.md "../APIReference/API_GetImportFileTask.md")
- [GetPortfolioPreferences](../APIReference/API_GetPortfolioPreferences.md "../APIReference/API_GetPortfolioPreferences.md")
- [GetPortfolioSummary](../APIReference/API_GetPortfolioSummary.md "../APIReference/API_GetPortfolioSummary.md")
- [GetServerDetails](../APIReference/API_GetServerDetails.md "../APIReference/API_GetServerDetails.md")
- [GetServerStrategies](../APIReference/API_GetServerStrategies.md "../APIReference/API_GetServerStrategies.md")
- [ListApplicationComponents](../APIReference/API_ListApplicationComponents.md "../APIReference/API_ListApplicationComponents.md")
- [ListCollectors](../APIReference/API_ListCollectors.md "../APIReference/API_ListCollectors.md")
- [ListImportFileTask](../APIReference/API_ListImportFileTask.md "../APIReference/API_ListImportFileTask.md")
- [ListServers](../APIReference/API_ListServers.md "../APIReference/API_ListServers.md")
- [PutPortfolioPreferences](../APIReference/API_PutPortfolioPreferences.md "../APIReference/API_PutPortfolioPreferences.md")
- [StartAssessment](../APIReference/API_StartAssessment.md "../APIReference/API_StartAssessment.md")
- [StartImportFileTask](../APIReference/API_StartImportFileTask.md "../APIReference/API_StartImportFileTask.md")
- [StopAssessment](../APIReference/API_StopAssessment.md "../APIReference/API_StopAssessment.md")
- [UpdateApplicationComponetConfig](../APIReference/API_UpdateApplicationComponetConfig.md "../APIReference/API_UpdateApplicationComponetConfig.md")
- [UpdateServerConfig](../APIReference/API_UpdateServerConfig.md "../APIReference/API_UpdateServerConfig.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
- Whether the request was made with temporary security credentials for a role or
  federated user
- Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md").

## Understanding Strategy Recommendations log file

entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the [GetServerDetails](../APIReference/API_GetServerDetails.md "../APIReference/API_GetServerDetails.md") action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "777777777777",
        "arn": "arn:aws:sts::111122223333:assumed-role/myUserName/...",
        "accountId": "111122223333",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "777777777777",
                "arn": "arn:aws:iam::111122223333:role/myUserName",
                "accountId": "111122223333",
                "userName": "myUserName"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "2021-09-20T01:07:16Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2021-09-20T01:07:43Z",
    "eventSource": "migrationhub-strategy.amazonaws.com",
    "eventName": "GetServerDetails",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "",
    "userAgent": "",
    "requestParameters": {
        "serverId": "ads-server-006"
    },
    "responseElements": null,
    "requestID": "07D681279BD94AED",
    "eventID": "cdc4b7ed-e171-4cef-975a-ad829d4123e8",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

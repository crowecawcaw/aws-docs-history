

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Logging Strategy Recommendations API calls with AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Migration Hub Strategy Recommendations is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Strategy Recommendations. CloudTrail captures API calls for Strategy Recommendations as events. The calls captured include calls from the Strategy Recommendations console and code calls to the Strategy Recommendations API operations. 

If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Strategy Recommendations. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Strategy Recommendations, the IP address from which the request was made, who made the request, when it was made, and additional details. 

To learn more about CloudTrail, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Strategy Recommendations information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is enabled on your AWS account when you create the account. When activity occurs in Strategy Recommendations, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html).

For an ongoing record of events in your AWS account, including events for Strategy Recommendations, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following: 
+ [Overview for creating a trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

Strategy Recommendations supports logging the following actions as events in CloudTrail log files:
+ [GetApplicationComponentStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentStrategies.html           )
+ [ GetApplicationComponentDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetApplicationComponentDetails.html)
+ [GetAssesment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetAssessment.html)
+ [GetImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetImportFileTask.html)
+ [GetPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioPreferences.html)
+ [GetPortfolioSummary](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetPortfolioSummary.html)
+ [GetServerDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html)
+ [GetServerStrategies](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerStrategies.html)
+ [ListApplicationComponents](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListApplicationComponents.html)
+ [ListCollectors](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListCollectors.html)
+ [ListImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListImportFileTask.html)
+ [ListServers](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_ListServers.html)
+ [PutPortfolioPreferences](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_PutPortfolioPreferences.html)
+ [StartAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartAssessment.html)
+ [StartImportFileTask](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StartImportFileTask.html)
+ [StopAssessment](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_StopAssessment.html)
+ [UpdateApplicationComponetConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateApplicationComponetConfig.html)
+ [UpdateServerConfig](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_UpdateServerConfig.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following: 
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials
+ Whether the request was made with temporary security credentials for a role or federated user
+ Whether the request was made by another AWS service

For more information, see the [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html).

## Understanding Strategy Recommendations log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the [GetServerDetails](https://docs.aws.amazon.com/migrationhub-strategy/latest/APIReference/API_GetServerDetails.html) action.

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
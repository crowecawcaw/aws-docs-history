# Logging Amazon Q Business API calls using

AWS CloudTrail

Amazon Q Business is integrated with AWS CloudTrail, a service that provides a record of
actions taken by a user, role, or an AWS service in Amazon Q Business. CloudTrail captures all
API calls for Amazon Q Business as events. The calls captured include calls from the
Amazon Q console and code calls to the Amazon Q Business API operations. A
_trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. If you create
a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events
for Amazon Q Business. If you don't configure a trail, you can still view the most recent
events in the CloudTrail console in **Event history**. Using the information
collected by CloudTrail, you can determine the request that was made to Amazon Q Business, the
IP address from which the request was made, who made the request, when it was made, and
additional details.

For more information about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md").

## Amazon Q Business information in

CloudTrail

CloudTrail is activated on your AWS account when you create the account. When activity occurs
in Amazon Q Business, that activity is recorded in a CloudTrail event along with other
AWS service events in **Event history**. You can view, search, and download
recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_.

For an ongoing record of events in your AWS account, including events for Amazon Q, create a trail. A _trail_ enables CloudTrail to deliver log files
to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to
all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers
the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other
AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more
information, see the following topics:

- [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md")
- [CloudTrail supported services and integrations](../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md "../../../awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.md")
- [Configuring Amazon SNS notifications for CloudTrail](../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md "../../../awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.md")
- [Receiving CloudTrail log files from multiple Regions](../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md "../../../awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.md") and [Receiving CloudTrail log files from multiple accounts](../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md "../../../awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.md")

## Control plane events in CloudTrail

CloudTrail supports logging the following Amazon Q Business actions documented in the
[Amazon Q Business API Reference](../api-reference/Welcome.md "../api-reference/Welcome.md"):

- [CreateApplication](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md")
- [DeleteApplication](../api-reference/API_DeleteApplication.md "../api-reference/API_DeleteApplication.md")
- [GetApplication](../api-reference/API_GetApplication.md "../api-reference/API_GetApplication.md")
- [ListApplications](../api-reference/API_ListApplications.md "../api-reference/API_ListApplications.md")
- [UpdateApplication](../api-reference/API_UpdateApplication.md "../api-reference/API_UpdateApplication.md")
- [DeleteChatControlsConfiguration](../api-reference/API_DeleteChatControlsConfiguration.md "../api-reference/API_DeleteChatControlsConfiguration.md")
- [GetChatControlsConfiguration](../api-reference/API_GetChatControlsConfiguration.md "../api-reference/API_GetChatControlsConfiguration.md")
- [UpdateChatControlsConfiguration](../api-reference/API_UpdateChatControlsConfiguration.md "../api-reference/API_UpdateChatControlsConfiguration.md")
- [CreateDataSource](../api-reference/API_CreateApplication.md "../api-reference/API_CreateApplication.md")
- [DeleteDataSource](../api-reference/API_DeleteDataSource.md "../api-reference/API_DeleteDataSource.md")
- [GetDataSource](../api-reference/API_ListDataSources.md "../api-reference/API_ListDataSources.md")
- [ListDataSources](../api-reference/API_ListDataSources.md "../api-reference/API_ListDataSources.md")
- [UpdateDataSource](../api-reference/API_UpdateDataSource.md "../api-reference/API_UpdateDataSource.md")
- [CreateWebExperience](../api-reference/API_CreateWebExperience.md "../api-reference/API_CreateWebExperience.md")
- [DeleteWebExperience](../api-reference/API_DeleteWebExperience.md "../api-reference/API_DeleteWebExperience.md")
- [ListWebExperiences](../api-reference/API_ListTagsForResource.md "../api-reference/API_ListTagsForResource.md")
- [UpdateWebExperience](../api-reference/API_UpdateWebExperience.md "../api-reference/API_UpdateWebExperience.md")
- [CreateIndex](../api-reference/API_CreateIndex.md "../api-reference/API_CreateIndex.md")
- [DeleteIndex](../api-reference/API_DeleteIndex.md "../api-reference/API_DeleteIndex.md")
- [GetIndex](../api-reference/API_GetIndex.md "../api-reference/API_GetIndex.md")
- [ListIndices](../api-reference/API_ListIndices.md "../api-reference/API_ListIndices.md")
- [UpdateIndex](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md")
- [CreatePlugin](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md")
- [DeletePlugin](../api-reference/API_DeleteIndex.md "../api-reference/API_DeleteIndex.md")
- [GetPlugin](../api-reference/API_GetPlugin.md "../api-reference/API_GetPlugin.md")
- [ListPlugins](../api-reference/API_GetPlugin.md "../api-reference/API_GetPlugin.md")
- [UpdatePlugin](../api-reference/API_UpdateIndex.md "../api-reference/API_UpdateIndex.md")
- [CreateRetriever](../api-reference/API_CreatePlugin.md "../api-reference/API_CreatePlugin.md")
- [DeleteRetriever](../api-reference/API_DeleteRetriever.md "../api-reference/API_DeleteRetriever.md")
- [GetRetriever](../api-reference/API_GetRetriever.md "../api-reference/API_GetRetriever.md")
- [ListRetrievers](../api-reference/API_ListRetrievers.md "../api-reference/API_ListRetrievers.md")
- [UpdateRetriever](../api-reference/API_UpdateRetriever.md "../api-reference/API_UpdateRetriever.md")
- [ListTagsForResource](../api-reference/API_ListTagsForResource.md "../api-reference/API_ListTagsForResource.md")
- [TagResource](../api-reference/API_TagResource.md "../api-reference/API_TagResource.md")
- [UntagResource](../api-reference/API_TagResource.md "../api-reference/API_TagResource.md")

Every event or log entry contains information about who generated the request. The
identity information helps you determine the following:

- Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
- Whether the request was made with temporary security credentials for a role or
  federated user.
- Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.md") in the _AWS CloudTrail User Guide_.

## Data plane events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3 object). These are also known as
_data plane operations_. By default, CloudTrail doesn't log data
events.

The following table shows the Amazon Q Business API operations logged to CloudTrail as
_data events_. The **Data event type
(console)** column shows the appropriate selection in the CloudTrail console. The
**Amazon Q Business resource types** column shows the
`resources.type` value that you would specify to log data events for the
resource.

| Data event type (console)           | Amazon Q Business resource types | Supported data events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------- | -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon Q Business application**   | `AWS::QBusiness::Application`    | • [ListDataSourceSyncJobs](../api-reference/API_ListDataSourceSyncJobs.md "../api-reference/API_ListDataSourceSyncJobs.md")<br>• [StartDataSourceSyncJob](../api-reference/API_StartDataSourceSyncJob.md "../api-reference/API_StartDataSourceSyncJob.md")<br>• [StopDataSourceSyncJob](../api-reference/API_StartDataSourceSyncJob.md "../api-reference/API_StartDataSourceSyncJob.md")<br>• [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md")<br>• [BatchDeleteDocument](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md")<br>• [PutFeedback](../api-reference/API_PutFeedback.md "../api-reference/API_PutFeedback.md")<br>• [ChatSync](../api-reference/API_ChatSync.md "../api-reference/API_ChatSync.md")<br>• [Chat](../api-reference/API_Chat.md "../api-reference/API_Chat.md")<br>• [DeleteConversation](../api-reference/API_DeleteConversation.md "../api-reference/API_DeleteConversation.md")<br>• [ListConversations](../api-reference/API_ListConversations.md "../api-reference/API_ListConversations.md")<br>• [ListMessages](../api-reference/API_ListMessages.md "../api-reference/API_ListMessages.md")<br>• [ListGroups](../api-reference/API_ListGroups.md "../api-reference/API_ListGroups.md")<br>• [DeleteGroup](../api-reference/API_DeleteGroup.md "../api-reference/API_DeleteGroup.md")<br>• [GetGroup](../api-reference/API_GetGroup.md "../api-reference/API_GetGroup.md")<br>• [PutGroup](../api-reference/API_PutGroup.md "../api-reference/API_PutGroup.md")<br>• [CreateUser](../api-reference/API_CreateUser.md "../api-reference/API_CreateUser.md")<br>• [DeleteUser](../api-reference/API_DeleteUser.md "../api-reference/API_DeleteUser.md")<br>• [GetUser](../api-reference/API_GetUser.md "../api-reference/API_GetUser.md")<br>• [UpdateUser](../api-reference/API_UpdateUser.md "../api-reference/API_UpdateUser.md")<br>• [ListDocuments](../api-reference/API_ListDocuments.md "../api-reference/API_ListDocuments.md") |
| **Amazon Q Business data resource** | `AWS::QBusiness::DataSource`     | • [ListDataSourceSyncJobs](../api-reference/API_ListDataSourceSyncJobs.md "../api-reference/API_ListDataSourceSyncJobs.md")<br>• [StartDataSourceSyncJob](../api-reference/API_StartDataSourceSyncJob.md "../api-reference/API_StartDataSourceSyncJob.md")<br>• [StopDataSourceSyncJob](../api-reference/API_StartDataSourceSyncJob.md "../api-reference/API_StartDataSourceSyncJob.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Amazon Q Business index**         | `AWS::QBusiness::Index`          | • [DeleteGroup](../api-reference/API_DeleteGroup.md "../api-reference/API_DeleteGroup.md")<br>• [GetGroup](../api-reference/API_GetGroup.md "../api-reference/API_GetGroup.md")<br>• [PutGroup](../api-reference/API_PutGroup.md "../api-reference/API_PutGroup.md")<br>• [ListGroups](../api-reference/API_ListGroups.md "../api-reference/API_ListGroups.md")<br>• [ListDocuments](../api-reference/API_ListDocuments.md "../api-reference/API_ListDocuments.md")<br>• [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md")<br>• [BatchDeleteDocument](../api-reference/API_BatchDeleteDocument.md "../api-reference/API_BatchDeleteDocument.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

You can log these API operations by configuring advanced event selectors to record data
events for the Amazon Q Business resource types:
`AWS::QBusiness::Application`, `AWS::QBusiness::DataSource`, and
`AWS::QBusiness::Index`. To configure advanced event selectors, you can use
either the CloudTrail console or the AWS CLI:

- From the CloudTrail console, choose the **Data event type** for which you
  want to log data events. Additionally, you can filter on the `eventName` and
  `resources.ARN` fields by choosing a custom log selector template. For more
  information, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") in the _AWS CloudTrail
  User Guide_.
- From the AWS CLI, specify the `resources.type` value for which you want to
  log data events and set the `eventCategory` equal to `Data`. For
  more information, see [Logging data events with the AWS CLI](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the _AWS CloudTrail
  User Guide_.

The following example shows how to configure a trail to log all Amazon Q Business data events for all Amazon Q Business resource types.

```
aws cloudtrail put-event-selectors --trail-name `trailName` \
--advanced-event-selectors \
'[
  {
    "Name": "Log all data events on an Amazon Q Business application",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::QBusiness::Application"] }
    ]
  },
  {
    "Name": "Log all data events on an Amazon Q Business data source",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::QBusiness::DataSource"] }
    ]
  },
  {
    "Name": "Log all data events on an Amazon Q Business index",
    "FieldSelectors": [
      { "Field": "eventCategory", "Equals": ["Data"] },
      { "Field": "resources.type", "Equals": ["AWS::QBusiness::Index"] }
    ]
  }
]'
```

You can additionally filter on the `eventName` and
`resources.ARN` fields. For more information about configuring these fields,
see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the _AWS CloudTrail API
Reference_.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Amazon Q Business management

events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are
performed on resources in your AWS account. These management events are also known as
_control plane operations_. CloudTrail logs management event API
operations by default.

Amazon Q Business logs the remainder of Amazon Q Business API operations as
management events. For a list of the Amazon Q Business API operations that Amazon Q logs to CloudTrail, see the [Amazon Q Business API
Reference](../api-reference/Welcome.md "../api-reference/Welcome.md").

## Understanding Amazon Q Business log

file entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the
`CreateApplication` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "`AssumedRole`",
        "principalId": "`principal ID`",
        "arn": "`ARN`",
        "accountId": "`account ID`",
        "accessKeyId": "`access key ID`",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "`principal ID`",
                "arn": "`ARN`",
                "accountId": "`account ID`",
                "userName": "`user name`"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "`yyyy-mm-ddThh:mm:ssZ`",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "`yyyy-mm-ddThh:mm:ssZ`",
    "eventSource": "qbusiness.amazonaws.com",
    "eventName": "`CreateApplication`",
    "awsRegion": "`region`",
    "sourceIPAddress": "`region`",
    "userAgent": "`user agent`",
    "requestParameters": {
        "name": "`name`",
        "roleArn": "`description`",
        "clientToken": "`client token`"
    },
    "responseElements": {
        "applicationId": "`application ID`"
    },
    "requestID": "`request ID`",
    "eventID": "`event ID`",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account ID`",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "`TLS version`",
        "cipherSuite":  "`cipher suite`",
        "clientProvidedHostHeader": "qbusiness.us-west-2.api.aws"
    }
}
```



Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Logging Amazon Q Business API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Amazon Q Business is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Q Business. CloudTrail captures all API calls for Amazon Q Business as events. The calls captured include calls from the Amazon Q console and code calls to the Amazon Q Business API operations. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. If you create a trail, you can enable continuous delivery of CloudTrail events to an Amazon S3 bucket, including events for Amazon Q Business. If you don't configure a trail, you can still view the most recent events in the CloudTrail console in **Event history**. Using the information collected by CloudTrail, you can determine the request that was made to Amazon Q Business, the IP address from which the request was made, who made the request, when it was made, and additional details.

For more information about CloudTrail, including how to configure and activate it, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).

## Amazon Q Business information in CloudTrail
<a name="service-name-info-in-cloudtrail"></a>

CloudTrail is activated on your AWS account when you create the account. When activity occurs in Amazon Q Business, that activity is recorded in a CloudTrail event along with other AWS service events in **Event history**. You can view, search, and download recent events in your AWS account. For more information, see [Viewing events with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*.

For an ongoing record of events in your AWS account, including events for Amazon Q, create a trail. A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs. For more information, see the following topics:
+ [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html)
+ [CloudTrail supported services and integrations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-aws-service-specific-topics.html)
+ [Configuring Amazon SNS notifications for CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/configure-sns-notifications-for-cloudtrail.html)
+ [Receiving CloudTrail log files from multiple Regions](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/receive-cloudtrail-log-files-from-multiple-regions.html) and [Receiving CloudTrail log files from multiple accounts](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-receive-logs-from-multiple-accounts.html)

## Control plane events in CloudTrail
<a name="service-name-control-plane-events-cloudtrail"></a>

CloudTrail supports logging the following Amazon Q Business actions documented in the [Amazon Q Business API Reference](https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome.html):
+ [CreateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html)
+ [DeleteApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteApplication.html)
+ [GetApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetApplication.html)
+ [ListApplications](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListApplications.html)
+ [UpdateApplication](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateApplication.html)
+ [DeleteChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteChatControlsConfiguration.html)
+ [GetChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetChatControlsConfiguration.html)
+ [UpdateChatControlsConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateChatControlsConfiguration.html)
+ [CreateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateApplication.html)
+ [DeleteDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteDataSource.html)
+ [GetDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSources.html)
+ [ListDataSources](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSources.html)
+ [UpdateDataSource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateDataSource.html)
+ [CreateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateWebExperience.html)
+ [DeleteWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteWebExperience.html)
+ [ListWebExperiences](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html)
+ [UpdateWebExperience](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateWebExperience.html)
+ [CreateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateIndex.html)
+ [DeleteIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIndex.html)
+ [GetIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetIndex.html)
+ [ListIndices](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListIndices.html)
+ [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html)
+ [CreatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html)
+ [DeletePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteIndex.html)
+ [GetPlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPlugin.html)
+ [ListPlugins](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetPlugin.html)
+ [UpdatePlugin](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html)
+ [CreateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreatePlugin.html)
+ [DeleteRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteRetriever.html)
+ [GetRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetRetriever.html)
+ [ListRetrievers](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListRetrievers.html)
+ [UpdateRetriever](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateRetriever.html)
+ [ListTagsForResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListTagsForResource.html)
+ [TagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html)
+ [UntagResource](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_TagResource.html)

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root or AWS Identity and Access Management (IAM) user credentials.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

For more information, see [CloudTrail userIdentity element](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-user-identity.html) in the *AWS CloudTrail User Guide*.

## Data plane events in CloudTrail
<a name="service-name-data-plane-events-cloudtrail"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These are also known as *data plane operations*. By default, CloudTrail doesn't log data events.

The following table shows the Amazon Q Business API operations logged to CloudTrail as *data events*. The **Data event type (console)** column shows the appropriate selection in the CloudTrail console. The **Amazon Q Business resource types** column shows the `resources.type` value that you would specify to log data events for the resource.


| Data event type (console) | Amazon Q Business resource types | Supported data events | 
| --- | --- | --- | 
| Amazon Q Business application |  AWS::QBusiness::Application  |  +  [ListDataSourceSyncJobs](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSourceSyncJobs.html) <br />+  [StartDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html) <br />+  [StopDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html) <br />+  [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) <br />+  [BatchDeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchDeleteDocument.html) <br />+  [PutFeedback](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html) <br />+  [ChatSync](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ChatSync.html) <br />+  [Chat](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Chat.html) <br />+  [DeleteConversation](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteConversation.html) <br />+  [ListConversations](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListConversations.html) <br />+  [ListMessages](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListMessages.html) <br />+  [ListGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListGroups.html) <br />+  [DeleteGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteGroup.html) <br />+  [GetGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetGroup.html) <br />+  [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html) <br />+  [CreateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateUser.html) <br />+  [DeleteUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteUser.html) <br />+  [GetUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetUser.html) <br />+  [UpdateUser](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateUser.html) <br />+  [ListDocuments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDocuments.html)   | 
| Amazon Q Business data resource |  AWS::QBusiness::DataSource  |  +  [ListDataSourceSyncJobs](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDataSourceSyncJobs.html) <br />+  [StartDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html) <br />+  [StopDataSourceSyncJob](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_StartDataSourceSyncJob.html)   | 
| Amazon Q Business index |  AWS::QBusiness::Index  |  +  [DeleteGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DeleteGroup.html) <br />+  [GetGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_GetGroup.html) <br />+  [PutGroup](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutGroup.html) <br />+  [ListGroups](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListGroups.html) <br />+  [ListDocuments](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_ListDocuments.html) <br />+  [BatchPutDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html) <br />+  [BatchDeleteDocument](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchDeleteDocument.html)   | 

You can log these API operations by configuring advanced event selectors to record data events for the Amazon Q Business resource types: `AWS::QBusiness::Application`, `AWS::QBusiness::DataSource`, and `AWS::QBusiness::Index`. To configure advanced event selectors, you can use either the CloudTrail console or the AWS CLI:
+ From the CloudTrail console, choose the **Data event type** for which you want to log data events. Additionally, you can filter on the `eventName` and `resources.ARN` fields by choosing a custom log selector template. For more information, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) in the *AWS CloudTrail User Guide*.
+ From the AWS CLI, specify the `resources.type` value for which you want to log data events and set the `eventCategory` equal to `Data`. For more information, see [ Logging data events with the AWS CLI](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

  The following example shows how to configure a trail to log all Amazon Q Business data events for all Amazon Q Business resource types.

  ```
  aws cloudtrail put-event-selectors --trail-name {{trailName}} \
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

  You can additionally filter on the `eventName` and `resources.ARN` fields. For more information about configuring these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## Amazon Q Business management events in CloudTrail
<a name="service-name-management-events-cloudtrail"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These management events are also known as *control plane operations*. CloudTrail logs management event API operations by default.

Amazon Q Business logs the remainder of Amazon Q Business API operations as management events. For a list of the Amazon Q Business API operations that Amazon Q logs to CloudTrail, see the [Amazon Q Business API Reference](https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome.html).

## Understanding Amazon Q Business log file entries
<a name="understanding-service-name-entries"></a>

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket that you specify. CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order. 

The following example shows a CloudTrail log entry that demonstrates the `CreateApplication` action.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "{{AssumedRole}}",
        "principalId": "{{principal ID}}",
        "arn": "{{ARN}}",
        "accountId": "{{account ID}}",
        "accessKeyId": "{{access key ID}}",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "{{principal ID}}",
                "arn": "{{ARN}}",
                "accountId": "{{account ID}}",
                "userName": "{{user name}}"
            },
            "webIdFederationData": {},
            "attributes": {
                "creationDate": "{{yyyy-mm-ddThh:mm:ssZ}}",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "{{yyyy-mm-ddThh:mm:ssZ}}",
    "eventSource": "qbusiness.amazonaws.com",
    "eventName": "{{CreateApplication}}",
    "awsRegion": "{{region}}",
    "sourceIPAddress": "{{region}}",
    "userAgent": "{{user agent}}",
    "requestParameters": {
        "name": "{{name}}",
        "roleArn": "{{description}}",
        "clientToken": "{{client token}}"
    },
    "responseElements": {
        "applicationId": "{{application ID}}"
    },
    "requestID": "{{request ID}}",
    "eventID": "{{event ID}}",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "{{account ID}}",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "{{TLS version}}",
        "cipherSuite":  "{{cipher suite}}",
        "clientProvidedHostHeader": "qbusiness.us-west-2.api.aws"
    }
}
```
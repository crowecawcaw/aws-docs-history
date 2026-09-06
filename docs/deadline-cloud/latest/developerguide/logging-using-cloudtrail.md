

# Logging Deadline Cloud API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Deadline Cloud is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Deadline Cloud as events. The calls captured include calls from the Deadline Cloud console and code calls to the Deadline Cloud API operations. Using the information collected by CloudTrail, you can determine the request that was made to Deadline Cloud, the IP address from which the request was made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity information helps you determine the following:
+ Whether the request was made with root user or user credentials.
+ Whether the request was made on behalf of an IAM Identity Center user.
+ Whether the request was made with temporary security credentials for a role or federated user.
+ Whether the request was made by another AWS service.

CloudTrail is active in your AWS account when you create the account and you automatically have access to the CloudTrail **Event history**. The CloudTrail **Event history** provides a viewable, searchable, downloadable, and immutable record of the past 90 days of recorded management events in an AWS Region. For more information, see [Working with CloudTrail Event history](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) in the *AWS CloudTrail User Guide*. There are no CloudTrail charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a [CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) event data store.

**CloudTrail trails**  
A *trail* enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) and [Creating a trail for an organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*.  
You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/).

**CloudTrail Lake event data stores**  
*CloudTrail Lake* lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [ Apache ORC](https://orc.apache.org/) format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into *event data stores*, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-concepts.html#adv-event-selectors). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) in the *AWS CloudTrail User Guide*.  
CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.html#cloudtrail-lake-manage-costs-pricing-option) you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

## Deadline Cloud data events in CloudTrail
<a name="cloudtrail-data-events"></a>

[Data events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events) provide information about the resource operations performed on or in a resource (for example, reading or writing to an Amazon S3 object). These operations are also known as data plane operations. Data events are often high-volume activities. By default, CloudTrail doesn't log data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/).

You can log data events for the Deadline Cloud resource types by using the CloudTrail console, AWS CLI, or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#logging-data-events-console) and [Logging data events with the AWS Command Line Interface](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html#creating-data-event-selectors-with-the-AWS-CLI) in the *AWS CloudTrail User Guide*.

The following table lists the Deadline Cloud resource types for which you can log data events. The **Data event type (console)** column shows the value to choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type` value, which you would specify when configuring advanced event selectors using the AWS CLI or CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API calls logged to CloudTrail for the resource type. 


| Data event type (console) | resources.type value | Data APIs logged to CloudTrail | 
| --- | --- | --- | 
| Deadline Fleet |  AWS::Deadline::Fleet  |  +  [SearchWorkers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchWorkers.html)   | 
| Deadline Queue |  AWS::Deadline::Fleet  |  +  [SearchJobs](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchJobs.html)   | 
| Deadline Worker |  AWS::Deadline::Worker  |  +  [GetWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetWorker.html) <br />+  [ListSessionsForWorker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessionsForWorker.html) <br />+  [UpdateWorkerSchedule](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorkerSchedule.html) <br />+  [BatchGetJobEntity](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_BatchGetJobEntity.html) <br />+  [ListWorkers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListWorkers.html)   | 
| Deadline Job |  AWS::Deadline::Job  |  +  [ListStepConsumers](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStepConsumers.html) <br />+  [UpdateTask](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateTask.html) <br />+  [ListJobs](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobs.html) <br />+  [GetStep](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStep.html) <br />+  [ListSteps](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSteps.html) <br />+  [GetJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetJob.html) <br />+  [GetTask](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetTask.html) <br />+  [GetSession](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSession.html) <br />+  [ListSessions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessions.html) <br />+  [CreateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateJob.html) <br />+  [ListSessionActions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListSessionActions.html) <br />+  [ListTasks](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListTasks.html) <br />+  [CopyJobTemplate](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CopyJobTemplate.html) <br />+  [UpdateSession](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateSession.html) <br />+  [UpdateStep](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateStep.html) <br />+  [UpdateJob](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateJob.html) <br />+  [ListJobParameterDefinitions](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobParameterDefinitions.html) <br />+  [GetSessionAction](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSessionAction.html) <br />+  [ListStepDependencies](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStepDependencies.html) <br />+  [SearchTasks](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchTasks.html) <br />+  [SearchSteps](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_SearchSteps.html)   | 

You can configure advanced event selectors to filter on the `eventName`, `readOnly`, and `resources.ARN` fields to log only those events that are important to you. For more information about these fields, see [AdvancedFieldSelector](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.html) in the *AWS CloudTrail API Reference*.

## Deadline Cloud management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Deadline Cloud logs the following Deadline Cloud control plane operations to CloudTrail as *management events*.
+ [associate-member-to-farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToFarm.html)
+ [associate-member-to-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToFleet.html)
+ [associate-member-to-job](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToJob.html)
+ [associate-member-to-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssociateMemberToQueue.html)
+ [assume-fleet-role-for-read](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForRead.html)
+ [assume-fleet-role-for-worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeFleetRoleForWorker.html)
+ [assume-queue-role-for-read](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForRead.html)
+ [assume-queue-role-for-user](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForUser.html)
+ [assume-queue-role-for-worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssumeQueueRoleForWorker.html)
+ [create-budget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateBudget.html)
+ [create-farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFarm.html)
+ [create-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateFleet.html)
+ [create-license-endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLicenseEndpoint.html)
+ [create-limit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateLimit.html)
+ [create-monitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateMonitor.html)
+ [create-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueue)
+ [create-queue-environment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueEnvironment.html)
+ [create-queue-fleet-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueFleetAssociation.html)
+ [create-queue-limit-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateQueueLimitAssociation.html)
+ [create-storage-profile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateStorageProfile)
+ [create-worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_CreateWorker)
+ [delete-budget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteBudget)
+ [delete-farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteFarm.html)
+ [delete-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteFleet.html)
+ [delete-license-endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteLicenseEndpoint.html)
+ [delete-limit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteLimit.html)
+ [delete-metered-product](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteMeteredProduct.html)
+ [delete-monitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteMonitor.html)
+ [delete-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueue.html)
+ [delete-queue-environment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueEnvironment.html)
+ [delete-queue-fleet-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueFleetAssociation.html)
+ [delete-queue-limit-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteQueueLimitAssociation.html)
+ [delete-storage-profile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteStorageProfile.html)
+ [delete-worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DeleteWorker.html)
+ [disassociate-member-from-farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromFarm.html)
+ [disassociate-member-from-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromFleet.html)
+ [disassociate-member-from-job](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromJob.html)
+ [disassociate-member-from-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_DisassociateMemberFromQueue.html)
+ [get-application-version](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetApplicationVersion.html)
+ [get-budget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetBudget.html)
+ [get-farm](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFarm.html)
+ [get-feature-map](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFeatureMap.html)
+ [get-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetFleet.html)
+ [get-license-endpoint](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetLicenseEndpoint.html)
+ [get-limit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetLimit.html)
+ [get-monitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetMonitor.html)
+ [get-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueue.html)
+ [get-queue-environment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueEnvironment.html)
+ [get-queue-fleet-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueFleetAssociation.html)
+ [get-queue-limit-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetQueueLimitAssociation.html)
+ [get-sessions-statistics-aggregation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetSessionsStatisticsAggregation.html)
+ [get-storage-profile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfile.html)
+ [get-storage-profile-for-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_GetStorageProfileForQueue.html)
+ [list-available-metered-products](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListAvailableMeteredProducts.html)
+ [list-budgets](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListBudgets.html)
+ [list-farm-members](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFarmMembers.html)
+ [list-farms](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFarms.html)
+ [list-fleet-members](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFleetMembers.html)
+ [list-fleets](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListFleets.html)
+ [list-job-members](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListJobMembers.html)
+ [list-license-endpoints](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListLicenseEndpoints.html)
+ [list-limit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListLImit.html)
+ [list-metered-products](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListMeteredProducts.html)
+ [list-monitors](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListMonitors.html)
+ [list-queue-environments](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueEnvironments.html)
+ [list-queue-fleet-associations](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueFleetAssociations.html)
+ [list-queue-limit-associations](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueLimitAssociations.html)
+ [list-queue-members](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueueMembers.html)
+ [list-queues](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListQueues.html)
+ [list-storage-profiles](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStorageProfiles.html)
+ [list-storage-profiles-for-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListStorageProfilesForQueue.html)
+ [list-tags-for-resource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_ListTagsForResources.html)
+ [put-metered-product](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_PutMeteredProduct.html)
+ [start-sessions-statistics-aggregation](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StartSessionsStatisticsAggregation.html)
+ [tag-resource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_TagResource.html)
+ [untag-resource](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UntagResource.html)
+ [update-budget](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateBudget.html)
+ [update-farm ](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFarm.html)
+ [update-fleet](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateFleet.html)
+ [update-limit](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateLimit.html)
+ [update-monitor](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateMonitor.html)
+ [update-queue](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueue.html)
+ [update-queue-environment](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueEnvironment.html)
+ [update-queue-fleet-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueFleetAssociation.html)
+ [update-queue-limit-association](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateQueueLimitAssociation.html)
+ [update-storage-profile](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateStorageProfile.html)
+ [update-worker](https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_UpdateWorker.html)

## Deadline Cloud event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `CreateFarm` operation.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "EXAMPLE-PrincipalID:EXAMPLE-Session",
        "arn": "arn:aws:sts::111122223333:assumed-role/EXAMPLE-UserName/EXAMPLE-Session",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE-accessKeyId",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "EXAMPLE-PrincipalID",
                "arn": "arn:aws:iam::111122223333:role/EXAMPLE-UserName",
                "accountId": "111122223333",
                "userName": "EXAMPLE-UserName"
            },
            "webIdFederationData": {},
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2021-03-08T23:25:49Z"
            }
        }
    },
    "eventTime": "2021-03-08T23:25:49Z",
    "eventSource": "deadline.amazonaws.com",
    "eventName": "CreateFarm",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "EXAMPLE-userAgent",
    "requestParameters": {
        "displayName": "example-farm",
        "kmsKeyArn": "arn:aws:kms:us-west-2:111122223333:key/111122223333",
        "X-Amz-Client-Token": "12abc12a-1234-1abc-123a-1a11bc1111a",
        "description": "example-description",
        "tags": {
            "purpose_1": "e2e",
            "purpose_2": "tag_test"
        }
    },
    "responseElements": {
        "farmId": "EXAMPLE-farmID"
    },
    "requestID": "EXAMPLE-requestID",
    "eventID": "EXAMPLE-eventID",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

The JSON example shows the AWS Region, IP address, and other "`requestParameters`" such as the "`displayName`" and "`kmsKeyArn`" that can help you identify the event.

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.
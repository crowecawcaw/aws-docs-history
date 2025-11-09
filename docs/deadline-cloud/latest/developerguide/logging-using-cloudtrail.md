# Logging Deadline Cloud API calls using

AWS CloudTrail

Deadline Cloud is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for Deadline Cloud as events. The calls captured include calls from the Deadline Cloud console
and code calls to the Deadline Cloud API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Deadline Cloud, the IP address from which the request was
made, when it was made, and additional details.

Every event or log entry contains information about who generated the request. The identity
information helps you determine the following:

- Whether the request was made with root user or user credentials.
- Whether the request was made on behalf of an IAM Identity Center user.
- Whether the request was made with temporary security credentials for a role or federated
  user.
- Whether the request was made by another AWS service.
  CloudTrail is active in your AWS account when you create the account and you automatically have
  access to the CloudTrail **Event history**. The CloudTrail **Event
  history** provides a viewable, searchable, downloadable, and immutable record of the
  past 90 days of recorded management events in an AWS Region. For more information, see [Working
  with CloudTrail Event history](../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md "../../../awscloudtrail/latest/userguide/view-cloudtrail-events.md") in the _AWS CloudTrail User Guide_. There are no CloudTrail
  charges for viewing the **Event history**.

For an ongoing record of events in your AWS account past 90 days, create a trail or a
[CloudTrail
Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") event data store.

**CloudTrail trails**

A _trail_ enables CloudTrail to deliver log files to an Amazon S3 bucket. All trails created using the AWS Management Console are multi-Region. You can create a single-Region or a multi-Region trail by using the AWS CLI. Creating a multi-Region trail is recommended because you capture activity in all AWS Regions in your account. If you create a single-Region trail, you can view only the events logged in the trail's AWS Region. For more information about trails, see [Creating a trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md") and [Creating a trail for an organization](../../../awscloudtrail/latest/userguide/creating-trail-organization.md "../../../awscloudtrail/latest/userguide/creating-trail-organization.md") in the _AWS CloudTrail User Guide_.

You can deliver one copy of your ongoing management events to your Amazon S3 bucket at no charge from CloudTrail by creating a trail, however, there are Amazon S3 storage charges. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/"). For information about Amazon S3 pricing, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

**CloudTrail Lake event data stores**

_CloudTrail Lake_ lets you run SQL-based queries on your events. CloudTrail Lake converts existing events in row-based JSON format to [Apache ORC](https://orc.apache.org/ "https://orc.apache.org/") format. ORC is a columnar storage format that is optimized for fast retrieval of data. Events are aggregated into _event data stores_, which are immutable collections of events based on criteria that you select by applying [advanced event selectors](../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors "../../../awscloudtrail/latest/userguide/cloudtrail-lake-concepts.md#adv-event-selectors"). The selectors that you apply to an event data store control which events persist and are available for you to query. For more information about CloudTrail Lake, see [Working with AWS CloudTrail Lake](../../../awscloudtrail/latest/userguide/cloudtrail-lake.md "../../../awscloudtrail/latest/userguide/cloudtrail-lake.md") in the _AWS CloudTrail User Guide_.

CloudTrail Lake event data stores and queries incur costs. When you create an event data store, you choose the [pricing option](../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option "../../../awscloudtrail/latest/userguide/cloudtrail-lake-manage-costs.md#cloudtrail-lake-manage-costs-pricing-option") you want to use for the event data store. The pricing option determines the cost for ingesting and storing events, and the default and maximum retention period for the event data store. For more information about CloudTrail pricing, see [AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

## Deadline Cloud data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3 object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the Deadline Cloud resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the Deadline Cloud resource types for which you can log data events.
The **Data event type (console)** column shows the value to
choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

| Data event type (console) | resources.type value    | Data APIs logged to CloudTrail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Deadline Fleet**        | `AWS::Deadline::Fleet`  | • [SearchWorkers](../APIReference/API_SearchWorkers.md "../APIReference/API_SearchWorkers.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Deadline Queue**        | `AWS::Deadline::Fleet`  | • [SearchJobs](../APIReference/API_SearchJobs.md "../APIReference/API_SearchJobs.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Deadline Worker**       | `AWS::Deadline::Worker` | • [GetWorker](../APIReference/API_GetWorker.md "../APIReference/API_GetWorker.md")<br>• [ListSessionsForWorker](../APIReference/API_ListSessionsForWorker.md "../APIReference/API_ListSessionsForWorker.md")<br>• [UpdateWorkerSchedule](../APIReference/API_UpdateWorkerSchedule.md "../APIReference/API_UpdateWorkerSchedule.md")<br>• [BatchGetJobEntity](../APIReference/API_BatchGetJobEntity.md "../APIReference/API_BatchGetJobEntity.md")<br>• [ListWorkers](../APIReference/API_ListWorkers.md "../APIReference/API_ListWorkers.md")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Deadline Job**          | `AWS::Deadline::Job`    | • [ListStepConsumers](../APIReference/API_ListStepConsumers.md "../APIReference/API_ListStepConsumers.md")<br>• [UpdateTask](../APIReference/API_UpdateTask.md "../APIReference/API_UpdateTask.md")<br>• [ListJobs](../APIReference/API_ListJobs.md "../APIReference/API_ListJobs.md")<br>• [GetStep](../APIReference/API_GetStep.md "../APIReference/API_GetStep.md")<br>• [ListSteps](../APIReference/API_ListSteps.md "../APIReference/API_ListSteps.md")<br>• [GetJob](../APIReference/API_GetJob.md "../APIReference/API_GetJob.md")<br>• [GetTask](../APIReference/API_GetTask.md "../APIReference/API_GetTask.md")<br>• [GetSession](../APIReference/API_GetSession.md "../APIReference/API_GetSession.md")<br>• [ListSessions](../APIReference/API_ListSessions.md "../APIReference/API_ListSessions.md")<br>• [CreateJob](../APIReference/API_CreateJob.md "../APIReference/API_CreateJob.md")<br>• [ListSessionActions](../APIReference/API_ListSessionActions.md "../APIReference/API_ListSessionActions.md")<br>• [ListTasks](../APIReference/API_ListTasks.md "../APIReference/API_ListTasks.md")<br>• [CopyJobTemplate](../APIReference/API_CopyJobTemplate.md "../APIReference/API_CopyJobTemplate.md")<br>• [UpdateSession](../APIReference/API_UpdateSession.md "../APIReference/API_UpdateSession.md")<br>• [UpdateStep](../APIReference/API_UpdateStep.md "../APIReference/API_UpdateStep.md")<br>• [UpdateJob](../APIReference/API_UpdateJob.md "../APIReference/API_UpdateJob.md")<br>• [ListJobParameterDefinitions](../APIReference/API_ListJobParameterDefinitions.md "../APIReference/API_ListJobParameterDefinitions.md")<br>• [GetSessionAction](../APIReference/API_GetSessionAction.md "../APIReference/API_GetSessionAction.md")<br>• [ListStepDependencies](../APIReference/API_ListStepDependencies.md "../APIReference/API_ListStepDependencies.md")<br>• [SearchTasks](../APIReference/API_SearchTasks.md "../APIReference/API_SearchTasks.md")<br>• [SearchSteps](../APIReference/API_SearchSteps.md "../APIReference/API_SearchSteps.md") |

You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

## Deadline Cloud management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

AWS Deadline Cloud logs the following Deadline Cloud control plane operations to CloudTrail as _management events_.

- [associate-member-to-farm](../APIReference/API_AssociateMemberToFarm.md "../APIReference/API_AssociateMemberToFarm.md")
- [associate-member-to-fleet](../APIReference/API_AssociateMemberToFleet.md "../APIReference/API_AssociateMemberToFleet.md")
- [associate-member-to-job](../APIReference/API_AssociateMemberToJob.md "../APIReference/API_AssociateMemberToJob.md")
- [associate-member-to-queue](../APIReference/API_AssociateMemberToQueue.md "../APIReference/API_AssociateMemberToQueue.md")
- [assume-fleet-role-for-read](../APIReference/API_AssumeFleetRoleForRead.md "../APIReference/API_AssumeFleetRoleForRead.md")
- [assume-fleet-role-for-worker](../APIReference/API_AssumeFleetRoleForWorker.md "../APIReference/API_AssumeFleetRoleForWorker.md")
- [assume-queue-role-for-read](../APIReference/API_AssumeQueueRoleForRead.md "../APIReference/API_AssumeQueueRoleForRead.md")
- [assume-queue-role-for-user](../APIReference/API_AssumeQueueRoleForUser.md "../APIReference/API_AssumeQueueRoleForUser.md")
- [assume-queue-role-for-worker](../APIReference/API_AssumeQueueRoleForWorker.md "../APIReference/API_AssumeQueueRoleForWorker.md")
- [create-budget](../APIReference/API_CreateBudget.md "../APIReference/API_CreateBudget.md")
- [create-farm](../APIReference/API_CreateFarm.md "../APIReference/API_CreateFarm.md")
- [create-fleet](../APIReference/API_CreateFleet.md "../APIReference/API_CreateFleet.md")
- [create-license-endpoint](../APIReference/API_CreateLicenseEndpoint.md "../APIReference/API_CreateLicenseEndpoint.md")
- [create-limit](../APIReference/API_CreateLimit.md "../APIReference/API_CreateLimit.md")
- [create-monitor](../APIReference/API_CreateMonitor.md "../APIReference/API_CreateMonitor.md")
- [create-queue](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md")
- [create-queue-environment](../APIReference/API_CreateQueueEnvironment.md "../APIReference/API_CreateQueueEnvironment.md")
- [create-queue-fleet-association](../APIReference/API_CreateQueueFleetAssociation.md "../APIReference/API_CreateQueueFleetAssociation.md")
- [create-queue-limit-association](../APIReference/API_CreateQueueLimitAssociation.md "../APIReference/API_CreateQueueLimitAssociation.md")
- [create-storage-profile](../APIReference/API_CreateStorageProfile.md "../APIReference/API_CreateStorageProfile.md")
- [create-worker](../APIReference/API_CreateWorker.md "../APIReference/API_CreateWorker.md")
- [delete-budget](../APIReference/API_DeleteBudget.md "../APIReference/API_DeleteBudget.md")
- [delete-farm](../APIReference/API_DeleteFarm.md "../APIReference/API_DeleteFarm.md")
- [delete-fleet](../APIReference/API_DeleteFleet.md "../APIReference/API_DeleteFleet.md")
- [delete-license-endpoint](../APIReference/API_DeleteLicenseEndpoint.md "../APIReference/API_DeleteLicenseEndpoint.md")
- [delete-limit](../APIReference/API_DeleteLimit.md "../APIReference/API_DeleteLimit.md")
- [delete-metered-product](../APIReference/API_DeleteMeteredProduct.md "../APIReference/API_DeleteMeteredProduct.md")
- [delete-monitor](../APIReference/API_DeleteMonitor.md "../APIReference/API_DeleteMonitor.md")
- [delete-queue](../APIReference/API_DeleteQueue.md "../APIReference/API_DeleteQueue.md")
- [delete-queue-environment](../APIReference/API_DeleteQueueEnvironment.md "../APIReference/API_DeleteQueueEnvironment.md")
- [delete-queue-fleet-association](../APIReference/API_DeleteQueueFleetAssociation.md "../APIReference/API_DeleteQueueFleetAssociation.md")
- [delete-queue-limit-association](../APIReference/API_DeleteQueueLimitAssociation.md "../APIReference/API_DeleteQueueLimitAssociation.md")
- [delete-storage-profile](../APIReference/API_DeleteStorageProfile.md "../APIReference/API_DeleteStorageProfile.md")
- [delete-worker](../APIReference/API_DeleteWorker.md "../APIReference/API_DeleteWorker.md")
- [disassociate-member-from-farm](../APIReference/API_DisassociateMemberFromFarm.md "../APIReference/API_DisassociateMemberFromFarm.md")
- [disassociate-member-from-fleet](../APIReference/API_DisassociateMemberFromFleet.md "../APIReference/API_DisassociateMemberFromFleet.md")
- [disassociate-member-from-job](../APIReference/API_DisassociateMemberFromJob.md "../APIReference/API_DisassociateMemberFromJob.md")
- [disassociate-member-from-queue](../APIReference/API_DisassociateMemberFromQueue.md "../APIReference/API_DisassociateMemberFromQueue.md")
- [get-application-version](../APIReference/API_GetApplicationVersion.md "../APIReference/API_GetApplicationVersion.md")
- [get-budget](../APIReference/API_GetBudget.md "../APIReference/API_GetBudget.md")
- [get-farm](../APIReference/API_GetFarm.md "../APIReference/API_GetFarm.md")
- [get-feature-map](../APIReference/API_GetFeatureMap.md "../APIReference/API_GetFeatureMap.md")
- [get-fleet](../APIReference/API_GetFleet.md "../APIReference/API_GetFleet.md")
- [get-license-endpoint](../APIReference/API_GetLicenseEndpoint.md "../APIReference/API_GetLicenseEndpoint.md")
- [get-limit](../APIReference/API_GetLimit.md "../APIReference/API_GetLimit.md")
- [get-monitor](../APIReference/API_GetMonitor.md "../APIReference/API_GetMonitor.md")
- [get-queue](../APIReference/API_GetQueue.md "../APIReference/API_GetQueue.md")
- [get-queue-environment](../APIReference/API_GetQueueEnvironment.md "../APIReference/API_GetQueueEnvironment.md")
- [get-queue-fleet-association](../APIReference/API_GetQueueFleetAssociation.md "../APIReference/API_GetQueueFleetAssociation.md")
- [get-queue-limit-association](../APIReference/API_GetQueueLimitAssociation.md "../APIReference/API_GetQueueLimitAssociation.md")
- [get-sessions-statistics-aggregation](../APIReference/API_GetSessionsStatisticsAggregation.md "../APIReference/API_GetSessionsStatisticsAggregation.md")
- [get-storage-profile](../APIReference/API_GetStorageProfile.md "../APIReference/API_GetStorageProfile.md")
- [get-storage-profile-for-queue](../APIReference/API_GetStorageProfileForQueue.md "../APIReference/API_GetStorageProfileForQueue.md")
- [list-available-metered-products](../APIReference/API_ListAvailableMeteredProducts.md "../APIReference/API_ListAvailableMeteredProducts.md")
- [list-budgets](../APIReference/API_ListBudgets.md "../APIReference/API_ListBudgets.md")
- [list-farm-members](../APIReference/API_ListFarmMembers.md "../APIReference/API_ListFarmMembers.md")
- [list-farms](../APIReference/API_ListFarms.md "../APIReference/API_ListFarms.md")
- [list-fleet-members](../APIReference/API_ListFleetMembers.md "../APIReference/API_ListFleetMembers.md")
- [list-fleets](../APIReference/API_ListFleets.md "../APIReference/API_ListFleets.md")
- [list-job-members](../APIReference/API_ListJobMembers.md "../APIReference/API_ListJobMembers.md")
- [list-license-endpoints](../APIReference/API_ListLicenseEndpoints.md "../APIReference/API_ListLicenseEndpoints.md")
- [list-limit](../APIReference/API_ListLImit.md "../APIReference/API_ListLImit.md")
- [list-metered-products](../APIReference/API_ListMeteredProducts.md "../APIReference/API_ListMeteredProducts.md")
- [list-monitors](../APIReference/API_ListMonitors.md "../APIReference/API_ListMonitors.md")
- [list-queue-environments](../APIReference/API_ListQueueEnvironments.md "../APIReference/API_ListQueueEnvironments.md")
- [list-queue-fleet-associations](../APIReference/API_ListQueueFleetAssociations.md "../APIReference/API_ListQueueFleetAssociations.md")
- [list-queue-limit-associations](../APIReference/API_ListQueueLimitAssociations.md "../APIReference/API_ListQueueLimitAssociations.md")
- [list-queue-members](../APIReference/API_ListQueueMembers.md "../APIReference/API_ListQueueMembers.md")
- [list-queues](../APIReference/API_ListQueues.md "../APIReference/API_ListQueues.md")
- [list-storage-profiles](../APIReference/API_ListStorageProfiles.md "../APIReference/API_ListStorageProfiles.md")
- [list-storage-profiles-for-queue](../APIReference/API_ListStorageProfilesForQueue.md "../APIReference/API_ListStorageProfilesForQueue.md")
- [list-tags-for-resource](../APIReference/API_ListTagsForResources.md "../APIReference/API_ListTagsForResources.md")
- [put-metered-product](../APIReference/API_PutMeteredProduct.md "../APIReference/API_PutMeteredProduct.md")
- [start-sessions-statistics-aggregation](../APIReference/API_StartSessionsStatisticsAggregation.md "../APIReference/API_StartSessionsStatisticsAggregation.md")
- [tag-resource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md")
- [untag-resource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md")
- [update-budget](../APIReference/API_UpdateBudget.md "../APIReference/API_UpdateBudget.md")
- [update-farm](../APIReference/API_UpdateFarm.md "../APIReference/API_UpdateFarm.md")
- [update-fleet](../APIReference/API_UpdateFleet.md "../APIReference/API_UpdateFleet.md")
- [update-limit](../APIReference/API_UpdateLimit.md "../APIReference/API_UpdateLimit.md")
- [update-monitor](../APIReference/API_UpdateMonitor.md "../APIReference/API_UpdateMonitor.md")
- [update-queue](../APIReference/API_UpdateQueue.md "../APIReference/API_UpdateQueue.md")
- [update-queue-environment](../APIReference/API_UpdateQueueEnvironment.md "../APIReference/API_UpdateQueueEnvironment.md")
- [update-queue-fleet-association](../APIReference/API_UpdateQueueFleetAssociation.md "../APIReference/API_UpdateQueueFleetAssociation.md")
- [update-queue-limit-association](../APIReference/API_UpdateQueueLimitAssociation.md "../APIReference/API_UpdateQueueLimitAssociation.md")
- [update-storage-profile](../APIReference/API_UpdateStorageProfile.md "../APIReference/API_UpdateStorageProfile.md")
- [update-worker](../APIReference/API_UpdateWorker.md "../APIReference/API_UpdateWorker.md")

## Deadline Cloud event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the
`CreateFarm` operation.

```
{
    "eventVersion": "0",
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
            "purpose_1": "e2e"
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
    "recipientAccountId": "111122223333"
    "eventCategory": "Management",
}

```

The JSON example shows the AWS Region, IP address, and other
"`requestParameters`" such as the "`displayName`" and
"`kmsKeyArn`" that can help you identify the event.

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.

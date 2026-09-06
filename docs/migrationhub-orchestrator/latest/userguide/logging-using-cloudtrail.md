

AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform).

# Logging Migration Hub Orchestrator API calls using AWS CloudTrail
<a name="logging-using-cloudtrail"></a>

Migration Hub Orchestrator is integrated with [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html), a service that provides a record of actions taken by a user, role, or an AWS service. CloudTrail captures all API calls for Migration Hub Orchestrator as events. The calls captured include calls from the Migration Hub Orchestrator console and code calls to the Migration Hub Orchestrator API operations. Using the information collected by CloudTrail, you can determine the request that was made to Migration Hub Orchestrator, the IP address from which the request was made, when it was made, and additional details.

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

## Migration Hub Orchestrator management events in CloudTrail
<a name="cloudtrail-management-events"></a>

[Management events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html#logging-management-events) provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Migration Hub Orchestrator logs the following Migration Hub Orchestrator control plane operations to CloudTrail as *management events*.
+ [CreateMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_CreateMigrationWorkflow.html)
+ [UpdateMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_UpdateMigrationWorkflow.html)
+ [DeleteMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_DeleteMigrationWorkflow.html)
+ [StartMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_StartMigrationWorkflow.html)
+ [StopMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_StopMigrationWorkflow.html)
+ [TagResource](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_TagResource.html)
+ [UntagResource](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_UntagResource.html)
+ [CreateWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStep.html)
+ [UpdateWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStep.html)
+ [DeleteWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStep.html)
+ [RetryWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_RetryWorkflowStep.html)
+ [CreateWorkflowStepGroup](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_CreateWorkflowStepGroup.html)
+ [UpdateWorkflowStepGroup](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_UpdateWorkflowStepGroup.html)
+ [DeleteWorkflowStepGroup](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_DeleteWorkflowStepGroup.html)
+ [GetMigrationWorkflow](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetMigrationWorkflow.html)
+ [ListMigrationWorkflows](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListMigrationWorkflows.html)
+ [GetMigrationWorkflowTemplate](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetMigrationWorkflowTemplate.html)
+ [ListMigrationWorkflowTemplates](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListMigrationWorkflowTemplates.html)
+ [ListTemplateStepGroups](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateStepGroups.html)
+ [GetTemplateStepGroup](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStepGroup.html)
+ [ListTemplateSteps](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListTemplateSteps.html)
+ [GetTemplateStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetTemplateStep.html)
+ [ListTagsForResource](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListTagsForResource.html)
+ [GetWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStep.html)
+ [ListWorkflowSteps](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowSteps.html)
+ [GetWorkflowStepGroup](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStepGroup.html)
+ [ListWorkflowStepGroups](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListWorkflowStepGroups.html)
+ [ListPlugins](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_ListPlugins.html)

## Migration Hub Orchestrator event examples
<a name="cloudtrail-event-examples"></a>

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `[GetWorkflowStep](https://amazonaws.com/migrationhub-orchestrator/latest/APIReference/API_GetWorkflowStep.html)` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        type": "AssumedRole",
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
                "creationDate": "2022-03-22T23:29:22Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "eventTime": "2022-03-23T03:16:55Z",
    "eventSource": "migrationhub-orchestrator.amazonaws.com",
    "eventName": "GetWorkflowStep",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "99.99.999.999",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
    "requestParameters": {
        "stepGroupId": "act-1",
        "id": "step-11111",
        "workflowId": "mw-1111111"
    },
    "responseElements": null,
    "requestID": "068e87d1",
    "eventID": "e699238c",
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail record contents](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.html) in the *AWS CloudTrail User Guide*.
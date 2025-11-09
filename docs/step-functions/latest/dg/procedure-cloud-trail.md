# Recording Step Functions API calls with AWS CloudTrail

AWS Step Functions is integrated with [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md"), a service that provides a record of actions taken by a user, role, or an
AWS service. CloudTrail captures all
API calls for Step Functions as events. The calls captured include calls from the Step Functions console
and code calls to the Step Functions API operations. Using the information collected by CloudTrail, you can
determine the request that was made to Step Functions, the IP address from which the request was
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

## Data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, reading or writing to an Amazon S3
object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the Step Functions resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

The following table lists the Step Functions resource types for which you can log data events.
The **Data event type** column shows the value to
choose from the **Data event type** list on the CloudTrail console. The **resources.type value** column shows the `resources.type`
value, which you would specify when configuring advanced event selectors using the AWS CLI or
CloudTrail APIs. The **Data APIs logged to CloudTrail** column shows the API
calls logged to CloudTrail for the resource type.

You can configure advanced event selectors to filter on the `eventName`,
`readOnly`, and `resources.ARN` fields to log only those events that
are important to you. For more information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

| Data event type                  | resources.type value               | Data APIs logged to CloudTrail               |
| -------------------------------- | ---------------------------------- | -------------------------------------------- |
| **Step Functions state machine** | `AWS::StepFunctions::StateMachine` | • InvokeHTTPEndpoint<br>• StartSyncExecution |
| **Step Functions activity**      | `AWS::StepFunctions::Activity`     | • GetActivityTask                            |

## Management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

**State Machine**

- [CreateStateMachine](../apireference/API_CreateStateMachine.md "../apireference/API_CreateStateMachine.md")
- [ListStateMachines](../apireference/API_ListStateMachines.md "../apireference/API_ListStateMachines.md")
- [DescribeStateMachine](../apireference/API_DescribeStateMachine.md "../apireference/API_DescribeStateMachine.md")
- [UpdateStateMachine](../apireference/API_UpdateStateMachine.md "../apireference/API_UpdateStateMachine.md")
- [DeleteStateMachine](../apireference/API_DeleteStateMachine.md "../apireference/API_DeleteStateMachine.md")
- [ValidateStateMachineDefinition](../apireference/API_ValidateStateMachineDefinition.md "../apireference/API_ValidateStateMachineDefinition.md")
- [TestState](../apireference/API_TestState.md "../apireference/API_TestState.md")

**State Machine Alias**

- [CreateStateMachineAlias](../apireference/API_CreateStateMachineAlias.md "../apireference/API_CreateStateMachineAlias.md")
- [ListStateMachineAliases](../apireference/API_ListStateMachineAliases.md "../apireference/API_ListStateMachineAliases.md")
- [DescribeStateMachineAlias](../apireference/API_DescribeStateMachineAlias.md "../apireference/API_DescribeStateMachineAlias.md")
- [UpdateStateMachineAlias](../apireference/API_UpdateStateMachineAlias.md "../apireference/API_UpdateStateMachineAlias.md")
- [DeleteStateMachineAlias](../apireference/API_DeleteStateMachineAlias.md "../apireference/API_DeleteStateMachineAlias.md")

**State Machine Version**

- [ListStateMachineVersions](../apireference/API_ListStateMachineVersions.md "../apireference/API_ListStateMachineVersions.md")
- [PublishStateMachineVersion](../apireference/API_PublishStateMachineVersion.md "../apireference/API_PublishStateMachineVersion.md")
- [DeleteStateMachineVersion](../apireference/API_DeleteStateMachineVersion.md "../apireference/API_DeleteStateMachineVersion.md")

**Executions**

- [StartExecution](../apireference/API_StartExecution.md "../apireference/API_StartExecution.md")
- [StartSyncExecution](../apireference/API_StartSyncExecution.md "../apireference/API_StartSyncExecution.md")
- [RedriveExecution](../apireference/API_RedriveExecution.md "../apireference/API_RedriveExecution.md")
- [ListExecutions](../apireference/API_ListExecutions.md "../apireference/API_ListExecutions.md")
- [DescribeExecution](../apireference/API_DescribeExecution.md "../apireference/API_DescribeExecution.md")
- [GetExecutionHistory](../apireference/API_GetExecutionHistory.md "../apireference/API_GetExecutionHistory.md")
- [DescribeStateMachineForExecution](../apireference/API_DescribeStateMachineForExecution.md "../apireference/API_DescribeStateMachineForExecution.md")
- [StopExecution](../apireference/API_StopExecution.md "../apireference/API_StopExecution.md")

**Activity**

- [CreateActivity](../apireference/API_CreateActivity.md "../apireference/API_CreateActivity.md")
- [ListActivities](../apireference/API_ListActivities.md "../apireference/API_ListActivities.md")
- [DescribeActivity](../apireference/API_DescribeActivity.md "../apireference/API_DescribeActivity.md")
- [DeleteActivity](../apireference/API_DeleteActivity.md "../apireference/API_DeleteActivity.md")
- [GetActivityTask](../apireference/API_GetActivityTask.md "../apireference/API_GetActivityTask.md")

**Task Token**

- [SendTaskSuccess](../apireference/API_SendTaskSuccess.md "../apireference/API_SendTaskSuccess.md")
- [SendTaskHeartbeat](../apireference/API_SendTaskHeartbeat.md "../apireference/API_SendTaskHeartbeat.md")
- [SendTaskFailure](../apireference/API_SendTaskFailure.md "../apireference/API_SendTaskFailure.md")

**MapRun**

- [ListMapRuns](../apireference/API_ListMapRuns.md "../apireference/API_ListMapRuns.md")
- [DescribeMapRun](../apireference/API_DescribeMapRun.md "../apireference/API_DescribeMapRun.md")
- [UpdateMapRun](../apireference/API_UpdateMapRun.md "../apireference/API_UpdateMapRun.md")

**Tags**

- [ListTagsForResource](../apireference/API_ListTagsForResource.md "../apireference/API_ListTagsForResource.md")
- [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
- [UntagResource](../apireference/API_UntagResource.md "../apireference/API_UntagResource.md")

## Event examples

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail **data event** that demonstrates `InvokeHTTPEndpoint`.

```
{
    "eventVersion": "1.09",
    "userIdentity": {
        "accountId": "`account-id`",
        "invokedBy": "states.amazonaws.com"
    },
    "eventTime": "2024-05-01T01:23:45Z",
    "eventSource": "states.amazonaws.com",
    "eventName": "InvokeHTTPEndpoint",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "states.amazonaws.com",
    "userAgent": "states.amazonaws.com",
    "requestParameters": null,
    "responseElements": null,
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
    "readOnly": false,
    "resources": [
        {
            "accountId": "`account-id`",
            "type": "AWS::StepFunctions::StateMachine",
            "ARN": "arn:aws:states:`region`:`account-id`:stateMachine:ExampleStateMachine"
        }
    ],
    "eventType": "AwsServiceEvent",
    "managementEvent": false,
    "recipientAccountId": "`account-id`",
    "serviceEventDetails": {
        "httpMethod": "GET",
        "httpEndpoint": "https://example.com"
    },
    "eventCategory": "Data"
}
```

The following example shows a CloudTrail **management event** that demonstrates the `CreateStateMachine` operation.

```
{
    "eventVersion": "1.08",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAJYDLDBVBI4EXAMPLE",
        "arn": "arn:aws:iam::`account-id`:user/test-user",
        "accountId": "`account-id`",
        "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
        "userName": "test-user"
    },
    "eventTime": "2024-05-01T01:23:45Z",
    "eventSource": "states.amazonaws.com",
    "eventName": "CreateStateMachine",
    "awsRegion": "`region`",
    "sourceIPAddress": "`AWS Internal`",
    "userAgent": "`AWS Internal`",
    "requestParameters": {
        "name": "MyStateMachine",
        "definition": "HIDDEN_DUE_TO_SECURITY_REASONS",
        "roleArn": "arn:aws:iam::`account-id`:role/MyStateMachineRole",
        "type": "STANDARD",
        "loggingConfiguration": {
            "level": "OFF",
            "includeExecutionData": false
        },
        "tags": [],
        "tracingConfiguration": {
            "enabled": false
        },
        "publish": false
    },
    "responseElements": {
        "stateMachineArn": "arn:aws:states:`region`:`account-id`:stateMachine:MyStateMachine",
        "creationDate": "May 1, 2024 1:23:45 AM"
    },
    "requestID": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
    "eventID": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "readOnly": false,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "`account-id`",
    "eventCategory": "Management"
}
```

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.

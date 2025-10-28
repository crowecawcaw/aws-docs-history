# CloudWatch Events notifications

AMS offers push notifications for the RFC State changes through CloudWatch Events. To get these notifications:

1. Create a topic and subscription where notifications will be sent. You can name the topic what
   you like; for information about doing this, see [SNS Topic and Subscription: Creating](../ctref/ex-sns-top-sub-create-col.md "../ctref/ex-sns-top-sub-create-col.md").
2. Submit an RFC with the Management | Other | Other | Create change type and include the SNS topic and subscription
   in the request for RFC state change notices.
   When you submit the Management | Other | Other RFC request for this feature, you
   can specify what RFC state changes you're interested in getting notified about and
   what change types, and set other filters. For example, you may want to request to be
   notified only when Admin Access change types are EventType = RfcSubmitted and
   EventType = RfcUpdated.

This is a template of CloudWatch event notifications that you can receive (with all possible values):

```
{
    "source ": "aws.managedservices",
    "detail-type": "AMS RFC State Change",
    "detail": {
        "ActionState": "`null | AwsActionPending | AwsOperatorAssigned | CustomerActionPending | NotApplicable | NoActionPending`",
        "ActualExecutionTimeRange": {
            "StartTime": "`null | Actual Start Time`",
            "EndTime": "`null | Actual End Time`"
        },
        "AutomationStatus": "`Automated | Manual`",
        "AwsAccountId": "`AWS Account ID`",
        "AwsApprovalStatus": "`null | SubmissionPending | NotRequired | ApprovalPending | Rejected | Approved`",
        "ChangeTypeId": "`Change_Type_ID`",
        "ChangeTypeVersion": "`Change_Type_Version`",
        "CreatedTime": "`Created_Time`",
        "CustomerApprovalStatus": "`null | SubmissionPending | NotRequired | ApprovalPending | Rejected | Approved`",
        "EventType": "`RfcActionStateUpdated | RfcApproved | RfcAutoRejected | RfcCanceled | RfcCompleted | RfcCreated | RfcInProgress | RfcRejected | RfcSubmitted | RfcUpdated`",
        "LastModifiedTime": "`Last_Updated_Time`",
        "LastSubmittedTime": "`null | Last_Submitted_Time`",
        "RequestedExecutionTimeRange": {
            "StartTime": "`null | Expected_Start_Time`",
            "EndTime": "`null | Expected_End_Time`"
        },
        "RfcId": "`RFC_ID`",
        "Status": "`Editing | PendingApproval | Scheduled | Rejected | Canceled | ExecutionLock | InProgress | Success | Failure`",
        "Title": "`Title`"
    }
}
```

The supported RFC state changes (EventType), as they appear in the actual CloudWatch Events notification are:

- RfcActionStateUpdated (no AMS console option): The RFC in one of the states, described
  later, changed.
- RfcApproved (no AMS console option): The RFC passed system and/or AMS operator validation
  and has been approved for completion.
- RfcAutoRejected (**Auto-Rejected**): The RFC failed system validation or AMS
  operator and has been rejected.
- RfcCanceled (**Canceled** or **Auto-Canceled**): The RFC was
  canceled by either the submitter or an AMS operator.
- RfcCompleted (**Completed**): The RFC run parameters have been
  completed, including UserData.
- RfcCreated (no AMS console option): The RFC was successfully created (the JSON and submitted parameters were valid).
- RfcInProgress (**InProgress**): The RFC run is still in progress.
- RfcRejected (**Rejected**): The RFC failed system or AMS operator validation
  has been rejected.
- RfcSubmitted (**Submitted**): The RFC has been submitted and is undergoing system validation.
- RfcUpdated (no AMS console option): The RFC has been manually updated by an AMS operator.
  Additionally, you can send CloudWatch Events (CWE) notifications to any of the
  supported destinations and build your own systems on top of these automated notifications:

- Amazon EC2 instances
- AWS Lambda functions
- Streams in Amazon Kinesis Data Streams
- Delivery streams in Amazon Data Firehose
- Log groups in Amazon CloudWatch Logs
- Amazon ECS tasks
- Systems Manager Run Command
- Systems Manager Automation
- AWS Batch jobs
- Step Functions state machines
- Pipelines in CodePipeline
- CodeBuild projects
- Amazon Inspector assessment templates
- Amazon SNS topics
- Amazon SQS queues
- Built-in targets: EC2 CreateSnapshot API call, EC2 RebootInstances API call, EC2 StopInstances API call,
  and EC2 TerminateInstances API call.
- The default event bus of another AWS account

###### Note

We send CloudWatch Events notification for RFC state changes, on a best-effort basis.

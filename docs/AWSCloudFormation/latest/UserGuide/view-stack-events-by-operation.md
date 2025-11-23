# View stack events by operation

You can view stack events grouped by operation to better understand the sequence and scope
of changes made to your stack. Operation-based grouping helps you track related events
together, making it easier to monitor progress and troubleshoot issues when they
occur.

Each stack operation (create, update, delete, rollback) is assigned a unique operation ID
that groups all related events. This allows you to focus on specific operations and quickly
identify the root cause of failures.

###### Topics

- [Prerequisites](#view-stack-events-by-operation-prerequisites "#view-stack-events-by-operation-prerequisites")
- [View stack events by operation
  (console)](#view-stack-events-by-operation-console "#view-stack-events-by-operation-console")
- [View stack events by operation
  (AWS CLI)](#view-stack-events-by-operation-cli "#view-stack-events-by-operation-cli")
- [Stack status codes](#stack-status-codes "#stack-status-codes")

## Prerequisites

To use `DescribeEvents` API, you must have the necessary IAM permissions
to: `DescribeEvents`.

## View stack events by operation

(console)

###### To view stack events grouped by operation

1. Sign in to the AWS Management Console and open the CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. On the navigation bar at the top of the screen, choose the AWS Region you
   created the stack in.
3. On the **Stacks** page, select the stack name. CloudFormation
   displays the stack details for the selected stack.
4. Choose the **Events** tab to view the stack events CloudFormation
   has generated for your stack.
5. Events are automatically grouped by operation ID. Each operation appears as an
   expandable section showing the operation type, status, and timestamp.
6. Click on an **operation ID** to open a detailed view showing
   only the events related to that specific operation.
7. In the operation detail view, select the **Display failures
   only** checkbox to display only failed events for root cause
   analysis.

CloudFormation automatically refreshes the stack events every minute. The **New
events available** badge appears when new stack events occur. Choose the
refresh icon to load these events into the list.

By viewing stack events grouped by operation, you can understand the sequence of
events for each operation and quickly identify which specific operation caused issues
(if you are debugging your stack).

While your stack operation is running, it's listed with a status of
`CREATE_IN_PROGRESS`, `UPDATE_IN_PROGRESS`, or
`DELETE_IN_PROGRESS`. After your operation has completed successfully,
its status changes to `CREATE_COMPLETE`, `UPDATE_COMPLETE`, or
`DELETE_COMPLETE`.

For more information, see [Understand CloudFormation stack creation
events](stack-resource-configuration-complete.md "stack-resource-configuration-complete.md") and [Monitor the progress of a stack
update](using-cfn-updating-stacks-monitor-stack.md "using-cfn-updating-stacks-monitor-stack.md").

## View stack events by operation

(AWS CLI)

You can use the `describe-events` command with operation ID filtering to
view events for specific operations.

### Get last operation IDs

The stack description available via describe-stacks API now includes
LastOperations information showing recent operation IDs and their types. This
enables you to quickly identify which operations occurred and their current status
without parsing through event logs.

```
aws cloudformation describe-stacks --stack-name `MyStack`
```

The following is an example response showing the last operation was a Rollback
following a failed Update operation.

```
{
    "Stacks": [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/MyStack/07580010-bb79-11f0-8f6c-0289bb5c804f",
            "StackName": "MyStack",
            "Description": "A simple CloudFormation template to create an S3 bucket.",
            "CreationTime": "2025-11-07T01:28:13.778000+00:00",
            "LastUpdatedTime": "2025-11-07T01:43:39.838000+00:00",
            "RollbackConfiguration": {},
            "StackStatus": "UPDATE_ROLLBACK_COMPLETE",
            "DisableRollback": false,
            "NotificationARNs": [],
            "Tags": [],
            "EnableTerminationProtection": false,
            "DriftInformation": {
                "StackDriftStatus": "NOT_CHECKED"
            },
            "LastOperations": [
                {
                    "OperationType": "ROLLBACK",
                    "OperationId": "d0f12313-7bdb-414d-a879-828a99b36f29"
                },
                {
                    "OperationType": "UPDATE_STACK",
                    "OperationId": "1c211b5a-4538-4dc9-bfed-e07734371e57"
                }
            ]
        }
    ]
}
```

### Filter events by operation

ID

The following `describe-events` command describes events for a specific
operation ID:

```
aws cloudformation describe-events \
  --operation-id `1c211b5a-4538-4dc9-bfed-e07734371e57`
```

To view only failed events for troubleshooting, use the `--filter
 FailedEvents=true` parameter:

```
aws cloudformation describe-events \
  --operation-id `1c211b5a-4538-4dc9-bfed-e07734371e57` \
  --filter FailedEvents=true
```

The new operation ID filtering capability allows you to focus on specific
operations and their related events. This is particularly useful for:

- Troubleshooting specific failures: Isolate
  events from a failed operation to understand what went wrong.
- Monitoring long-running operations: Track
  progress of complex updates or large stack deployments.
- Auditing changes: Review all events
  associated with a particular update operation.
- Root cause analysis: Use the failure filter
  to quickly identify the source of deployment issues.

## Stack status codes

The following table describes the fields returned by the `describe-events`
command when using operation ID filtering:

| Field                  | Description                                                                                                                                                                                     |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `EventId`              | Event identifier.                                                                                                                                                                               |
| `OperationId`          | Unique identifier for the operation that generated this<br>event.                                                                                                                               |
| `StackName`            | Name of the stack that the event corresponds to.                                                                                                                                                |
| `StackId`              | Identifier of the stack that the event corresponds to.                                                                                                                                          |
| `LogicalResourceId`    | Logical identifier of the resource.                                                                                                                                                             |
| `PhysicalResourceId`   | Physical identifier of the resource.                                                                                                                                                            |
| `ResourceProperties`   | Properties of the resource.                                                                                                                                                                     |
| `ResourceType`         | Type of the resource.                                                                                                                                                                           |
| `Timestamp`            | Time when the event occurred.                                                                                                                                                                   |
| `ResourceStatus`       | The status of the resource (`CREATE_COMPLETE`,<br>`UPDATE_FAILED`, etc.).                                                                                                                       |
| `DetailedStatus`       | The detailed status of the stack. If<br>`CONFIGURATION_COMPLETE` is present, the stack resources<br>configuration phase has completed and the stabilization of the resources<br>is in progress. |
| `ResourceStatusReason` | More information on the status.                                                                                                                                                                 |

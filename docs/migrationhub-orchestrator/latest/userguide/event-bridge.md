AWS Migration Hub is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Migration Hub Orchestrator events in EventBridge

AWS Migration Hub Orchestrator generates status change events through Amazon EventBridge. Migration Hub Orchestrator sends these events to
EventBridge as [best effort](../../../eventbridge/latest/userguide/eb-service-event-list.md "../../../eventbridge/latest/userguide/eb-service-event-list.md") delivery attempts. Events are only delivered to the Region where
Migration Hub Orchestrator operations are invoked from. For more information, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the
_EventBridge User Guide_.

With EventBridge, you can establish rules that trigger programmatic actions in response to these
events. For example, you can create a rule that sends a notification to your email when a
workflow requires manual inputs. For more information, see [Configure User Notifications for Migration Hub Orchestrator status change
events](event-bridge-notifications.md "event-bridge-notifications.md").

###### Topics

- [Migration Hub Orchestrator event JSON structure](#event-bridge-events "#event-bridge-events")
- [Configure User Notifications for Migration Hub Orchestrator status change
  events](event-bridge-notifications.md "event-bridge-notifications.md")

## Migration Hub Orchestrator event JSON structure

Events in EventBridge are represented as JSON objects. The fields that are unique to the
event are contained in the `detail` section of the JSON object. For more
information, see [Amazon EventBridge event
patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge User Guide_.

- `accountId` – Your AWS account ID.
- `resourceId` – The unique ID of the resource.
  - When the `resourceType` value is `Workflow`, the
    `resourceId` is in the format of a workflow ID
    (_mw-abcd1234_).
  - When the `resouceType` value is
    `WorkflowStepGroup`, the `resourceId` is in
    the format of a workflow ID and step group ID
    (_mw-abcd1234#example-step-group_).
  - When the `resourceType` value is `WorkflowStep`,
    `resourceId` is in the format of a workflow ID, step
    group ID, and step ID
    (_mw-abcd1234#example-step-group#example-step_).
  - When the `resourceType` value is `Template`,
    `resourceId` is in the format of a template ID
    (_template-abcdefghijklmno1234567890_).

- `resourceType` – The type of resource.
  - `Workflow`
  - `WorkflowStepGroup`
  - `WorkflowStep`
  - `Template`

- `status` – The status of the resource. The available
  statuses are determined by the `resourceType`.
  - For the `Workflow` resource type, see the status values of the [GetWorkflow](../APIReference/API_GetWorkflow.md#migrationhuborchestrator-GetWorkflow-response-status "../APIReference/API_GetWorkflow.md#migrationhuborchestrator-GetWorkflow-response-status") API operation.
  - For the `WorkflowStepGroup` resource type, see the status values of the [GetWorkflowStepGroup](../APIReference/API_GetWorkflowStepGroup.md#migrationhuborchestrator-GetWorkflowStepGroup-response-status "../APIReference/API_GetWorkflowStepGroup.md#migrationhuborchestrator-GetWorkflowStepGroup-response-status") API
    operation.
  - For the `WorkflowStep` resource type, see the status values of the [GetWorkflowStep](../APIReference/API_GetWorkflowStep.md#migrationhuborchestrator-GetWorkflowStep-response-status "../APIReference/API_GetWorkflowStep.md#migrationhuborchestrator-GetWorkflowStep-response-status") API operation.
  - For the `Template` resource type, see the status values of the [GetTemplate](../APIReference/API_GetTemplate.md#migrationhuborchestrator-GetTemplate-response-status "../APIReference/API_GetTemplate.md#migrationhuborchestrator-GetTemplate-response-status") API operation.

- `timestamp` – The timestamp of when Migration Hub Orchestrator emitted an event
  to EventBridge.

The following example shows a status change event for Migration Hub Orchestrator with
the initial workflow status of `NOT_STARTED`:

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Migration Hub Orchestrator Resource Status Changed",
  "source": "aws.migrationhub-orchestrator",
  "account": "123456789012",
  "time": "2020-03-15T15:24:31Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "accountId": "123456789012",
    "resourceId": "mw-abcd123",
    "resourceType": "Workflow",
    "status": "NOT_STARTED",
    "timestamp": "2020-03-15T15:24:31Z"
    "version": "1.0"
  }
}
```

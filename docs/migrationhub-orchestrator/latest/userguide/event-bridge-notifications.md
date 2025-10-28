AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Configure User Notifications for Migration Hub Orchestrator status change

events

You can configure AWS User Notifications to send notifications in response to status changes that
occur in Migration Hub Orchestrator. User Notifications uses EventBridge to send notifications about events
from AWS services to the AWS Management Console Notifications Center and your chosen delivery
channels. For more information about Migration Hub Orchestrator events in EventBridge, see [Migration Hub Orchestrator events in EventBridge](event-bridge.md "event-bridge.md").

When you are creating a notification configuration, you can specify an
**Advanced filter** per event rule to receive notifications that
fit specific use cases. For more information on how to create a notification configuring
in User Notifications, see [Creating your first
notification configuration in AWS User Notifications](../../../notifications/latest/userguide/getting-started.md "../../../notifications/latest/userguide/getting-started.md") in the _AWS User Notifications User
Guide_.

###### JSON samples

The following JSON samples can be used as advanced filters for your notification
configurations to support common use cases.

- Receive a notification when a workflow fails:

```
{
  "detail": {
    "$or": [
      {
        "status": [
        "WORKFLOW_FAILED"
        ]
      },
      {
        "status": [
            "FAILED"
        ]
      }
    ]
  }
}
```

- Receive a notification when a workflow’s step changes:

```
{
  "detail": {
    "resourceType": [
      "Workflow Step"
    ]
  }
}
```

- Receive a notification when a workflow requires manual input:

```
{
  "detail": {
    "status": [
      "USER_ATTENTION_REQUIRED"
    ]
  }
}
```

# Enabling the Deadline Cloud assistant

Only Deadline Cloud administrators can enable or disable the assistant. The
assistant is disabled by default.

## Prerequisites

To use the assistant, your monitor must have the following:

- An administrator who enables the assistant through the Deadline Cloud console
- The IAM policy attached to the monitor user
  role

## Enabling the assistant

Use the following procedure to enable the assistant for all monitor users.

###### To enable the assistant

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. In the navigation pane, choose **Monitors**, and then choose
   your monitor.
3. Choose **Edit** to open the monitor settings.
4. Select the **Enable Deadline Cloud assistant** checkbox.
5. Choose **Save**.

When you enable the assistant, Deadline Cloud:

- Creates a IAM policy on the monitor user role that grants
  `bedrock:InvokeModelWithResponseStream` permission scoped to your Region's
  cross-region inference profile.
- Persists the enabled state through the monitor settings API.

## Disabling the assistant

Use the following procedure to disable the assistant.

###### To disable the assistant

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. In the navigation pane, choose **Monitors**, and then choose
   your monitor.
3. Choose **Edit** to open the monitor settings.
4. Clear the **Enable Deadline Cloud assistant** checkbox.
5. Choose **Save**.

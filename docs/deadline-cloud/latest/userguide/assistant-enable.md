# Enabling the Deadline Cloud assistant

Only Deadline Cloud administrators can enable or disable the assistant. The
assistant is disabled by default.

## Prerequisites

To use the assistant, your monitor must have the following:

- An administrator who enables the assistant through the Deadline Cloud console
- The Amazon Bedrock IAM policy attached to the monitor user
  role

## Enabling the assistant

You can turn on the assistant when you first set up your monitor, or at any time
afterward from the monitor settings. Use the following procedure to enable the
assistant for all users of an existing monitor.

###### To enable the assistant

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. In the navigation pane, choose **Dashboard**.
3. In the **Monitor overview** section, choose
   **Actions**, and then choose **Edit** to open
   the monitor settings page.
4. In the **Deadline Cloud Assistant** section, select
   **Enable Deadline Cloud Assistant**.
5. Choose **Update**.

To verify that the assistant is enabled, check that the **Deadline Cloud
Assistant** field in the **Monitor overview** section shows
**Enabled**.

When you enable the assistant, Deadline Cloud:

- Attaches an Amazon Bedrock IAM policy to the monitor user role. The policy name
  begins with `DeadlineCloudAssistantBedrockPolicy` and grants the
  `bedrock:InvokeModelWithResponseStream` permission scoped to your
  Region's cross-region inference profile.
- Persists the enabled state through the monitor settings API.

## Disabling the assistant

Use the following procedure to disable the assistant.

###### To disable the assistant

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home "https://console.aws.amazon.com/deadlinecloud/home").
2. In the navigation pane, choose **Dashboard**.
3. In the **Monitor overview** section, choose
   **Actions**, and then choose **Edit** to open
   the monitor settings page.
4. In the **Deadline Cloud Assistant** section, clear
   **Enable Deadline Cloud Assistant**.
5. Choose **Update**.

Disabling the assistant turns it off for all monitor users, but the Amazon Bedrock IAM
policy remains attached to the monitor user role. To also remove the Amazon Bedrock
permissions, detach the policy whose name begins with
`DeadlineCloudAssistantBedrockPolicy` from the monitor user role in the
IAM console.

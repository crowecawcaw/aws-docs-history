Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Configuring approval notifications

You can have CodeCatalyst send a notification to a Slack channel informing users that a
workflow run requires an approval. Users see the notification and click the link inside
of it. The link takes them to a CodeCatalyst approvals page where they can either approve or
reject the workflow.

You can also configure notifications to inform users that a workflow was approved,
rejected, or that the approval request has expired.

Use the following instructions to set up Slack notifications.

###### Before you begin

Make sure you have added an **Approval** gate to your
workflow. For more information, see [Adding an 'Approval' gate](workflows-approval-add.md "workflows-approval-add.md").

###### To send workflow approval notifications to a Slack channel

1. Configure CodeCatalyst with Slack. For more information, see [Getting started with Slack notifications](getting-started-notifications.md "getting-started-notifications.md").
2. In the CodeCatalyst project that contains the workflow that requires an approval,
   enable notifications, if they're not already enabled. To enable
   notifications:
   1. Navigate to your project and in the navigation pane, choose
      **Project settings**.
   2. At the top, choose **Notifications**.
   3. In **Notification events**, choose **Edit
      notifications**.
   4. Turn on **Workflow approval pending** and choose a
      Slack channel where CodeCatalyst will send the notification.
   5. (Optional) Turn on additional notifications to alert people about
      approved, rejected, and expired approvals. You can turn on
      **Workflow run approved**, **Workflow run
      rejected**, **Workflow approval
      superseded**, and **Workflow approval timed
      out**. Next to each notification, choose the Slack channel
      where CodeCatalyst will send the notification.
   6. Choose **Save**.

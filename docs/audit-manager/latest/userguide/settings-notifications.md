# Configuring your Audit Manager notifications

You can configure Audit Manager to send notifications to the Amazon SNS topic of your choice. If
you're subscribed to that SNS topic, you receive notifications directly whenever you
sign in to Audit Manager.

Follow the steps on this page to learn how to view and update your notification
settings to suit your preferences. You can use either a standard SNS topic or a FIFO
(first-in-first-out) SNS topic. Although Audit Manager supports sending notifications to FIFO
topics, the order that messages are sent in isn't guaranteed.

## Prerequisites

If you want to use an Amazon SNS topic that you don't own, you must configure your
AWS Identity and Access Management (IAM) policy for this. More specifically, you must configure it to allow
publishing from the Amazon Resource Name (ARN) of the topic. For an example policy
that you can use, see [Example 1 (Permissions for the SNS
topic)](security_iam_id-based-policy-examples.md#sns-topic-permissions "security_iam_id-based-policy-examples.md#sns-topic-permissions").

## Procedure

You can update this setting using the Audit Manager console, the AWS Command Line Interface (AWS CLI), or the
Audit Manager API.

Audit Manager console

###### To update your notification settings on the Audit Manager console

1. From the **Assessment** settings tab, go to
   the **Notifications** section.
2. To use an existing SNS topic, select the topic name from the
   dropdown menu.
3. To create a new SNS topic, choose **Create new
   topic**.
4. When you’re done, choose **Save**.

AWS CLI

###### To update your notification settings in the AWS CLI

Run the [update-settings](../../../cli/latest/reference/auditmanager/update-settings.md "../../../cli/latest/reference/auditmanager/update-settings.md") command and use the
`--sns-topic` parameter to specify an SNS
topic.

In the following example, replace the `placeholder
 text` with your own information:

```
aws auditmanager update-settings --sns-topic `arn:aws:sns:us-east-1:111122223333:my-assessment-topic`
```

Audit Manager API

###### To update your notification settings using the API

Call the [UpdateSettings](../APIReference/API_UpdateSettings.md "../APIReference/API_UpdateSettings.md") operation and use the [snsTopic](../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-snsTopic "../APIReference/API_UpdateSettings.md#auditmanager-UpdateSettings-request-snsTopic") parameter to specify an SNS topic.

## Additional

resources

- For instructions on how to create an Amazon SNS topic, see [Creating
  an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the _Amazon SNS User Guide_.
- For an example policy that you can use to allow Audit Manager to send notifications
  to Amazon SNS topics , see [Example 1 (Permissions for the SNS
  topic)](security_iam_id-based-policy-examples.md#sns-topic-permissions "security_iam_id-based-policy-examples.md#sns-topic-permissions")
- To learn more about the list of actions that invoke notifications in Audit Manager,
  see [Notifications in AWS Audit Manager](notifications.md "notifications.md").
- For solutions to notification issues in Audit Manager, see [Troubleshooting notification issues](notification-issues.md "notification-issues.md").

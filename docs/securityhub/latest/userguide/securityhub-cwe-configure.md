

# Creating a custom action
<a name="securityhub-cwe-configure"></a>

When you create a custom action in AWS Security Hub CSPM, you specify its name, description, and a unique identifier.

A custom action specifies which actions to take when an EventBridge event matches an EventBridge rule. Security Hub CSPM sends each finding to EventBridge as an event.

Choose your preferred method, and follow the steps to create a custom action.

------
#### [ Console ]

**To create a custom action in Security Hub CSPM (console)**

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/).

1. In the navigation pane, choose **Settings** and then choose **Custom actions**.

1. Choose **Create custom action**.

1. Provide a **Name**, **Description**, and **Custom action ID** for the action.

   The **Name** must be fewer than 20 characters.

   The **Custom action ID** must be unique for each AWS account.

1. Choose **Create custom action**.

1. Make a note of the **Custom action ARN**. You need to use the ARN when you create a rule to associate with this action in EventBridge.

------
#### [ API ]

**To create a custom action (API)**

Use the [CreateActionTarget](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CreateActionTarget.html) operation. If you're using the AWS CLI, run the [create-action-target](https://docs.aws.amazon.com/cli/latest/reference/securityhub/create-action-target.html) command.

The following example creates a custom action to send findings to a remediation tool. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securityhub create-action-target --name "{{Send to remediation}}" --description "{{Action to send the finding for remediation tracking}}" --id "{{Remediation}}"
```

------
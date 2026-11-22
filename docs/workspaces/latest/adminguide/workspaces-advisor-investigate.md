

# Investigate a WorkSpace

Use Investigate a WorkSpace to identify and resolve issues impacting a specific WorkSpaces Personal resource. You start an investigation by describing the problem you're experiencing in your own words. WorkSpaces Advisor then reviews telemetry, knowledge bases, and best practices, anchored to your description. It surfaces the most relevant issues, along with recommended remediation actions, in the Amazon WorkSpaces console.

With Investigate a WorkSpace, you can:
+ Describe the issue you're experiencing so Advisor can focus its investigation
+ Investigate a WorkSpace and receive the issues most relevant to what you described
+ Review supporting telemetry data, including Amazon CloudWatch metrics, for each issue
+ Take recommended remediation actions
+ Chat with WorkSpaces Advisor for follow-up questions through the AWS assistant
+ Create a support case pre-populated with investigation context

Investigate a WorkSpace is available in all AWS Regions that support Amazon WorkSpaces Personal at no additional cost.

## How investigations work
<a name="workspaces-advisor-how-it-works"></a>

To start an investigation, select a WorkSpace and choose **Investigate**. On the **Investigate with Advisor** screen, describe the problem you're experiencing, for example, the symptoms or any error messages observed, so WorkSpaces Advisor can focus its investigation. Do not include personally identifiable or confidential information. When you choose **Investigate**, WorkSpaces Advisor deploys AI agents to analyze data from the selected WorkSpace. The analysis typically completes in under 60 seconds.

WorkSpaces Advisor returns the issues most relevant to what you reported. For each issue, WorkSpaces Advisor provides at least one recommended action, describes the risk and impact to your resources, and might offer alternative actions.

Describing the issue is optional. If you leave the description blank, WorkSpaces Advisor runs a broad scan of the WorkSpace instead.

If WorkSpaces Advisor cannot identify your issue, it tells you the issue needs a specialist and offers to create an AWS Support case pre-populated with the investigation context. You can also provide feedback through the console.

### Investigation limits
<a name="workspaces-advisor-limits"></a>
+ You can investigate one WorkSpace at a time.

**To investigate a WorkSpace**

1. Open the [Amazon WorkSpaces console](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**, then **Personal**.

1. Select the WorkSpace that you want to investigate.

1. Choose **Investigate**.

1. On the **Investigate with Advisor** screen, describe the issue you're experiencing. Include any symptoms or error messages observed so WorkSpaces Advisor can focus its investigation. Do not include personally identifiable or confidential information. (This step is optional; leave it blank to run a broad scan.)

1. Choose **Investigate** to start the investigation.

1. Review the identified issues, which are focused on what you described. Choose an issue to view details, including supporting telemetry and the recommended action.

1. Review the risk and impact information for the recommended action, then choose the action to initiate it.

## Get additional help with AWS assistant
<a name="workspaces-advisor-additional-help"></a>
+ **Chat with WorkSpaces Advisor** — Choose **Chat with WorkSpaces Advisor** on the issue details page to ask follow-up questions through AWS Console chat. The chat session automatically includes the full context of the issue.
+ **Create a support case** — Choose **Create support case** to contact AWS Support. The support case is pre-populated with the investigation context.
+ In both cases you will need [permissions to use AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/getting-started.html#permissions-overview) in the console. For more information about using the AWS assistant, see [Using AWS assistant](https://docs.aws.amazon.com/assistant/latest/userguide/using-assistant.html).
AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Tutorial: Configuring Amazon Q Developer operational investigations in chat applications

To set up Amazon Q operational investigations in your chat applications, you must add the following policies to enable two-way communication between investigations and Amazon Q Developer in chat applications. You can add these policies during
step 2 of the Amazon Q Developer in chat applications channel configuration process for [Slack](slack-setup.md#slack-client-setup2 "slack-setup.md#slack-client-setup2") and [Microsoft Teams](teams-setup.md#teams-client-setup-2 "teams-setup.md#teams-client-setup-2") when you define your user permissions or by editing your configurations' **Permissions** in the Amazon Q Developer in chat applications console.

- Add **Notification permissions** and **Amazon Q operations assistant permissions** as policy templates
  when you define your user permissions. For more information about Channel role templates, see [Role setting](understanding-permissions.md#role-settings "understanding-permissions.md#role-settings").
- Attach the **AIOpsOperatorAccess** managed IAM policy to your guardrail policies in Amazon Q Developer in chat applications. This grants permissions to Amazon Q Developer in chat applications to interact with Amazon Q operational investigations
  and perform required actions on your behalf.

## Step 1: Connecting Amazon Q Developer in chat applications with an investigation group

You can integrate Amazon Q Developer operational investigations with your Microsoft Teams and Slack channels using Amazon SNS topics. Once integrated, you can receive and act on operational investigation notifications from your chat channel.

###### Tip

You can make investigations in your chat channels easier by adding [custom actions](custom-actions.md "custom-actions.md") to your notifications and by creating [command aliases](creating-aliases.md "creating-aliases.md") for frequently used tasks to fetch telemetry information.

###### To connect Amazon Q Developer in chat applications with an investigation group

1. Follow the steps in [Get started with Amazon Q Developer operational investigations](../../../AmazonCloudWatch/latest/monitoring/Investigations-GetStarted.md "../../../AmazonCloudWatch/latest/monitoring/Investigations-GetStarted.md") to create an investigation group.
2. Follow the steps in [Integration with third-party chat systems](../../../AmazonCloudWatch/latest/monitoring/Investigations-Integrations.md#Investigations-Integrations-Chat "../../../AmazonCloudWatch/latest/monitoring/Investigations-Integrations.md#Investigations-Integrations-Chat") to integrate Amazon Q operational investigations with your chat channel.

###### Note

When selecting an Amazon SNS topic, select the same topic configured in your Amazon Q Developer in chat applications channel configuration.

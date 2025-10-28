AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Custom actions using Amazon Q Developer in chat applications

Custom actions are preconfigured buttons you add to custom and default notifications. These actions allow you to automate commonly used DevOps processes and incident response tasks.
When you create a custom action, you configure your action button to run either a CLI command, a Lambda function, or an SSM Automation runbook. Action targets can be paramaterized by using the parameters available in your notification metadata. You can use custom actions to retrieve telemetry information, run runbooks, and notify team members. When an issue arises, you can take
action directly from your notifications. Custom actions are available in Amazon Q Developer in chat applications configurations for Microsoft Teams and Slack.

No additional permissions are needed to configure or run custom actions. When your channel members choose the custom action button, the action target is invoked using the configured IAM permissions in your channel configuration.

###### Topics

- [Creating a custom action using Amazon Q Developer in chat applications](creating-custom-actions.md "creating-custom-actions.md")
- [Sample use cases](sample-custom-action.md "sample-custom-action.md")

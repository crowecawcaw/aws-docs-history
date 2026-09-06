# Budget threshold notifications to email and Slack with CloudFormation

The
[budget\_events\_notification](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/notification_templates/budget_events_notification "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/notification_templates/budget_events_notification")
CloudFormation template on the GitHub website sets up notifications by email and to
Slack when a budget threshold is reached in the `aws.deadline`
service. The template creates the following resources:

- An SNS topic with an email subscription.
- An SNS topic policy that allows AWS services such as EventBridge
  to publish messages to the topic.
- An IAM role that grants AWS Chatbot permission to publish
  messages.
- An AWS Chatbot configuration that sends notifications to your
  Slack channel.
- An EventBridge rule that captures
  `Budget Threshold Reached` events from
  `aws.deadline` and sends them to the SNS topic.
  To deploy the template for Slack notifications, add AWS Chatbot to
  your Slack workspace, then copy the Slack channel ID and workspace ID for
  use as template parameters.

For more information about Deadline Cloud budgets and events, see
[Managing Deadline Cloud events using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md").

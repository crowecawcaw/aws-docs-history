# Configure Amazon SNS to send

messages for alerts to other destinations

Amazon Managed Service for Prometheus can only send alert messages to Amazon Simple Notification Service (Amazon SNS). To send those
messages to other destinations, such as email, webhook, Slack, or OpsGenie, you
must configure Amazon SNS to forward the messages on to those endpoints.

The following sections describing configuring Amazon SNS to forward alerts to other
destinations.

###### Topics

- [Email](#AMP-alertmanager-SNS-otherdestinations-email "#AMP-alertmanager-SNS-otherdestinations-email")
- [Webhook](#AMP-alertmanager-SNS-otherdestinations-webhook "#AMP-alertmanager-SNS-otherdestinations-webhook")
- [Slack](#AMP-alertmanager-SNS-otherdestinations-Slack "#AMP-alertmanager-SNS-otherdestinations-Slack")
- [OpsGenie](#AMP-alertmanager-SNS-otherdestinations-OpsGenie "#AMP-alertmanager-SNS-otherdestinations-OpsGenie")

## Email

To configure an Amazon SNS topic to output messages to email, create a
subscription. In the Amazon SNS console, choose the
**Subscriptions** tab to open the
**Subscriptions** list page. Choose **Create
Subscription** and select **Email**. Amazon SNS
sends a confirmation email to the listed email address. After you accept the
confirmation, you are able to receive Amazon SNS notifications as emails from the
topic you subscribed to. For more information, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md").

## Webhook

To configure an Amazon SNS topic to output messages to a webhook endpoint,
create a subscription. In the Amazon SNS console, choose the
**Subscriptions** tab to open the
**Subscriptions** list page. Choose **Create
Subscription** and select **HTTP/HTTPS**.
After you create the subscription, you must follow the confirmation steps to
activate it. When it is active, your HTTP endpoint should receive the Amazon SNS
notifications. For more information, see [Subscribing to an Amazon SNS topic](../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md "../../../sns/latest/dg/sns-create-subscribe-endpoint-to-topic.md"). For more information about using
Slack webhooks to publish messages to various destinations, see [How do I use webhooks to publish Amazon SNS messages to Amazon Chime, Slack, or
Microsoft Teams?](https://aws.amazon.com/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/ "https://aws.amazon.com/premiumsupport/knowledge-center/sns-lambda-webhooks-chime-slack-teams/")

## Slack

To configure an Amazon SNS topic to output messages to Slack, you have two
options. You can either integrate with Slack’s email-to-channel integration,
which allows Slack to accept email messages and forward them to a Slack
channel, or you can use a Lambda function to rewrite the Amazon SNS notification
to Slack. For more information about forwarding emails to slack channels,
see [Confirming AWS SNS Topic Subscription for Slack Webhook](https://stackoverflow.com/questions/49341187/confirming-aws-sns-topic-subscription-for-slack-webhook "https://stackoverflow.com/questions/49341187/confirming-aws-sns-topic-subscription-for-slack-webhook"). For
more information about constructing a Lambda function to convert Amazon SNS
messages to Slack, see [How to integrate Amazon Managed Service for Prometheus with Slack](https://aws.amazon.com/blogs/mt/how-to-integrate-amazon-managed-service-for-prometheus-with-slack/ "https://aws.amazon.com/blogs/mt/how-to-integrate-amazon-managed-service-for-prometheus-with-slack/").

## OpsGenie

For information about how to configure an Amazon SNS topic to output messages
to OpsGenie, see [Integrate Opsgenie with Incoming Amazon SNS](https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-incoming-amazon-sns/ "https://support.atlassian.com/opsgenie/docs/integrate-opsgenie-with-incoming-amazon-sns/").

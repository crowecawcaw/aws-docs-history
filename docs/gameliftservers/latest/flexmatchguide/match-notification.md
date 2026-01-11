# Set up FlexMatch event notifications

You can use event notifications to track the status of individual matchmaking requests. All
games in production, or in pre-production with high-volume matchmaking activity should use event
notifications.

There are two options for setting up event notifications.

- Have your matchmaker publish event notifications to an Amazon Simple Notification Service (Amazon SNS) topic.
- Use automatically published Amazon EventBridge events and its suite of tools for managing
  events.
  For a list of the FlexMatch events that Amazon GameLift Servers emits, see [FlexMatch matchmaking events](match-events.md "match-events.md").

###### Important

For high-volume matchmaking systems, we recommend using standard (non-FIFO) Amazon SNS topics rather than FIFO topics.
FIFO topics have lower publishing limits than standard topics, which can lead to throttling exceptions during high load.
If you experience throttling with FIFO topics, you may lose FlexMatch notifications.

###### Note

Amazon GameLift Servers automatically handles Amazon SNS delivery failures and throttling with built-in retry logic. When Amazon SNS returns
throttling errors or temporary failures, Amazon GameLift Servers retries the notification delivery with progressive delays between
attempts. This helps ensure event notifications are delivered reliably. However, notifications may be lost if failures
persist after all retry attempts, or for non-retryable errors such as authorization failures or missing topics.

###### Topics

- [Set up EventBridge events](#match-notification-cwe "#match-notification-cwe")
- [Tutorial: Set up an Amazon SNS topic](match-notification-sns.md "match-notification-sns.md")
- [Set up an SNS topic with server-side encryption](queue-notification-sns-sse.md "queue-notification-sns-sse.md")
- [Configure a topic subscription to invoke a Lambda
  function](match-notification-lambda.md "match-notification-lambda.md")

## Set up EventBridge events

Amazon GameLift Servers automatically posts all matchmaking events to Amazon EventBridge. With EventBridge, you can set up
rules to have matchmaking events routed to targets for processing. For example, you can set a
rule to route the event "PotentialMatchCreated" to an AWS Lambda function that handles player
acceptances. For more information, see [What is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")

###### Note

When you configure your matchmakers, keep the notification target field empty or
reference an SNS topic if you want to use both EventBridge and Amazon SNS.

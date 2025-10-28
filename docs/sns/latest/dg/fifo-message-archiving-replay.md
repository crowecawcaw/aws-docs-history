# Amazon SNS message archiving and replay for FIFO

topics

## What is message archiving and

replay?

Amazon SNS provides a no-code message archiving and replay feature, specifically designed
for FIFO (First-In-First-Out) topics. This feature allows topic owners to store messages
directly within the topic archive for up to 365 days and replay them to subscribers when
needed. Message archiving and replay are essential for recovering lost messages and
synchronizing applications across regions or systems by replicating states.

This functionality can be accessed through the AWS API, SDK, AWS CloudFormation, and
AWS Management Console.

**Key use cases**

- **Message recovery** – Recover messages
  lost due to downstream application failures by replaying them to the
  subscriber’s endpoint.
- **State replication** – Replicate the
  state of an existing system in a new environment by replaying messages starting
  from a specific timestamp.
- **Error correction** – Resend missed
  messages during outages to ensure all events are processed correctly.

### Components of message

archiving and replay

Manage message archiving and replay for Amazon SNS FIFO topics, including setting
retention periods, monitoring archived messages using CloudWatch, initiating replays
through subscription attributes, and understanding the permissions required to
modify and initiate replays.

**Message archiving**

- The topic owner enables the archiving feature and sets the message
  retention period, which can be up to 365 days. For more, see [Amazon SNS message archiving for
  FIFO topic owners](message-archiving-and-replay-topic-owner.md "message-archiving-and-replay-topic-owner.md")
- CloudWatch metrics help monitor the archived messages.

**Message replay**

- A subscriber initiates a replay, selecting the time window for the
  messages to be reprocessed to the subscribed endpoint. For more see, [Amazon SNS message replay for FIFO
  topic subscribers](message-archiving-and-replay-subscriber.md "message-archiving-and-replay-subscriber.md").
- You manage the replay through subscription attributes using the
  `ReplayPolicy` feature.

**Relevant permissions**

- **`SetSubscriptionAttributes`**
  – Required to configure or modify replay settings using the
  `ReplayPolicy` attribute on a subscription.
- **`Subscribe`** – Necessary
  to attach a new subscription and initiate replays.
- **`GetTopicAttributes`** –
  Allows viewing the topic's properties, but replay initiation primarily
  revolves around subscription management.

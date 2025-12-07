# Set attributes

This topic defines the flow block for storing key-value pairs that can be referenced
throughout a journey flow. You can define and update attributes at any step to pass data between
blocks or personalize later actions.

## Description

The Set Attributes block stores key-value pairs that can be referenced throughout a
journey flow. You can define and update attributes at any step to pass data between blocks or
personalize later actions.

For example, you can:

- Store campaign or contact-level data such as customerSegment, preferredChannel, or accountType to drive conditional logic
- Capture and reuse values returned from external systems through Lambda functions, such as offer eligibility or compliance status
- Record message delivery results, such as SMS delivery status or email bounce reason, for use in follow-up logic
- Set loop-level counters or flags to control iterations in multi-step journeys

The Set Attributes block supports the following namespaces:

- Flow attributes – Attributes that persist within the journey execution context
- Lambda invocation – Attributes generated or returned by Lambda function calls
- Loop – Attributes created or updated within looping constructs in a journey
- Delivery receipts – Attributes populated based on message delivery results, such as DeliveryStatus.
- Outbound communication – Attributes related to outbound campaign execution, such as
  ChannelType or outbound communication ID.

Example use case:

- You can use the Set Attributes block to retry a failed SMS message on another channel.
  When an SMS delivery receipt returns a DeliveryStatus of failed, you can set an attribute
  preferredChannel to Email and route the flow to an email delivery branch. This helps ensure
  the customer still receives the message without manual intervention.

## How to configure this

block

You can configure the Set attributes block by using the Amazon Connect admin website or by
using the SetAttributes action in Flow language.

## Common properties

| Property       | Description                                            |
| -------------- | ------------------------------------------------------ |
| Attribute name | Enter the key name for the attribute.                  |
| Value          | Define a literal value or reference another attribute. |
| Namespace      | Choose the applicable namespace for the attribute.     |

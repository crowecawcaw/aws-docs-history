# Automating notifications from AWS services

to Amazon SQS using Amazon EventBridge

Amazon EventBridge allows you to automate AWS services and respond to events, such as application
issues or resource changes, in near real-time.

- You can create rules to filter specific events and define automated actions when a rule
  matches an event.
- EventBridge supports multiple targets, including Amazon SQS standard and FIFO queues, which receive
  events in JSON format.
  For more information, see [Amazon EventBridge targets](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md") in the
  _[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")_.

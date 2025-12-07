# Automation rules in EventBridge

You can use automation rules in Amazon EventBridge to respond to Security Hub findings.
Security Hub sends findings to EventBridge as events in near real time.
You can write basic rules that indicate what automated actions to take when an events match the rules.
Actions that can be automatically triggered include the following:

- Configuring an API destination in EventBridge.
- Invoking Amazon EC2 run commands
- Invoking Lambda functions
- Invoking Step Functions state machines
- Notifying an Amazon SNS topic or an Amazon SQS queue
- Relaying events to Kinesis Data Streams
- Sending a finding to a third-party ticketing, chat, SIEM, or incident response and management tool
- [Sending an event to an EventBridge bus in another AWS account](../../../eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account-custom-bus-source.md "../../../eventbridge/latest/userguide/eb-event-bus-example-policy-cross-account-custom-bus-source.md")

Security Hub sends new findings and updated findings to EventBridge as events.
Then you configure EventBridge rules to respond to each Security Hub event.
For more information, see [What is EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") in the _EventBridge User Guide_.

###### Note

If you have EventBridge rules defined for findings in Security Hub CSPM, the rules could overlap with rules defined for Security Hub.
To avoid sending duplicate findings, evaluate the rules you have defined for Security Hub CSPM to determine if they overlap with rules you are have defined for Security Hub.
Where applicable disable any Security Hub CSPM rules that are replaced by Security Hub rules.

###### Note

As a best practice, make sure users with permission to access EventBridge use AWS Identity and Access Management policies that grant the minimum required permissions.
For more information, see [EventBridge and AWS Identity and Access Management](../../../eventbridge/latest/userguide/eb-iam.md "../../../eventbridge/latest/userguide/eb-iam.md") in the _EventBridge User Guide_.

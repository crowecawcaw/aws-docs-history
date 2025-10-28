# Connect application components with

Amazon EventBridge

You can integrate IAM Identity Center with [Amazon EventBridge](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") to raise events that
initiate administrative notifications or invoke automated workflows in response to specific
IAM Identity Center actions recorded in CloudTrail events.

For example, you might configure [EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") to detect when a user
deletes an application or when IAM Identity Center creates a new group. Depending on your use case, you
can route these events to an Amazon SNS topic to notify administrators or invoke additional
automation using AWS Lambda, [Step Functions](../../../step-functions/latest/dg/connect-eventbridge.md "../../../step-functions/latest/dg/connect-eventbridge.md"), or other
[EventBridge-supported services](../../../eventbridge/latest/userguide/eb-create-rule.md#eb-create-rule-target "../../../eventbridge/latest/userguide/eb-create-rule.md#eb-create-rule-target").

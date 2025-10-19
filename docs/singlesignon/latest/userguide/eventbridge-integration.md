# Connect application components with
 Amazon EventBridge

 You can integrate IAM Identity Center with [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html") to raise events that
 initiate administrative notifications or invoke automated workflows in response to specific
 IAM Identity Center actions recorded in CloudTrail events. 

 For example, you might configure [EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html") to detect when a user
 deletes an application or when IAM Identity Center creates a new group. Depending on your use case, you
 can route these events to an Amazon SNS topic to notify administrators or invoke additional
 automation using AWS Lambda, [Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html "https://docs.aws.amazon.com/step-functions/latest/dg/connect-eventbridge.html"), or other
 [EventBridge-supported services](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-target "https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html#eb-create-rule-target").

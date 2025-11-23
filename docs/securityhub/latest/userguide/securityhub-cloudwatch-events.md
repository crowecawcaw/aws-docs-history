# Using EventBridge for automated response and remediation

By creating rules in Amazon EventBridge, you can respond automatically to AWS Security Hub CSPM findings. Security Hub CSPM sends
findings as _events_ to EventBridge in near-real time. You can write
simple rules to indicate which events you are interested in and what automated actions to
take when an event matches a rule. The actions that can be automatically triggered include
the following:

- Invoking an AWS Lambda function
- Invoking the Amazon EC2 run command
- Relaying the event to Amazon Kinesis Data Streams
- Activating an AWS Step Functions state machine
- Notifying an Amazon SNS topic or an Amazon SQS queue
- Sending a finding to a third-party ticketing, chat, SIEM, or incident response and
  management tool
  Security Hub CSPM automatically sends all new findings and all updates to existing findings to EventBridge as
  EventBridge events. You can also create custom actions that allow you to send selected findings and
  insight results to EventBridge.

You then configure EventBridge rules to respond to each type of event.

For more information about using EventBridge, see the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md").

###### Note

As a best practice, make sure that the permissions granted to your users to access
EventBridge use least-privilege AWS Identity and Access Management (IAM) policies that grant only the required permissions.

For more information, see [Identity and access management in Amazon EventBridge](../../../eventbridge/latest/userguide/auth-and-access-control-eventbridge.md "../../../eventbridge/latest/userguide/auth-and-access-control-eventbridge.md").

A set of templates for cross-account automated response and remediation is also available
in AWS Solutions. The templates leverage EventBridge event rules and Lambda functions. You deploy
the solution using CloudFormation and AWS Systems Manager. The solution can create fully automated response and
remediation actions. It can also use Security Hub CSPM custom actions to create user-triggered response
and remediation actions. For details on how to configure and use the solution, see the
[Automated Security Response on AWS](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/ "https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/") solution page.

###### Topics

- [Security Hub CSPM event types in EventBridge](securityhub-cwe-integration-types.md "securityhub-cwe-integration-types.md")
- [EventBridge event formats for Security Hub CSPM](securityhub-cwe-event-formats.md "securityhub-cwe-event-formats.md")
- [Configuring an EventBridge rule for
  Security Hub CSPM findings](securityhub-cwe-all-findings.md "securityhub-cwe-all-findings.md")
- [Using custom actions to send findings
  and insight results to EventBridge](securityhub-cwe-custom-actions.md "securityhub-cwe-custom-actions.md")

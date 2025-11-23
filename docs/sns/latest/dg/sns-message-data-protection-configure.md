# Creating data protection policies in

Amazon SNS

[Data protection policies](sns-message-data-protection-policies.md "sns-message-data-protection-policies.md") help
you safeguard the data that's published to your Amazon SNS topics by auditing, de-identifying
(masking or redacting), and denying (blocking) sensitive information that moves between
applications or AWS services. You can use AWS API, AWS CLI, CloudFormation, or
AWS Management Console to create data protection policies in Amazon SNS. Only one policy can be defined per
Amazon SNS topic. Each data protection policy can have one or more de-identify and deny
statements, but only one audit statement.

###### Topics

- [Using API](sns-message-data-protection-configure-api.md "sns-message-data-protection-configure-api.md")
- [Using AWS CLI](sns-message-data-protection-configure-cli.md "sns-message-data-protection-configure-cli.md")
- [Using CloudFormation](sns-message-data-protection-configure-cfn.md "sns-message-data-protection-configure-cfn.md")
- [Using the AWS Management Console](sns-message-data-protection-configure-console.md "sns-message-data-protection-configure-console.md")
- [Using AWS SDK](sns-message-data-protection-configure-sdk.md "sns-message-data-protection-configure-sdk.md")

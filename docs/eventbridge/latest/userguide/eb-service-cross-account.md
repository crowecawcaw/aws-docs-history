# Sending events to an AWS service in another account in EventBridge

EventBridge can send events from an event bus in one AWS account to supported AWS services in another account, thereby simplifying the architecture of your event-driven solutions and reducing latency.

For example, suppose you have a set of event buses, hosted in multiple accounts, that you require to send security-related events to an Amazon SQS queue in a centralized account for further asynchronous processing and analysis.

EventBridge supports sending events to cross-account targets in the same Region.

## Supported services

EventBridge supports sending events to the following targets in other AWS accounts:

- Amazon API Gateway APIs
- Amazon Kinesis Data Streams streams
- Lambda functions
- Amazon SNS topics
- Amazon SQS queues

For pricing, see [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/").

## Permissions

Enabling access for cross-account event delivery to AWS services as targets involves the following steps:

- Specify an execution role
- Attach a resource policy to the target

### Specify an execution role

Specify an execution role for EventBridge to use when sending events to the target when the rule is triggered.

This execution role must be in the same account as the event bus. EventBridge assumes
this role when attempting to invoke the target, and any Service Control Policies
(SCPs) affecting this account are applied.

SCPs are a type of organization policy that you can use to manage permissions in your organization. For more information, see [Service control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.

For example, the following policy allows the EventBridge service to assume the execution role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "events.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

And the following policy allows the role to send messages to Amazon SQS queues:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "sqs:SendMessage",
 "Resource": "arn:aws:sqs:`us-east-1`:`123456789012`:`queue-name`"
 }
 ]
}`

```

For accounts using AWS Organizations, you can apply an SCP to
prevent invoking resources that do not belong to your organization, as shown in
the following example:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "*"
 ],
 "Resource": "*",
 "Effect": "Deny",
 "Condition": {
 "StringNotEquals": {
 "aws:ResourceOrgID": "`o-1234567890`"
 }
 }
 }
 ]
}`

```

###### Note

For cross-account targets other than event buses, calling `PutTarget` from a different account than the event bus, even if supplying an execution role from the calling account, is not supported.

### Attach a resource access policy to the target

The AWS services that can receive cross-account events support IAM
resource-based policies. This enables you to attach a resource access policy to the
target, so you can specify which account has access to it.

Building on our earlier example, the following policy allows the event bus account
access to the Amazon SQS queue in the target account:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "SQS:SendMessage"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:sqs:`us-east-1`:`123456789012`:`queue-name`",
 "Principal": {
 "AWS": "`123456789012`"
 }
 }
 ]
}`

```

For more information, see [Identity-based policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the _AWS Identity and Access Management User Guide_.

## Creating rules that send events

to AWS services in other accounts

Specifying an AWS service in another account as a target is part of creating the event bus rule.

###### To create a rule that sends events to an AWS service in a different AWS account using the

console

1. Follow the steps in the [Creating rules that react to events in Amazon EventBridge](eb-create-rule.md "eb-create-rule.md") procedure.
2. In the [Select targets](eb-create-rule.md#eb-create-rule-target "eb-create-rule.md#eb-create-rule-target") step, when prompted to choose a target type:
   1. Select **AWS service**.
   2. Select an AWS service that supports cross-account targets.

   For more information, see [Supported services](#eb-service-cross-account-services "#eb-service-cross-account-services"). 3. For **Target location** choose **Target in another AWS
   account**. 4. Enter the ARN of the target resource to which you want to send events. 5. Select the name of the execution role to use
   from the dropdown list. 6. Provide any additional information
   requested for the service you select. The fields displayed vary depending on the service selected.

3. Complete creating the rule following the procedure steps.

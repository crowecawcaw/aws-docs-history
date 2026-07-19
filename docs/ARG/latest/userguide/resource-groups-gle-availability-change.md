# Group Lifecycle Events feature of AWS Resource Groups availability change

###### Note

AWS Group Lifecycle Events (GLE) feature of AWS Resource Groups will no longer be open to new customers starting July 30, 2026.
If you would like to use the feature, sign up prior to July 30, 2026. Existing customers can continue to use the service as normal.

The Group Lifecycle Events (GLE) feature of AWS Resource Groups is entering maintenance mode.
Starting July 30, 2026, the GLE feature will no longer be available to new customers.
Accounts that have not previously used GLE will no longer be able to enable the feature.
Accounts where the feature is already enabled can continue using GLE with no disruption.
AWS will maintain availability, including addressing critical issues, and provide
continued support through AWS Support channels but will not add new capabilities to the GLE
feature or launch it in additional AWS Regions.

The GLE feature notifies customers of Resource Group membership changes by emitting an event to Amazon EventBridge when resources are added or
removed from a Resource Group as a result of resource tag changes (Tag-based Resource Group) or CloudFormation stack updates (CloudFormation-based
Resource Group), depending on the group type.

As an alternative to GLE, we recommend that you use a combination of native and already existing AWS services including EventBridge,
Lambda, and DynamoDB to replicate the GLE feature.

At a high level, customers will need to create an EventBridge rule that invokes a Lambda function on Tag Change on Resource events (`aws.tag`),
and CloudFormation Resource Status Change events (`aws.cloudformation`). The Lambda function will then need to call AWS Resource Groups
`ListGroupResources` API to retrieve the current resource membership of each in scope Resource Group, compare it against the membership recorded
in a customer-managed persistent storage (for example, in a DynamoDB table) and emit a custom AWS EventBridge event for each resource that was added or
removed. Downstream consumers (for example, SNS, SQS, Lambda, Step Functions) can then subscribe to these custom events. AWS will provide step-by-step
guidance to support customers in implementing alternatives to GLE upon request using AWS Support channels.

If you have additional questions, open a case in the [AWS Support Center](https://support.console.aws.amazon.com/support/home#/ "https://support.console.aws.amazon.com/support/home#/").

# Managing targets in EventBridge Scheduler

The following topics describe how to use templated, and universal targets with EventBridge Scheduler, and provides a list of supported AWS services that you can configure using EventBridge Scheduler's universal target parameter.

_Templated targets_ are a set of common API operations across a group of core AWS services such as Amazon SQS, Lambda, and Step Functions. For example, you can target Lambda's
[Invoke](../../../lambda/latest/dg/API_Invoke.md "../../../lambda/latest/dg/API_Invoke.md") API operation by providing the function ARN, or Amazon SQS's `SendMessage` operation
with the queue ARN of the target.

The _universal target_ is a customizable set of parameters that allow you to invoke a wider set of API operation for many AWS service. For example, you can use EventBridge Scheduler's universal target parameter (UTP)
to create a new Amazon SQS queue using the [`CreateQueue`](../../../AWSSimpleQueueService/latest/APIReference/API_CreateQueue.md "../../../AWSSimpleQueueService/latest/APIReference/API_CreateQueue.md") operation.

To configure either templated or universal targets, your schedule must have permission to call the API operation that you configure as your target. You do this by attaching the required permissions to
your schedule's execution role. For example, to target Amazon SQS's [`SendMessage`](../../../index.md "../../../index.md") operation, the execution role be granted permission to perform the
`sqs:SendMessage` action. In most cases, you can add the necessary permissions by using the [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies")
that the target service supports. However, you can also create your own [customer managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#customer-managed-policies"),
or add [inline permissions](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies") to an existing policy attached to the execution role.
The following topics demonstrate examples of adding permissions for both templated, and universal, target types.

For more information about setting up an execution role for a schedule, see [Set up the execution role](setting-up.md#setting-up-execution-role "setting-up.md#setting-up-execution-role").

###### Topics

- [Using templated targets in EventBridge Scheduler](managing-targets-templated.md "managing-targets-templated.md")
- [Using universal targets in EventBridge Scheduler](managing-targets-universal.md "managing-targets-universal.md")
- [Adding context attributes in EventBridge Scheduler](managing-schedule-context-attributes.md "managing-schedule-context-attributes.md")
- [What's next?](#managing-targets-whats-next "#managing-targets-whats-next")

## What's next?

For more information on the EventBridge Scheduler data types and API operations, see [EventBridge Scheduler API Reference](../APIReference.md "../APIReference.md").

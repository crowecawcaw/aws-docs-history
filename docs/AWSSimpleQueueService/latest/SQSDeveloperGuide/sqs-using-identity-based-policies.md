# Using policies with Amazon SQS

This topic provides examples of identity-based policies in which an account
administrator can attach permissions policies to IAM identities (users, groups, and
roles).

###### Important

We recommend that you first review the introductory topics that explain the basic
concepts and options available for you to manage access to your Amazon Simple Queue Service resources.
For more information, see [Overview of managing access in
Amazon SQS](sqs-overview-of-managing-access.md "sqs-overview-of-managing-access.md").

With the exception of `ListQueues`, all Amazon SQS actions support resource-level permissions. For more information, see [Amazon SQS API permissions:
Actions and resource reference](sqs-api-permissions-reference.md "sqs-api-permissions-reference.md").

## Using Amazon SQS and IAM

policies

There are two ways to give your users permissions to your Amazon SQS resources: using
the Amazon SQS policy system (resource-based policies) and using the IAM policy system
(identity-based policies). You can use one or both methods, with the exception of
the `ListQueues` action, which is a regional permission that can only be
set in an IAM policy.

For example, the following diagram shows an IAM policy and an Amazon SQS policy
equivalent to it. The IAM policy grants the rights to the Amazon SQS
`ReceiveMessage` and `SendMessage` actions for the queue
called `queue_xyz` in your AWS Account, and the policy is attached to
users named Bob and Susan (Bob and Susan have the permissions stated in the policy).
This Amazon SQS policy also gives Bob and Susan rights to the `ReceiveMessage`
and `SendMessage` actions for the same queue.

###### Note

The following example shows simple policies without conditions. You can
specify a particular condition in either policy and get the same result.

![Diagram comparing an IAM policy and an Amazon SQS policy equivalent to it. The IAM policy grants the rights to the Amazon SQS ReceiveMessage and SendMessage actions for the queue called queue_xyz in your AWS Account, and the policy is attached to users named Bob and Susan (Bob and Susan have the permissions stated in the policy). This Amazon SQS policy also gives Bob and Susan rights to the ReceiveMessage and SendMessage actions for the same queue.](images/sqs-iam-policies-equivalent.png)

There is one major difference between IAM and Amazon SQS policies: the Amazon SQS policy
system lets you grant permission to other AWS Accounts, whereas IAM
doesn't.

It is up to you how you use both of the systems together to manage your
permissions. The following examples show how the two policy systems work
together.

- In the first example, Bob has both an IAM policy and an Amazon SQS policy
  that apply to his account. The IAM policy grants his account permission
  for the `ReceiveMessage` action on `queue_xyz`,
  whereas the Amazon SQS policy gives his account permission for the
  `SendMessage` action on the same queue. The following diagram
  illustrates the concept.

![Diagram comparing the components of an IAM policy to an Amazon SQS policy. In the first example, Bob has both an IAM policy and an Amazon SQS policy that apply to his account. The IAM policy grants his account permission for the ReceiveMessage action on queue_xyz, whereas the Amazon SQS policy gives his account permission for the SendMessage action on the same queue.](images/sqs-iam-policies-union.png)

If Bob sends a `ReceiveMessage` request to
`queue_xyz`, the IAM policy allows the action. If Bob sends
a `SendMessage` request to `queue_xyz`, the Amazon SQS
policy allows the action.

- In the second example, Bob abuses his access to `queue_xyz`, so
  it becomes necessary to remove his entire access to the queue. The easiest
  thing to do is to add a policy that denies him access to all actions for the
  queue. This policy overrides the other two because an explicit
  `deny` always overrides an `allow`. For more
  information about policy evaluation logic, see [Using custom policies with the Amazon SQS
  Access Policy Language](sqs-creating-custom-policies.md "sqs-creating-custom-policies.md"). The following diagram
  illustrates the concept.

![Diagram showing an IAM policy override with an Amazon SQS policy. Bob abuses his access to queue_xyz, so it becomes necessary to remove his entire access to the queue. The easiest thing to do is to add a policy that denies him access to all actions for the queue. This policy overrides the other two because an explicit deny always overrides an allow.](images/sqs-iam-policies-deny-override.png)

You can also add an additional statement to the Amazon SQS policy that denies
Bob any type of access to the queue. It has the same effect as adding an
IAM policy that denies Bob access to the queue. For examples of policies
that cover Amazon SQS actions and resources, see [Basic examples of Amazon SQS
policies](sqs-basic-examples-of-sqs-policies.md "sqs-basic-examples-of-sqs-policies.md"). For more
information about writing Amazon SQS policies, see [Using custom policies with the Amazon SQS
Access Policy Language](sqs-creating-custom-policies.md "sqs-creating-custom-policies.md").

## Permissions required to use the Amazon SQS

console

A user who wants to work with the Amazon SQS console must have the minimum set of
permissions to work with the Amazon SQS queues in the user's AWS account. For example,
the user must have the permission to call the `ListQueues` action to be
able to list queues, or the permission to call the `CreateQueue` action
to be able to create queues. In addition to Amazon SQS permissions, to subscribe an Amazon SQS
queue to an Amazon SNS topic, the console also requires permissions for Amazon SNS
actions.

If you create an IAM policy that is more restrictive than the minimum required
permissions, the console might not function as intended for users with that IAM
policy.

You don't need to allow minimum console permissions for users that make calls only
to the AWS CLI or Amazon SQS actions.

# Sending and receiving events between AWS accounts in Amazon EventBridge

You can configure EventBridge to send and receive [events](eb-events.md "eb-events.md") between [event buses](eb-event-bus.md "eb-event-bus.md") in AWS accounts. When
you configure EventBridge to send or receive events between accounts, you can specify which
AWS accounts can send events to or receive events from the event bus in your account. You can
also allow or deny events from specific [rules](eb-rules.md "eb-rules.md") associated with the event bus,
or events from specific sources. For more information, see [Simplifying cross-account access with Amazon EventBridge resource policies](https://aws.amazon.com/blogs/compute/simplifying-cross-account-access-with-amazon-eventbridge-resource-policies/ "https://aws.amazon.com/blogs/compute/simplifying-cross-account-access-with-amazon-eventbridge-resource-policies/")

###### Note

If you use AWS Organizations, you can specify an organization and grant access to all accounts in
that organization. In addition, the sending event bus must have IAM roles attached to them when sending events to another account.
For more information, see [What is AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") in the _AWS Organizations User Guide_.

###### Note

If you're using an Incident Manager response plan as a target, all the response plans that are shared with your account are available by default.

You can send and receive events between event buses in AWS accounts within the same Region in all Regions and between accounts in different Regions as long as the destination Region is a supported
[cross-Region](eb-cross-region.md "eb-cross-region.md") destination Region.

The steps to configure EventBridge to send events to or receive events from an event bus in a different account include the following:

- On the _receiver_ account, edit the permissions on an event
  bus to allow specified AWS accounts, an organization, or all AWS accounts to send events
  to the receiver account.
- On the _sender_ account, set up one or more rules that have the
  receiver account's event bus as the target.

If the sender account inherits permissions to send events from an AWS Organization,
the sender account also must have an IAM role with policies that enable it
to send events to the receiver account. If you use the AWS Management Console to create the rule that
targets the event bus in the receiver account, the role is created automatically. If you use
the AWS CLI, you must create the role manually.

- On the _receiver_ account, set up one or more rules that match events
  that come from the sender account.
  Events sent from one account to another are charged to the sending account as custom events.
  The receiving account is not charged. For more information, see [Amazon EventBridge Pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/").

If a receiver account sets up a rule that sends events received from a sender account on to
a third account, these events are not sent to the third account.

If you have three event buses in the same account, and set up a rule on the first event bus to forward events from the second event bus to a third event bus, those events are not sent to the third event bus.

The following video covers routing events between accounts:

## Grant permissions to allow events

from other AWS accounts

To receive events from other accounts or organizations, you must first edit the permissions on the event bus where you intend to receive events.
The default event bus accepts events from AWS services, other authorized AWS accounts, and
`PutEvents` calls. The permissions for an event bus are granted or denied using
a resource-based policy attached to the event bus. In the policy, you can grant permissions to
other AWS accounts using the account ID, or to an AWS organization using the organization ID.
To learn more about event bus permissions, including example policies, see [Permissions for event buses in Amazon EventBridge](eb-event-bus-perms.md "eb-event-bus-perms.md").

###### Note

EventBridge now requires all new cross account event bus targets to add IAM roles.
This only applies to event bus targets created after March 2, 2023.
Applications created without an IAM role before that date are not affected.
However, we recommend adding IAM roles to grant users access to resources in another account,
as this ensures organization boundaries using Service Control Policies (SCPs) are applied to determine who can send and receive events from accounts in your organization.

###### Important

If you choose to receive events from all AWS accounts, be careful to create rules that
match only the events to receive from others. To create more secure rules, make sure that
the event pattern for each rule contains an `Account` field with the account IDs
of one or more accounts from which to receive events. Rules that have an event pattern
containing an Account field do not match events sent from accounts that are not listed in
the `Account` field. For more information, see [Events in Amazon EventBridge](eb-events.md "eb-events.md").

## Rules for events

between AWS accounts

If your account is set up to receive events from event buses in other AWS accounts, you can write rules
that match those events. Set the [event
pattern](eb-event-patterns.md "eb-event-patterns.md") of the rule to match the events you are
receiving from event buses in the other account.

Unless you specify `account` in the event pattern of a rule, any of your
account's rules, both new and existing, that match events you receive from event buses in other accounts
trigger based on those events. If you are receiving events from event buses in another account, and you want
a rule to trigger only on that event pattern when it is generated from your own account, you
must add `account` and specify your own account ID to the event pattern of the
rule.

If you set up your AWS account to accept events from event buses in all AWS accounts, we strongly
recommend that you add `account` to every EventBridge rule in your account. This prevents
rules in your account from triggering on events from unknown AWS accounts. When you specify
the `account` field in the rule, you can specify the account IDs of more than one
AWS account in the field.

To have a rule trigger on a matching event from any event buses in AWS account that you have granted
permissions to, do not specify \* in the `account` field of the rule. Doing so would
not match any events, because \* never appears in the `account` field of an event.
Instead, just omit the `account` field from the rule.

## Creating rules that send events

between AWS accounts

Specifying an event bus in another account as a target is part of creating the rule.

###### To create a rule that sends events to a different AWS account using the

console

1. Follow the steps in the [Creating rules in Amazon EventBridge](eb-create-rule-visual.md "eb-create-rule-visual.md") procedure.
2. In the [Select targets](eb-create-rule-wizard.md#eb-create-rule-target "eb-create-rule-wizard.md#eb-create-rule-target") step, when prompted to choose a target type:
   1. Select **EventBridge event bus**.
   2. Select **Event bus in a
      different account or Region**.
   3. For **Event bus as target**, enter the ARN of the event bus you want to use.

3. Complete creating the rule following the procedure steps.

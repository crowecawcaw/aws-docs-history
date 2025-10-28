# Permissions for event buses in Amazon EventBridge

The default [event bus](eb-event-bus.md "eb-event-bus.md") in your AWS account only allows
[events](eb-events.md "eb-events.md") from one account. You can grant additional permissions
to an event bus by attaching a [resource-based
policy](eb-use-resource-based.md "eb-use-resource-based.md") to it. With a resource-based policy, you can allow `PutEvents`,
`PutRule`, and `PutTargets` API calls from another account. You can also
use [IAM conditions](eb-use-conditions.md "eb-use-conditions.md") in the policy to grant permissions to an organization, apply [tags](eb-tagging.md "eb-tagging.md"), or filter events to only those from a specific rule or
account. You can set a resource-based policy for an event bus when you create it or
afterward.

EventBridge APIs that accept an event bus `Name` parameter such as `PutRule`,
`PutTargets`, `DeleteRule`, `RemoveTargets`,
`DisableRule`, and `EnableRule` also accept the event bus ARN. Use these
parameters to reference cross-account or cross-Region event buses through the APIs. For example,
you can call `PutRule` to create a [rule](eb-rules.md "eb-rules.md") on an event
bus in a different account without needing to assume a role.

You can attach the example policies in this topic to an IAM role to grant permission to send events to a
different account or Region. Use IAM roles to set organization control policies and boundaries on who can send events from your account to other accounts.
We recommend always using IAM roles when the target of a rule is an event bus. You can attach IAM roles using `PutTarget` calls.
For information about creating a rule to send events to a different account or Region, see [Sending and receiving events between AWS accounts in Amazon EventBridge](eb-cross-account.md "eb-cross-account.md").

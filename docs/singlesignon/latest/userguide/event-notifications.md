

# IAM Identity Center event notifications
<a name="event-notifications"></a>

You receive an event in Amazon EventBridge when a user, group, group membership, or the identity store itself is created, updated, or deleted in IAM Identity Center Identity Store. You can use these events to respond to changes as they happen, instead of periodically checking for changes. For example, you can use these events to:
+ Start onboarding tasks, such as creating resources for a user in an application, when the user is added to a group.
+ Remove access in downstream applications when a user is deleted or removed from a group.
+ Send identity changes to your security information and event management (SIEM) system.

## How event notifications work
<a name="how-event-notifications-work"></a>

You receive events automatically on the default event bus in the AWS account where your IAM Identity Center instance is enabled. For an organization instance, this is the management account of your organization. For an account instance, this is the member account where you enabled your IAM Identity Center instance.

To receive events, create an EventBridge rule on the default event bus in the account and AWS Region that matches the event source `aws.identitystore`. Choose a target for the rule, such as an AWS Lambda function or an Amazon SNS topic.

IAM Identity Center Identity Store starts delivering events after your rule and target are in place. Delivery is forward-looking only. IAM Identity Center Identity Store doesn't backfill or replay changes that occurred before the rule existed, and it doesn't store events that don't match a rule.

If you replicated your IAM Identity Center instance to additional AWS Regions, you also receive events on the default event bus in each additional AWS Region. For more information, see [Receive events in other accounts and Regions](receive-events-other-accounts-regions.md).

## Events that IAM Identity Center Identity Store sends
<a name="events-identitystore-sends"></a>

All events use the event source `aws.identitystore`. The event name is in the `detail-type` field. Identity Store sends the following events.



| Event | Description | 
| --- | --- | 
| User Created | A user is created. | 
| User Updated | A user's attributes are updated. | 
| User Deleted | A user is deleted. | 
| Group Created | A group is created. | 
| Group Updated | A group's attributes are updated. | 
| Group Deleted | A group is deleted. | 
| GroupMembership Created | A user is added to a group. | 
| GroupMembership Deleted | A user is removed from a group. | 
| IdentityStore Created | An identity store is created, for example when you enable IAM Identity Center. | 
| IdentityStore Updated | An identity store's settings are updated. | 
| IdentityStore Deleted | An identity store is deleted, for example when you delete your IAM Identity Center instance. | 

## Event contents
<a name="event-notifications-contents"></a>

Each event contains the following information:
+ The ID of the identity store, and the ARNs of the IAM Identity Center instances that use it.
+ The ID and ARN of the user, group, or group membership that changed. Group membership events also include the IDs and ARNs of the user and the group.
+ The ID of the request that made the change.
+ The time of the change and the AWS Region where the event was sent.

Events don't include user or group attributes, such as names or email addresses, and `Updated` events don't describe what changed. To get the current attributes, call the [DescribeUser](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeUser.html), [DescribeGroup](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroup.html), or [DescribeGroupMembership](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/API_DescribeGroupMembership.html) operation. For more information, see the *[Identity Store API Reference](https://docs.aws.amazon.com/singlesignon/latest/IdentityStoreAPIReference/welcome.html)*. For the event structure, see [Set up event notifications](setup-event-notifications.md).

## Considerations for event notifications
<a name="event-notifications-considerations"></a>
+ IAM Identity Center delivers events at least once. You might receive an event more than once, and events might not arrive in the order in which the changes happened. Design your workflow so that processing the same event twice has no additional effect, and call the Identity Store API when you need the current state of a user, group, or group membership.
+ Delivery time isn't guaranteed. To keep downstream systems accurate, periodically compare them with the data that the Identity Store API returns, in addition to processing events.
+ You receive deletion events for a deleted identity store over time. When you delete your IAM Identity Center instance, you receive an `IdentityStore Deleted` event. IAM Identity Center then deletes the users, groups, and group memberships in the identity store in the background, and you receive a `Deleted` event for each one. These events can arrive some time after the `IdentityStore Deleted` event.
+ Event notifications don't map one to one to CloudTrail events. A CloudTrail event records an API call. An event notification records a change to a user, group, group membership, or identity store, so one API call can result in no event notifications or in several. To respond to changes, use event notifications. To audit who called which API operation, use AWS CloudTrail. For more information, see [Logging IAM Identity Center API calls with AWS CloudTrail](logging-using-cloudtrail.md).

## Related information
<a name="event-notifications-related-info"></a>
+ [Events that IAM Identity Center Identity Store sends](#events-identitystore-sends)
+ [Using IAM Identity Center across multiple AWS Regions](multi-region-iam-identity-center.md)
+ [Set up event notifications](setup-event-notifications.md)
+ [Receive events in other accounts and Regions](receive-events-other-accounts-regions.md)
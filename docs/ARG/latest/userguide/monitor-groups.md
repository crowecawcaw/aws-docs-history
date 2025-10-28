# Group lifecycle events: Monitoring resource groups for changes

After you use AWS Resource Groups to organize your resources into groups, you can monitor those
groups for changes that are exposed to you as _events_. You
can receive a notification about a group event as a signal for you to take some kind of
action. For example, you could configure a notification that is sent whenever a group's
membership changes. You could use an event from adding a new group member to trigger a Lambda
function that programmatically reviews the change to ensure that new group members meet
compliance requirements set by your organization. Such a Lambda function could perform
automatic remediation for any new group members that fail to meet those requirements. An
event caused by the removal of a group member could trigger a Lambda function that performs
any required cleanup, such as deleting linked resources.

By turning on group lifecycle events for your resource groups, you allow events about changes to your
groups to be captured by Amazon EventBridge and made available to all of the various EventBridge supported
target services. You can then configure those target services to automatically take whatever
actions your scenario requires. These targets include a variety of AWS services such as
Amazon Simple Notification Service (Amazon SNS), Amazon Simple Queue Service (Amazon SQS), and AWS Lambda. With services like Lambda, your events
can trigger _programmatic_ responses that use code to
perform whatever actions you require. For a list of the AWS services that you can target
with EventBridge, see [Amazon EventBridge targets](../../../eventbridge/latest/userguide/eventbridge-targets.md "../../../eventbridge/latest/userguide/eventbridge-targets.md") in the _Amazon EventBridge User Guide_.

When you turn on group lifecycle events, AWS Resource Groups creates the following items:

- An AWS Identity and Access Management (IAM) service-linked role that has permission to monitor your
  resources for any changes to their tags and your AWS CloudFormation stacks for any changes to the
  resources that are part of a stack.
- A Resource Groups managed EventBridge rule that captures the details of any tag or stack changes to
  your resources. EventBridge uses this rule to notify Resource Groups about those changes. Then, Resource Groups
  generates membership events to send to EventBridge for your custom rules to process.
  The service-linked role can be assumed by _only_ the
  Resource Groups service. For more information about the service-linked role used by Resource Groups for this
  feature, see [Using service-linked roles for
  Resource Groups](security_iam_service-linked-roles.md "security_iam_service-linked-roles.md").

When this feature is turned on, Resource Groups generates an event when you make any of the
following changes to a resource group:

- Create a new resource group.
- Update the query which defines the membership of [query-based resource group](gettingstarted-query.md "gettingstarted-query.md").
- Update the configuration of a [service linked resource group](../APIReference/about-slg.md "../APIReference/about-slg.md").
- Update the description of a resource group.
- Delete a resource group.
- Change a resource group's membership by adding or removing a resource from the
  group. A membership change can also happen when tags change, or when a AWS CloudFormation stack
  changes.

###### Important

- To successfully receive and respond to group events, you must make changes to
  both Resource Groups and EventBridge. You can perform the changes in any order, but no group
  events are published to EventBridge targets until after you make changes to both
  services.

- The resource group changes don't include changes to any tags attached to the
  resource group itself. To generate events based on tag changes to your groups,
  you must use an EventBridge rule that uses the `aws.tag` source, instead of
  the `aws.resource-groups` source. For more information, see [Tag change events on AWS Resources](../../../eventbridge/latest/userguide/event-types.md#tag-event-types "../../../eventbridge/latest/userguide/event-types.md#tag-event-types") in the _Amazon EventBridge User Guide_.

###### Topics

- [Turning on group lifecycle events in Resource Groups](monitor-groups-turn-on.md "monitor-groups-turn-on.md")
- [Creating an EventBridge rule to capture group lifecycle events and
  publish notifications](monitor-groups-create-rule.md "monitor-groups-create-rule.md")
- [Turning off group lifecycle events](monitor-groups-turn-off.md "monitor-groups-turn-off.md")
- [Structure and syntax of Resource Groups lifecycle
  events](monitor-groups-syntax.md "monitor-groups-syntax.md")

# Best practices when defining rules in Amazon EventBridge

Below are some best practices to consider when you create rules for your event buses.

## Set a single target for each rule

While you can specify up to five targets for a given rule, managing rules is easier when you specify a single target for each rule. If more than one target needs to receive the same set of events, we recommend duplicating the rule to deliver the same events to different targets. This encapsulation simplifies maintaining rules: if the needs of the event targets diverge over time, you can update each rule and its event pattern independently of the others.

## Set rule permissions

You can enable event-consuming application components or services to be in control
of managing their own rules. A common architectural approach adopted by customers is to
isolate these application components or services by using separate AWS accounts. To
enable the flow of events from one account to another, you must create a rule on one
event bus that routes events to an event bus in another account. You can enable
event-consuming teams or services to be in control of managing their own rules. You do
this by specifying the appropriate permissions to their accounts through resource
policies. This works across accounts and Regions.

For more information, see [Permissions for event buses in Amazon EventBridge](eb-event-bus-perms.md "eb-event-bus-perms.md").

For example of resource policies, see
[Multi-account design patterns with Amazon EventBridge](https://github.com/aws-samples/amazon-eventbridge-resource-policy-samples/tree/main/patterns "https://github.com/aws-samples/amazon-eventbridge-resource-policy-samples/tree/main/patterns")
on GitHub.

## Monitor rule performance

Monitor your rules to make sure they are performing as you expect:

- Monitor the `TriggeredRules` metric for missing data-points or anomalies can assist
  you in detecting discrepancies for a publisher that made a breaking change.
  For more information, see [Monitoring Amazon EventBridge](eb-monitoring.md "eb-monitoring.md").
- Alarm on anomalies or maximum expected count can also help detecting when a rule is matching
  against new events. This can happen when event publishers, including AWS
  services and SaaS partners, introduce new events when enabling new use-cases
  and features. When these new events are unexpected and lead to a higher
  volume than the processing rate of the downstream target, they can lead to
  an event backlog.

Such processing of unexpected events can also lead to unwanted billing charges.

It can also trigger throttling of rules when the account goes over its
aggregate target invocations per second service quota. EventBridge will still
attempt to deliver events matched by throttled rules and retry up to 24 hours or
as described within the target’s custom retry policy.
You can detect and alarm throttled rules using the `ThrottledRules` metric

- For low-latency use cases, you can also monitor latency using `IngestionToInvocationStartLatency`,
  which provides an indication of health of your event bus.
  Any extended periods of high latency over 30 seconds may indicate a service disruption or rule throttling.

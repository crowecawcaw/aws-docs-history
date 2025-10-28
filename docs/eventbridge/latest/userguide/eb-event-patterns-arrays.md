# Matching on multiple values for an event field in Amazon EventBridge

The value of each field in an [event pattern](eb-event-patterns.md "eb-event-patterns.md") is an
array containing one or more values. An event pattern matches the [event](eb-events.md "eb-events.md") if any of the values in the array match the value in the event. If the
value in the event is an array, then the event pattern matches if the intersection of the
event pattern array and the event array is non-empty.

###### Important

In EventBridge, it is possible to create rules that can lead to higher-than-expected charges
and throttling. For example, you can inadvertently create a rule that leads to an
infinite loop, where a rule is fired recursively without end. Suppose you created a rule
to detect that ACLs have changed on an Amazon S3 bucket, and trigger software to change them
to the desired state. If the rule is not written carefully, the subsequent change to the
ACLs fires the rule again, creating an infinite loop.

For guidance on how to write precise rules and event patterns to minimize such unexpected results,
see [Best practices for rules](eb-rules-best-practices.md "eb-rules-best-practices.md") and [Best practices](eb-patterns-best-practices.md "eb-patterns-best-practices.md").

For example, consider an event pattern that includes the following field.

```

"resources": [
   "arn:aws:ec2:us-east-1:123456789012:instance/i-b188560f",
   "arn:aws:ec2:us-east-1:111122223333:instance/i-b188560f",
   "arn:aws:ec2:us-east-1:444455556666:instance/i-b188560f",
]
```

The preceding event pattern matches an event that includes the following field because the
first item in the event pattern array matches the second item in the event array.

```

"resources": [
   "arn:aws:autoscaling:us-east-1:123456789012:autoScalingGroup:eb56d16b-bbf0-401d-b893-d5978ed4a025:autoScalingGroupName/ASGTerminate",
   "arn:aws:ec2:us-east-1:123456789012:instance/i-b188560f"
]
```

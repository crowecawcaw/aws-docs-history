# Event pattern syntax

To create an event pattern, you specify the fields of an event that you want the event
pattern to match. Only specify the fields that you use for matching.

For example, the following event pattern example only provides values for three
fields: the top-level fields `"source"` and `"detail-type"`, and
the `"state"` field inside the `"detail"` object field. EventBridge
ignores all the other fields in the event when applying the rule.

```
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["terminated"]
  }
}
```

For an event pattern to match an event, the event must contain all the field
names listed in the event pattern. The field names must also appear in the event with
the same nesting structure.

When you write event patterns to match events, you can use the
`TestEventPattern` API or the `test-event-pattern` CLI command
to test that your pattern matches the correct events. For more information, see [TestEventPattern](../../../AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.md "../../../AmazonCloudWatchEvents/latest/APIReference/API_TestEventPattern.md").

## Matching event values

In an event pattern, the value to match is in a JSON array, surrounded by square
brackets ("[", "]") so that you can provide multiple values. For example, to match
events from Amazon EC2 or AWS Fargate, you could use the following pattern, which
matches events where the value for the `"source"` field is either
`"aws.ec2"` or `"aws.fargate"`.

```
{
    "source": ["aws.ec2", "aws.fargate"]
}
```

For more information, see [Matching on multiple field values](eb-event-patterns-arrays.md "eb-event-patterns-arrays.md").

## Using comparison operators in Amazon EventBridge event patterns

Amazon EventBridge supports declarative content filtering using event patterns. With content filtering, you can write complex event patterns
that only match events under very specific conditions. For example, you can create an event
pattern that matches an event when:

- A field of the event is within a specific numeric range.
- The event comes from a specific IP address.
- A specific field doesn't exist in the event JSON.

For more information, see [Comparison operators](eb-create-pattern-operators.md "eb-create-pattern-operators.md").

## Considerations when creating event patterns

Below are some things to consider when constructing your event patterns:

- EventBridge ignores the fields in the event that aren't included in the event pattern.
  The effect is that there is a `"*": "*"` wildcard for fields that don't appear in the
  event pattern.
- The values that event patterns match follow JSON rules. You can include strings
  enclosed in quotation marks ("), numbers, and the keywords `true`,
  `false`, and `null`.
- For strings, EventBridge uses exact character-by-character matching without
  case-folding or any other string normalization.
- For numbers, EventBridge uses string representation. For example, 300, 300.0, and
  3.0e2 are not considered equal.
- If multiple patterns are specified for the same JSON field, EventBridge only uses the last one.
- Be aware that when EventBridge compiles event patterns for use, it uses dot (.) as the joining character.

This means EventBridge will treat the following event patterns as identical:

```
## has no dots in keys
{ "detail" : { "state": { "status": [ "running" ] } } }

## has dots in keys
{ "detail" : { "state.status": [ "running" ] } }
```

And that both event patterns will match the following two events:

```
## has no dots in keys
{ "detail" : { "state": { "status": "running" } } }

## has dots in keys
{ "detail" : { "state.status": "running"  } }
```

###### Note

This describes current EventBridge behavior, and should not be relied on to not change.

- Event patterns containing duplicate fields are invalid. If a pattern contains duplicate fields, EventBridge only considers the final field value.

For example, the following event patterns will match the same event:

```
## has duplicate keys
{
  "source": ["aws.s3"],
  "source": ["aws.sns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail":  {
      "eventSource": ["s3.amazonaws.com"],
      "eventSource": ["sns.amazonaws.com"]
  }
}

## has unique keys
{
  "source": ["aws.sns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": { "eventSource": ["sns.amazonaws.com"] }
}
```

And EventBridge treats the following two events as identical:

```
## has duplicate keys
{
  "source": ["aws.s3"],
  "source": ["aws.sns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail":  [
    {
      "eventSource": ["s3.amazonaws.com"],
      "eventSource": ["sns.amazonaws.com"]
    }
  ]
}

## has unique keys
{
  "source": ["aws.sns"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": [
    { "eventSource": ["sns.amazonaws.com"] }
  ]
}
```

###### Note

This describes current EventBridge behavior, and should not be relied on to not change.

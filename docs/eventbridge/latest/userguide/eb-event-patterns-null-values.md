# Matching events on null values and empty strings in Amazon EventBridge

###### Important

In EventBridge, it is possible to create rules that can lead to higher-than-expected charges
and throttling. For example, you can inadvertently create a rule that leads to an
infinite loop, where a rule is fired recursively without end. Suppose you created a rule
to detect that ACLs have changed on an Amazon S3 bucket, and trigger software to change them
to the desired state. If the rule is not written carefully, the subsequent change to the
ACLs fires the rule again, creating an infinite loop.

For guidance on how to write precise rules and event patterns to minimize such unexpected results,
see [Best practices for rules](eb-rules-best-practices.md "eb-rules-best-practices.md") and [Best practices](eb-patterns-best-practices.md "eb-patterns-best-practices.md").

You can create an [event pattern](eb-event-patterns.md "eb-event-patterns.md") that matches a
field in an [event](eb-events.md "eb-events.md") that has a null value or is an empty
string. Consider the following example event.

See best practices to avoid higher than expected charges and throttling

```
{
  "version": "0",
  "id": "3e3c153a-8339-4e30-8c35-687ebef853fe",
  "detail-type": "EC2 Instance Launch Successful",
  "source": "aws.autoscaling",
  "account": "123456789012",
  "time": "2015-11-11T21:31:47Z",
  "region": "us-east-1",
  "resources": [
   ],
  "detail": {
    "eventVersion": "",
    "responseElements": null
   }
}

```

To match events where the value of `eventVersion` is an empty string, use the
following event pattern, which matches the preceding event.

```
{
  "detail": {
     "eventVersion": [""]
  }
}
```

To match events where the value of `responseElements` is null, use the
following event pattern, which matches the preceding event.

```
{
  "detail": {
     "responseElements": [null]
  }
}
```

###### Note

Null values and empty strings are not interchangeable in pattern matching. An event pattern
that matches empty strings doesn't match values of `null`.

## Using null values in AWS CloudFormation templates

AWS CloudFormation does not allow `null` values in templates. If you define an event
pattern with a null value using YAML or JSON object syntax, the template validation fails
with the error: `'null' values are not allowed in templates`.

To work around this limitation, specify the `EventPattern` property as a
JSON string instead of a YAML or JSON object. The following example shows how to match
on null values in a AWS CloudFormation template:

```
MyRule:
  Type: AWS::Events::Rule
  Properties:
    EventPattern: '{"detail":{"responseElements":[null]}}'
```

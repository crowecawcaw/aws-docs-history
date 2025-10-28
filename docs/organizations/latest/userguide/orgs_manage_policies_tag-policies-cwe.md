# Using Amazon EventBridge to monitor noncompliant

tags

You can use Amazon EventBridge, formerly Amazon CloudWatch Events, to monitor when noncompliant tags are introduced. In the following
example event, the `"false"` value for `tag-policy-compliant`
indicates that a new tag is noncompliant with the effective tag policy.

```
{
  "detail-type": "Tag Change on Resource",
  "region": "us-east-1",
  "resources": [
    "arn:aws:ec2:us-east-1:123456789012:instance/i-0000000aaaaaaaaaa"
  ],
  "detail": {
    "changed-tag-keys": [
      "a-new-key"
    ],
    "service": "ec2",
    "resource-type": "instance",
    "version": 3,
    "tag-policy-compliant": "false",
    "tags": {
      "a-new-key": "tag-value-on-new-key-just-added"
    }
  }
}
```

You can subscribe to events and specify strings or patterns to monitor. For more
information on EventBridge, see the _[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md")_.

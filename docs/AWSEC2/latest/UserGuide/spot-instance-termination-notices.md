# Spot Instance interruption notices

A _Spot Instance interruption notice_ is a warning that is issued
two minutes before Amazon EC2 stops or terminates your Spot Instance. If you specify hibernation
as the interruption behavior, you receive an interruption notice, but you do not
receive a two-minute warning because the hibernation process begins
immediately.

The best way for you to gracefully handle Spot Instance interruptions is to architect your
application to be fault-tolerant. To accomplish this, you can take advantage of Spot Instance
interruption notices. We recommend that you check for these interruption notices
every 5 seconds.

The interruption notices are made available as an EventBridge event and as items in the [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md") on the Spot Instance.
Interruption notices are emitted on a best effort basis.

## EC2 Spot Instance Interruption Warning event

When Amazon EC2 is going to interrupt your Spot Instance, it emits an event two minutes prior to the
actual interruption (except for hibernation, which gets the interruption notice,
but not two minutes in advance, because hibernation begins immediately). This
event can be detected by Amazon EventBridge. For more information about EventBridge events, see
the [Amazon EventBridge User Guide](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md"). For a detailed example that walks you through how to create
and use event rules, see [Taking Advantage of Amazon EC2 Spot Instance Interruption Notices](https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/ "https://aws.amazon.com/blogs/compute/taking-advantage-of-amazon-ec2-spot-instance-interruption-notices/").

The following is an example of the event for Spot Instance interruption. The possible values for
`instance-action` are `hibernate`, `stop`,
or `terminate`.

```
{
    "version": "0",
    "id": "`12345678-1234-1234-1234-123456789012`",
    "detail-type": "EC2 Spot Instance Interruption Warning",
    "source": "aws.ec2",
    "account": "`123456789012`",
    "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "region": "`us-east-2`",
    "resources": ["arn:aws:ec2:`us-east-2a`:instance/`i-1234567890abcdef0`"],
    "detail": {
        "instance-id": "`i-1234567890abcdef0`",
        "instance-action": "`action`"
    }
}
```

###### Note

The ARN format of the Spot Instance interruption event is
`arn:aws:ec2:`availability-zone`:instance/`instance-id``.
This format differs from the [EC2 resource ARN format](../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies "../../../service-authorization/latest/reference/list_amazonec2.md#amazonec2-resources-for-iam-policies").

## instance-action

The `instance-action` item specifies the action and the approximate
time, in UTC, when the action will occur.

If your Spot Instance is marked to be stopped or terminated by Amazon EC2, the
`instance-action` item is present in your [instance metadata](ec2-instance-metadata.md "ec2-instance-metadata.md"). Otherwise, it is
not present. You can retrieve the `instance-action` using
Instance Metadata Service Version 2 (IMDSv2) as follows.

Linux

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/spot/instance-action
```

Windows

```
[string]$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/meta-data/spot/instance-action
```

The following example output indicates the time at which this instance will be
stopped.

```
{"action": "stop", "time": "2017-09-18T08:22:00Z"}
```

The following example output indicates the time at which this instance will be
terminated.

```
{"action": "terminate", "time": "2017-09-18T08:22:00Z"}
```

If Amazon EC2 is not preparing to stop or terminate the instance, or if you terminated the
instance yourself, `instance-action` is not present in the instance
metadata and you receive an HTTP 404 error when you try to retrieve it.

## termination-time

The `termination-time` item specifies the approximate time in UTC when the
instance will receive the shutdown signal.

###### Note

This item is maintained for backward compatibility; you should use
`instance-action` instead.

If your Spot Instance is marked for termination by Amazon EC2 (either due to a Spot Instance interruption where
the interruption behavior is set to `terminate`, or due to the
cancellation of a persistent Spot Instance request), the `termination-time`
item is present in your [instance
metadata](ec2-instance-metadata.md "ec2-instance-metadata.md"). Otherwise, it is not present. You can retrieve the
`termination-time` using IMDSv2 as follows.

Linux

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
if curl -H "X-aws-ec2-metadata-token: $TOKEN" -s http://169.254.169.254/latest/meta-data/spot/termination-time | grep -q .*T.*Z; then echo termination_scheduled; fi
```

Windows

```
[string]$token = Invoke-RestMethod -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} -Method PUT -Uri http://169.254.169.254/latest/meta-data/spot/termination-time
```

The following is example output.

```
2015-01-05T18:02:00Z
```

If Amazon EC2 is not preparing to terminate the instance (either because there is no Spot Instance
interruption or because your interruption behavior is set to `stop`
or `hibernate`), or if you terminated the Spot Instance yourself, the
`termination-time` item is either not present in the instance
metadata (so you receive an HTTP 404 error) or contains a value that is not a
time value.

If Amazon EC2 fails to terminate the instance, the request status is set to
`fulfilled`. The `termination-time` value remains in
the instance metadata with the original approximate time, which is now in the
past.

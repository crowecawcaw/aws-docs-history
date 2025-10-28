# Detach a principal from a thing

You can use the `DetachThingPrincipal` command to detach a
certificate from a thing:

```
$ aws iot detach-thing-principal \
    --thing-name "MyLightBulb" \
    --principal "arn:aws:iot:`us-east-1:123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`"
```

The **DetachThingPrincipal** command doesn't produce any
output.

For more information, see [detach-thing-principal](../apireference/API_DetachThingPrincipal.md "../apireference/API_DetachThingPrincipal.md") from the _AWS IoT Core API
Reference_.

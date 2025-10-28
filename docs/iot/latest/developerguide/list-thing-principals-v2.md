# List principals associated with a thing

V2

To list the certificates associated with the specified thing, along with the
attachment type, run the [`list-thing-principals-V2`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principalsv2.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principalsv2.html") command. The attachment type
refers to how the certificate is attached to the thing.

```
$ aws iot list-thing-principals-v2 \
    --thing-name "thing_1"
```

The output can look like the following.

```
{
    "ThingPrincipalObjects": [
        {
            "thingPrincipalType": "NON_EXCLUSIVE_THING",
            "principal": "arn:aws:iot:`us-east-1`:`123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`"
        },
        {
            "thingPrincipalType": "NON_EXCLUSIVE_THING",
            "principal": "arn:aws:iot:`us-east-1`:`123456789012`:cert/`1a234b39b4b68278f2e9d84bf97eac2cbf4a1c28b23ea29a44559b9bcf8d395b`"
        }
    ]
}
```

For more information, see [ListThingsPrincipalV2](../apireference/API_ListThingPrincipalsV2.md "../apireference/API_ListThingPrincipalsV2.md") from the _AWS IoT Core API
Reference_.

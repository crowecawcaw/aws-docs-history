# List principals associated with a thing

To list the principals associated with the specified thing, run the [`list-thing-principals`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principals.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principals.html") command. Note that this command
doesn't list the attachment type between the thing and the certificate. To list the
attachment type, use the [`list-thing-principals-v2`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principalsv2.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-thing-principalsv2.html") command. For more
information, see [List principals associated with a thing
V2](list-thing-principals-v2.md "list-thing-principals-v2.md").

```
$ aws iot list-thing-principals \
    --thing-name "MyLightBulb1"
```

The output can look like the following.

```
{
    "principals": [
         "arn:aws:iot:`us-east-1`:`123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`",
         "arn:aws:iot:`us-east-1`:`123456789012`:cert/`1a234b39b4b68278f2e9d84bf97eac2cbf4a1c28b23ea29a44559b9bcf8d395b`"
    ]
}
```

For more information, see [ListThingPrincipals](../apireference/API_ListThingPrincipals.md "../apireference/API_ListThingPrincipals.md") from the _AWS IoT Core API
Reference_.

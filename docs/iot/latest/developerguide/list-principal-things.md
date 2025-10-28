# List things associated with a principal

To list the things associated with the specified principal, run the [`list-principal-things`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-things.htmls "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-things.htmls") command. Note that this command
doesn't list the attachment type between the thing and the certificate. To list the
attachment type, use the [`list-principal-things-v2`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-thingsv2.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-thingsv2.html") command. For more
information, see [List things associated with a principal
V2](list-principal-things-v2.md "list-principal-things-v2.md").

```
$ aws iot list-principal-things \
    --principal "arn:aws:iot:`us-east-1:123456789012`:cert/`2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8`"
```

The output can look like the following.

```
{
    "things": [
        "MyLightBulb1",
        "MyLightBulb2"
    ]
}
```

For more information, see [ListPrincipalThings](../apireference/API_ListPrincipalThings.md "../apireference/API_ListPrincipalThings.md") from the _AWS IoT Core API
Reference_.

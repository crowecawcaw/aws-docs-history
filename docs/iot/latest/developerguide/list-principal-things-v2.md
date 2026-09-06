

# List things associated with a principal V2
<a name="list-principal-things-v2"></a>

To list the things associated with the specified certificate, along with the attachment type, run the [`list-principal-things-v2`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-principal-thingsv2.html) command. The attachment type refers to how the certificate is attached to the thing.

```
$ aws iot list-principal-things-v2 \
    --principal "arn:aws:iot:{{us-east-1:123456789012}}:cert/{{2e1eb273792174ec2b9bf4e9b37e6c6c692345499506002a35159767055278e8}}"
```

The output can look like the following.

```
{
    "PrincipalThingObjects": [
        {
            "thingPrincipalType": "NON_EXCLUSIVE_THING",
            "thing": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:thing/{{thing_1}}"
        }, 
        {
            "thingPrincipalType": "NON_EXCLUSIVE_THING",
            "thing": "arn:aws:iot:{{us-east-1}}:{{123456789012}}:thing/{{thing_2}}"
        }

    ]
}
```

For more information, see [ListPrincipalThingsV2](https://docs.aws.amazon.com/iot/latest/apireference/API_ListPrincipalThingsV2.html) from the *AWS IoT Core API Reference*.
# Describe things

You can use the **DescribeThing** command to display more detailed
information about a thing:

```
$ aws iot describe-thing --thing-name "MyLightBulb"
{
    "version": 3,
    "thingName": "MyLightBulb",
    "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyLightBulb",
    "thingId": "12345678abcdefgh12345678ijklmnop12345678",
    "defaultClientId": "MyLightBulb",
    "thingTypeName": "StopLight",
    "attributes": {
        "model": "123",
        "wattage": "75"
    }
}
```

For more information, see [describe-thing](../../../cli/latest/reference/iot/describe-thing.md "../../../cli/latest/reference/iot/describe-thing.md") from
the AWS CLI Command Reference.

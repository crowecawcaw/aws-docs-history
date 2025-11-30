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

You can also access this API within the rules engine using the inline function
`get_registry_data()`. You can use this function to dynamically access
and utilize thing registry information (including attributes, thing types, and group
memberships) by calling `DescribeThing` and
`ListThingGroupsForThing` APIs directly within AWS IoT rules, enabling
real-time message processing and routing based on your device registry data. For
more information, see [`get_registry_data`](iot-sql-functions.md#iot-sql-function-get-registry_data "iot-sql-functions.md#iot-sql-function-get-registry_data").

For more information, see [describe-thing](../../../cli/latest/reference/iot/describe-thing.md "../../../cli/latest/reference/iot/describe-thing.md") from
the AWS CLI Command Reference.

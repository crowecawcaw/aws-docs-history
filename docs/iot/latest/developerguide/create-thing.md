# Create a thing

The following command shows how to use the AWS IoT **CreateThing**
command from the CLI to create a thing. You can't change a thing's name after you
create it. To change a thing's name, create a new thing, give it the new name, and
then delete the old thing.

```
$ aws iot create-thing \
    --thing-type-name "MyLightBulb" \
    --attribute-payload "{\"attributes\": {\"wattage\":\"75\", \"model\":\"123\"}}"
```

The **CreateThing** command displays the name and Amazon Resource
Name (ARN) of your new thing:

```
{
    "thingArn": "arn:aws:iot:us-east-1:123456789012:thing/MyLightBulb",
    "thingName": "MyLightBulb",
    "thingId": "12345678abcdefgh12345678ijklmnop12345678"
}
```

###### Note

We don't recommend using personally identifiable information in your thing
names.

For more information, see [create-thing](../../../cli/latest/reference/iot/create-thing.md "../../../cli/latest/reference/iot/create-thing.md") from the
AWS CLI Command Reference.

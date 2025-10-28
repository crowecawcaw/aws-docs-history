# Create a thing type

You can use the **CreateThingType** command to create a thing
type:

```
$ aws iot create-thing-type

                --thing-type-name "LightBulb" --thing-type-properties "thingTypeDescription=light bulb type, searchableAttributes=wattage,model"
```

The **CreateThingType** command returns a response that contains
the thing type and its ARN:

```
{
    "thingTypeName": "LightBulb",
    "thingTypeId": "df9c2d8c-894d-46a9-8192-9068d01b2886",
    "thingTypeArn": "arn:aws:iot:us-west-2:123456789012:thingtype/LightBulb"
}
```

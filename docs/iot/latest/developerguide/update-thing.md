# Update a thing

You can use the **UpdateThing** command to update a thing. This
command updates only the thing's attributes. You can't change a thing's name. To
change a thing's name, create a new thing, give it the new name, and then delete the
old thing.

```
$ aws iot update-thing --thing-name "MyLightBulb" --attribute-payload "{\"attributes\": {\"wattage\":\"150\", \"model\":\"456\"}}"
```

The **UpdateThing** command does not produce output. You can use
the **DescribeThing** command to see the result:

```
$ aws iot describe-thing --thing-name "MyLightBulb"
{
    "attributes": {
        "model": "456",
        "wattage": "150"
    },
    "version": 2,
    "thingName": "MyLightBulb"
}
```

For more information, see [update-thing](../../../cli/latest/reference/iot/update-thing.md "../../../cli/latest/reference/iot/update-thing.md") from the
AWS CLI Command Reference.

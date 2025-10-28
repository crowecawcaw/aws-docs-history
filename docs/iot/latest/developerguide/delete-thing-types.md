# Delete a thing type

You can delete thing types only after they have been deprecated. To delete a thing
type, use the **DeleteThingType** command:

```
$ aws iot delete-thing-type --thing-type-name "StopLight"
```

###### Note

Before you can delete a thing type, wait for five minutes after you deprecate
it.

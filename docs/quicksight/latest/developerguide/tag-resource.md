# TagResource

Use the `TagResource` API operation to assign one or more tags (key-value pairs) to the specified Amazon Quick Sight resource.

Following
is an example AWS CLI command for this operation. To find a resource's Amazon Resource
Name (ARN), use the `List` operation for the resource, for example
`ListDashboards`.

AWS CLI

```
aws quicksight tag-resource
    --resource-arn `777788889999`
    --tags Key=`NewDashboard`,Value=`True`
```

For more information about the `TagResource` API operation, see [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") in the _Amazon Quick Sight API Reference_.

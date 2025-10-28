# UntagResource

Use the `UntagResource` API operation to remove a tag from a resource.
Before you do so, you can call the `ListTagsForResource` API operation to list the tags assigned to a resource.

Following
is an example AWS CLI command for this operation. To find a resource’s Amazon Resource
Name (ARN), use the `List` operation for the resource, for example
`ListDashboards`.

AWS CLI

```
aws quicksight untag-resource
    --resource-arn `777788889999`
    --tag-keys `NewDashboard`,`ExampleDashboard`
```

For more information about the `UntagResource` API operation, see [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") in the _Amazon Quick Sight API Reference_.

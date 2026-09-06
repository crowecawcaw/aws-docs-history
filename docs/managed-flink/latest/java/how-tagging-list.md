

# List tags for an application
<a name="how-tagging-list"></a>

To list existing tags, you use the [ListTagsForResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListTagsForResource.html) action.

The following example request for the `ListTagsForResource` action lists tags for an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalyticsus-west-2:{{012345678901}}:application/MyApplication"
}
```


# Remove tags from an application
<a name="how-tagging-remove"></a>

To remove tags from an application, you use the [UntagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UntagResource.html) action.

The following example request for the `UntagResource` action removess tags from an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalyticsus-west-2:{{012345678901}}:application/MyApplication",
   "TagKeys": [ "KeyOfFirstTagToRemove", "KeyOfSecondTagToRemove" ]
}
```
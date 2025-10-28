Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Remove tags from an application

To remove tags from an application, you use the [UntagResource](../apiv2/API_UntagResource.md "../apiv2/API_UntagResource.md") action.

The following example request for the `UntagResource` action removess tags from an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalyticsus-west-2:`012345678901`:application/MyApplication",
   "TagKeys": [ "KeyOfFirstTagToRemove", "KeyOfSecondTagToRemove" ]
}
```

Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Add or update tags for an existing application

You add tags to an application using the [TagResource](../apiv2/API_TagResource.md "../apiv2/API_TagResource.md") action. You cannot add tags to an application using the
[UpdateApplication](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") action.

To update an existing tag, add a tag with the same key of the existing tag.

The following example request for the `TagResource` action adds new tags or updates existing tags:

```
{
   "ResourceARN": "string",
   "Tags": [
      {
         "Key": "NewTagKey",
         "Value": "NewTagValue"
      },
      {
         "Key": "ExistingKeyOfTagToUpdate",
         "Value": "NewValueForExistingTag"
      }
   ]
}
```

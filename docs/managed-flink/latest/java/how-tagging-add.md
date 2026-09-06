

# Add or update tags for an existing application
<a name="how-tagging-add"></a>

You add tags to an application using the [TagResource](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_TagResource.html) action. You cannot add tags to an application using the [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) action.

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
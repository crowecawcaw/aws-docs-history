After careful consideration, we have decided to discontinue Amazon Kinesis
Data Analytics for SQL applications:

1. From **September 1, 2025**, we won't provide any bug fixes for Amazon Kinesis Data Analytics for SQL applications because we will have limited support for it, given the upcoming discontinuation.

2. From **October 15, 2025**, you will not be able to create new Kinesis Data Analytics for SQL
   applications.

3. We will delete your applications starting **January 27, 2026**. You will not be able to
   start or operate your Amazon Kinesis Data Analytics for SQL applications. Support will no longer
   be available for Amazon Kinesis Data Analytics for SQL from that time. For more information, see
   [Amazon Kinesis Data Analytics for SQL Applications discontinuation](discontinuation.md "discontinuation.md").

# Using Tagging

This section describes how to add key-value metadata tags to Kinesis Data Analytics applications. These tags can be used for the following purposes:

- Determining billing for individual Kinesis Data Analytics applications. For more information, see
  [Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
  in the _AWS Billing and Cost Management Guide_.
- Controlling access to application resources based on tags. For more information, see
  [Controlling Access Using Tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md")
  in the _User Guide_.
- User-defined purposes. You can define application functionality based on the presence of user tags.
  Note the following information about tagging:

- The maximum number of application tags includes system tags. The maximum number of user-defined application tags is 50.
- If an action includes a tag list that has duplicate `Key` values, the service throws an `InvalidArgumentException`.

###### This topic contains the following sections:

- [Adding Tags when an Application is Created](#how-tagging-create "#how-tagging-create")
- [Adding or Updating Tags for an Existing Application](#how-tagging-add "#how-tagging-add")
- [Listing Tags for an Application](#how-tagging-list "#how-tagging-list")
- [Removing Tags from an Application](#how-tagging-remove "#how-tagging-remove")

## Adding Tags when an Application is Created

You add tags when creating an application using the `tags` parameter of the [CreateApplication](API_CreateApplication.md "API_CreateApplication.md") action.

The following example request shows the `Tags` node for a `CreateApplication` request:

```
"Tags": [
    {
        "Key": "Key1",
        "Value": "Value1"
    },
    {
        "Key": "Key2",
        "Value": "Value2"
    }
]
```

## Adding or Updating Tags for an Existing Application

You add tags to an application using the [TagResource](API_TagResource.md "API_TagResource.md") action. You cannot add tags to an application using the
[UpdateApplication](API_UpdateApplication.md "API_UpdateApplication.md") action.

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

## Listing Tags for an Application

To list existing tags, you use the [ListTagsForResource](API_ListTagsForResource.md "API_ListTagsForResource.md") action.

The following example request for the `ListTagsForResource` action lists tags for an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalytics:us-west-2:012345678901:application/MyApplication"
}
```

## Removing Tags from an Application

To remove tags from an application, you use the [UntagResource](API_UntagResource.md "API_UntagResource.md") action.

The following example request for the `UntagResource` action removes tags from an application:

```
{
   "ResourceARN": "arn:aws:kinesisanalytics:us-west-2:012345678901:application/MyApplication",
   "TagKeys": [ "KeyOfFirstTagToRemove", "KeyOfSecondTagToRemove" ]
}
```

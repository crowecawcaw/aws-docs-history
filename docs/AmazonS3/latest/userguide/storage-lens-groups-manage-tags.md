# Managing AWS resource tags with Storage

Lens groups

Each Amazon S3 Storage Lens group is counted as an AWS resource with its own Amazon Resource
Name (ARN). Therefore, when you configure your Storage Lens group, you can optionally add
AWS resource tags to the group. You can add up to 50 tags for each Storage Lens group. To
create a Storage Lens group with tags, you must have the
`s3:CreateStorageLensGroup` and `s3:TagResource`
permissions.

You can use AWS resource tags to categorize resources according to department, line of
business, or project. Doing so is useful when you have many resources of the same type. By
applying tags, you can quickly identify a specific Storage Lens group based on the tags that
you've assigned to it. You can also use tags to track and allocate costs.

In addition, when you add an AWS resource tag to your Storage Lens group, you activate
[attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). ABAC is an authorization strategy that
defines permissions based on attributes, in this case tags. You can also use conditions that
specify resource tags in your IAM policies to [control access
to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources").

You can edit tag keys and values, and you can remove tags from a resource at any time.
Also, be aware of the following limitations:

- Tag keys and tag values are case sensitive.
- If you add a tag that has the same key as an existing tag on that resource, the
  new value overwrites the old value.
- If you delete a resource, any tags for the resource are also deleted.
- Don't include private or sensitive data in your AWS resource tags.
- System tags (with tag keys that begin with `aws:`) aren't
  supported.
- The length of each tag key can't exceed 128 characters. The length of each tag
  value can't exceed 256 characters.
  The following examples demonstrate how to use AWS resource tags with Storage Lens
  groups.

###### Topics

- [Adding an AWS resource tag to a Storage
  Lens group](storage-lens-groups-add-tags.md "storage-lens-groups-add-tags.md")
- [Updating Storage Lens group tag
  values](storage-lens-groups-update-tags.md "storage-lens-groups-update-tags.md")
- [Deleting an AWS resource tag from a
  Storage Lens group](storage-lens-groups-delete-tags.md "storage-lens-groups-delete-tags.md")
- [Listing Storage Lens group tags](storage-lens-groups-list-tags.md "storage-lens-groups-list-tags.md")

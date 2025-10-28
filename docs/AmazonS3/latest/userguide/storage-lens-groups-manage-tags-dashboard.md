# Managing AWS resource tags

with S3 Storage Lens

Each Amazon S3 Storage Lens dashboard is counted as an AWS resource with its own Amazon
Resource Name (ARN). Therefore, when you configure your Storage Lens dashboard, you can
optionally add AWS resource tags to the dashboard. You can add up to 50 tags for each
Storage Lens dashboard. To create a Storage Lens dashboard with tags, you must have the
following [S3 Storage Lens permissions](storage_lens_iam_permissions.md "storage_lens_iam_permissions.md"):

- `s3:ListStorageLensConfigurations`
- `s3:GetStorageLensConfiguration`
- `s3:GetStorageLensConfigurationTagging`
- `s3:PutStorageLensConfiguration`
- `s3:PutStorageLensConfigurationTagging`
  You can use AWS resource tags to categorize resources according to department, line of
  business, or project. This is useful when you have many resources of the same type. By
  applying tags, you can quickly identify a specific S3 Storage Lens dashboard based on the tags that
  you've assigned to it. You can also use tags to track and allocate costs.

In addition, when you add an AWS resource tag to your Storage Lens dashboard, you activate
[attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). ABAC is an authorization strategy that
defines permissions based on attributes such as tags. You can also use conditions that
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
  dashboard.

###### Topics

- [Add AWS resource tags to a Storage Lens
  dashboard](storage-lens-add-tags.md "storage-lens-add-tags.md")
- [Retrieve AWS resource tags for a Storage Lens
  dashboard](storage-lens-get-tags.md "storage-lens-get-tags.md")
- [Updating Storage Lens dashboard tags](storage-lens-update-tags.md "storage-lens-update-tags.md")
- [Deleting AWS resource tags from
  a S3 Storage Lens dashboard](storage-lens-dashboard-delete-tags.md "storage-lens-dashboard-delete-tags.md")

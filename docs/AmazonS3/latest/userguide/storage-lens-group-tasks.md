# Using Storage Lens groups

Amazon S3 Storage Lens groups aggregates metrics using custom filters based on object metadata.
You can analyze and filter S3 Storage Lens metrics using prefixes, suffixes, object tags, object
size, or object age. With Amazon S3 Storage Lens groups, you can also categorize your usage
within and across Amazon S3 buckets. As a result, you'll be able to better understand and
optimize your S3 storage.

To start visualizing the data for a Storage Lens group, you must first [attach your Storage Lens group to an S3 Storage Lens dashboard](storage-lens-groups-dashboard-console.md#storage-lens-groups-attach-dashboard-console "storage-lens-groups-dashboard-console.md#storage-lens-groups-attach-dashboard-console"). If you need to manage
Storage Lens groups in the dashboard, you can edit the dashboard configuration. To check
which Storage Lens groups are under your account, you can list them. To check which Storage
Lens groups are attached to your dashboard, you can always check the **Storage Lens
groups** tab in the dashboard. To review or update the scope of an existing
Storage Lens group, you can view its details. You can also permanently delete a Storage Lens
group.

To manage permissions, you can create and add user-defined AWS resource tags to your
Storage Lens groups. You can use AWS resource tags to categorize resources according to
department, line of business, or project. Doing so is useful when you have many resources of
the same type. By applying tags, you can quickly identify a specific Storage Lens group
based on the tags that you've assigned to it.

In addition, when you add an AWS resource tag to your Storage Lens group, you activate
[attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md"). ABAC is an authorization strategy that
defines permissions based on attributes, in this case tags. You can also use conditions that
specify resource tags in your IAM policies to [control access
to AWS resources](../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources "../../../IAM/latest/UserGuide/access_tags.md#access_tags_control-resources").

###### Topics

- [Creating a Storage Lens group](storage-lens-groups-create.md "storage-lens-groups-create.md")
- [Attaching or removing S3 Storage Lens groups
  to or from your dashboard](storage-lens-groups-dashboard-console.md "storage-lens-groups-dashboard-console.md")
- [Visualizing your Storage Lens groups
  data](storage-lens-groups-visualize.md "storage-lens-groups-visualize.md")
- [Updating a Storage Lens group](storage-lens-groups-update.md "storage-lens-groups-update.md")
- [Managing AWS resource tags with Storage
  Lens groups](storage-lens-groups-manage-tags.md "storage-lens-groups-manage-tags.md")
- [Listing all Storage Lens groups](storage-lens-groups-list.md "storage-lens-groups-list.md")
- [Viewing Storage Lens group details](storage-lens-groups-view.md "storage-lens-groups-view.md")
- [Deleting a Storage Lens group](storage-lens-groups-delete.md "storage-lens-groups-delete.md")

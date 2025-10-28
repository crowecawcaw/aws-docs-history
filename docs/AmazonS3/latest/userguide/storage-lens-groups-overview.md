# Working with S3 Storage Lens groups to filter and aggregate metrics

An Amazon S3 Storage Lens group aggregates metrics using custom filters based on object metadata.
Storage Lens groups help you drill down into characteristics of your data, such as
distribution of objects by age, your most common file types, and more. For example, you can
filter metrics by object tag to identify your fastest-growing datasets, or visualize your
storage based on object size and age to inform your storage archive strategy. As a result,
Amazon S3 Storage Lens groups helps you to better understand and optimize your S3
storage.

When you use Storage Lens groups, you can analyze and filter S3 Storage Lens metrics using object
metadata such as prefixes, suffixes, [object tags](object-tagging.md "object-tagging.md"), object size, or
object age. You can also apply a combination of these filters. After you attach your Storage
Lens group to your S3 Storage Lens dashboard, you can view S3 Storage Lens metrics aggregated by Amazon S3
Storage Lens groups directly in your dashboard.

For example, you can also filter your metrics by object size or age bands to determine
which portion of your storage consists of small objects. You can then use this information
with S3 Intelligent-Tiering or S3 Lifecycle to transition small objects to different storage
classes for cost and storage optimization.

###### Topics

- [How S3 Storage Lens groups work](storage-lens-groups.md "storage-lens-groups.md")
- [Using Storage Lens groups](storage-lens-group-tasks.md "storage-lens-group-tasks.md")

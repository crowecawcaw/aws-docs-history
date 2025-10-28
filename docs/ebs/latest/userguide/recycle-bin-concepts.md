# How does Recycle Bin work?

To enable and use Recycle Bin, you must create _retention rules_ in the AWS Regions
in which you want to protect your resources. Retention rules specify the following:

- The resource type that you want to protect (snapshots or AMIs).
- The type of retention rule:
  - **Tag-level retention rules** — These retention rules use
    resource tags to identify the resources to protect. For each retention rule, you specify one or
    more tag key and value pairs. Resources (of the specified type) that have at least one of these
    tag key and value pairs are automatically retained in the Recycle Bin upon deletion. Use this
    type of retention rule to protect specific resources in your account based on their tags.
  - **Region-level retention rules** — These retention rules,
    by default, apply to all of the resources (of the specified type) in the Region, even if the
    resources are not tagged. However, you can specify exclusion tags to exclude resources that have
    specific tags. Use this type of retention rule to protect all resources of a specific type in a
    Region.

- The retention period to retain resources after they are deleted. After this period expires, the
  resources are permanently deleted from the Recycle Bin.
  While a resource is in the Recycle Bin, you have the ability to restore it for use at any time. The resource
  remains in the Recycle Bin until one of the following happens:

- You manually restore it for use. When you restore a resource from the Recycle Bin, the resource is
  removed from the Recycle Bin and it immediately becomes available for use. You can use restored
  resources in the same way as any other resource of that type in your account.
- The retention period expires. If the retention period expires, and the resource has not been restored
  from the Recycle Bin, the resource is permanently deleted from the Recycle Bin and it can no longer
  be viewed or restored.

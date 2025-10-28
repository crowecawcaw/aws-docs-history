# Tagging in Amazon Managed Service for Prometheus

A _tag_ is a custom attribute label that you or AWS assigns to an
AWS resource. Each AWS tag has two parts:

- A _tag key_ (for example, `CostCenter`,
  `Environment`, `Project`, or `Secret`). Tag
  keys are case sensitive.
- An optional field known as a _tag value_ (for example,
  `111122223333`, `Production`, or a team name).
  Omitting the tag value is the same as using an empty string. Like tag keys, tag
  values are case sensitive.
  Together these are known as key-value pairs. You can have as many as 50 tags assigned to
  each workspace.

Tags help you identify and organize your AWS resources. Many AWS services support
tagging, so you can assign the same tag to resources from different services to indicate
that the resources are related. For example, you can assign the same tag to an Amazon Managed Service for Prometheus
workspace that you assign to an Amazon S3 bucket. For more information about tagging strategies,
see [Tagging AWS
Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

In Amazon Managed Service for Prometheus, both workspaces and rule groups namespaces can be tagged. You can use the
console, the AWS CLI, APIs, or SDKs to add, manage, and remove tags for these resources. In
addition to identifying, organizing, and tracking your workspaces and rule groups namespaces
with tags, you can use tags in IAM policies to help control who can view and interact with
your Amazon Managed Service for Prometheus resources.

**Tag restrictions**

The following basic restrictions apply to tags:

- Each resource can have a maximum of 50 tags.
- For each resource, each tag key must be unique, and each tag key can have only one
  value.
- The maximum tag key length is 128 Unicode characters in UTF-8.
- The maximum tag value length is 256 Unicode characters in UTF-8.
- If your tagging schema is used across multiple AWS services and resources,
  remember that other services may have restrictions on allowed characters. Generally
  allowed characters are letters, numbers, spaces representable in UTF-8, and the
  following characters: **_. : + = @ \_ / -_** (hyphen).
- Tag keys and values are case sensitive. As a best practice, decide on a strategy
  for capitalizing tags and consistently implement that strategy across all resource
  types. For example, decide whether to use `Costcenter`,
  `costcenter`, or `CostCenter` and use the same convention
  for all tags. Avoid using similar tags with inconsistent case treatment.
- Don't use `aws:`, `AWS:`, or any upper or lowercase
  combination of such as a prefix for either keys or values. These are reserved only
  for AWS use. You can't edit or delete tag keys or values with this prefix. Tags
  with this prefix do not count against your tags-per-resource limit.

###### Topics

- [Tag Amazon Managed Service for Prometheus workspaces](tagging-workspaces.md "tagging-workspaces.md")
- [Tagging rule groups namespaces](tagging-rulegroupsnamespaces.md "tagging-rulegroupsnamespaces.md")

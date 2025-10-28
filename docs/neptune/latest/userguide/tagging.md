# Tagging Amazon Neptune resources

You can use Neptune tags to add metadata to your Neptune resources. In addition, you
can use tags with AWS Identity and Access Management (IAM) policies to manage access to Neptune resources and
control what actions can be applied to those resources. Finally, you can use tags to track
costs by grouping expenses for similarly tagged resources.

All Neptune administrative resources can be tagged, including the following:

- DB instances
- DB clusters
- Read Replicas
- DB snapshots
- DB cluster snapshots
- Event subscriptions
- DB parameter groups
- DB cluster parameter groups
- DB subnet groups

## Overview of Neptune resource tags

An Amazon Neptune tag is a name-value pair that you define and associate with a Neptune
resource. The name is referred to as the _key_. Supplying a value for
the key is optional. You can use tags to assign arbitrary information to a Neptune
resource. You can use a tag key, for example, to define a category, and the tag value
might be an item in that category. For example, you might define a tag key of “project”
and a tag value of “Salix,” indicating that the Neptune resource is assigned to the
Salix project. You can also use tags to designate Neptune resources as being used for
test or production by using a key such as `environment=test` or
`environment=production`. We recommend that you use a consistent set of
tag keys to make it easier to track metadata that is associated with Neptune
resources.

Use tags to organize your AWS bill to reflect your own cost structure.
To do this, sign up to get your AWS account bill with tag key values included.
Then, to see the cost of combined resources, organize your billing information
according to resources with the same tag key values. For example, you can tag
several resources with a specific application name, and then organize your billing
information to see the total cost of that application across several services.
For more information, see
[Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

Each Neptune resource has a tag set, which contains all the tags that are assigned to that
Neptune resource. A tag set can contain as many as 10 tags, or it can be empty. If you
add a tag to a Neptune resource that has the same key as an existing tag on resource,
the new value overwrites the old value.

AWS does not apply any semantic meaning to your tags; tags are interpreted strictly as
character strings. Neptune can set tags on a DB instance or other Neptune resources,
depending on the settings that you use when you create the resource. For example, Neptune
might add a tag indicating that a DB instance is for production or for testing.

- The tag key is the required name of the tag. The string value
  can be from 1 to 128 Unicode characters in length and cannot be prefixed with
  "`aws:`" or "`rds:`". The string can contain only the
  set of Unicode letters, digits, white space, '\_', '.', '/', '=', '+', '-'
  (Java regex: "`^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$`").
- The tag value is an optional string value of the tag.
  The string value can be from 1 to 256 Unicode characters in length and cannot
  be prefixed with "`aws:`". The string can contain only the set of
  Unicode letters, digits, white space, '\_', '.', '/', '=', '+', '-'
  (Java regex: "`^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$`").

Values do not have to be unique in a tag set and can be null. For example,
you can have a key-value pair in a tag set of `project/Trinity` and
`cost-center/Trinity`.

###### Note

You can add a tag to a snapshot. However, your bill won't reflect
this grouping.

You can use the AWS Management Console, the AWS CLI, or the Neptune API to add, list, and delete
tags on Neptune resources. When using the AWS CLI or the Neptune API, you must provide the
Amazon Resource Name (ARN) for the Neptune resource that you want to work with. For
more information about constructing an ARN, see [Constructing an ARN for Neptune](tagging-arns-constructing.md "tagging-arns-constructing.md").

Tags are cached for authorization purposes. Because of this, additions and updates to tags
on Neptune resources can take several minutes before they are available.

### Copying tags in Neptune

When you create or restore a DB instance, you can specify that the tags from the DB
instance are copied to snapshots of the DB instance. Copying tags ensures that the
metadata for the DB snapshots matches that of the source DB instance, and that any
access policies for the DB snapshot also match those of the source DB instance. Tags
are not copied by default.

You can specify that tags are copied to DB snapshots for the following actions:

- Creating a DB instance.
- Restoring a DB instance.
- Creating a Read Replica.
- Copying a DB snapshot.

###### Note

If you include a value for the `--tag-key` parameter of the [create-db-cluster-snapshot](../../../cli/latest/reference/neptune/create-db-cluster-snapshot.md "../../../cli/latest/reference/neptune/create-db-cluster-snapshot.md") AWS CLI command (or supply at least one tag to the
[CreateDBClusterSnapshot](api-snapshots.md#CreateDBClusterSnapshot "api-snapshots.md#CreateDBClusterSnapshot")
API action), Neptune doesn't copy tags from the source DB instance to the
new DB snapshot. This is true even if the source DB instance has the
`--copy-tags-to-snapshot` (`CopyTagsToSnapshot`) option enabled.

This means that you can create a copy of a DB instance from a DB snapshot and
avoid adding tags that don't apply to the new DB instance. After you create your DB
snapshot using the AWS CLI `create-db-cluster-snapshot` command (or the
`CreateDBClusterSnapshot` Neptune API action), you can then add tags
as described later in this topic.

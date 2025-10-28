# Tagging resources in AWS Database Migration Service

You can use tags in AWS Database Migration Service (AWS DMS) to add metadata to your resources. In addition,
you can use these tags with AWS Identity and Access Management (IAM) policies to manage access to AWS DMS
resources and to control what actions can be applied to the AWS DMS resources. Finally,
you can use these tags to track costs by grouping expenses for similarly tagged resources.

All AWS DMS resources can be tagged:

- Certificates
- Data providers
- Data migrations
- Endpoints
- Event subscriptions
- Instance profiles
- Migration projects
- Replication instances
- Replication subnet groups
- Replication tasks
  An AWS DMS tag is a name-value pair that you define and associate with an AWS DMS
  resource. The name is referred to as the key. Supplying a value for the key is optional.
  You can use tags to assign arbitrary information to an AWS DMS resource. A tag key
  could be used, for example, to define a category, and the tag value could be a item in
  that category. For example, you could define a tag key of "project" and a tag value of
  "Salix", indicating that the AWS DMS resource is assigned to the Salix project. You
  could also use tags to designate AWS DMS resources as being used for test or
  production by using a key such as environment=test or environment =production. We
  recommend that you use a consistent set of tag keys to make it easier to track metadata
  associated with AWS DMS resources.

Use tags to organize your AWS bill to reflect your own cost structure.
To do this, sign up to get your AWS account bill with tag key values included.
Then, to see the cost of combined resources, organize your billing information
according to resources with the same tag key values. For example, you can tag
several resources with a specific application name, and then organize your billing
information to see the total cost of that application across several services.
For more information, see
[Using Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing User Guide_.

Each AWS DMS resource has a tag set, which contains all the tags that are assigned to
that AWS DMS resource. A tag set can contain as many as ten tags, or it can be empty.
If you add a tag to an AWS DMS resource that has the same key as an existing tag on
resource, the new value overwrites the old value.

AWS does not apply any semantic meaning to your tags; tags are interpreted strictly as
character strings. AWS DMS might set tags on an AWS DMS resource, depending on the
settings that you use when you create the resource.

The following list describes the characteristics of an AWS DMS tag.

- The tag key is the required name of the tag. The string value can be from 1 to 128 Unicode
  characters in length and cannot be prefixed with "aws:" or "dms:". The string
  might contain only the set of Unicode letters, digits, white-space, '\_', '.',
  '/', '=', '+', '-' (Java regex: `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$"`).

- The tag value is an optional string value of the tag. The string value can be from 1 to 256
  Unicode characters in length and cannot be prefixed with "aws:" or "dms:". The
  string might contain only the set of Unicode letters, digits, white-space, '\_',
  '.', '/', '=', '+', '-' (Java regex:
  `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$"`).

Values do not have to be unique in a tag set and can be null. For example, you can have a key-value pair in a tag set of
project/Trinity and cost-center/Trinity.
You can use the AWS CLI or the AWS DMS API to add, list, and delete tags on AWS DMS
resources. When using the AWS CLI or the AWS DMS API, you must provide the Amazon
Resource Name (ARN) for the AWS DMS resource you want to work with. For more
information about constructing an ARN,
see [Constructing an Amazon Resource Name
(ARN) for AWS DMS](CHAP_Introduction.AWS.md "CHAP_Introduction.AWS.md").

Note that tags are cached for authorization purposes. Because of this, additions and updates
to tags on AWS DMS resources might take several minutes before they are available.

## API

You can add, list, or remove tags for a AWS DMS resource using the AWS DMS API.

- To add a tag to an AWS DMS resource, use the
  [`AddTagsToResource`](../APIReference/API_AddTagsToResource.md "../APIReference/API_AddTagsToResource.md") operation.
- To list tags that are assigned to an AWS DMS resource, use
  the [`ListTagsForResource`](../APIReference/API_ListTagsForResource.md "../APIReference/API_ListTagsForResource.md") operation.
- To remove tags from an AWS DMS resource, use the [`RemoveTagsFromResource`](../APIReference/API_RemoveTagsFromResource.md "../APIReference/API_RemoveTagsFromResource.md")
  operation.

To learn more about how to construct the required ARN,
see [Constructing an Amazon Resource Name
(ARN) for AWS DMS](CHAP_Introduction.AWS.md "CHAP_Introduction.AWS.md").

When working with XML using the AWS DMS API, tags use the following schema:

```
<Tagging>
  <TagSet>
  	<Tag>
  		<Key>Project</Key>
  		<Value>Trinity</Value>
  	</Tag>
  	<Tag>
  		<Key>User</Key>
  		<Value>Jones</Value>
  	</Tag>
  </TagSet>
</Tagging>
```

The following table provides a list of the allowed XML tags and their characteristics. Note that values for Key and Value are
case dependent. For example, project=Trinity and PROJECT=Trinity are two distinct tags.

| Tagging element | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TagSet          | A tag set is a container for all tags assigned to an Amazon RDS resource. There can be only one tag set per resource. You work with a TagSet only through the AWS DMS API.                                                                                                                                                                                                                                                                                                                                          |
| Tag             | A tag is a user-defined key-value pair. There can be from 1 to 10 tags in a tag set.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Key             | A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and cannot be prefixed with "dms:" or "aws:". The string might only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '+', '-' (Java regex: `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$"`). Keys must be unique to a tag set. For example, you cannot have a key-pair in a tag set with the key the same but with different values, such as project/Trinity and project/Xanadu. |
| Value           | A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and cannot be prefixed with "dms:" or "aws:". The string might only contain only the set of Unicode letters, digits, white-space, '\_', '.', '/', '=', '+', '-' (Java regex: `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$"`). Values do not have to be unique in a tag set and can be null. For example, you can have a key-value pair in a tag set of project/Trinity and cost-center/Trinity.                |

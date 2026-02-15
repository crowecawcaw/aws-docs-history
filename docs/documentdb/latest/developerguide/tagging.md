# Tagging Amazon DocumentDB resources

You can use Amazon DocumentDB (with MongoDB compatibility) tags to add metadata to your Amazon DocumentDB resources. These tags can be used with AWS Identity and Access Management (IAM) policies to manage access to
Amazon DocumentDB resources and to control what actions can be applied to the resources. You can also use tags to track costs by grouping expenses for similarly
tagged resources.

You can tag the following Amazon DocumentDB resources:

- Clusters
- Instances
- Snapshots
- Cluster snapshots
- Parameter groups
- Cluster parameter groups
- Security groups
- Subnet groups

## Overview of Amazon DocumentDB resource tags

An Amazon DocumentDB tag is a name-value pair that you define and associate with an Amazon DocumentDB resource. The name is referred to as the _key_.
Supplying a value for the key is optional. You can use tags to assign arbitrary information to an Amazon DocumentDB resource. You can use a tag key, for example,
to define a category, and the tag value might be an item in that category. For example, you might define a tag key of `project` and a tag
value of `Salix`, indicating that the Amazon DocumentDB resource is assigned to the Salix project. You can also use tags to designate Amazon DocumentDB
resources as being used for test or production by using a key such as `environment=test` or `environment=production`. We
recommend that you use a consistent set of tag keys to make it easier to track metadata that is associated with Amazon DocumentDB resources.

You can use tags to organize your AWS bill to reflect your own cost structure. To do this, sign up to get your AWS account bill with tag key values
included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For
example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that
application across several services. For more information, see [Using
Cost Allocation Tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md") in the _AWS Billing and Cost Management User Guide_.

Each Amazon DocumentDB resource has a tag set, which contains all the tags that are assigned to that resource. A tag set can contain as many as 10
tags, or it can be empty. If you add a tag to an Amazon DocumentDB resource that has the same key as an existing tag on resource, the new value overwrites the
old value.

AWS does not apply any semantic meaning to your tags; tags are interpreted strictly as character strings. Amazon DocumentDB can set tags on an instance or
other Amazon DocumentDB resources, depending on the settings that you use when you create the resource. For example, Amazon DocumentDB might add a tag indicating that an
instance is for production or for testing.

You can add a tag to a snapshot, but your bill will not reflect this grouping.

You can use the AWS Management Console or the AWS CLI to add, list, and delete tags on Amazon DocumentDB resources. When using the AWS CLI, you must provide the Amazon
Resource Name (ARN) for the resource that you want to work with. For more information about Amazon DocumentDB ARNs, see [Understanding Amazon DocumentDB Amazon Resource Names (ARNs)](documentdb-arns.md "documentdb-arns.md").

## Tag constraints

The following constraints apply to Amazon DocumentDB tags:

- Maximum number of tags per resource - 10
- Maximum **Key** length - 128 Unicode characters
- Maximum **Value** length - 256 Unicode characters
- Valid characters for **Key** and **Value** - uppercase and lowercase letters in the
  UTF-8 character set, digits, space, and the following characters: `_ . : / = + -` and `@` (Java regex:
  `"^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-]*)$"`)
- Tag keys and values are case sensitive.
- The prefix `aws:` cannot be used for tag keys or values; it is reserved for AWS.

## Adding and updating tags on an Amazon DocumentDB resource

You can add up to 10 tags to a resource using the AWS Management Console or the AWS CLI.

Using the AWS Management Console
The process for adding a tag to a resource is similar regardless of what resource you're adding the tag to. In this example, you add a tag to a
cluster.

###### To add or update tags to a cluster using the console

1. Sign in to the AWS Management Console, and open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. From the navigation pane, choose **clusters**.
3. Choose the name of the cluster that you want to add tags to.
4. Scroll down to the **Tags** section, and then choose **Edit**.
5. For each tag you that want to add to this resource, do the following:
   1. To add a new tag, enter in the name of the tag in the **Key** box. To change a tag's value, find the tag's name in
      the **Key** column.
   2. To give the tag a new or updated value, enter a value for the tag in the **Value** box.
   3. If you have more tags to add, choose **Add**. Otherwise, when finished, choose **Save**.

Using the AWS CLI
The process for adding a tag to a resource is similar regardless of what resource you're adding the tags to. In this example, you add three tags
to a cluster. The second tag, `key2`, has no value.

Use the AWS CLI operation `add-tags-to-resource` with these parameters.

###### Parameters

- `--resource-name`—The ARN of the Amazon DocumentDB resource that you want to add tags to.
- `--tags`—A list the tags (key-value pair) that you want to add to this resource in the format
  `Key=`key-name`,Value=`tag-value``.

###### Example

For Linux, macOS, or Unix:

```
aws docdb add-tags-to-resource \
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster` \
    --tags Key=`key1`,Value=`value1` Key=`key2` Key=`key3`,Value=`value3`
```

For Windows:

```
aws docdb add-tags-to-resource ^
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster` \
    --tags Key=`key1`,Value=`value1` Key=`key2` Key=`key3`,Value=`value3`
```

The `add-tags-to-resource` operation produces no output. To see the results of the operation, use the
`list-tags-for-resource` operation.

## Listing tags on an Amazon DocumentDB resource

You can use the AWS Management Console or the AWS CLI to get a listing of the tags for an Amazon DocumentDB resource.

Using the AWS Management Console
The process for listing tags on a resource is similar regardless of what resource you're adding the tag to. In this example, you list the tags
for a cluster.

###### To list the tags on a cluster using the console

1. Open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. From the navigation pane, choose **clusters**.
3. Choose the name of the cluster that you want to list tags for.
4. To see a listing of the tags on this resource, scroll down to the **Tags** section.

Using the AWS CLI
The process for listing the tags on a resource is similar regardless of what resource you're listing the tag for. In this example, you list the
tags on a cluster.

Use the AWS CLI operation `list-tags-for-resource` with these parameters.

###### Parameters

- `--resource-name`—Required. The ARN of the Amazon DocumentDB resource that you want to list tags
  for.

###### Example

For Linux, macOS, or Unix:

```
aws docdb list-tags-for-resource \
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster`
```

For Windows:

```
aws docdb list-tags-for-resource ^
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster`
```

Output from this operation looks something like the following (JSON format).

```
{
    "TagList": [
        {
            "Key": "key1",
            "Value": "value1"
        },
        {
            "Key": "key2",
            "Value": ""
        },
        {
            "Key": "key3",
            "Value": "value3"
        }
    ]
}
```

## Removing tags from an Amazon DocumentDB resource

You can use the AWS Management Console or the AWS CLI to remove tags from Amazon DocumentDB resources.

Using the AWS Management Console
The process for removing tags from a resource is similar regardless of what resource you're adding the tag to. In this example, you remove tags
from a cluster.

###### To remove tags from a cluster using the console

1. Open the Amazon DocumentDB console at [https://console.aws.amazon.com/docdb](https://console.aws.amazon.com/docdb "https://console.aws.amazon.com/docdb").
2. From the navigation pane, choose **clusters**.
3. Choose the name of the cluster that you want to remove tags from.
4. Scroll down to the **Tags** section, and then choose **Edit**.
5. If you want to remove all tags from this resource, choose **Remove all**. Otherwise, for each tag that you want to remove
   from this resource, do the following:
   1. Locate the name of the tag in the **Key** column.
   2. Choose **Remove** on the same row as the tag key.
   3. When finished, choose **Save**.

Using the AWS CLI
The process for removing a tag from a resource is similar regardless of what resource you're removing the tag from. In this example, you remove a
tag from a cluster.

Use the AWS CLI operation `remove-tags-from-resource` with these parameters.

- `--resource-name`—Required. The ARN of the Amazon DocumentDB resource that you want to remove tags
  from.
- `--tag-keys`—Required. A list the tag keys that you want removed from this resource.

###### Example

For Linux, macOS, or Unix:

```
aws docdb remove-tags-from-resource \
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster` \
    --tag-keys `key1 key3`
```

For Windows:

```
aws docdb remove-tags-from-resource ^
    --resource-name arn:aws:rds:us-east-1:`1234567890`:`cluster`:`sample-cluster` \
    --tag-keys `key1 key3`
```

The `removed-tags-from-resource` operation produces no output. To see the results of the operation, use the
`list-tags-for-resource` operation.

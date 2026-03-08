# Managing your cost allocation tags using the AWS CLI

You can use the AWS CLI to add, modify, or remove cost allocation tags.

Sample arn: `arn:aws:memorydb:us-east-1:1234567890:cluster/my-cluster`

###### Topics

- [Listing tags using the AWS CLI](#tagging.managing.cli.List "#tagging.managing.cli.List")
- [Adding tags using the AWS CLI](#tagging.managing.cli.Add "#tagging.managing.cli.Add")
- [Modifying tags using the AWS CLI](#tagging.managing.cli.modify "#tagging.managing.cli.modify")
- [Removing tags using the AWS CLI](#tagging.managing.cli.Remove "#tagging.managing.cli.Remove")

## Listing tags using the AWS CLI

You can use the AWS CLI to list tags on an existing MemoryDB resource by using the
[list-tags](../../../cli/latest/reference/memorydb/list-tags.md "../../../cli/latest/reference/memorydb/list-tags.md") operation.

The following code uses the AWS CLI to list the tags on the MemoryDB
cluster `my-cluster` in region us-east-1.

For Linux, macOS, or Unix:

```
aws memorydb list-tags \
  --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster`
```

For Windows:

```
aws memorydb list-tags ^
  --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster`
```

Output from this operation will look something like the following, a list of all the tags
on the resource.

```
{
   "TagList": [
      {
         "Value": "10110",
         "Key": "CostCenter"
      },
      {
         "Value": "EC2",
         "Key": "Service"
      }
   ]
}
```

If there are no tags on the resource, the output will be an empty TagList.

```
{
   "TagList": []
}
```

For more information, see the AWS CLI for MemoryDB [list-tags](../../../cli/latest/reference/memorydb/list-tags.md "../../../cli/latest/reference/memorydb/list-tags.md").

## Adding tags using the AWS CLI

You can use the AWS CLI to add tags to an existing MemoryDB resource by using the
tag-resource CLI operation.
If the tag key does not exist on the resource, the key and value are added to
the resource. If the key already exists on the resource, the value associated
with that key is updated to the new value.

The following code uses the AWS CLI to add the keys `Service` and `Region` with the
values `memorydb` and `us-east-1` respectively
to the cluster
`my-cluster` in region us-east-1.

For Linux, macOS, or Unix:

```
aws memorydb tag-resource \
 --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster` \
 --tags Key=`Service`,Value=`memorydb` \
        Key=`Region`,Value=`us-east-1`
```

For Windows:

```
aws memorydb tag-resource ^
 --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster` ^
 --tags Key=`Service`,Value=`memorydb` ^
        Key=`Region`,Value=`us-east-1`
```

Output from this operation will look something like the following, a list of all the tags
on the resource following the operation.

```
{
   "TagList": [
      {
         "Value": "memorydb",
         "Key": "Service"
      },
      {
         "Value": "us-east-1",
         "Key": "Region"
      }
   ]
}
```

For more information, see the AWS CLI for MemoryDB tag-resource.

You can also use the AWS CLI to add tags to a cluster when you create a new cluster by using the operation
[create-cluster](../../../cli/latest/reference/memorydb/create-cluster.md "../../../cli/latest/reference/memorydb/create-cluster.md").

## Modifying tags using the AWS CLI

You can use the AWS CLI to modify the tags on a MemoryDB cluster.

To modify tags:

- Use [tag-resource](../../../cli/latest/reference/memorydb/tag-resource.md "../../../cli/latest/reference/memorydb/tag-resource.md") to either add a new tag and value or to
  change the value associated with an existing tag.
- Use [untag-resource](../../../cli/latest/reference/memorydb/untag-resource.md "../../../cli/latest/reference/memorydb/untag-resource.md") to
  remove specified tags from the resource.

Output from either operation will be a list of tags and their values on the specified
cluster.

## Removing tags using the AWS CLI

You can use the AWS CLI to remove tags from an existing from a MemoryDB cluster by using the
[untag-resource](../../../cli/latest/reference/memorydb/untag-resource.md "../../../cli/latest/reference/memorydb/untag-resource.md") operation.

The following code uses the AWS CLI to remove the tags with the keys `Service` and `Region`
from the cluster
`my-cluster` in the us-east-1 region.

For Linux, macOS, or Unix:

```
aws memorydb untag-resource \
 --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster` \
 --tag-keys `Region Service`
```

For Windows:

```
aws memorydb untag-resource ^
 --resource-arn arn:aws:memorydb:`us-east-1:0123456789:cluster/my-cluster` ^
 --tag-keys `Region Service`
```

Output from this operation will look something like the following, a list of all the tags
on the resource following the operation.

```
{
   "TagList": []
}
```

For more information, see the AWS CLI for MemoryDB [untag-resource](../../../cli/latest/reference/memorydb/untag-resource.md "../../../cli/latest/reference/memorydb/untag-resource.md").

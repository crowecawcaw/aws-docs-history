# Managing your cost allocation tags using the MemoryDB API

You can use the MemoryDB API to add, modify, or remove cost allocation tags.

Cost allocation tags are applied to MemoryDB for clusters. The cluster to be tagged
is specified using an ARN (Amazon Resource Name).

Sample arn: `arn:aws:memorydb:us-east-1:1234567890:cluster/my-cluster`

###### Topics

- [Listing tags using the MemoryDB API](#tagging.managing.api.List "#tagging.managing.api.List")
- [Adding tags using the MemoryDB API](#tagging.managing.api.Add "#tagging.managing.api.Add")
- [Modifying tags using the MemoryDB API](#tagging.managing.api.modify "#tagging.managing.api.modify")
- [Removing tags using the MemoryDB API](#tagging.managing.api.Remove "#tagging.managing.api.Remove")

## Listing tags using the MemoryDB API

You can use the MemoryDB API to list tags on an existing resource by using the
[ListTags](../APIReference/API_ListTags.md "../APIReference/API_ListTags.md") operation.

The following code uses the MemoryDB API to list the tags on the resource `my-cluster` in the us-east-1 region.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=ListTags
   &ResourceArn=arn:aws:memorydb:us-east-1:0123456789:cluster/my-cluster
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Version=2021-01-01
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

## Adding tags using the MemoryDB API

You can use the MemoryDB API to add tags to an existing MemoryDB cluster by using the
[TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation.
If the tag key does not exist on the resource, the key and value are added to
the resource. If the key already exists on the resource, the value associated
with that key is updated to the new value.

The following code uses the MemoryDB API to add the keys `Service` and `Region`
with the values `memorydb` and `us-east-1` respectively to the resource
`my-cluster`
in the us-east-1 region.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=TagResource
   &ResourceArn=arn:aws:memorydb:us-east-1:0123456789:cluster/my-cluster
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &Tags.member.1.Key=Service
   &Tags.member.1.Value=memorydb
   &Tags.member.2.Key=Region
   &Tags.member.2.Value=us-east-1
   &Version=2021-01-01
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

For more information, see
[TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md").

## Modifying tags using the MemoryDB API

You can use the MemoryDB API to modify the tags on a MemoryDB cluster.

To modify the value of a tag:

- Use [TagResource](../APIReference/API_TagResource.md "../APIReference/API_TagResource.md") operation to either add a new tag and value or
  to change the value of an existing tag.
- Use [UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") to remove tags from the resource.

Output from either operation will be a list of tags and their values on the specified
resource.

## Removing tags using the MemoryDB API

You can use the MemoryDB API to remove tags from an existing MemoryDB cluster by using the
[UntagResource](../APIReference/API_UntagResource.md "../APIReference/API_UntagResource.md") operation.

The following code uses the MemoryDB API to remove the tags with the keys `Service` and `Region`
from the cluster
`my-cluster` in region us-east-1.

```
https://memory-db.us-east-1.amazonaws.com/
   ?Action=UntagResource
   &ResourceArn=arn:aws:memorydb:us-east-1:0123456789:cluster/my-cluster
   &SignatureVersion=4
   &SignatureMethod=HmacSHA256
   &TagKeys.member.1=Service
   &TagKeys.member.2=Region
   &Version=2021-01-01
   &Timestamp=20210802T192317Z
   &X-Amz-Credential=<credential>
```

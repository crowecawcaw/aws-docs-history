Amazon FSx File Gateway is no longer available to new customers. Existing
customers of FSx File Gateway can continue to use the service normally. For capabilities
similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

# Understanding Storage Gateway resources and resource

IDs

In Storage Gateway, the primary resource is a _gateway_ but other resource
types is _file share_. File shares are referred to as
_subresources_ and they don't exist unless they are associated with a
gateway.

These resources and subresources have unique Amazon Resource Names (ARNs) associated with
them as shown in this table.

| Resource Type  | ARN Format                                                          |
| -------------- | ------------------------------------------------------------------- |
| Gateway ARN    | `arn:aws:storagegateway:`region`:`account-id`:gateway/`gateway-id`` |
| File Share ARN | `arn:aws:storagegateway:`region`:`account-id`:share/`share-id``     |

## Working with Resource IDs

When you create a resource, Storage Gateway assigns the resource a unique resource ID.
This resource ID is part of the resource ARN. A resource ID takes the form of a resource
identifier, followed by a hyphen, and a unique combination of eight letters and numbers.
For example, a gateway ID is of the form `sgw-12A3456B` where
`sgw` is the resource identifier for gateways.

Storage Gateway resource IDs are in uppercase. However, when you use these resource IDs with
the Amazon EC2 API, Amazon EC2 expects resource IDs in lowercase. You must change your resource ID
to lowercase to use it with the EC2 API. For example, in Storage Gateway the ID for a
volume might be `vol-1122AABB`. When you use this ID with the EC2 API, you
must change it to `vol-1122aabb`. Otherwise, the EC2 API might not behave as
expected.

###### Important

IDs for Storage Gateway volumes and Amazon EBS snapshots created from gateway volumes are
changing to a longer format. Starting in December 2016, all new volumes and
snapshots will be created with a 17-character string. Starting in April 2016, you
will be able to use these longer IDs so you can test your systems with the new
format. For more information, see [Longer EC2 and EBS Resource IDs](https://aws.amazon.com/ec2/faqs/#longer-ids "https://aws.amazon.com/ec2/faqs/#longer-ids").

For example, a volume ARN with the longer volume ID format will look like
this:

`arn:aws:storagegateway:us-west-2:111122223333:gateway/sgw-12A3456B/volume/vol-1122AABBCCDDEEFFG`.

A snapshot ID with the longer ID format will look like this:
`snap-78e226633445566ee`.

For more information, see [Announcement: Heads-up – Longer Storage Gateway volume and snapshot IDs coming in
2016](https://forums.aws.amazon.com/ann.jspa?annID=3557 "https://forums.aws.amazon.com/ann.jspa?annID=3557").

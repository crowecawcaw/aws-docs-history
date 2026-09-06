

# Understanding Storage Gateway Resources and Resource IDs
<a name="storage-gateway-resource-id"></a>

In Storage Gateway, the primary resource is a *gateway* but other resource types include: *volume*, * virtual tape*, *iSCSI target*, and *vtl device*. These are referred to as *subresources* and they don't exist unless they are associated with a gateway.

These resources and subresources have unique Amazon Resource Names (ARNs) associated with them as shown in the following table.


| Resource Type | ARN Format | 
| --- | --- | 
| Gateway ARN | `arn:aws:storagegateway:{{region}}:{{account-id}}:gateway/{{gateway-id}}` | 
| Volume ARN | `arn:aws:storagegateway:{{region}}:{{account-id}}:gateway/{{gateway-id}}/volume/{{volume-id}}` | 
| Target ARN ( iSCSI target) | `arn:aws:storagegateway:{{region}}:{{account-id}}:gateway/{{gateway-id}}/target/{{iSCSItarget}}` | 

Storage Gateway also supports the use of EC2 instances and EBS volumes and snapshots. These resources are Amazon EC2 resources that are used in Storage Gateway.

## Working with Resource IDs
<a name="working-with-id"></a>

When you create a resource, Storage Gateway assigns the resource a unique resource ID. This resource ID is part of the resource ARN. A resource ID takes the form of a resource identifier, followed by a hyphen, and a unique combination of eight letters and numbers, or 17 numbers and letters for a volume or snapshot. For example, a gateway ID is of the form `sgw-12A3456B` where `sgw` is the resource identifier for gateways, while a volume ID takes the form `vol-112233AABBCCDDEEF` where `vol` is the resource identifier for volumes.

Storage Gateway resource IDs are in uppercase. However, if you use these resource IDs with the Amazon EC2 API, Amazon EC2 expects resource IDs in lowercase. You must change your resource ID to lowercase to use it with the EC2 API. For example, in Storage Gateway the ID for a volume might be `vol-112233AABBCCDDEEF`. If you use this ID with the EC2 API, you must change it to `vol-112233aabbccddeef`. Otherwise, the EC2 API might not behave as expected.
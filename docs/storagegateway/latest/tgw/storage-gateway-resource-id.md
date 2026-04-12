# Understanding Storage Gateway Resources and Resource IDs

In Storage Gateway, the primary resource is a _gateway_ but other resource
types include: _volume_, _virtual tape_,
_iSCSI target_, and _vtl device_. These are
referred to as _subresources_ and they don't exist unless they are
associated with a gateway.

These resources and subresources have unique Amazon Resource Names (ARNs) associated with
them as shown in the following table.

| Resource Type              | ARN Format                                                                               |
| -------------------------- | ---------------------------------------------------------------------------------------- |
| Gateway ARN                | `arn:aws:storagegateway:`region`:`account-id`:gateway/`gateway-id``                      |
| Tape ARN                   | `arn:aws:storagegateway:`region`:`account-id`:tape/`tapebarcode``                        |
| Target ARN ( iSCSI target) | `arn:aws:storagegateway:`region`:`account-id`:gateway/`gateway-id`/target/`iSCSItarget`` |
| VTL Device ARN             | `arn:aws:storagegateway:`region`:`account-id`:gateway/`gateway-id`/device/`vtldevice``   |

Storage Gateway also supports the use of EC2 instances and EBS volumes and snapshots. These
resources are Amazon EC2 resources that are used in Storage Gateway.

## Working with Resource IDs

When you create a resource, Storage Gateway assigns the resource a unique resource ID.
This resource ID is part of the resource ARN. A resource ID takes the form of a resource
identifier, followed by a hyphen, and a unique combination of eight letters and
numbers. For example, a gateway ID is of the form
`sgw-12A3456B` where `sgw` is the resource identifier for
gateways.

For virtual tapes, you can prepend a up to a four character prefix to
the barcode ID to help you organize your tapes.

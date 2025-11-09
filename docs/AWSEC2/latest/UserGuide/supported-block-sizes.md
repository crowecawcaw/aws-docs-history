# Block sizes for torn write prevention on Amazon EC2

Torn write prevention supports write operations for 4 KiB, 8 KiB, and 16 KiB blocks of data.
The data block start logical block address (LBA) must be aligned to the respective block boundary
size of 4 KiB, 8 KiB, or 16 KiB. For example, for 16 KiB write operations, the data block start
LBA must be aligned to a block boundary size of 16 KiB.

The following table shows support across storage and instance types.

|                            | 4 KiB blocks                                                                                                                                            | 8 KiB blocks                                                                       | 16 KiB blocks |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ------------- |
| **Instance store volumes** | All NVMe instance store volumes attached to current generation I-family instances.                                                                      | I4i, Im4gn, Is4gen, I7i, I7ie, I8g, and I8ge instances supported by AWS Nitro SSD. |
| **Amazon EBS volumes**     | All Amazon EBS volumes attached<br>to [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"). |

To confirm whether your instance and volume support torn write prevention, query to
check if the instance supports torn write prevention and other details, like supported
block and boundary sizes. For more information, see [Check Amazon EC2 instance support for torn write prevention](twp-namespace.md "twp-namespace.md").

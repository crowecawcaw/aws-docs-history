AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Using block storage with Amazon EC2-compatible instances on Snowball Edge

With block storage on Snowball Edge, you can add or remove block storage based on
the needs of your applications. Volumes that are attached to an Amazon EC2-compatible instance are
exposed as storage volumes that persist independently from the life of the instance. You
can manage block storage using the familiar Amazon EBS API.

Certain Amazon EBS commands are supported by using the EC2-compatible endpoint. Supported commands
include `attach-volume`, `create-volume`,
`delete-volume`, `detach-volume`, and
`describe-volumes`. For more information about these commands, see [List of supported EC2-compatible AWS CLI
commands on a Snowball Edge](using-ec2-endpoint.md#list-cli-commands-ec2-edge "using-ec2-endpoint.md#list-cli-commands-ec2-edge").

###### Important

Be sure to unmount any file systems on the device within your operating system
before detaching the volume. Failure to do so can potentially result in data
loss.

Following, you can find Amazon EBS volume quotas and differences between Amazon EBS volumes on
your device and Amazon EBS volumes in the cloud:

- Amazon EBS volumes are only available to EC2-compatible instances running on the device
  hosting the volumes.
- Volume types are limited to either capacity-optimized HDD (`sbg1`)
  or performance-optimized SSD (`sbp1`). The default volume type is
  `sbg1`.
- Snowball Edge shares HDD memory between Amazon S3 objects and Amazon EBS. If you use
  HDD-based block storage on AWS Snowball Edge, it reduces the amount of
  memory available for Amazon S3 objects. Likewise, Amazon S3 objects reduce the amount of
  memory available for Amazon EBS block storage on HDD volumes.
- Amazon EC2-compatible root volumes always use the IDE driver. Additional Amazon EBS volumes will
  preferentially use the Virtio driver if available. If the Virtio driver
  isn't available, SBE defaults to the IDE driver. The Virtio driver allows
  for better performance and is recommended.
- When creating Amazon EBS volumes, the `encrypted` parameter isn't
  supported. However, all data on your device is encrypted by default.
  .
- Volumes can be from 1 GB to 10 TB in size.
- Up to 10 Amazon EBS volumes can be attached to a single EC2-compatible instance.
- There is no formal limit to the number of Amazon EBS volumes you can have on your
  AWS Snowball Edge device. However, total Amazon EBS volume capacity is limited by the available
  space on your device.

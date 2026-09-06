

# Amazon EBS volumes and NVMe
<a name="nvme-ebs-volumes"></a>

Amazon EBS volumes are exposed as NVMe block devices on Amazon EC2 instances built on the [AWS Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html). To fully utilize the performance and capabilities of Amazon EBS volumes exposed as NVMe block devices, the EC2 instance must have the AWS NVMe driver installed. All current generation AWS Windows and Linux AMIs come with the AWS NVMe driver installed by default.

If you use an AMI that does not have the AWS NVMe driver, you can manually install it. For more information, see [AWS NVMe drivers](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-nvme-drivers.html) in the *Amazon EC2 User Guide*.

**Linux instances**  
The device names are `/dev/nvme0n1`, `/dev/nvme1n1`, and so on. The device names that you specify in a block device mapping are renamed using NVMe device names (`/dev/nvme[0-26]n1`). The block device driver can assign NVMe device names in a different order than you specified for the volumes in the block device mapping.

**Windows instances**  
When you attach a volume to your instance, you include a device name for the volume. This device name is used by Amazon EC2. The block device driver for the instance assigns the actual volume name when mounting the volume, and the name assigned can be different than the name that Amazon EC2 uses.

**Topics**
+ [Map Amazon EBS volumes to NVMe device names](identify-nvme-ebs-device.md)
+ [NVMe I/O operation timeout for Amazon EBS volumes](timeout-nvme-ebs-volumes.md)
+ [NVMe Abort command for Amazon EBS volumes](abort-command.md)
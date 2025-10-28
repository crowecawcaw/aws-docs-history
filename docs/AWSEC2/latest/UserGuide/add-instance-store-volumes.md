# Add instance store volumes to an EC2 instance

For instance types with **NVMe instance store volumes**, all
of the supported instance store volumes are automatically attached to the instance at
launch. They are automatically enumerated and assigned a device name on instance launch.

For instance types with **non-NVMe instance store volumes**,
such as C1, C3, M1, M2, M3, R3, D2, H1, I2, X1, and X1e, you must manually specify the
block device mappings for the instance store volumes that you want to attach at launch. Block
device mappings can be specified in the instance launch request or in the AMI used to launch
the instance. The block device mapping includes a device name and the volume that it maps
to. For more information, see [Block device mappings for volumes on Amazon EC2 instances](block-device-mapping-concepts.md "block-device-mapping-concepts.md")

###### Important

Instance store volumes can be attached to an instance only when you launch it. You can't
attach instance store volumes to an instance after you've launched it.

After you launch an instance, you must ensure that the instance store volumes for your
instance are formatted and mounted before you can use them. The instance store root volume is
mounted automatically.

###### Consideration for root volumes

A block device mapping always specifies the root volume for the instance. The root
volume is always mounted automatically.

Linux instances – The root volume is either an
Amazon EBS volume or an instance store volume. For instances with an instance store volume for
the root volume, the size of this volume varies by AMI, but the maximum size is 10 GB. For
more information, see [Root volume type](ComponentsAMIs.md#storage-for-the-root-device "ComponentsAMIs.md#storage-for-the-root-device").

Windows instances – The root volume must be an
Amazon EBS volume. Instance store is not supported for the root volume.

###### Contents

- [Add instance store volumes to an Amazon EC2 AMI](adding-instance-storage-ami.md "adding-instance-storage-ami.md")
- [Add instance store volumes to an EC2 instance during launch](adding-instance-storage-instance.md "adding-instance-storage-instance.md")
- [Make instance store volume available for use on an EC2 instance](making-instance-stores-available-on-your-instances.md "making-instance-stores-available-on-your-instances.md")

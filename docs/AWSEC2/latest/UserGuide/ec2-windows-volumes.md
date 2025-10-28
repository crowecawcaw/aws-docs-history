# How volumes are attached and mapped for Amazon EC2 Windows

instances

###### Note

This topic applies to Windows instances only.

Your Windows instance comes with an EBS volume that serves as the root volume. If your
Windows instance uses AWS PV or Citrix PV drivers, you can optionally add up to 25
volumes, making a total of 26 volumes. For more information, see [Amazon EBS volume limits for Amazon EC2 instances](volume_limits.md "volume_limits.md").

Depending on the instance type of your instance, you'll have from 0 to 24 possible
instance store volumes available to the instance. To use any of the instance store volumes
that are available to your instance, you must specify them when you create your AMI or
launch your instance. You can also add EBS volumes when you create your AMI or launch your
instance, or attach them while your instance is running.

When you add a volume to your instance, you specify the device name that Amazon EC2 uses. For
more information, see [Device names for volumes on Amazon EC2 instances](device_naming.md "device_naming.md"). AWS
Windows Amazon Machine Images (AMIs) contain a set of drivers that are used by Amazon EC2 to map
instance store and EBS volumes to Windows disks and drive letters.

###### Methods to map disks to EBS volumes

- [Map NVME disks to volumes](windows-list-disks-nvme.md "windows-list-disks-nvme.md")
- [Map non-NVME disks to volumes](windows-list-disks.md "windows-list-disks.md")

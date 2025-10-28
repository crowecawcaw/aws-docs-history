# Create an EC2 instance from an imported image

After the import image task is complete, you can launch an instance using the
resulting AMI or copy the AMI to another Region. For more information, see the following
documentation in the _Amazon EC2 User Guide_:

- [Launch an instance](../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md "../../../AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.md")
- [Copy an AMI](../../../AWSEC2/latest/UserGuide/CopyingAMIs.md "../../../AWSEC2/latest/UserGuide/CopyingAMIs.md")
  For some operating systems, the device drivers for enhanced networking and
  NVMe block devices that are required by [instances built
  on the Nitro system](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md") are not installed automatically during import.
  To install these drivers manually, use the directions in the following documentation
  in the _Amazon EC2 User Guide_.

- (Windows instances) Install the latest version of one of the following:
  [EC2LaunchV2](../../../AWSEC2/latest/UserGuide/ec2launch-v2-install.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2-install.md"),
  [EC2Launch](../../../AWSEC2/latest/UserGuide/ec2launch-download.md "../../../AWSEC2/latest/UserGuide/ec2launch-download.md"), or
  [EC2Config](../../../AWSEC2/latest/UserGuide/UsingConfig_Install.md "../../../AWSEC2/latest/UserGuide/UsingConfig_Install.md").
- (Windows instances) [Install or upgrade AWS NVMe drivers using PowerShell](../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md#install-nvme-drivers "../../../AWSEC2/latest/UserGuide/aws-nvme-drivers.md#install-nvme-drivers")
- (Linux instances) [Install or upgrade the NVMe driver](../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md#install-nvme-driver "../../../AWSEC2/latest/UserGuide/nvme-ebs-volumes.md#install-nvme-driver")
- [Enable enhanced networking](../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md")
  After you finish customizing your instance, create you can create a new image from the
  customized instance. For more information, see [Create an AMI](../../../AWSEC2/latest/UserGuide/create-ami.md "../../../AWSEC2/latest/UserGuide/create-ami.md") in the _Amazon EC2 User Guide_.

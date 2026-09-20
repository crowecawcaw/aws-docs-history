

# `AWSEC2-CloneInstanceAndUpgradeWindows`
<a name="automation-awsec2-CloneInstanceAndUpgradeWindows"></a>

**Description**

Create an Amazon Machine Image (AMI) from a Windows Server 2008 R2, 2012 R2, 2016, 2019, or 2022 instance, and then upgrade the AMI to Windows Server 2016, 2019, 2022, or 2025. The supported upgrade paths are as follows.
+ Windows Server 2008 R2 to Windows Server 2016
+ Windows Server 2012 R2 to Windows Server 2016
+ Windows Server 2012 R2 to Windows Server 2019
+ Windows Server 2012 R2 to Windows Server 2022 [1](#awsec2-clone-upgrade-windows-footnote1)
+ Windows Server 2012 R2 to Windows Server 2025
+ Windows Server 2016 to Windows Server 2019
+ Windows Server 2016 to Windows Server 2022
+ Windows Server 2016 to Windows Server 2025
+ Windows Server 2019 to Windows Server 2022
+ Windows Server 2019 to Windows Server 2025
+ Windows Server 2022 to Windows Server 2025

1 Microsoft's Windows Setup permits this in-place upgrade to complete. However, Microsoft does not list Windows Server 2012 R2 to Windows Server 2022 as a supported upgrade path. This path exceeds Microsoft's two-version limit for targets of Windows Server 2022 and earlier. See Microsoft's [Supported in-place upgrade paths by version](https://learn.microsoft.com/en-us/windows-server/get-started/install-upgrade-migrate?tabs=media#supported-in-place-upgrade-paths-by-version). For a Microsoft-supported outcome, upgrade Windows Server 2012 R2 to Windows Server 2025 directly. Alternatively, upgrade Windows Server 2012 R2 to Windows Server 2019 first, and then to Windows Server 2022.

The upgrade operation is a multi-step process that can take 2 hours to complete. We recommend performing an operating system upgrade on instances with at least 2 vCPUs and 4 GB of RAM. The automation creates an AMI from the instance and then launches a temporary instance from the newly created AMI in the `SubnetId` that you specify. The security groups associated with your original instance are applied to the temporary instance. The automation then performs an in-place upgrade to the `TargetWindowsVersion` on the temporary instance. Directly upgrading Windows Server 2008 R2 to Windows Server 2016, 2019, or 2022 is not supported. To upgrade a Windows Server 2008 R2 instance to one of these versions, the automation performs an in-place upgrade twice. The automation also updates or installs the AWS drivers required by the temporary instance. After the upgrade, the automation creates a new AMI from the temporary instance and then terminates the temporary instance.

You can test application functionality by launching a test instance from the upgraded AMI in your Amazon Virtual Private Cloud (Amazon VPC). When testing is complete, schedule application downtime before you switch over to the upgraded AMI.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSEC2-CloneInstanceAndUpgradeWindows)

**Document Type**

Automation

**Owner**

Amazon

**Platforms**

Windows Server 2008 R2, 2012 R2, 2016, 2019, or 2022 Standard and Datacenter editions

**Prerequisites**
+ TLS version 1.2.
+ Verify that SSM Agent is installed on your instance. For more information, see [Installing and configuring SSM Agent on EC2 instances for Windows Server](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-install-ssm-win.html).
+ Windows PowerShell 3.0 or later must be installed on your instance.
+ For instances that are joined to a Microsoft Active Directory domain, we recommend specifying a `SubnetId` that does not have connectivity to your domain controllers to help avoid hostname conflicts.
+ The instance subnet must have outbound connectivity to the internet, which provides access to AWS services such as Amazon S3 and access to download patches from Microsoft. This requirement is met if either the subnet is a public subnet and the instance has a public IP address, or if the subnet is a private subnet with a route that sends internet traffic to a public NAT device.
+ This automation works only with Windows Server 2008 R2, 2012 R2, 2016, 2019, and 2022 instances.
+ Configure the Windows Server instance with an AWS Identity and Access Management (IAM) instance profile that provides the requisite permissions for Systems Manager. For more information, see [Create an IAM instance profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html).
+ Verify that the instance has 20 GB of free disk space on the boot disk.
+ If the instance does not use an AWS-provided Windows license, then specify an Amazon EBS snapshot ID that includes Windows Server 2012 R2 installation media. To do this, complete the following steps:

  1. Verify that the EC2 instance is running Windows Server 2012 or later.

  1. Create a 6 GB EBS volume in the same Availability Zone where the instance is running. Attach the volume to the instance. Mount it as drive D, for example. 

  1. Open the context menu for the ISO file (right-click it, or press the Menu key), and then mount it to the instance as drive E, for example.

  1. Copy the content of the ISO from drive E:\\ to drive D:\\.

  1. Create an EBS snapshot of the 6 GB volume that you created earlier.
+ For Windows Server 2025 upgrades, the source instance must be [Nitro-based](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#instance-hypervisor-type).

**Limitations**

This automation doesn't support upgrading Windows domain controllers, clusters, or Windows desktop operating systems. This automation also doesn't support EC2 instances for Windows Server with the following roles installed.
+ Remote Desktop Session Host (RDSH)
+ Remote Desktop Connection Broker (RDCB)
+ Remote Desktop Virtualization Host (RDVH)
+ Remote Desktop Web Access (RDWA)

**Parameters**
+ AlternativeKeyPairName

  Type: String

  Description: (Optional) The name of an alternative key pair to use during the upgrade process. This is useful in situations where the key pair assigned to the original instance is unavailable. If the original instance was not assigned a key pair, you must specify a value for this parameter.
+ BYOLWindowsMediaSnapshotId

  Type: String

  Description: (Optional) The ID of the Amazon EBS snapshot to copy that includes Windows Server 2012 R2 installation media. Required only if you are upgrading a bring your own license (BYOL) instance.
+ IamInstanceProfile

  Type: String

  Description: (Required) The name of the IAM instance profile that enables Systems Manager to manage the instance.
+ InstanceId

  Type: String

  Description: (Required) The EC2 instance running Windows Server 2008 R2, 2012 R2, 2016, 2019, or 2022.
+ KeepPreUpgradeImageBackUp

  Type: String

  Description: (Optional) If set to True, the automation doesn't delete the pre-upgrade AMI that it creates from the EC2 instance, and you must delete that AMI yourself. By default, the automation deletes the AMI.
+ SubnetId

  Type: String

  Description: (Required) This is the subnet for the upgrade process and where your source EC2 instance resides. Verify that the subnet has outbound connectivity to AWS services, Amazon S3, and Microsoft (to download patches).
+ TargetWindowsVersion

  Type: String

  Description: (Required) Select the target Windows version.

  Default: 2025
+ RebootInstanceBeforeTakingImage

  Type: String

  Description: (Optional) If set to True, the automation reboots the instance before creating a pre-upgrade AMI. By default, the automation doesn't reboot before upgrade.
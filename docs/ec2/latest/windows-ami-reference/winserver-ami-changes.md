# Changes in Windows Server AMIs by OS version

AWS provides AMIs for Windows Server 2016 and later. These AMIs include the
following high-level changes between AWS Windows AMIs for different Windows
operating system versions:

- Windows Server 2025 AMIs use UEFI boot mode by default, except
  for Windows Server 2025 AMIs named
  `BIOS-Windows_Server-2025-English-Full-Base`.

###### Note

EC2 metal instance sizes and some EC2 instance types do not support
UEFI boot mode for Windows Server. To launch
Windows Server 2025 on these instances, you must use the
AWS managed `BIOS-Windows_Server-2025-English-Full-Base`
AMI, or an AMI that is based on that image. For more information about
UEFI requirements, [Requirements for UEFI boot mode](../../../AWSEC2/latest/UserGuide/launch-instance-boot-mode.md "../../../AWSEC2/latest/UserGuide/launch-instance-boot-mode.md") in the
_Amazon EC2 User Guide_.

- Windows Server 2025 AMIs support Nitro EC2 instance types only.
- Windows Server 2025 AMIs use `gp3` EBS volume types
  by default.
- Windows Server 2025 AMIs use the AWS.Tools PowerShell module.

- To accommodate the change from .NET Framework to .NET Core, the EC2Config
  service has been deprecated on Windows Server 2016 AMIs and replaced by
  EC2Launch. EC2Launch is a bundle of Windows PowerShell scripts that
  perform many of the tasks performed by the EC2Config service. For more
  information, see [Configure a Windows
  instance using EC2Launch](../../../AWSEC2/latest/UserGuide/ec2launch.md "../../../AWSEC2/latest/UserGuide/ec2launch.md"). EC2Launch v2 replaces EC2Launch in
  Windows Server 2022 and later. For more information, see [Configure a Windows instance using EC2Launch v2](../../../AWSEC2/latest/UserGuide/ec2launch-v2.md "../../../AWSEC2/latest/UserGuide/ec2launch-v2.md").
- On earlier versions of Windows Server AMIs, you can use the EC2Config
  service to join an EC2 instance to a domain and configure integration with
  Amazon CloudWatch. On Windows Server 2016 and later AMIs, you can use the
  CloudWatch agent to configure integration with Amazon CloudWatch. For more information
  about configuring instances to send log data to CloudWatch, see [Collect Metrics and Logs
  from Amazon EC2 Instances and On-Premises Servers with the CloudWatch Agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md").
  For information about joining an EC2 instance to a domain, see [Join an Instance to a Domain Using the
  `AWS-JoinDirectoryServiceDomain` JSON
  Document](../../../systems-manager/latest/userguide/walkthrough-powershell.md#walkthrough-powershell-domain-join "../../../systems-manager/latest/userguide/walkthrough-powershell.md#walkthrough-powershell-domain-join") in the _AWS Systems Manager User Guide_.

###### Other differences

Note the following additional important differences for instances created from
Windows Server 2016 and later AMIs.

- By default, EC2Launch does not initialize secondary EBS volumes. You can
  configure EC2Launch to initialize disks automatically by either scheduling the
  script to run or by calling EC2Launch in user data. For the procedure to
  initialize disks using EC2Launch, see "Initialize Drives and Drive Letter
  Mappings" in [Configure
  EC2Launch](../../../AWSEC2/latest/UserGuide/ec2launch.md#ec2launch-config "../../../AWSEC2/latest/UserGuide/ec2launch.md#ec2launch-config").
- If you previously enabled CloudWatch integration on your instances by using a local
  configuration file (`AWS.EC2.Windows.CloudWatch.json`), you
  can configure the file to work with the SSM Agent on instances created from
  Windows Server 2016 and later AMIs.

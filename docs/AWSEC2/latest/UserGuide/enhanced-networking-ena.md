# Enable enhanced networking with ENA on your EC2 instances

Amazon EC2 provides enhanced networking capabilities through the Elastic Network Adapter
(ENA). To use enhanced networking, you must use an AMI that includes the required ENA
driver or manually install it. Then you can enable ENA support on your instance.

To review release notes or install instructions for an ENA driver, see the tab that
matches your instance operating system platform.

Linux
You can review the following documentation on GitHub:

- Review [ENA Linux kernel driver release notes](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/RELEASENOTES.md "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/RELEASENOTES.md") on GitHub.
- For an overview of the ENA Linux kernel driver that includes install instructions
  see [Linux kernel driver for Elastic Network Adapter (ENA) family](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/README.rst "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/README.rst") on GitHub.

Windows
You can review the following documentation from the
**Manage device drivers** section of this guide:

- [Track ENA Windows driver version releases](ena-driver-releases-windows.md "ena-driver-releases-windows.md").
- [Install the ENA driver on EC2 Windows instances](ena-adapter-driver-install-upgrade-win.md "ena-adapter-driver-install-upgrade-win.md").

For Nitro-based instances, enhanced networking capabilities vary by the Nitro
version that the instance type implements.

To review network specifications for your instance, choose the instance family link
for your instance type. If you're not sure which instance family applies, see [Naming conventions](../../../ec2/latest/instancetypes/instance-type-names.md "../../../ec2/latest/instancetypes/instance-type-names.md") in the
_Amazon EC2 Instance Types_ guide.

- [Network specifications for
  accelerated computing instances](../../../ec2/latest/instancetypes/ac.md#ac_network "../../../ec2/latest/instancetypes/ac.md#ac_network")
- [Network specifications for
  compute optimized instances](../../../ec2/latest/instancetypes/co.md#co_network "../../../ec2/latest/instancetypes/co.md#co_network")
- [Network specifications for
  general purpose instances](../../../ec2/latest/instancetypes/gp.md#gp_network "../../../ec2/latest/instancetypes/gp.md#gp_network")
- [Network specifications for
  high-performance computing instances](../../../ec2/latest/instancetypes/hpc.md#hpc_network "../../../ec2/latest/instancetypes/hpc.md#hpc_network")
- [Network specifications for
  memory optimized instances](../../../ec2/latest/instancetypes/mo.md#mo_network "../../../ec2/latest/instancetypes/mo.md#mo_network")
- [Network specifications for
  storage optimized instances](../../../ec2/latest/instancetypes/so.md#so_network "../../../ec2/latest/instancetypes/so.md#so_network")

###### Contents

- [Prerequisites for enhanced networking with ENA](#ena-requirements "#ena-requirements")
- [Test whether enhanced networking is enabled](test-enhanced-networking-ena.md "test-enhanced-networking-ena.md")
- [Enable enhanced networking on your instance](enabling_enhanced_networking.md "enabling_enhanced_networking.md")
- [ENA queues](ena-queues.md "ena-queues.md")
- [Troubleshoot the ENA kernel driver on Linux](troubleshooting-ena.md "troubleshooting-ena.md")
- [Troubleshoot the Elastic Network Adapter Windows driver](troubleshoot-ena-driver.md "troubleshoot-ena-driver.md")

## Prerequisites for enhanced networking with ENA

To prepare for enhanced networking using the ENA, set up your instance as
follows:

- Launch a [Nitro-based instance](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").
- Ensure that the instance has internet connectivity.
- If you have important data on the instance that you want to preserve, you
  should back that data up now by creating an AMI from your instance. Updating
  the ENA kernel driver and enabling the `enaSupport`
  attribute might render incompatible instances or operating systems
  unreachable. If you have a recent backup, your data will still be retained
  if this happens.
- Linux instances –
  Launch the instance using a supported version of the Linux kernel and a
  supported distribution, so that ENA enhanced networking is enabled for your
  instance automatically. For more information, see [ENA Linux Kernel Driver Release Notes](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/RELEASENOTES.md "https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/RELEASENOTES.md").
- Windows instances –
  If the instance is running Windows Server 2008 R2 SP1, ensure that is has
  the [SHA-2 code signing support update](https://support.microsoft.com/en-us/help/4474419/sha-2-code-signing-support-update "https://support.microsoft.com/en-us/help/4474419/sha-2-code-signing-support-update").
- Use [AWS CloudShell](https://console.aws.amazon.com/cloudshell "https://console.aws.amazon.com/cloudshell") from the AWS Management Console, or install and configure the [AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") or the
  [AWS Tools for Windows PowerShell](../../../powershell/latest/userguide.md "../../../powershell/latest/userguide.md") on any computer you choose,
  preferably your local desktop or laptop. For more information, see [Access Amazon EC2](concepts.md#access-ec2 "concepts.md#access-ec2") or the
  [AWS CloudShell User Guide](../../../cloudshell/latest/userguide/welcome.md "../../../cloudshell/latest/userguide/welcome.md"). Enhanced networking
  cannot be managed from the Amazon EC2 console.

# Windows Prerequisites

Observe the requirements listed in [Migrating Workloads: Prerequisites for Linux and Windows](ex-migrate-instance-prereqs.md "ex-migrate-instance-prereqs.md") and ensure the following before submitting a WIGS RFC:

- Powershell version 3 or higher is installed.
- [AWS EC2 Config](../../../AWSEC2/latest/WindowsGuide/UsingConfig_Install.md "../../../AWSEC2/latest/WindowsGuide/UsingConfig_Install.md") is
  installed on the instance with the workload that you will migrate.
- Install the AWS drivers that support the latest generation instance types: PV, ENA, and NVMe. You can use
  the information in these links:
  - [Upgrading PV Drivers on Your Windows Instances](../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md "../../../AWSEC2/latest/WindowsGuide/Upgrading_PV_drivers.md")
  - [Enhanced Networking on Windows](../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md "../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md")
  - [AWS NVMe Drivers for Windows Instances](../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md "../../../AWSEC2/latest/WindowsGuide/aws-nvme-drivers.md")
  - [Part 3: Upgrading AWS NVMe drivers](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgrade-nvme "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#upgrade-nvme")
  - [Part 5: Installing the Serial Port Driver for Bare Metal Instances](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#install-serial-port-bare-metal "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#install-serial-port-bare-metal")
  - [Part 6: Updating Power Management Settings](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#power-management "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md#power-management")

- (Optional but recommended) Disable critical Services – Set critical application services, such as
  databases, to disabled,
  but ensure that any changes are documented so they can be reverted to their original startup mode during the
  application verification stage.
- (Optional but recommended) Create a Failsafe AMI from the prepared instance:
  - Use the Deployment | Advanced stack components | AMI | Create
  - During creation, add a tag Key=Name, Value=APPLICATION-ID_IngestReady
  - Wait until AMI is created before proceeding

- Third-party software components that will conflict with AMS components have been removed:
  - Anti-virus Clients
  - Backup Clients
  - Virtualization software (such as VM Tools or Hyper-V Integration services)

###### Note

[The End-of-Support Migration Program for Windows server (EMP)](https://aws.amazon.com/emp-windows-server/ "https://aws.amazon.com/emp-windows-server/") includes tooling to migrate your legacy applications
from Windows Server 2003, 2008, and 2008 R2 to newer, supported versions on AWS, without any refactoring.

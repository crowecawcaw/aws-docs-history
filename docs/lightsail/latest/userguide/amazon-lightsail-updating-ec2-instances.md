# Enable enhanced networking for Amazon EC2

instances

Some Lightsail instances are incompatible with the current generation EC2 instance types
(T3, M5, C5, or R5) because they are not enabled for enhanced networking. If your source
Lightsail instance is incompatible, you will need to choose a previous generation instance
type (T2, M4, C4, or R4) when creating an EC2 instance from your exported snapshot. These
instance type options are presented to you when creating an EC2 instance using the
**Create an Amazon EC2 instance** page in the Lightsail console.

###### Note

For more information about enhanced networking, see [Enhanced
Networking on Linux](../../../AWSEC2/latest/UserGuide/enhanced-networking.md "../../../AWSEC2/latest/UserGuide/enhanced-networking.md") or [Enhanced Networking on Windows](../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md "../../../AWSEC2/latest/WindowsGuide/enhanced-networking.md") in the Amazon EC2 documentation.

To use the latest generation EC2 instance types when the source Lightsail instance is
incompatible, you need to create the new EC2 instance using a previous generation instance type
(T2, M4, C4, or R4), update the networking driver on your instance, and then upgrade the
instance to the desired current generation instance type.

## Prerequisites

You must create an Amazon EC2 instance from an exported Lightsail snapshot. If your
Lightsail instance is incompatible, you’ll choose a previous generation instance type (T2,
M4, C4, or R4) when creating the Amazon EC2 instance. To learn more, see [Creating Amazon EC2
instances from exported snapshots in Lightsail](amazon-lightsail-creating-ec2-instances-from-exported-snapshots.md "amazon-lightsail-creating-ec2-instances-from-exported-snapshots.md").

After your new EC2 instance is up and running, continue to the [Enable
Enhanced Networking with the Elastic Network Adapter](#enabling-enhanced-networking-with-elastic-network-adapter "#enabling-enhanced-networking-with-elastic-network-adapter") section of this guide to learn
how to enable enhanced networking.

## Enable Enhanced

Networking with the Elastic Network Adapter

After your new instance is up and running, see one of the following guides in the Amazon EC2
documentation to enable enhanced networking with the Elastic Network Adapter (ENA):

- [Enabling Enhanced Networking with the ENA on Linux Instances](../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/UserGuide/enhanced-networking-ena.md")
- [Enabling Enhanced Networking with the ENA on Windows Instances](../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md "../../../AWSEC2/latest/WindowsGuide/enhanced-networking-ena.md")

## Upgrade your instance type

After you have enabled enhanced networking, you can upgrade the instance type by following
the instructions in one of the following guides:

- For Windows Server instances — [Migrating
  to Latest Generation Instance Types](../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md "../../../AWSEC2/latest/WindowsGuide/migrating-latest-types.md")
- For Linux or Unix instances — [Changing the Instance Type](../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md "../../../AWSEC2/latest/UserGuide/ec2-instance-resize.md")

# Connect to your Windows instance using RDP

You can connect to Amazon EC2 instances created from most Windows Amazon Machine Images (AMIs) using
Remote Desktop. Remote Desktop uses the Remote Desktop Protocol (RDP) to connect to and use your instance in the same
way you use a computer sitting in front of you (local computer). It is available on most
editions of Windows and is also available for Mac OS.

The license for the Windows Server operating system allows two simultaneous remote
connections for administrative purposes. The license for Windows Server is included in the
price of your Windows instance. If you require more than two simultaneous remote
connections, you must purchase a Remote Desktop Services (RDS) license. If you attempt a
third connection, an error occurs.

###### Tip

If you need to connect to your instance in order to troubleshoot boot, network
configuration, and other issues for instances built on the [AWS Nitro System](https://aws.amazon.com/ec2/nitro/ "https://aws.amazon.com/ec2/nitro/"), you can use the [EC2 Serial Console for instances](ec2-serial-console.md "ec2-serial-console.md").

###### Contents

- [Connect to your Windows instance using an RDP client](connect-rdp.md "connect-rdp.md")
- [Connect to your Windows instance using Fleet Manager](connect-rdp-fleet-manager.md "connect-rdp-fleet-manager.md")
- [Transfer files to a Windows instance using RDP](connect-to-linux-instanceWindowsFileTransfer.md "connect-to-linux-instanceWindowsFileTransfer.md")

# Accessing your data

You can access your Amazon FSx file systems using a variety of supported clients and methods from
both the AWS Cloud and on-premises environments.

###### Topics

- [Supported clients](#supported-clients-fsx "#supported-clients-fsx")
- [Accessing data from within the AWS Cloud](#access-environments "#access-environments")
- [Accessing data from on-premises](#on-premise-access "#on-premise-access")
- [Accessing data using default DNS names](#dns-name "#dns-name")
- [Support for Distributed File System (DFS) namespaces](#dfs-namespace "#dfs-namespace")
- [Accessing data using DNS aliases](dns-aliases.md "dns-aliases.md")
- [Accessing data using file shares](using-file-shares.md "using-file-shares.md")
- [Creating, updating, removing file shares](managing-file-shares.md "managing-file-shares.md")

## Supported clients

FSx for Windows File Server supports the Server Message Block (SMB) protocol versions 2.0 through 3.1.1, giving you the
flexibility to connect to your file systems using a wide variety of compute instances
and operating systems.

The following AWS compute instances are supported for use with Amazon FSx:

- Amazon Elastic Compute Cloud (Amazon EC2) instances, including Microsoft Windows, Mac, Amazon Linux and Amazon Linux 2 instances. For more information,
  see [Mapping file shares](using-file-shares.md#mapping-file-shares "using-file-shares.md#mapping-file-shares").
- Amazon Elastic Container Service (Amazon ECS) containers. For more information, see
  [FSx for Windows File Server volumes](../../../AmazonECS/latest/developerguide/wfsx-volumes.md "../../../AmazonECS/latest/developerguide/wfsx-volumes.md") in the _Amazon Elastic Container Service Developer Guide_.
- WorkSpaces instances – To learn more, see the AWS blog post [Using FSx for Windows File Server with Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-amazon-fsx-for-windows-file-server-with-amazon-workspaces/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-amazon-fsx-for-windows-file-server-with-amazon-workspaces/").
- Amazon AppStream 2.0 instances – To learn more, see the AWS blog post [Using Amazon FSx with Amazon AppStream 2.0](https://aws.amazon.com/blogs/desktop-and-application-streaming/using-amazon-fsx-with-amazon-appstream-2-0/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/using-amazon-fsx-with-amazon-appstream-2-0/").
- VMs running in VMware Cloud on AWS environments – To learn more, see
  the AWS blog post [Storing and Sharing Files with FSx for Windows File Server in a VMware Cloud on AWS
  Environment](https://aws.amazon.com/blogs/apn/storing-and-sharing-files-with-amazon-fsx-in-a-vmware-cloud-on-aws-environment/ "https://aws.amazon.com/blogs/apn/storing-and-sharing-files-with-amazon-fsx-in-a-vmware-cloud-on-aws-environment/").

The following operating systems are supported for use with Amazon FSx:

- Windows Server 2008, Windows Server 2008 R2, Windows Server 2012, Windows
  Server 2012 R2, Windows Server 2016, Windows Server 2019, and Windows Server 2022.
- Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10 (including
  the Windows 7 and Windows 10 desktop experiences of WorkSpaces), and Windows 11.
- Linux, using the `cifs-utils` tool.
- macOS

## Accessing data from within the AWS Cloud

Each Amazon FSx file system is associated with a Virtual Private Cloud (VPC). You can access your FSx for Windows File Server file system from anywhere
in the file system's VPC, regardless of Availability Zone. You can also access your file system from VPCs that are in different AWS accounts
or AWS Regions than the file system. In addition to the requirements described in the following sections for accessing FSx for Windows File Server resources,
you also need to ensure that your file system's VPC security group is configured so that data and management traffic can flow between your file
system and clients. For more information about configuring security groups with the required ports, see
[File system access control with Amazon VPC](limit-access-security-groups.md "limit-access-security-groups.md").

You can access FSx for Windows File Server file system from supported clients that are in the same VPC as your file system.

The following table illustrates the environments from which Amazon FSx supports access from clients in each of the supported
environments, depending on when the file system was created.

| Clients located in...                                               | Access to file systems created before February 22, 2019 | Access to file systems created before December 17, 2020                                                                                                                                                    | Access to file systems created after December 17, 2020                          |
| ------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Subnets in which the file system is created                         | ✓                                                       | ✓                                                                                                                                                                                                          | ✓                                                                               |
| Primary CIDR blocks of the VPC in which the file system was created | ✓                                                       | ✓                                                                                                                                                                                                          | ✓                                                                               |
| Secondary CIDRs of the VPC in which the file system was created     |                                                         | Clients with IP addresses in an [RFC 1918](http://www.faqs.org/rfcs/rfc1918.html "http://www.faqs.org/rfcs/rfc1918.html") private IP address range:<br>• 10.0.0.0/8<br>• 172.16.0.0/12<br>• 192.168.0.0/16 | Clients with IP addresses outside the following CIDR block range: 198.19.0.0/16 |
| Other CIDRs or peered networks                                      |

###### Note

In some cases, you might want to access a file system that was created before December 17, 2020
from on-premises using a non-private IP address range. To do this, create a new file system from a backup of the file system.
For more information, see [Protecting your data with backups](using-backups.md "using-backups.md").

### Accessing data from a different VPC, AWS account, or AWS Region

You can access your FSx for Windows File Server file system from support clients that are located in a different
VPC, AWS account, or AWS Region than what is associated with your file system using
VPC peering or transit gateways. When you use a VPC peering
connection or transit gateway to connect VPCs, compute instances that are in one VPC
can access Amazon FSx file systems that are in another VPC. This access is possible even if the
VPCs belong to different AWS accounts, and even if the VPCs reside in different AWS Regions.

A _VPC peering connection_ is a networking connection between
two VPCs that you can use to route traffic between them using private IPv4 or IP
version 6 (IPv6) addresses. You can use VPC peering to connect VPCs within the same
AWS Region or between AWS Regions. For more information on VPC peering, see [What is VPC Peering?](../../../vpc/latest/peering/Welcome.md "../../../vpc/latest/peering/Welcome.md") in the _Amazon VPC Peering Guide_.

A _transit gateway_ is a network transit hub that you can use
to interconnect your VPCs and on-premises networks. For more information about using
VPC transit gateways, see [Getting
Started with Transit Gateways](../../../vpc/latest/tgw/tgw-getting-started.md "../../../vpc/latest/tgw/tgw-getting-started.md") in the _Amazon VPC Transit Gateways_.

After you set up a VPC peering or transit gateway connection, you can access your
file system using its DNS name. You do so just as you do from compute instances
within the associated VPC.

## Accessing data from on-premises

FSx for Windows File Server supports the use of AWS Direct Connect or AWS VPN to access your file
systems from your on-premises compute instances. With support for AWS Direct Connect, FSx for Windows File Server
enables you to access your file system over a dedicated network connection from your
on-premises environment. With support for AWS VPN, FSx for Windows File Server enables you to access
your file system from your on-premises devices over a secure and private
tunnel.

After you connect your on-premises environment to the VPC associated with your
Amazon FSx file system, you can access your file system using its DNS name or a DNS alias. You do so
just as you do from compute instances within the VPC. For more information on
AWS Direct Connect, see the _[AWS Direct Connect User Guide](../../../directconnect/latest/UserGuide/Welcome.md "../../../directconnect/latest/UserGuide/Welcome.md")_. For more information on setting up
AWS VPN connections, see [VPN
Connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon VPC User Guide_.

###### Note

In some cases, you might want to access a file system that was created before December 17, 2020
from on-premises using a non-private IP address range. To do this, create a new file system from a backup of the file system.
For more information, see [Protecting your data with backups](using-backups.md "using-backups.md").

FSx for Windows File Server also supports the use of Amazon FSx File Gateway to provide low latency,
seamless access to your in-cloud FSx for Windows File Server file shares from your on-premises compute
instances. For more information, see
the _[Amazon FSx File Gateway User Guide](../../../filegateway/latest/filefsxw/what-is-file-fsxw.md "../../../filegateway/latest/filefsxw/what-is-file-fsxw.md")_.

###### Note

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use
the service normally. For capabilities similar to FSx File Gateway, visit
[this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/").

## Accessing data using default DNS names

FSx for Windows File Server provides a Domain Name System (DNS) name for every file system. You access your FSx for Windows File Server
file system by mapping a drive letter on your compute instance to your Amazon FSx
file share using this DNS name. To learn more, see
[Accessing data using file shares](using-file-shares.md "using-file-shares.md").

###### Important

Amazon FSx only registers DNS records for a file system if you are using Microsoft DNS as the
default DNS. If you are using a third-party DNS, you must manually set up DNS
entries for your Amazon FSx file systems. For information about choosing the correct
IP addresses to use for the file system, see [Getting the correct file system IP addresses to use for manual DNS entries](file-system-ip-addresses-for-dns.md "file-system-ip-addresses-for-dns.md").

To find the DNS name:

- In the Amazon FSx console, choose **File systems**, and then
  choose **Details**. View the DNS name in the
  **Network & Security** section.
- Or, view it in the response of the **CreateFileSystem** or
  **DescribeFileSystems** API command.

For all Single-AZ file systems joined to an AWS Managed Microsoft Active Directory, the DNS name has the
following format:
`fs-0123456789abcdef0.`ad-dns-domain-name``

For all Single-AZ file systems joined to a self-managed Active Directory, and any
Multi-AZ file system, the DNS name has the following format:
`amznfsxaa11bb22.`ad-domain`.com`

### Using Kerberos authentication with DNS names

We recommend that you use Kerberos-based authentication and encryption in
transit with Amazon FSx. Kerberos provides the most secure authentication for clients
accessing your file system. To enable Kerberos-based authentication and
encryption of data in transit for your SMB sessions, use the file system's
DNS name provided by Amazon FSx to access your file system.

If you have an external trust configured between your AWS Managed Microsoft Active Directory and your
on-premises Active Directory, to use the Amazon FSx Remote PowerShell with
Kerberos authentication, you must configure a local group policy on the client
for forest search order. For more information, see [Configure Kerberos Forest Search Order (KFSO)](<https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh921473(v=ws.10)?redirectedfrom=MSDN> "https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/hh921473(v=ws.10)?redirectedfrom=MSDN") in the Microsoft
documentation.

## Support for Distributed File System (DFS) namespaces

FSx for Windows File Server supports the use of Microsoft DFS
Namespaces. Use DFS Namespaces to organize file shares that are located on multiple file
systems into one common folder structure (a namespace) that you use to access the
entire file dataset. You can use a name in your DFS Namespace to access your Amazon
FSx file system by configuring its link target to be the file system's DNS
name. For more information, see [Group multiple FSx for Windows File Server file systems with DFS Namespaces](using-dfs-namespaces.md#group-file-systems "using-dfs-namespaces.md#group-file-systems").
